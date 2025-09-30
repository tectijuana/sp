# 📡 Automatización Doméstica con MQTT
*Un Framework para el Control Distribuido de Dispositivos*

---

## 📋 Datos

| Campo | Detalle |
|-------|---------|
| **Autor** | Jaime Antonio Alvarez Crisóstomo |
| **Materia** | Sistemas Programables |
| **Carrera** | Ingeniería en Sistemas Computacionales |
| **Colaboración** | Investigación asistida con IA **Claude** |

---

## 📑 Tabla de Contenidos

- [Introducción](#-introducción)
- [¿Qué es MQTT?](#-qué-es-mqtt)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Componentes Principales](#-componentes-principales)
- [Ventajas de MQTT en Automatización](#-ventajas-de-mqtt-en-automatización)
- [Casos de Uso](#-casos-de-uso)
- [Implementación Básica](#-implementación-básica)
- [Brokers Populares](#-brokers-populares)
- [Herramientas y Tecnologías](#-herramientas-y-tecnologías)
- [Consideraciones de Seguridad](#-consideraciones-de-seguridad)
- [Conclusiones](#-conclusiones)
- [Referencias](#-referencias)

---

## 🎯 Introducción

La automatización doméstica ha evolucionado significativamente en los últimos años, transformando la manera en que interactuamos con nuestros hogares. En este contexto, el protocolo MQTT (Message Queuing Telemetry Transport) se ha consolidado como una solución estándar para la comunicación entre dispositivos IoT, ofreciendo un framework ligero, eficiente y escalable para el control distribuido de sistemas domóticos.

Este proyecto explora la implementación de MQTT como base para un sistema de automatización doméstica, permitiendo la integración y comunicación eficiente entre diversos dispositivos inteligentes.

---

## 🔍 ¿Qué es MQTT?

**MQTT** es un protocolo de mensajería ligero diseñado específicamente para entornos donde el ancho de banda es limitado y la eficiencia energética es crítica. Desarrollado originalmente por IBM en 1999, se ha convertido en el estándar de facto para aplicaciones IoT y automatización doméstica.

### Características Principales

- **Ligero**: Requiere mínimos recursos de red y procesamiento
- **Basado en eventos**: Arquitectura orientada a la publicación/suscripción
- **Bidireccional**: Permite comunicación en ambos sentidos entre dispositivos
- **Escalable**: Soporta desde pequeñas instalaciones hasta miles de dispositivos
- **Confiable**: Ofrece tres niveles de calidad de servicio (QoS)

### Especificaciones Técnicas

```
Protocolo: TCP/IP
Puerto por defecto: 1883 (sin cifrar), 8883 (cifrado TLS/SSL)
Tamaño de mensaje: Mínimo overhead (solo 2 bytes de encabezado)
QoS Levels: 0 (At most once), 1 (At least once), 2 (Exactly once)
```

---

## 🏗️ Arquitectura del Sistema

MQTT utiliza una **arquitectura Publish/Subscribe (Pub/Sub)** que se diferencia fundamentalmente del modelo cliente-servidor tradicional. Esta arquitectura permite un desacoplamiento total entre emisores y receptores de mensajes.

### Diagrama de Arquitectura

```
┌─────────────┐          ┌─────────────┐          ┌─────────────┐
│  Publisher  │          │    BROKER   │          │ Subscriber  │
│   (Sensor)  │──────────│   Central   │──────────│  (Actuador) │
└─────────────┘  Publish │   (Hub)     │ Subscribe└─────────────┘
                         └─────────────┘
                               │
                    ┌──────────┼──────────┐
                    │          │          │
              ┌─────▼───┐ ┌────▼────┐ ┌──▼──────┐
              │Publisher│ │Publisher│ │Subscriber│
              └─────────┘ └─────────┘ └─────────┘
```

### Flujo de Comunicación

1. **Conexión**: Los clientes (publishers y subscribers) se conectan al broker
2. **Publicación**: Un publisher envía un mensaje a un topic específico
3. **Enrutamiento**: El broker recibe y almacena el mensaje
4. **Distribución**: El broker envía el mensaje a todos los subscribers del topic
5. **Recepción**: Los subscribers procesan el mensaje recibido

---

## 🔧 Componentes Principales

### 1. **Broker (Agente Central)**

El broker es el corazón del sistema MQTT. Actúa como intermediario que:
- Recibe todos los mensajes de los publishers
- Filtra mensajes según los topics
- Distribuye mensajes a los subscribers apropiados
- Gestiona las sesiones de clientes
- Maneja la autenticación y autorización

### 2. **Publisher (Publicador)**

Dispositivos o aplicaciones que generan y envían información:
- Sensores de temperatura, humedad, movimiento
- Cámaras de seguridad
- Dispositivos de medición
- Interfaces de usuario

**Ejemplo de código Publisher (Python):**

```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

# Publicar datos de un sensor
client.publish("home/livingroom/temperature", "22.5")
```

### 3. **Subscriber (Suscriptor)**

Dispositivos o aplicaciones que reciben y procesan información:
- Actuadores (relés, switches)
- Sistemas de notificación
- Bases de datos
- Paneles de control

**Ejemplo de código Subscriber (Python):**

```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Temperatura: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

# Suscribirse a un topic
client.subscribe("home/livingroom/temperature")
client.loop_forever()
```

### 4. **Topics (Temas)**

Los topics son rutas jerárquicas que organizan los mensajes:

```
home/
├── livingroom/
│   ├── temperature
│   ├── humidity
│   └── light/status
├── bedroom/
│   ├── temperature
│   └── alarm
└── kitchen/
    ├── temperature
    └── appliances/
        ├── refrigerator
        └── oven
```

**Wildcards en Topics:**
- `+` : Comodín de un solo nivel → `home/+/temperature`
- `#` : Comodín multinivel → `home/#`

---

## ✨ Ventajas de MQTT en Automatización

### 1. **Eficiencia de Recursos**

| Característica | Ventaja |
|----------------|---------|
| Bajo ancho de banda | Ideal para redes IoT con limitaciones |
| Mínimo overhead | Headers de solo 2 bytes |
| Batería eficiente | Perfecto para dispositivos alimentados por batería |

### 2. **Desacoplamiento**

- **Espacial**: Publishers y subscribers no necesitan conocerse
- **Temporal**: Los dispositivos no necesitan estar conectados simultáneamente
- **Sincronización**: Comunicación asíncrona y no bloqueante

### 3. **Escalabilidad**

```
Pequeña instalación:  1 broker + 10 dispositivos
Instalación mediana:  1 broker + 100 dispositivos
Gran instalación:     Cluster de brokers + 10,000+ dispositivos
```

### 4. **Confiabilidad**

#### Niveles de QoS (Quality of Service):

| QoS | Nombre | Descripción | Uso Recomendado |
|-----|--------|-------------|-----------------|
| 0 | At most once | Sin confirmación | Datos no críticos (temperatura) |
| 1 | At least once | Con confirmación | Comandos de control |
| 2 | Exactly once | Entrega garantizada | Operaciones críticas (alarmas) |

### 5. **Interoperabilidad**

Compatible con múltiples plataformas y lenguajes:
- Python, JavaScript, C++, Java
- ESP32, ESP8266, Arduino
- Raspberry Pi, Linux, Windows
- Home Assistant, Node-RED, OpenHAB

---

## 💡 Casos de Uso

### 1. **Monitoreo Ambiental**

```
┌──────────────────────────────────────────┐
│  Sensores DHT22 (Temp/Humedad)          │
│  ↓                                       │
│  ESP32 Publisher                         │
│  ↓                                       │
│  MQTT Broker (Mosquitto)                 │
│  ↓                                       │
│  Dashboard (Node-RED/Grafana)            │
└──────────────────────────────────────────┘
```

**Aplicaciones:**
- Control de clima
- Detección de condiciones adversas
- Optimización de consumo energético
- Alertas de temperatura/humedad

### 2. **Control de Iluminación**

```yaml
Topics:
  - home/lights/livingroom/status
  - home/lights/livingroom/brightness
  - home/lights/bedroom/color
  - home/lights/all/command
```

**Características:**
- Encendido/apagado remoto
- Control de intensidad (dimming)
- Cambio de color (RGB)
- Escenas predefinidas
- Automatización por horarios

### 3. **Seguridad y Vigilancia**

```
Sensores PIR → Detección de movimiento → Publicación al broker
                                              ↓
                    ┌─────────────────────────┴─────────────────────┐
                    ↓                                               ↓
            Notificación push                              Activación de cámara
            (Smartphone)                                   (Grabación de video)
```

### 4. **Gestión de Electrodomésticos**

| Dispositivo | Topic | Funcionalidad |
|-------------|-------|---------------|
| Cafetera | `home/kitchen/coffee/brew` | Preparar café programado |
| Termostato | `home/climate/setpoint` | Ajuste de temperatura |
| Persiana | `home/livingroom/blinds/position` | Control de apertura |
| Lavadora | `home/laundry/washer/status` | Estado y notificaciones |

---

## 💻 Implementación Básica

### Instalación del Broker Mosquitto

#### En Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

#### En Raspberry Pi:
```bash
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto.service
```

### Configuración Básica

**Archivo: `/etc/mosquitto/mosquitto.conf`**

```conf
# Configuración del puerto
listener 1883
protocol mqtt

# Configuración de persistencia
persistence true
persistence_location /var/lib/mosquitto/

# Archivo de log
log_dest file /var/log/mosquitto/mosquitto.log
log_type all

# Configuración de seguridad
allow_anonymous false
password_file /etc/mosquitto/passwd
```

### Crear Usuarios

```bash
sudo mosquitto_passwd -c /etc/mosquitto/passwd usuario1
sudo mosquitto_passwd /etc/mosquitto/passwd usuario2
sudo systemctl restart mosquitto
```

### Ejemplo Completo: Sistema de Temperatura

**Publisher (Sensor DHT22 con ESP32):**

```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22

const char* ssid = "TU_WIFI";
const char* password = "TU_PASSWORD";
const char* mqtt_server = "192.168.1.100";

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  
  if (!isnan(temperature) && !isnan(humidity)) {
    String temp_msg = String(temperature);
    String hum_msg = String(humidity);
    
    client.publish("home/sensor/temperature", temp_msg.c_str());
    client.publish("home/sensor/humidity", hum_msg.c_str());
  }
  
  delay(60000); // Cada minuto
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Client", "usuario", "password")) {
      Serial.println("Conectado al broker");
    } else {
      delay(5000);
    }
  }
}
```

**Subscriber (Python con acciones):**

```python
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print(f"Conectado con código: {rc}")
    client.subscribe("home/sensor/#")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    
    if topic == "home/sensor/temperature":
        temp = float(payload)
        print(f"🌡️  Temperatura: {temp}°C")
        
        # Activar aire acondicionado si hace calor
        if temp > 25:
            client.publish("home/climate/ac", "ON")
            print("🔵 Aire acondicionado activado")
        elif temp < 20:
            client.publish("home/climate/heater", "ON")
            print("🔴 Calefacción activada")
    
    elif topic == "home/sensor/humidity":
        hum = float(payload)
        print(f"💧 Humedad: {hum}%")
        
        if hum > 70:
            client.publish("home/climate/dehumidifier", "ON")
            print("⚠️  Deshumidificador activado")

client = mqtt.Client()
client.username_pw_set("usuario", "password")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.100", 1883, 60)
client.loop_forever()
```

---

## 🔐 Brokers Populares

### Comparativa de Brokers

| Broker | Tipo | Características | Ideal Para |
|--------|------|-----------------|------------|
| **Mosquitto** | Open Source | Ligero, confiable, ampliamente usado | Instalaciones locales |
| **HiveMQ** | Comercial | Alta escalabilidad, clustering | Empresas grandes |
| **EMQX** | Open Source/Comercial | Altamente escalable, dashboard web | IoT a gran escala |
| **VerneMQ** | Open Source | Distribuido, alta disponibilidad | Sistemas críticos |
| **RabbitMQ** | Open Source | Multi-protocolo, robusto | Aplicaciones empresariales |

### Mosquitto: El Broker Más Popular

**Ventajas:**
- ✅ Totalmente gratuito y open source
- ✅ Bajo consumo de recursos
- ✅ Excelente documentación
- ✅ Compatible con MQTT 3.1, 3.1.1 y 5.0
- ✅ Soporte para bridging (conexión entre brokers)

**Instalación y Uso:**

```bash
# Test básico del broker
mosquitto_pub -h localhost -t test/topic -m "Hola MQTT"
mosquitto_sub -h localhost -t test/#

# Test con credenciales
mosquitto_pub -h localhost -t home/lights -m "ON" -u usuario -P password

# Monitoreo de todos los mensajes
mosquitto_sub -h localhost -t '#' -v
```

---

## 🛠️ Herramientas y Tecnologías

### Plataformas de Integración

#### 1. **Home Assistant**
- Plataforma de automatización doméstica completa
- Integración nativa con MQTT
- Interfaz gráfica intuitiva
- Más de 2000 integraciones

```yaml
# configuration.yaml
mqtt:
  broker: 192.168.1.100
  port: 1883
  username: usuario
  password: password
  
sensor:
  - platform: mqtt
    name: "Temperatura Sala"
    state_topic: "home/sensor/temperature"
    unit_of_measurement: "°C"
```

#### 2. **Node-RED**
- Programación visual basada en flujos
- Excelente para prototipado rápido
- Gran comunidad y nodos disponibles

```json
[
  {
    "id": "mqtt_in",
    "type": "mqtt in",
    "topic": "home/sensor/temperature",
    "broker": "mosquitto_broker"
  },
  {
    "id": "function_node",
    "type": "function",
    "func": "if(msg.payload > 25) { return {payload: 'ON'}; }"
  }
]
```

#### 3. **ESPHome**
- Configuración declarativa para ESP32/ESP8266
- Integración automática con Home Assistant
- OTA updates

```yaml
# esphome_sensor.yaml
esphome:
  name: sensor_temperatura
  platform: ESP32
  board: esp32dev

mqtt:
  broker: 192.168.1.100
  username: usuario
  password: password

sensor:
  - platform: dht
    pin: GPIO4
    temperature:
      name: "Temperatura"
    humidity:
      name: "Humedad"
    update_interval: 60s
```

### Herramientas de Desarrollo

| Herramienta | Propósito | Plataforma |
|-------------|-----------|------------|
| **MQTT Explorer** | Cliente GUI para testing | Windows, Mac, Linux |
| **MQTT.fx** | Cliente de pruebas avanzado | Multiplataforma |
| **Mosquitto CLI** | Herramientas de línea de comandos | Linux, Mac, Windows |
| **MQTTBox** | Cliente multiplataforma | Chrome, Desktop |

### Librerías por Lenguaje

```python
# Python
pip install paho-mqtt

# JavaScript (Node.js)
npm install mqtt

# Arduino/ESP
// Instalar desde Library Manager:
// - PubSubClient
// - WiFi (incluido)
```

---

## 🔒 Consideraciones de Seguridad

### Niveles de Seguridad

#### Nivel 1: Sin Seguridad (NO RECOMENDADO)
```conf
allow_anonymous true
listener 1883
```
⚠️ **Solo para desarrollo en red local aislada**

#### Nivel 2: Autenticación Básica
```conf
allow_anonymous false
password_file /etc/mosquitto/passwd
```

#### Nivel 3: TLS/SSL (RECOMENDADO)
```conf
listener 8883
cafile /etc/mosquitto/ca_certificates/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
require_certificate false
```

#### Nivel 4: TLS + Certificados de Cliente
```conf
listener 8883
cafile /etc/mosquitto/ca_certificates/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
require_certificate true
use_identity_as_username true
```

### Mejores Prácticas

1. **Autenticación Fuerte**
   ```bash
   # Usar contraseñas robustas
   mosquitto_passwd -c /etc/mosquitto/passwd usuario
   # Ingresar contraseña con mínimo 16 caracteres
   ```

2. **Separación de Redes**
   - VLAN dedicada para dispositivos IoT
   - Firewall entre IoT y red principal
   - Sin acceso directo a Internet

3. **Listas de Control de Acceso (ACL)**
   ```conf
   acl_file /etc/mosquitto/acl
   ```
   
   ```
   # /etc/mosquitto/acl
   user sensor1
   topic write home/sensor/temperature
   
   user controller
   topic read home/sensor/#
   topic write home/actuators/#
   ```

4. **Actualización Regular**
   ```bash
   sudo apt update
   sudo apt upgrade mosquitto
   ```

5. **Monitoreo y Logs**
   ```bash
   # Revisar logs regularmente
   tail -f /var/log/mosquitto/mosquitto.log
   
   # Detectar intentos de acceso no autorizados
   grep "connection refused" /var/log/mosquitto/mosquitto.log
   ```

### Checklist de Seguridad

- [ ] Cambiar credenciales por defecto
- [ ] Deshabilitar acceso anónimo
- [ ] Implementar TLS/SSL
- [ ] Configurar ACLs apropiadas
- [ ] Separar red IoT de red principal
- [ ] Actualizar firmware regularmente
- [ ] Monitorear logs de acceso
- [ ] Implementar rate limiting
- [ ] Backup de configuraciones
- [ ] Documentar políticas de seguridad

---

## 📊 Conclusiones

La implementación de MQTT como protocolo de comunicación para sistemas de automatización doméstica ofrece numerosas ventajas que lo posicionan como una solución óptima para entornos IoT:

### Hallazgos Principales

1. **Eficiencia Comprobada**: El overhead mínimo de MQTT (2 bytes de header) lo hace ideal para dispositivos con recursos limitados, permitiendo comunicación fluida incluso en redes con ancho de banda restringido.

2. **Escalabilidad Real**: La arquitectura pub/sub permite crecer desde instalaciones pequeñas (10 dispositivos) hasta sistemas complejos (10,000+ dispositivos) sin cambios arquitectónicos significativos.

3. **Adopción Industrial**: La estandarización de MQTT y su adopción por parte de plataformas como Home Assistant, AWS IoT, y Google Cloud IoT Core valida su robustez y confiabilidad.

4. **Flexibilidad de Implementación**: La capacidad de trabajar con múltiples lenguajes, plataformas y dispositivos facilita la integración heterogénea de sistemas.

### Ventajas Clave

| Aspecto | Beneficio |
|---------|-----------|
| **Económico** | Soluciones open source sin costos de licenciamiento |
| **Técnico** | Bajo consumo de recursos y alta eficiencia |
| **Operacional** | Facilidad de mantenimiento y escalabilidad |
| **Funcional** | Interoperabilidad y flexibilidad de integración |

### Perspectivas Futuras

El ecosistema MQTT continúa evolucionando con:
- **MQTT 5.0**: Mejoras en metadatos, propiedades de mensajes y manejo de errores
- **Edge Computing**: Procesamiento local para reducir latencia
- **AI/ML Integration**: Análisis predictivo y automatización inteligente
- **Seguridad Mejorada**: Implementación de estándares como OAuth 2.0

### Recomendaciones

Para implementaciones exitosas de automatización doméstica con MQTT:

1. Comenzar con un prototipo pequeño (5-10 dispositivos)
2. Utilizar Mosquitto como broker inicial por su simplicidad
3. Implementar seguridad desde el inicio (autenticación + TLS)
4. Documentar la jerarquía de topics desde el diseño
5. Planificar escalabilidad futura en la arquitectura

---

## 📚 Referencias

### Documentación Oficial

1. **MQTT.org** - Especificación oficial del protocolo  
   URL: https://mqtt.org/

2. **Eclipse Mosquitto** - Documentación del broker  
   URL: https://mosquitto.org/documentation/

3. **Paho MQTT** - Librerías cliente  
   URL: https://www.eclipse.org/paho/

### Recursos Académicos

4. HiveMQ. (2023). *MQTT Essentials: Publish/Subscribe Architecture*. Recuperado de: https://www.hivemq.com/blog/mqtt-essentials-part2-publish-subscribe/

5. EMQX. (2025). *MQTT Broker: How It Works, Popular Options*. Recuperado de: https://www.emqx.com/en/blog/the-ultimate-guide-to-mqtt-broker-comparison

6. Luis Llamas. (2024). *¿Qué es MQTT? Su importancia como protocolo IoT*. Recuperado de: https://www.luisllamas.es/que-es-mqtt-su-importancia-como-protocolo-iot/

### Tutoriales y Guías

7. Home Assistant. (2025). *MQTT Integration Documentation*. Recuperado de: https://www.home-assistant.io/integrations/mqtt/

8. Programar Fácil. (2022). *Guía de introducción a MQTT con ESP8266 y Raspberry Pi*. Recuperado de: https://programarfacil.com/esp8266/mqtt-esp8266-raspberry-pi/

9. Steve's Internet Guide. (2025). *Using Mosquitto_pub and Mosquitto_sub MQTT Client Tools*. Recuperado de: http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/

### Plataformas y Herramientas

10. **Node-RED** - Herramienta de programación visual  
    URL: https://nodered.org/

11. **Home Assistant** - Plataforma de automatización doméstica  
    URL: https://www.home-assistant.io/

12. **ESPHome** - Framework para ESP32/ESP8266  
    URL: https://esphome.io/

### Artículos de Investigación

13. ScienceDirect. (2024). *Internet of Things-based Home Automation with Network Mapper and MQTT Protocol*. Recuperado de: https://www.sciencedirect.com/science/article/pii/S0045790624007341

---

## 📝 Notas Adicionales

### Glosario de Términos

- **Broker**: Servidor central que gestiona la comunicación MQTT
- **Publisher**: Cliente que envía mensajes
- **Subscriber**: Cliente que recibe mensajes
- **Topic**: Ruta jerárquica para organizar mensajes
- **QoS**: Quality of Service, nivel de garantía de entrega
- **Payload**: Contenido del mensaje
- **Retained Message**: Mensaje guardado por el broker para nuevos suscriptores
- **Will Message**: Mensaje enviado automáticamente si un cliente se desconecta inesperadamente

### Licencia

Este documento es material educativo desarrollado con fines académicos para la materia de Sistemas Programables de la carrera de Ingeniería en Sistemas Computacionales.

### Contacto

**Autor**: Jaime Antonio Alvarez Crisóstomo   
**Fecha de Elaboración**: 30 de Septiembre del 2025

---

<div align="center">

**🔧 Desarrollado con dedicación para Sistemas Programables 🔧**

*"La automatización no es el futuro, es el presente"*

![MQTT](https://img.shields.io/badge/MQTT-Protocol-purple?style=for-the-badge)
![IoT](https://img.shields.io/badge/IoT-Enabled-blue?style=for-the-badge)
![Home Automation](https://img.shields.io/badge/Home-Automation-green?style=for-the-badge)

</div>
