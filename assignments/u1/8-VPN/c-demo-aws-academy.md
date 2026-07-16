# Paso C — Demo experimental: servidor VPN propio (ocserv) en AWS Academy

> Subtema [8-VPN](readme.md) · Paso **C** de 3 · Anterior: [Paso B — Práctica F5 BIG-IP](b-practica-f5-iot.md)
>
> 🧪 **Estatus: EXPERIMENTAL — no validada aún.** Este documento es un *runbook*: está escrito para ejecutarse paso a paso y verificarse con los checkpoints de la sección 12. Al final se incluye el prompt para lanzar un agente que la valide automáticamente.

---

## 1. Objetivo

Reproducir la arquitectura completa del [paso B](b-practica-f5-iot.md) **sin el F5 BIG-IP institucional**: cada equipo despliega y administra **su propio servidor VPN** en AWS Academy y opera **sus propios clientes**. El equipo es responsable de ambos extremos del túnel.

En el paso A se explicó por qué no se usa un BIG-IP real: es un producto con licencia comercial y sus AMIs de Marketplace están bloqueadas en el Learner Lab. El sustituto es **ocserv** (OpenConnect VPN Server, open source), que habla el protocolo AnyConnect — el cliente sigue siendo `openconnect`.

## 2. Equivalencias con la práctica F5 (paso B)

| Componente | Paso B (institucional) | Paso C (demo AWS Academy) |
|---|---|---|
| Gateway VPN | F5 BIG-IP APM | **ocserv** en EC2 Ubuntu |
| Protocolo del cliente | `--protocol=f5` | `--protocol=anyconnect` |
| Grupo de autenticación | `--authgroup=IoT-Lab` | *(no se usa; se omite)* |
| Certificado del gateway | Institucional (CA pública) | Autofirmado (se acepta por *fingerprint*) |
| Política de acceso mínimo | ACL del grupo VPN en F5 (sección 8.1 de B) | `route` de ocserv + **Security Group de AWS** |
| Broker MQTT | `broker-iot.interno` = 10.20.30.10 | `broker-iot.interno` = **192.168.55.1** (IP del servidor dentro del túnel, vía `/etc/hosts`) |
| Cuentas VPN | Una por estudiante (institucional) | Una por integrante con `ocpasswd` |
| `simulador.py` / `analizador.py` | Sin cambios | **Sin cambios** (solo las variables de entorno) |
| Mosquitto: TLS, passwd, ACL | Secciones 8.2–8.5 de B | **Idénticas** (se reutilizan tal cual) |

Todo lo demás — tópicos, JSON, Isolation Forest, Node-RED, pruebas de seguridad — se conserva íntegro.

## 3. Topología

```text
Laptop(s) del equipo                         AWS Academy (Learner Lab)
┌─────────────────────────┐                 ┌─────────────────────────────────────┐
│ openconnect             │   Internet      │ EC2 Ubuntu 24.04 (t2.micro/t3.small)│
│ (anyconnect, TCP 443)   │◄═══ túnel ═════►│                                     │
│                         │                 │  ocserv        :443  (SG: ABIERTO)  │
│ simulador.py            │                 │  mosquitto TLS :8883 (SG: CERRADO)  │
│ analizador.py           │─── via túnel ──►│  node-red      :1880 (SG: CERRADO)  │
│ navegador → Node-RED    │                 │  sshd          :22   (SG: mi IP)    │
└─────────────────────────┘                 └─────────────────────────────────────┘

Red del túnel: 192.168.55.0/24 · Servidor dentro del túnel: 192.168.55.1
```

**Idea clave:** el Security Group de AWS deja `8883` y `1880` **cerrados a Internet**. La única puerta es el túnel (`443`). Así, la prueba "sin VPN el broker no responde" del paso B se cumple de forma real, igual que con la política del F5.

## 4. Restricciones de AWS Academy Learner Lab

| Restricción | Impacto | Mitigación |
|---|---|---|
| Sesiones de ~4 horas | El lab se apaga solo | La demo cabe en una sesión; documentar todo con capturas al momento |
| **La IP pública cambia** al reiniciar el lab | El *fingerprint*/destino de la VPN cambia de sesión a sesión | Anotar la IP nueva cada sesión; re-aceptar el certificado |
| AMIs de Marketplace bloqueadas | No hay F5 BIG-IP VE ni imágenes comerciales | Usamos ocserv (repositorio estándar de Ubuntu) |
| Presupuesto limitado (~$50 USD) | No dejar instancias corriendo | `t2.micro`/`t3.small`; **detener el lab al terminar** |
| IAM restringido | No se pueden crear roles arbitrarios | La demo no necesita IAM, solo EC2 + Security Group |

## 5. Fase 1 — Instancia EC2 (10 min)

1. Iniciar el Learner Lab y entrar a la consola de AWS → **EC2 → Launch instance**.
2. Configuración:
   - **AMI:** Ubuntu Server 24.04 LTS (64-bit x86).
   - **Tipo:** `t2.micro` (o `t3.small` si Node-RED se siente lento).
   - **Key pair:** crear o reutilizar (`vockey` funciona en Learner Lab).
   - **Security Group** (crear uno nuevo, `sg-iot-vpn`):

| Regla | Puerto | Protocolo | Origen | Propósito |
|---|---|---|---|---|
| SSH | 22 | TCP | *Mi IP* | Administración |
| HTTPS | 443 | TCP | 0.0.0.0/0 | ocserv (túnel TLS) |
| Custom UDP | 443 | UDP | 0.0.0.0/0 | ocserv (DTLS, opcional pero mejora latencia) |
| ~~MQTT~~ | ~~8883~~ | — | **NO ABRIR** | Solo vía VPN |
| ~~Node-RED~~ | ~~1880~~ | — | **NO ABRIR** | Solo vía VPN |

3. Lanzar y anotar la **IP pública** (la llamaremos `IP_PUBLICA`).
4. Conectarse:

```bash
ssh -i labsuser.pem ubuntu@IP_PUBLICA
```

## 6. Fase 2 — Certificados con una sola CA (15 min)

Se genera **una CA propia del equipo** que firma dos certificados: el del broker Mosquitto (validado estrictamente por los scripts de Python) y el del servidor ocserv. Los clientes solo necesitan distribuir `ca.crt`.

```bash
sudo apt update
sudo apt install -y gnutls-bin

sudo mkdir -p /etc/ssl/iot-lab && cd /etc/ssl/iot-lab
```

### 6.1 Autoridad certificadora del equipo

```bash
sudo certtool --generate-privkey --outfile ca.key

sudo tee ca.tmpl > /dev/null <<'EOF'
cn = "CA IoT-Lab equipo01"
ca
cert_signing_key
expiration_days = 365
EOF

sudo certtool --generate-self-signed \
  --load-privkey ca.key --template ca.tmpl --outfile ca.crt
```

### 6.2 Certificado del broker MQTT (nombre: `broker-iot.interno`)

```bash
sudo certtool --generate-privkey --outfile broker.key

sudo tee broker.tmpl > /dev/null <<'EOF'
cn = "broker-iot.interno"
dns_name = "broker-iot.interno"
tls_www_server
signing_key
encryption_key
expiration_days = 365
EOF

sudo certtool --generate-certificate \
  --load-privkey broker.key \
  --load-ca-certificate ca.crt --load-ca-privkey ca.key \
  --template broker.tmpl --outfile broker.crt
```

### 6.3 Certificado del servidor VPN

```bash
sudo certtool --generate-privkey --outfile vpn.key

sudo tee vpn.tmpl > /dev/null <<'EOF'
cn = "vpn-iot-lab"
tls_www_server
signing_key
encryption_key
expiration_days = 365
EOF

sudo certtool --generate-certificate \
  --load-privkey vpn.key \
  --load-ca-certificate ca.crt --load-ca-privkey ca.key \
  --template vpn.tmpl --outfile vpn.crt
```

> 📝 Como la IP pública cambia en cada sesión del lab, el certificado VPN no lleva la IP: el cliente lo validará por **fingerprint** (`--servercert pin-sha256:...`), que openconnect muestra en la primera conexión. Es el equivalente didáctico de "conocer y fijar" la identidad del servidor.

### 6.4 Copiar `ca.crt` a las laptops del equipo

Desde cada laptop:

```bash
scp -i labsuser.pem ubuntu@IP_PUBLICA:/etc/ssl/iot-lab/ca.crt .
```

(Si `scp` no puede leerlo, primero en el servidor: `sudo chmod 644 /etc/ssl/iot-lab/ca.crt`.)

## 7. Fase 3 — Servidor VPN ocserv (20 min)

### 7.1 Instalación y configuración

```bash
sudo apt install -y ocserv

sudo tee /etc/ocserv/ocserv.conf > /dev/null <<'EOF'
# --- Demo IoT-Lab: ocserv como sustituto didáctico del F5 BIG-IP APM ---
auth = "plain[passwd=/etc/ocserv/ocpasswd]"

tcp-port = 443
udp-port = 443

server-cert = /etc/ssl/iot-lab/vpn.crt
server-key  = /etc/ssl/iot-lab/vpn.key

max-clients = 16
max-same-clients = 4

device = vpns
default-domain = iot-lab.local

# Red del túnel: el servidor será 192.168.55.1
ipv4-network = 192.168.55.0
ipv4-netmask = 255.255.255.0

# Principio de mínimo acceso (equivalente a la política F5 de la sección 8.1 del paso B):
# los clientes SOLO reciben ruta hacia la red del túnel, nada más.
route = 192.168.55.0/255.255.255.0

keepalive = 32400
dpd = 90
mobile-dpd = 1800
try-mtu-discovery = true
tunnel-all-dns = false
EOF
```

### 7.2 Cuentas VPN (una por integrante)

```bash
sudo ocpasswd -c /etc/ocserv/ocpasswd alumno01   # pedirá contraseña
sudo ocpasswd    /etc/ocserv/ocpasswd alumno02   # sin -c para agregar
```

### 7.3 Arranque

En Ubuntu, el paquete `ocserv` viene con activación por socket de systemd en el puerto 443; para que use nuestra configuración de forma predecible, se deshabilita el socket y se corre el servicio directo:

```bash
sudo systemctl disable --now ocserv.socket
sudo systemctl enable  --now ocserv.service
sudo systemctl status ocserv --no-pager
```

Habilitar reenvío IP (buena práctica aunque el destino sea el propio servidor):

```bash
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-ocserv.conf
sudo sysctl -p /etc/sysctl.d/99-ocserv.conf
```

## 8. Fase 4 — Broker Mosquitto y Node-RED (20 min)

### 8.1 Mosquitto

Se reutiliza **exactamente** la configuración de las secciones 8.2–8.5 del [paso B](b-practica-f5-iot.md), apuntando a los certificados de la fase 2:

```bash
sudo apt install -y mosquitto mosquitto-clients

sudo tee /etc/mosquitto/conf.d/iot-lab.conf > /dev/null <<'EOF'
listener 8883

cafile   /etc/ssl/iot-lab/ca.crt
certfile /etc/ssl/iot-lab/broker.crt
keyfile  /etc/ssl/iot-lab/broker.key

allow_anonymous false
password_file /etc/mosquitto/passwd
acl_file /etc/mosquitto/acl

persistence true
persistence_location /var/lib/mosquitto/

log_type error
log_type warning
log_type notice
EOF

sudo chown mosquitto: /etc/ssl/iot-lab/broker.key
```

Cuentas y ACL (igual que el paso B, secciones 8.3–8.4):

```bash
sudo mosquitto_passwd -c /etc/mosquitto/passwd equipo01

sudo tee /etc/mosquitto/acl > /dev/null <<'EOF'
user equipo01
topic readwrite curso/iot/equipo01/telemetria
topic readwrite curso/iot/equipo01/resultado
EOF

sudo systemctl restart mosquitto
sudo systemctl status mosquitto --no-pager
```

> 📝 **¿Por qué `listener 8883` escucha en todas las interfaces si dijimos "solo por VPN"?** Porque quien cierra la puerta a Internet es el **Security Group** (8883 no está abierto). Ligar Mosquitto a la IP del túnel sería frágil: la interfaz `vpns0` solo existe cuando hay clientes conectados y Mosquitto fallaría al arrancar. Defensa en capas: el firewall de la nube hace el papel de la política F5.

### 8.2 Node-RED

```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered) --confirm-install --confirm-pi

sudo systemctl enable --now nodered.service
```

No abrir el puerto 1880 en el Security Group: se accederá en `http://192.168.55.1:1880` **a través de la VPN**. El flujo a construir es el de la sección 17 del paso B (usando `Servidor: broker-iot.interno`, previo alta del nombre en `/etc/hosts` **del servidor** también: `127.0.0.1 broker-iot.interno`).

## 9. Fase 5 — Clientes del equipo (15 min)

### 9.1 Conexión VPN

Instalar openconnect (`sudo apt install openconnect` / `brew install openconnect` / paquete Windows). Conectar:

```bash
sudo openconnect \
  --protocol=anyconnect \
  --user=alumno01 \
  https://IP_PUBLICA
```

La primera vez, openconnect mostrará el certificado autofirmado y su huella `pin-sha256:...`. Verificarla contra el servidor y aceptarla; para las siguientes conexiones puede fijarse:

```bash
sudo openconnect \
  --protocol=anyconnect \
  --user=alumno01 \
  --servercert pin-sha256:XXXXXXXXXXXXXXXX \
  https://IP_PUBLICA
```

Comparar con el paso B: desaparece `--authgroup` y `--protocol=f5` se vuelve `--protocol=anyconnect`. **Todo lo demás del flujo cliente es idéntico.**

### 9.2 Nombre interno del broker

Para conservar la validación TLS por nombre (y no tocar los scripts), en cada laptop agregar a `/etc/hosts` (en Windows: `C:\Windows\System32\drivers\etc\hosts`):

```text
192.168.55.1  broker-iot.interno
```

### 9.3 Verificación de conectividad (sección 11 del paso B)

```bash
nc -vz broker-iot.interno 8883      # CON VPN: succeeded
```

Desconectar la VPN (Ctrl+C en la terminal de openconnect) y repetir: **debe fallar**.

### 9.4 Ejecutar la práctica

Con la VPN activa, seguir las secciones 12–17 del [paso B](b-practica-f5-iot.md) **sin cambios en el código**, con estas variables:

```bash
export MQTT_BROKER=broker-iot.interno
export MQTT_USER=equipo01
export MQTT_PASSWORD='CONTRASEÑA_ASIGNADA'
export MQTT_TEAM=equipo01
export MQTT_CA=ca.crt
```

Terminal 1: openconnect · Terminal 2: `python analizador.py` · Terminal 3: `python simulador.py` · Navegador: `http://192.168.55.1:1880`.

## 10. Pruebas de seguridad

Las cuatro pruebas de la sección 18 del paso B aplican igual (sin VPN / con VPN / ACL de tópico ajeno / validación TLS). Prueba adicional propia de la demo:

**Prueba 5 — el broker no existe para Internet:** desde una red externa (o con la VPN caída), escanear el puerto:

```bash
nc -vz IP_PUBLICA 8883        # debe fallar: el SG no expone 8883
nc -vz IP_PUBLICA 443         # debe conectar: solo la VPN está publicada
```

## 11. Riesgos conocidos (por eso es experimental)

| Riesgo | Síntoma | Mitigación |
|---|---|---|
| UDP 443 bloqueado en la red del estudiante | Aviso "DTLS handshake failed"; la VPN funciona pero más lenta | Ignorable: el túnel cae a TCP 443 automáticamente |
| `ocserv.socket` compite con el servicio | ocserv no toma la config o el puerto está ocupado | Sección 7.3: deshabilitar el socket; diagnosticar con `sudo ss -tlnp` (buscar el 443) |
| La IP del servidor en el túnel no es `192.168.55.1` | `nc` a 192.168.55.1 falla con VPN activa | En el servidor, con un cliente conectado: `ip addr show dev vpns0` y usar la IP local mostrada (ajustar `/etc/hosts`) |
| MTU del túnel | MQTT conecta pero se congela con payloads grandes | `try-mtu-discovery = true` ya está en la config; probar `--base-mtu 1300` en el cliente |
| IP pública cambió (nueva sesión del lab) | openconnect no conecta o cambia el fingerprint | Actualizar `IP_PUBLICA`; re-verificar y re-fijar el pin |
| t2.micro sin RAM para Node-RED + Mosquitto | Lentitud, OOM | Subir a `t3.small`; o prescindir de Node-RED y usar `mosquitto_sub` como visor |
| El lab se cierra a las 4 h | Todo se detiene | La instancia sobrevive (detenida); reiniciar lab → nueva IP → repetir fase 5.1 |

## 12. Checkpoints de validación (PASS/FAIL)

| # | Checkpoint | Evidencia |
|---|---|---|
| 1 | `ocserv` activo y escuchando en 443 | `systemctl status ocserv` + `ss -tlnp` |
| 2 | Cliente establece el túnel y recibe IP `192.168.55.x` | Salida de openconnect / `ip a` |
| 3 | **Sin VPN**, `IP_PUBLICA:8883` inaccesible desde Internet | `nc -vz` fallido |
| 4 | **Con VPN**, `broker-iot.interno:8883` accesible | `nc -vz` exitoso |
| 5 | TLS validado con `ca.crt` (sin `tls_insecure`) | Conexión de `simulador.py` |
| 6 | Telemetría publicada en el tópico del equipo | Consola del simulador / `mosquitto_sub` |
| 7 | Modelo entrena con 60 muestras y publica `modelo_preparado` | Consola del analizador |
| 8 | Anomalías inyectadas (muestra ≥80) detectadas como `"anomalia": true` | JSON de resultado |
| 9 | Publicación a tópico de otro equipo **rechazada** por ACL | Prueba 3 |
| 10 | Node-RED muestra datos y alerta vía `192.168.55.1:1880` | Captura del flujo |

**La demo se considera exitosa con los checkpoints 1–9 en PASS** (el 10 es deseable; en `t2.micro` puede omitirse).

## 13. Evidencias y mini-rúbrica de la demo

| Criterio | Puntos |
|---|---:|
| Instancia EC2 y Security Group correctos (8883/1880 cerrados) | 15 |
| CA propia y certificados generados (broker + VPN) | 15 |
| ocserv operando con cuentas por integrante | 20 |
| Túnel establecido desde ≥1 cliente y pruebas con/sin VPN | 15 |
| Pipeline completo del paso B corriendo sobre la demo (checkpoints 5–8) | 25 |
| ACL verificada + reporte con capturas de los 10 checkpoints | 10 |
| **Total** | **100** |

Entregar: capturas de cada checkpoint (sin contraseñas ni llaves privadas), la tabla PASS/FAIL llenada, y una conclusión comparando la demo con el escenario F5 institucional.

## 14. 🤖 Prompt para el agente de validación

Antes de impartir la práctica, el docente puede validarla lanzando un agente (Claude Code) **con el Learner Lab activo** y las credenciales de AWS CLI del lab cargadas en `~/.aws/credentials` (botón *AWS Details → CLI* en Vocareum). Copiar y pegar:

```text
Valida la práctica experimental del archivo assignments/u1/8-VPN/c-demo-aws-academy.md
de punta a punta en mi cuenta de AWS Academy (credenciales ya cargadas en ~/.aws/credentials,
región us-east-1).

1. Crea el Security Group sg-iot-vpn y una instancia EC2 Ubuntu 24.04 t3.small con la
   key pair vockey, tal como indica la fase 1 (8883 y 1880 CERRADOS, 443 TCP/UDP abierto,
   22 abierto).
2. Vía SSH ejecuta las fases 2, 3 y 4 (certificados con certtool, ocserv, mosquitto con
   passwd+ACL, y Node-RED si la instancia lo aguanta). Usa contraseñas aleatorias y
   repórtamelas al final.
3. Haz de cliente desde esta máquina: instala openconnect si falta, conecta con
   --protocol=anyconnect, agrega broker-iot.interno a /etc/hosts apuntando a la IP del
   túnel, y corre simulador.py y analizador.py del paso B (sección 14 y 15 de
   b-practica-f5-iot.md) en un venv del scratchpad.
4. Ejecuta los 10 checkpoints de la sección 12 y entrégame la tabla PASS/FAIL con la
   evidencia (salidas de comando) de cada uno. Si un checkpoint falla, intenta el
   diagnóstico de la sección 11 antes de marcarlo FAIL, y documenta qué corrección
   aplicaste para actualizar el documento.
5. Al terminar, termina (terminate) la instancia y borra el Security Group para no
   consumir presupuesto, salvo que yo indique lo contrario.

Reporta al final: tabla PASS/FAIL, correcciones necesarias al documento
c-demo-aws-academy.md, y tiempo total estimado para un equipo de estudiantes.
```

> El resultado de esta validación define si la práctica pasa de **experimental** a **lista para impartirse**; las correcciones que arroje el agente deben incorporarse a este documento.

---

⬅️ Regresar al [índice del subtema 8-VPN](readme.md)
