# Paso A — Teoría: VPN como seguridad empresarial

> Subtema [8-VPN](readme.md) · Paso **A** de 3 · Siguiente: [Paso B — Práctica F5 BIG-IP + IoT + IA](b-practica-f5-iot.md)

---

## 1. ¿Qué es una VPN?

Una **VPN** (*Virtual Private Network*, red privada virtual) crea un **túnel cifrado** entre un dispositivo (o una red) y otra red, sobre una infraestructura pública como Internet. Dentro del túnel, el tráfico viaja:

* **Cifrado** — un tercero que intercepte los paquetes no puede leerlos.
* **Autenticado** — solo entra quien demuestra su identidad (usuario/contraseña, certificado, MFA).
* **Íntegro** — los paquetes no pueden modificarse en tránsito sin ser detectados.

El efecto práctico: el dispositivo remoto se comporta **como si estuviera físicamente conectado** a la red privada de la organización, con una dirección IP interna y acceso a servicios que no están expuestos a Internet.

```text
   Internet (hostil) ─────────────────────────────────────
                                                          
   Laptop del estudiante ══════ túnel cifrado ══════ Gateway VPN ──── red privada
   (cliente VPN)                                     (concentrador)   ├── broker MQTT
                                                                      ├── Node-RED
                                                                      └── bases de datos
```

## 2. Tipos de VPN en la empresa

| Tipo | ¿Qué conecta? | Ejemplo de uso |
|------|---------------|----------------|
| **Acceso remoto** (*remote access*) | Un usuario/dispositivo → la red corporativa | Empleado en home office; estudiante que entra al laboratorio IoT del Tec |
| **Sitio a sitio** (*site-to-site*) | Una red completa → otra red | Sucursal Tijuana ↔ corporativo CDMX; planta ↔ nube |

En este subtema trabajamos con **VPN de acceso remoto**: cada estudiante establece su propio túnel hacia la red donde vive el broker MQTT.

## 3. SSL-VPN vs IPsec

Las dos grandes familias tecnológicas:

| Característica | **SSL/TLS VPN** | **IPsec (IKEv2)** |
|---|---|---|
| Capa donde opera | Aplicación/transporte (sobre TLS, normalmente puerto 443) | Red (protocolos ESP/AH, puertos UDP 500/4500) |
| Atraviesa firewalls y NAT | ✅ Muy bien (parece tráfico HTTPS) | ⚠️ Requiere NAT-Traversal; suele bloquearse en redes restrictivas |
| Cliente | Ligero (navegador o agente como AnyConnect/OpenConnect) | Integrado al SO, configuración más compleja |
| Caso típico | Acceso remoto de usuarios | Túneles sitio-a-sitio permanentes |
| Ejemplos | F5 BIG-IP APM, Cisco AnyConnect, ocserv | strongSwan, Cisco ASA IPsec, FortiGate IPsec |

Los productos de este subtema (**F5 BIG-IP APM** y **ocserv**) son **SSL-VPN**: el túnel viaja sobre el puerto 443, lo que facilita conectarse incluso desde redes con firewalls estrictos (cafeterías, 4G, campus).

## 4. Appliances empresariales y el cliente OpenConnect

En el mercado empresarial, la VPN de acceso remoto la ofrecen *appliances* (equipos dedicados físicos o virtuales) de distintos fabricantes:

| Fabricante / producto | Protocolo propietario | Cliente oficial |
|---|---|---|
| **F5 BIG-IP APM** | F5 SSL-VPN | BIG-IP Edge Client / F5 Access |
| **Cisco ASA / Firepower** | AnyConnect (hoy *Cisco Secure Client*) | Cisco Secure Client |
| **Fortinet FortiGate** | FortiSSL | FortiClient |
| **Palo Alto** | GlobalProtect | GlobalProtect App |

**OpenConnect** es un cliente **libre y multiplataforma** que habla varios de estos protocolos propietarios:

```bash
openconnect --protocol=anyconnect servidor   # Cisco AnyConnect / ocserv (default)
openconnect --protocol=f5 servidor           # F5 BIG-IP (soporte experimental)
openconnect --protocol=gp servidor           # Palo Alto GlobalProtect
openconnect --protocol=fortinet servidor     # Fortinet FortiGate
```

Esto es clave para el subtema: **el mismo cliente sirve para el F5 institucional (paso B) y para nuestro servidor ocserv de la demo (paso C)** — solo cambia el valor de `--protocol`.

Del lado servidor, el proyecto hermano **ocserv** (*OpenConnect VPN Server*) es un servidor SSL-VPN open source compatible con el protocolo AnyConnect, instalable con `apt` en Ubuntu. Es el que usaremos en AWS Academy.

## 5. 💰 Licenciamiento de F5: ¿es gratis para estudiantes?

**No.** F5 BIG-IP es un **producto comercial con licencia**; no existe un programa de licencias gratuitas para estudiantes. Lo que sí ofrece F5:

| Opción | Costo | Limitación |
|---|---|---|
| **Trial de BIG-IP Virtual Edition** ([f5.com/trials](https://www.f5.com/trials)) | Gratis | Temporal (expira) — sirve para un laboratorio puntual, no para un semestre |
| **Lab license** (licencia de laboratorio, no expira) | De bajo costo, pero **se compra** vía partner de F5 ([info oficial](https://support.education.f5.com/hc/en-us/articles/4408096080155-Lab-License-and-Free-Trial-Information), [guía DevCentral](https://community.f5.com/kb/technicalarticles/how-to-get-a-f5-big-ip-ve-developer-lab-license/279858)) | Requiere trámite comercial |
| **Imágenes PAYG en AWS/Azure Marketplace** | Pago por hora | 🚫 Bloqueadas en AWS Academy Learner Lab |
| **Cursos LearnF5** | Gratis | Solo formación teórica, no incluye producto |

**Conclusión para el curso:** el estudiante no puede montar su propio BIG-IP gratis. Por eso el [paso C](c-demo-aws-academy.md) usa **ocserv** (open source) como servidor, y el F5 real solo se toca **como cliente** (`openconnect --protocol=f5`) contra el equipo licenciado por la institución en el [paso B](b-practica-f5-iot.md).

## 6. Comparativa de servidores VPN open source

Si cada equipo va a ser responsable de su propio servidor VPN, ¿cuál conviene montar?

| Servidor | Instalación en Ubuntu | Complejidad | Autenticación | Cliente | ¿Modela una SSL-VPN empresarial? |
|---|---|---|---|---|---|
| **ocserv** ⭐ | `apt install ocserv` + 1 config + `ocpasswd` | **Baja** | Usuario/contraseña, certificados, PAM | **El mismo `openconnect`** del paso B | ✅ Sí (protocolo AnyConnect) |
| OpenVPN | PKI con easy-rsa, distribuir perfiles `.ovpn` | Media | Certificados (+ user/pass) | OpenVPN client | Parcial |
| strongSwan (IPsec/IKEv2) | Certificados + conceptos IPsec + NAT-T | **Alta** | Certificados, EAP | Nativo de cada SO (config distinta en cada uno) | Parcial (IPsec, no SSL-VPN) |
| WireGuard | Config mínima, intercambio de llaves | Baja | Solo llaves públicas (sin usuario/contraseña) | wg / apps WireGuard | ❌ No (VPN moderna P2P, otro paradigma) |
| SoftEther | Instalación manual + consola propia | Media-alta | Varias | Cliente propio | Parcial |

⭐ **ocserv** gana para este curso: mínima fricción de servidor, y el lado cliente es idéntico al escenario institucional.

## 7. Defensa en capas: la VPN no es suficiente

Un error común: creer que "ya con la VPN todo está seguro". La VPN protege **el acceso a la red**, pero dentro de la red siguen haciendo falta los demás controles. La práctica del paso B aplica exactamente esta pila:

```text
1️⃣  VPN (F5 BIG-IP / ocserv)        → controla QUIÉN entra a la red
        +
2️⃣  TLS en MQTT (puerto 8883)       → cifra el tráfico broker↔cliente,
                                       incluso dentro de la red privada
        +
3️⃣  Usuario y contraseña MQTT       → autentica CADA cliente ante el broker
        +
4️⃣  ACL por tópico                  → autoriza QUÉ puede publicar/leer cada quien
        +
5️⃣  Broker no expuesto a Internet   → reduce la superficie de ataque
```

Preguntas guía para distinguir capas (aparecerán en el reporte del paso B):

* Si la VPN ya cifra el túnel, ¿por qué MQTT usa TLS además? *(Pista: ¿qué pasa con el tramo dentro de la red privada? ¿Y si otro usuario de la VPN escucha?)*
* Si el broker exige usuario/contraseña, ¿para qué la ACL? *(Autenticación ≠ autorización.)*
* ¿Qué principio de seguridad aplica la política F5 que solo permite los puertos 8883 y 1880? *(Mínimo privilegio / mínima exposición.)*

## 8. VPN en arquitecturas IoT

En IoT, la VPN típicamente **no corre en el sensor** (un ESP32 no ejecuta OpenConnect): corre en un **gateway** — una computadora, Raspberry Pi o router industrial — que concentra los sensores locales y establece el túnel hacia la infraestructura central:

```text
  ESP32 / sensores ──(USB serial, BLE, WiFi local)──► Gateway IoT ══ VPN ══► Broker MQTT
                                                     (laptop / RPi)          institucional
```

Este patrón aparece en la industria como *edge gateway*: los dispositivos restringidos hablan protocolos ligeros localmente, y el gateway aporta las capacidades pesadas (VPN, TLS, buffering, incluso inferencia de IA como el `analizador.py` del paso B).

## 9. Autoevaluación

1. ¿Qué diferencia hay entre una VPN de acceso remoto y una sitio-a-sitio? Da un ejemplo de cada una en un contexto industrial.
2. ¿Por qué una SSL-VPN atraviesa firewalls restrictivos con más facilidad que IPsec?
3. ¿Qué papel juega F5 BIG-IP APM en la arquitectura del paso B, y qué componente lo sustituye en el paso C?
4. ¿Puede un estudiante montar legalmente un BIG-IP gratuito y permanente para su casa? Justifica con las opciones de licenciamiento de F5.
5. Explica con tus palabras por qué "VPN + TLS + usuario/contraseña + ACL" no es redundancia sino defensa en capas.
6. ¿Por qué OpenConnect no se instala en el ESP32 y qué patrón arquitectónico lo resuelve?
7. De la tabla de servidores open source, ¿cuál elegirías si el requisito fuera "sin usuarios ni contraseñas, solo llaves"? ¿Y si fuera "emular el flujo cliente de una VPN empresarial"?

---

➡️ Continúa con el [Paso B — Práctica: Detección inteligente de anomalías IoT mediante VPN F5 BIG-IP](b-practica-f5-iot.md)
