## CESAR GONZALEZ SALAZAR - 22211575
# Prácticas seguras de firmware IoT usando MQTT con TLS y autenticación mutua (mTLS)

**Objetivo:** lista práctica, accionable y referenciada para diseñar/implementar actualizaciones de firmware (OTA) y comunicación MQTT seguras usando TLS y autenticación mutua entre dispositivos y broker.

---

## Resumen ejecutivo
- Usa **TLS 1.3** para cifrado de transporte y **autenticación mutua (mTLS)** para garantizar que broker y dispositivo se autentiquen mutuamente.
- Firma y verifica firmwares antes de instalarlos (firma con clave asimétrica; verificar en el dispositivo). Usa manifests o árboles Merkle si haces chunking.
- Protege claves privadas en hardware seguro (TPM, Secure Element) o en almacenamiento cifrado y automatiza rotación y revocación de certificados.
- Aplica control de acceso y políticas en el broker; prueba y audita OTA y firmware en CI/CD con pentesting IoT.

---

## Alcance y supuesto de amenaza
Dispositivos remotos conectados por MQTT a un broker público o privado. El atacante puede interceptar la red, intentar suplantar al broker o inyectar firmware malicioso. Las siguientes recomendaciones mitigan MITM, firmware no firmado, robo de credenciales y exposición de claves.

---

## 1) Recomendaciones TLS / mTLS generales
1. **Forzar TLS 1.3** y evitar versiones obsoletas (TLS 1.0/1.1).  
2. **mTLS**: exigir al broker que valide certificados de cliente firmados por la CA de la organización; los clientes validan el certificado del broker contra un truststore/CA.  
3. **Validación estricta de certificados**: no usar flags `insecure` ni validaciones laxas; valida CN/SAN según política o usa certificate pinning con cuidado.  
4. **Cifras seguras**: en TLS 1.3 usar suites por defecto; si soportas TLS 1.2, restringe a AEAD (AES-GCM, ChaCha20-Poly1305).  
5. **Certificados de corta vida y renovación automática** cuando sea posible para reducir ventana de compromiso.

---

## 2) Gestión de identidad y provisión (provisioning)
- **Identidad por dispositivo**: cada dispositivo tiene su propia identidad (certificado/credencial), no reutilices credenciales entre dispositivos.  
- **Provisioning seguro**:
  - Provisión en fábrica: grabar certificado/claves en un elemento seguro (TPM / Secure Element como ATECC/SE050) o durante el proceso de ensamblaje bajo control.  
  - Enrollment JIT (Just-in-time): emitir certificados tras verificación del dispositivo para evitar exponer claves de fábrica.  
- **Revocación y rotación**: implementar revocación (OCSP/CRL) o usar certificados de vida corta con renovación automática.

---

## 3) Diseño seguro de OTA / firmware delivery sobre MQTT
### Principios generales
- **Firmar el firmware** con la clave privada del fabricante; el dispositivo debe verificar la firma antes de instalar.  
- **Integridad**: publicar hashes y manifests (version, tamaño, hash, firma). Para chunking usa checksums por bloque o árboles Merkle.  
- **Confidencialidad**: TLS protege el transporte; si el firmware contiene secretos, cifrar el payload además de TLS.  
- **Atomicidad & rollback protection**: usar particiones A/B o staging + bootloader seguro que verifique la firma. Implementa rollback controlado si la verificación falla.  
- **Autorización en el broker**: sólo servicios autorizados deben poder publicar en topics de firmware; dispositivos sólo deben suscribirse a sus topics de control.

### Patrones de entrega
- **Control channel + data channel**:
  - *Control topic* (pequeño, QoS 1/2): señales de actualización con metadata, manifest y firma.  
  - *Data channel* o URL (preferido para payloads grandes): transferencia real del binario — puede ser chunked via MQTT o descarga segura via HTTPS/Blob storage; MQTT se usa para señalización.
- **Chunking seguro**: si transfieres via MQTT, fragmenta en bloques firmados/hasheados y verifica cada bloque antes de ensamblar.
- **Verificación fuera de banda**: la verificación final de firma y hash debe ocurrir localmente antes de activar el firmware.

---

## 4) Broker y control de acceso
- **Habilitar mTLS en el broker**; configurar truststore con la CA emisora de dispositivos.  
- **Políticas y ACLs**: minimizar permisos: separar topics de control (OTA) de telemetría; usar políticas por identidad (cert CN, atributos).  
- **Negociación de recursos (MQTT 5)**: usar `Receive Maximum`, `Message Expiry`, `SessionExpiry` y `Topic Alias` para mitigar DoS y gestionar ventana de mensajes.  
- **Deshabilitar listeners no seguros**: evitar listeners sin TLS, puentes inseguros o WebSockets sin autenticación robusta.

---

## 5) Almacenamiento y protección de claves en dispositivo
- **Hardware Root of Trust**: almacenar claves privadas y realizar operaciones criptográficas en TPM o Secure Element (recomendado).  
- **Si no hay SE**: usar almacenamiento cifrado y técnicas de ofuscación como mitigación subsidiaria, pero entender que no reemplaza a un SE.  
- **No exponer claves en logs** ni en telemetría.

---

## 6) Ciclo de vida: firmwares, pruebas y despliegue
- **Firma en CI/CD**: firmar artefactos en pipeline usando HSM/KMS para proteger la clave de firma.  
- **Pruebas**: unit tests, fuzzing y pruebas de interrupción/rollback de OTA; seguir guías como OWASP IoT Testing Guide.  
- **Despliegue gradual**: canary releases, rollouts por lotes, monitorización y rollback automático si se detectan fallos.

---

## 7) Telemetría, detección y respuesta
- **Registro seguro** de eventos de OTA, intentos de conexión y errores de verificación.  
- **Alertas y detección** de comportamiento anómalo (p. ej. provisioning masivo, dispositivos sin actualizar).  
- **Correlación con revocaciones** y estrategias de mitigación en caso de compromiso.

---

## 8) Ejemplos prácticos (snippets)
### mosquitto.conf — exigir mTLS (ejemplo)
```conf
listener 8883
cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key

require_certificate true
crlfile /etc/mosquitto/certs/crl.pem
allow_anonymous false
```

### OpenSSL — CA, server y client (resumen)
```bash
# Crear CA
openssl genpkey -algorithm RSA -out ca.key -pkeyopt rsa_keygen_bits:4096
openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt -subj "/CN=MyIoT-Root-CA"

# Server
openssl genpkey -algorithm RSA -out server.key -pkeyopt rsa_keygen_bits:2048
openssl req -new -key server.key -out server.csr -subj "/CN=mqtt.example.com"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 825 -sha256

# Client
openssl genpkey -algorithm RSA -out client.key -pkeyopt rsa_keygen_bits:2048
openssl req -new -key client.key -out client.csr -subj "/CN=device-001"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 825 -sha256
```

### Paho (Python) — cliente con mTLS (ejemplo)
```python
import ssl
import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="device-001")
client.tls_set(ca_certs="/path/to/ca.crt",
               certfile="/path/to/client.crt",
               keyfile="/path/to/client.key",
               tls_version=ssl.PROTOCOL_TLS_CLIENT)
client.tls_insecure_set(False)

client.connect("mqtt.example.com", 8883)
client.loop_start()
```

---

## 9) Checklist rápido
- [ ] TLS 1.3 habilitado en broker y cliente.  
- [ ] mTLS configurado (broker exige certificado cliente).  
- [ ] Firmware firmado y verificado antes de instalación.  
- [ ] Almacenamiento de claves en SE/TPM o mitigaciones aplicadas.  
- [ ] Provisión segura (factory/JIT) implementada.  
- [ ] Rollout canary + rollback y particionado A/B.  
- [ ] Políticas/ACLs en broker para topics de OTA.  
- [ ] Telemetría de OTA habilitada y registros seguros.  
- [ ] Pentest / IoT-specific tests realizados.

---

## 10) Lecturas y guías recomendadas
- HiveMQ — MQTT Security Fundamentals (TLS, certificados, mTLS).  
- AWS IoT — Security best practices (provisioning, unique identity).  
- NIST / NCCoE — material sobre onboarding y lifecycle de IoT.  
- Mosquitto docs — SSL/TLS options y ejemplos.  
- OWASP IoT Project & IoT Testing Guide — pruebas y vulnerabilidades IoT.  
- Publicaciones sobre Merkle trees y OTA chunking para integridad.

---

### Observaciones finales
No hay una solución única: el equilibrio entre seguridad, coste y capacidades del dispositivo determina las elecciones. Implementar mTLS + firma verificada de firmware y utilizar un elemento seguro para claves ofrece un alto nivel de defensa. Si quieres, adapto este README.md a tus necesidades (ej. configurar Mosquitto completo, playbook CI/CD para firmar artefactos o ejemplos para devices concretos).

