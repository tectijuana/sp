

# Sensor de Presencia IR (PIR)
#### Abner Nahum Ortega Medina - #20211819  

---

## 🔍 ¿Qué es un sensor de presencia por IR (PIR)?


Un sensor de presencia por IR (Infrarrojo), también conocido como sensor PIR (Passive Infrared Sensor), es un dispositivo utilizado para detectar la presencia de personas o animales en un área determinada mediante la detección de radiación infrarroja. Este sensor no emite radiación; más bien, detecta los cambios en la radiación infrarroja emitida por objetos calientes, como cuerpos humanos, debido a su temperatura (generalmente más alta que la del entorno).

---

## ⚙️ Función en el Sistema IoT

Este proyecto utiliza un **sensor PIR conectado a un ESP32**, que envía datos mediante **WiFi y MQTT** a un servidor remoto para **monitoreo en tiempo real**.  

Además, se integran **variables simuladas** (temperatura, humedad, luz) para enriquecer los datos enviados y su posterior análisis.

---
## ¿Cómo funciona un sensor de presencia por IR?
Los sensores PIR detectan variaciones en los niveles de radiación infrarroja que los seres humanos o animales emiten en su calor corporal.

Cuando alguien se mueve en el campo de visión del sensor, el sensor detecta el cambio en la radiación, lo que genera una señal de salida. En términos de hardware, el sensor PIR tiene un detector de infrarrojos pasivo que no interactúa con el objeto, sino que simplemente observa el cambio en los niveles de radiación infrarroja.

En el caso del código proporcionado, el sensor PIR está conectado a un microcontrolador (como un ESP32), que lee la señal del sensor PIR (a través de un pin de entrada) y, según esa señal, decide si la presencia ha sido detectada o no.

--

## 🔌 Conexión del ESP32 a WiFi y MQTT

Se utilizan las librerías:

- `network`
- `umqtt.simple`

**Credenciales de conexión:**

- **Broker MQTT**: `mqtt.flespi.io`  
- **Tópico de publicación**: `sensor/presencia`

---

## 📍 Configuración del Sensor PIR

El sensor se conecta a una entrada digital del ESP32. Ejemplo:

```python
from machine import Pin

pir_sensor = Pin(15, Pin.IN)  # Sensor conectado al GPIO 15

```
---

## 🎯 Objetivo del Proyecto

- Detectar presencia en tiempo real usando un sensor PIR.  
- Transmitir datos a un servidor MQTT para monitoreo remoto.  
- Simular variables ambientales adicionales (temperatura, humedad, luz).  
- Ser escalable e integrable con plataformas IoT (como Grafana, Node-RED, Home Assistant).

---

## 🔗 Relación del Sensor PIR con el Proyecto

| **Elemento** | **Función** |
|--------------|-------------|
| **Hardware** | El sensor PIR actúa como entrada principal del sistema. |
| **Software** | La señal del sensor (0/1) activa la lógica para enviar datos JSON. |
| **IoT**      | Se transmite información útil para visualización y análisis remoto. |

---
#### Codigo en Wokwi
```python
import network
import utime
import ujson
import random
from umqtt.simple import MQTTClient
from machine import Pin

# --- Configuración WiFi y MQTT ---
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""

MQTT_BROKER = "mqtt.flespi.io"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/presencia"
MQTT_TOKEN = "HOT7egKVzIAGa9hs0kjBQmXZrGbsWKoVYQ4R34kTBkjThjhAHEKO8gq4QZvfrLHs"

# --- Configurar sensor PIR (GPIO 15) ---
pir_sensor = Pin(15, Pin.IN)

# --- Conectar a WiFi ---
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    
    while not wlan.isconnected():
        print("Conectando a WiFi...")
        utime.sleep(1)
    
    print("✅ WiFi conectado. IP:", wlan.ifconfig()[0])

# --- Conectar a MQTT ---
def connect_mqtt():
    client_id = f"sensor_presencia_{random.randint(0, 10000)}"
    client = MQTTClient(client_id, MQTT_BROKER, port=MQTT_PORT, user=MQTT_TOKEN, password="")
    try:
        client.connect()
        print("✅ Conectado a MQTT")
    except Exception as e:
        print("❌ Error al conectar a MQTT:", str(e))
        return None
    return client

# --- Función para generar datos simulados ---
def generate_sensor_data(pir_value):
    timestamp_ms = utime.time() * 1000  # Convertir a milisegundos
    
    # Datos base
    data = {
        "sensor": "PIR",
        "estado": "presencia_detectada" if pir_value == 1 else "sin_presencia",
        "timestamp": timestamp_ms,
        "value": pir_value,
        "device_id": "ESP32-SENSOR01"
    }
    
    # Datos simulados adicionales
    data["temperatura"] = round(20 + random.random() * 10, 1)  # Temperatura entre 20-30°C
    data["humedad"] = round(40 + random.random() * 30, 1)      # Humedad entre 40-70%
    data["luz"] = round(random.random() * 1000, 1)             # Nivel de luz 0-1000
    
    return data

# --- Iniciar conexiones ---
connect_wifi()
mqtt_client = connect_mqtt()

# --- Variables de control ---
last_detection_time = 0  # Tiempo cuando se detectó por última vez presencia
presence_timeout = 30  # Tiempo para considerar que la persona sigue presente (en segundos)

# --- Loop principal ---
while True:
    current_time = utime.time()
    current_state = pir_sensor.value()
    
    if current_state == 1:  # Cuando se detecta presencia
        last_detection_time = current_time  # Actualizamos la hora de detección
        data = generate_sensor_data(1)
        json_data = ujson.dumps(data)
        
        try:
            mqtt_client.publish(MQTT_TOPIC, json_data)
            print("👤 Presencia detectada")
            print("📤 Mensaje enviado:", json_data)
        except Exception as e:
            print("❌ Error publicando MQTT:", str(e))
    
    # Si no se detecta presencia, pero ha pasado el tiempo de timeout, simula que sigue presente
    elif current_time - last_detection_time < presence_timeout:
        data = generate_sensor_data(1)  # Simula que la presencia sigue activa
        json_data = ujson.dumps(data)
        
        try:
            mqtt_client.publish(MQTT_TOPIC, json_data)
            print("📊 Datos de presencia continua enviados:", json_data)
        except Exception as e:
            print("❌ Error publicando MQTT:", str(e))
    
    # Si ha pasado el tiempo de timeout y no se detecta movimiento, considera la presencia como terminada
    elif current_time - last_detection_time >= presence_timeout:
        data = generate_sensor_data(0)  # No hay presencia detectada
        json_data = ujson.dumps(data)
        
        try:
            mqtt_client.publish(MQTT_TOPIC, json_data)
            print("👋 Presencia terminada")
            print("📤 Mensaje enviado:", json_data)
        except Exception as e:
            print("❌ Error publicando MQTT:", str(e))
    
    utime.sleep(0.2)

```
#### Ejecucion 
![image](https://github.com/user-attachments/assets/15b3d5f3-b9eb-4805-81a1-c0dbc139df09)

![Captura de pantalla 2025-04-06 104430](https://github.com/user-attachments/assets/0d86fa47-2117-4af9-bd1d-a36b4bfa7220)


#### Loom
https://www.loom.com/share/7fad3c9c5d4a4244b1138c2d042393ff

---


