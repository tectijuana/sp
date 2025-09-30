<div align="center">

# Seguridad en MQTT

### Instituto Tecnológico de Tijuana

**Materia:** Sistemas Programables

**Alumno:** Suarez Castro Jair Alberto

**Número de Control:** 22211663

---

</div>

## 🔐 Cifrado de Comunicaciones con TLS/SSL

### Introducción

MQTT por defecto usa conexiones TCP sin cifrado, lo que significa que los mensajes viajan en texto claro y pueden ser interceptados o modificados por terceros. Para proteger la confidencialidad y la integridad de los datos, se emplea **TLS (Transport Layer Security)** sobre MQTT.

### Características del Cifrado TLS

| Aspecto | Detalle |
|---------|---------|
| **Puerto estándar seguro** | 8883 (IANA secure-mqtt) |
| **Puerto sin cifrar** | 1883 (no recomendado en producción) |
| **Versión TLS recomendada** | TLS 1.3 (idealmente) o TLS 1.2 mínimo |
| **Versiones NO recomendadas** | SSLv3, TLS 1.0/1.1 (vulnerables a POODLE, CRIME) |

### Proceso de Handshake TLS

```
Cliente                                    Broker
   |                                          |
   |------- Solicitud de conexión ---------->|
   |                                          |
   |<------ Presenta certificado X.509 ------|
   |                                          |
   |------- Valida certificado ------------->|
   |                                          |
   |<----- Negociación de algoritmos ------->|
   |                                          |
   |<===== Canal cifrado bidireccional =====>|
   |                                          |
   |  Todo el tráfico MQTT viaja cifrado     |
```

### Configuración en Mosquitto

#### mosquitto.conf

```conf
listener 8883
cafile /ruta/ca.crt
certfile /ruta/broker.crt
keyfile /ruta/broker.key
```

#### Conexión del Cliente

```bash
mosquitto_sub --cafile /ruta/ca.crt \
  -h broker.ejemplo.com \
  -p 8883 \
  -t topic/prueba \
  -v
```

### ⚠️ Riesgos sin TLS

| Riesgo | Consecuencia |
|--------|--------------|
| **Tráfico en texto claro** | Los mensajes pueden ser leídos o alterados |
| **Credenciales expuestas** | Usuario/contraseña pueden ser robadas fácilmente |
| **Ataques MITM** | Atacantes pueden interceptar y modificar comunicaciones |
| **Falta de validación** | Certificados no verificados permiten suplantación |

---

## 🎫 Autenticación con Certificados X.509

### Mutual TLS (mTLS)

En el esquema de mutual TLS, tanto el broker como el cliente se autentican mutuamente mediante certificados X.509.

### Arquitectura de Autenticación

```
                 CA (Autoridad de Certificación)
                              |
                    +---------+---------+
                    |                   |
                    v                   v
           Certificado Broker    Certificado Cliente
                    |                   |
                    v                   v
               Broker MQTT <=TLS=> Cliente MQTT
                              
         (Handshake TLS mutual con validación bidireccional)
```

### Componentes Necesarios

| Componente | Descripción |
|------------|-------------|
| **Par de claves** | Clave pública y privada para cada cliente |
| **Certificado firmado** | Emitido por una CA de confianza |
| **CA raíz** | Certificado de la Autoridad de Certificación |
| **Common Name (CN)** | Identificador único del certificado (puede usarse como username) |

### Configuración del Broker (Mosquitto)

```conf
listener 8883
cafile /ruta/ca.crt
certfile /ruta/broker.crt
keyfile /ruta/broker.key
require_certificate true
use_identity_as_username true
```

| Opción | Función |
|--------|---------|
| `require_certificate true` | Obliga al cliente a presentar un certificado válido |
| `use_identity_as_username true` | Usa el CN del certificado como nombre de usuario MQTT |

### Conexión del Cliente con Certificado

```bash
mosquitto_sub --cafile /ruta/ca.crt \
  --cert /ruta/client.crt \
  --key /ruta/client.key \
  -h broker.ejemplo.com \
  -p 8883 \
  -t topic/prueba \
  -v
```

### Flujo de Autenticación mTLS

```
Cliente (C)          Broker (B)          Autoridad Certificación (CA)
    |                     |                          |
    |--1. Solicitud TLS-->|                          |
    |                     |                          |
    |<-2. Cert Broker-----|                          |
    |                     |                          |
    |--------3. Valida cert broker----------------->|
    |                     |                          |
    |<-------4. Certificado válido------------------|
    |                     |                          |
    |<-5. Solicita cert---|                          |
    |                     |                          |
    |--6. Envía cert C--->|                          |
    |                     |                          |
    |                     |--7. Verifica firma------>|
    |                     |                          |
    |                     |<-8. Cert válido----------|
    |                     |                          |
    |<==9. Conexión establecida y cifrada==>|       |
```

### ⚠️ Consideraciones de Seguridad

- **Revocación**: Implementar mecanismos CRL o OCSP para certificados comprometidos
- **Gestión del ciclo de vida**: Emisión, renovación y revocación de certificados
- **Infraestructura PKI**: Requiere una gestión cuidadosa de la infraestructura

---

## 👤 Autenticación con Usuario y Contraseña

### Descripción

El protocolo MQTT incluye en el paquete CONNECT campos opcionales para usuario y contraseña. El cliente envía estas credenciales al conectar, y el broker las verifica contra su base de datos.

### Configuración en Mosquitto

#### 1. Crear archivo de contraseñas

```bash
mosquitto_passwd -c /ruta/credenciales usuario1
# Solicita contraseña y la guarda hasheada (SHA512-PBKDF2)
```

#### 2. Configurar mosquitto.conf

```conf
allow_anonymous false
password_file /ruta/credenciales
```

#### 3. Conexión del cliente

```bash
mosquitto_sub -h broker.ejemplo.com \
  -p 8883 \
  -u usuario1 \
  -P mi_contraseña \
  -t topic/prueba \
  -v
```

### Códigos de Respuesta CONNACK

| Código | Significado |
|--------|-------------|
| **0** | Conexión aceptada |
| **4** | Usuario/contraseña incorrectos |
| **5** | No autorizado |

### Comparativa: Con y Sin TLS

```
SIN TLS (❌ INSEGURO)
┌─────────┐                                      ┌─────────┐
│ Cliente │──usuario:contraseña EN TEXTO CLARO──>│ Broker  │
└─────────┘                                      └─────────┘
     ↑                                                ↑
     └──────────────┐                    ┌───────────┘
              ┌─────┴────┐               │
              │ Atacante │───────────────┘
              │ Intercepta credenciales  │
              └──────────┘

CON TLS (✅ SEGURO)
┌─────────┐                                      ┌─────────┐
│ Cliente │═══usuario:contraseña CIFRADOS═══════>│ Broker  │
└─────────┘                                      └─────────┘
              ┌──────────┐
              │ Atacante │
              │ No puede │
              │   leer   │
              └──────────┘
```

### ⚠️ Limitaciones y Protecciones

| Aspecto | Detalle |
|---------|---------|
| **Sin TLS** | Credenciales viajan en claro y pueden ser capturadas |
| **Contraseñas débiles** | Vulnerables a ataques de fuerza bruta |
| **Acceso anónimo** | `allow_anonymous true` permite conexiones sin credenciales (INSEGURO) |
| **Recomendación** | Siempre combinar con TLS y usar contraseñas fuertes |

### Almacenamiento Seguro

Mosquitto utiliza **SHA512-PBKDF2** por defecto para hashear contraseñas, lo que proporciona:
- Hash salado
- Protección contra ataques de diccionario
- Múltiples iteraciones para ralentizar ataques de fuerza bruta

---

## ✅ Buenas Prácticas de Seguridad

### Matriz de Seguridad MQTT

| Capa | Práctica | Prioridad |
|------|----------|-----------|
| **Transporte** | Usar TLS 1.2/1.3 en puerto 8883 | 🔴 Crítica |
| **Transporte** | Deshabilitar puerto 1883 sin cifrar | 🔴 Crítica |
| **Transporte** | Deshabilitar SSLv3, TLS 1.0/1.1 | 🔴 Crítica |
| **Certificados** | Usar CA de confianza (Let's Encrypt, etc.) | 🟠 Alta |
| **Certificados** | Validar cadena completa del certificado | 🔴 Crítica |
| **Certificados** | Implementar revocación (CRL/OCSP) | 🟠 Alta |
| **Autenticación** | `allow_anonymous false` | 🔴 Crítica |
| **Autenticación** | `require_certificate true` (si usa X.509) | 🟠 Alta |
| **Autenticación** | Contraseñas hasheadas (PBKDF2) | 🔴 Crítica |
| **Autorización** | Implementar ACL por tópicos | 🟡 Media |
| **Aplicación** | Cifrar payload de mensajes sensibles | 🟡 Media |
| **Aplicación** | Firmas digitales para integridad | 🟡 Media |
| **Mantenimiento** | Actualizar broker y librerías regularmente | 🟠 Alta |
| **Mantenimiento** | Rotar certificados y contraseñas periódicamente | 🟠 Alta |
| **Monitoreo** | Revisar logs para detectar ataques | 🟡 Media |

### Checklist de Implementación

#### Transporte
- [ ] TLS 1.2 o 1.3 configurado
- [ ] Puerto 8883 habilitado
- [ ] Puerto 1883 deshabilitado en producción
- [ ] SSLv3 y TLS 1.0/1.1 deshabilitados
- [ ] Suites de cifrado seguras configuradas

#### Certificados
- [ ] Certificados de CA confiable instalados
- [ ] Validación de certificados habilitada en clientes
- [ ] Certificados con fechas de expiración válidas
- [ ] Mecanismo de revocación implementado
- [ ] Permisos restrictivos en archivos de claves privadas

#### Autenticación
- [ ] `allow_anonymous false` configurado
- [ ] Archivo de contraseñas con hashes seguros
- [ ] Certificados X.509 para clientes (si aplica)
- [ ] `require_certificate true` (si usa mTLS)
- [ ] Contraseñas robustas implementadas

#### Autorización
- [ ] ACL por tópicos configuradas
- [ ] Permisos mínimos por cliente
- [ ] Lista blanca de clientes autorizados

#### Operaciones
- [ ] Monitoreo de logs activo
- [ ] Plan de rotación de credenciales
- [ ] Actualizaciones de seguridad aplicadas
- [ ] Backups de configuración
- [ ] Documentación de la arquitectura de seguridad

### Niveles de Seguridad MQTT

| Nivel | Descripción | Estado | Uso Recomendado |
|-------|-------------|--------|-----------------|
| **Nivel 0** | Puerto 1883, sin autenticación | ❌ NUNCA usar | Ninguno |
| **Nivel 1** | Usuario/contraseña sin TLS | ⚠️ Solo desarrollo | Redes privadas cerradas |
| **Nivel 2** | TLS + Usuario/contraseña | ✅ Mínimo aceptable | Producción estándar |
| **Nivel 3** | TLS + Certificados X.509 | ✅✅ Recomendado | Producción ideal |
| **Nivel 4** | mTLS + ACL + Cifrado payload | ✅✅✅ Máxima seguridad | Entornos críticos |

### Arquitectura Segura Recomendada

```
┌─────────────────── CLIENTES IoT ───────────────────┐
│                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────┐ │
│  │ Dispositivo 1│  │ Dispositivo 2│  │ Disp. 3  │ │
│  │ device1.crt  │  │ device2.crt  │  │ dev3.crt │ │
│  └──────┬───────┘  └──────┬───────┘  └────┬─────┘ │
│         │                 │                │       │
└─────────┼─────────────────┼────────────────┼───────┘
          │                 │                │
          └─────────┬───────┴────────┬───────┘
                    │  CIFRADO TLS   │
          ┌─────────▼────────────────▼─────────┐
          │    CAPA DE SEGURIDAD              │
          │  ┌──────────────────────────┐     │
          │  │  TLS 1.3 - Puerto 8883   │     │
          │  └──────────┬───────────────┘     │
          │             │                      │
          │  ┌──────────▼───────────────┐     │
          │  │  Autenticación mTLS + ACL│     │
          │  └──────────┬───────────────┘     │
          └─────────────┼──────────────────────┘
                        │
          ┌─────────────▼──────────────────────┐
          │       BROKER MQTT                  │
          │  ┌──────────────────────────┐      │
          │  │ Mosquitto Broker         │      │
          │  │ Certificado: broker.crt  │      │
          │  └──────────┬───────────────┘      │
          │             │                       │
          │  ┌──────────▼───────────────┐      │
          │  │ Control de Acceso (ACL)  │      │
          │  └──────────┬───────────────┘      │
          │             │                       │
          │  ┌──────────▼───────────────┐      │
          │  │   Monitoreo de Logs      │      │
          │  └──────────────────────────┘      │
          └─────────────┬──────────────────────┘
                        │
          ┌─────────────▼──────────────────────┐
          │         BACKEND                    │
          │  ┌──────────────────────────┐      │
          │  │ Aplicación               │      │
          │  │ Suscriptores autorizados │      │
          │  └──────────┬───────────────┘      │
          │             │                       │
          │  ┌──────────▼───────────────┐      │
          │  │   Base de Datos          │      │
          │  └──────────────────────────┘      │
          └────────────────────────────────────┘
```

### Resumen de Comandos Útiles

#### Generar certificados autofirmados

```bash
# Crear CA
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt

# Crear certificado del broker
openssl genrsa -out broker.key 2048
openssl req -new -key broker.key -out broker.csr
openssl x509 -req -in broker.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out broker.crt -days 365

# Crear certificado del cliente
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

#### Gestión de contraseñas

```bash
# Crear nuevo archivo de contraseñas
mosquitto_passwd -c /ruta/credenciales usuario1

# Añadir usuario adicional
mosquitto_passwd /ruta/credenciales usuario2

# Eliminar usuario
mosquitto_passwd -D /ruta/credenciales usuario1
```

#### Verificar configuración

```bash
# Probar conexión con TLS
mosquitto_sub --cafile /ruta/ca.crt \
  -h broker.ejemplo.com \
  -p 8883 \
  -t test/topic \
  -v

# Probar con autenticación
mosquitto_sub --cafile /ruta/ca.crt \
  -u usuario1 \
  -P password \
  -h broker.ejemplo.com \
  -p 8883 \
  -t test/topic \
  -v

# Probar con certificado de cliente
mosquitto_sub --cafile /ruta/ca.crt \
  --cert /ruta/client.crt \
  --key /ruta/client.key \
  -h broker.ejemplo.com \
  -p 8883 \
  -t test/topic \
  -v
```

---

## 📚 Referencias

1. **HiveMQ Team**. (2024, 6 de marzo). *TLS/SSL – MQTT Security Fundamentals*. HiveMQ Blog.  
   https://www.hivemq.com/blog/mqtt-security-fundamentals-tls-ssl/

2. **HiveMQ Team**. (2015, 25 de mayo). *X509 Client Certificate Authentication – MQTT Security Fundamentals*. HiveMQ Blog.  
   https://www.hivemq.com/blog/mqtt-security-fundamentals-x509-client-certificate-authentication/

3. **HiveMQ Team**. (2024, 7 de marzo). *Authentication with Username and Password – MQTT Security Fundamentals*. HiveMQ Blog.  
   https://www.hivemq.com/blog/mqtt-security-fundamentals-authentication-username-password/

4. **Schiffler, A.** (2025, 6 de marzo). *How to Configure MQTT TLS/SSL and Certificate-based Authorization for Mosquitto MQTT Broker*. Cedalo.  
   https://cedalo.com/blog/mqtt-tls-configuration-guide/

5. **Schiffler, A.** (2023, 14 de diciembre). *How to enable MQTT Authentication and Authorization on Mosquitto*. Cedalo.  
   https://cedalo.com/blog/mqtt-authentication-and-authorization-on-mosquitto/

6. **Eclipse Foundation**. (s.f.). *Authentication methods*. Eclipse Mosquitto Documentation.  
   https://mosquitto.org/documentation/authentication-methods/

7. **Rius, O.** (2025, 7 de febrero). *MQTT Broker (Mosquitto) con certificado servidor (self-signed)*. Blog de Oriol Rius.  
   https://oriolrius.cat/2025/02/07/mqtt-broker-mosquitto-con-certificado-servidor-self-signed/

8. **Rius, O.** (2025, 18 de febrero). *MQTT Broker (Mosquitto) con certificado servidor (self-signed) y certificado en los clientes*. Blog de Oriol Rius.  
   https://oriolrius.cat/2025/02/18/mqtt-broker-mosquitto-con-certificado-servidor-self-signed-y-certificado-en-los-clientes/

9. **Centro de Ciberseguridad Industrial**. (2025, 17 de julio). *Seguridad en MQTT en entornos de Ciberseguridad Industrial*.  
   https://www.cci-es.org/seguridad-en-mqtt-en-entornos-de-ciberseguridad-industrial/

---

### Riesgos Críticos a Evitar

- ❌ Usar MQTT sin TLS permite espionaje y suplantación
- ❌ No validar certificados permite ataques MITM
- ❌ Permitir acceso anónimo facilita accesos no autorizados
- ❌ Usar versiones antiguas de TLS expone a vulnerabilidades conocidas

