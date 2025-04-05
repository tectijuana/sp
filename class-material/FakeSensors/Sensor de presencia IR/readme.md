

# Sensor de Presencia IR (PIR)
#### Abner Nahum Ortega Medina - #20211819  

---

## 🔍 ¿Qué es un sensor de presencia por IR (PIR)?

Un **sensor PIR (Passive Infrared Sensor)** es un dispositivo electrónico que **detecta cambios en la radiación infrarroja (calor)** emitida por objetos o personas dentro de su campo de visión.  

A diferencia de sensores activos (como los ultrasónicos o láser), **no emite señales**, sino que **funciona de forma pasiva**, midiendo las variaciones de calor en el ambiente.

---

## ⚙️ Función en el Sistema IoT

Este proyecto utiliza un **sensor PIR conectado a un ESP32**, que envía datos mediante **WiFi y MQTT** a un servidor remoto para **monitoreo en tiempo real**.  

Además, se integran **variables simuladas** (temperatura, humedad, luz) para enriquecer los datos enviados y su posterior análisis.

---

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
    
    # Si se detecta presencia, añadir más datos simulados
    if pir_value == 1:
        data["movimiento_intensidad"] = round(0.5 + random.random() * 0.5, 2)  # 0.5-1.0
        data["duracion_estimada"] = random.randint(1, 10)  # 1-10 segundos
    
    return data

# --- Iniciar conexiones ---
connect_wifi()
mqtt_client = connect_mqtt()

# --- Variables de control ---
last_state = 0
counter = 0
last_publish_time = 0

# --- Loop principal ---
while True:
    # Verifica conexión WiFi
    if not network.WLAN(network.STA_IF).isconnected():
        print("⚠️ WiFi desconectado. Reintentando...")
        connect_wifi()
    
    current_time = utime.time()
    current_state = pir_sensor.value()
    
    # Publicar datos cuando se detecta movimiento
    if current_state == 1 and last_state == 0:
        data = generate_sensor_data(1)
        json_data = ujson.dumps(data)
        
        try:
            mqtt_client.publish(MQTT_TOPIC, json_data)
            mqtt_client.ping()
            print("👤 Presencia detectada")
            print("📤 Mensaje enviado:", json_data)
            last_publish_time = current_time
        except Exception as e:
            print("❌ Error publicando MQTT:", str(e))
            mqtt_client = connect_mqtt()
    
    # Publicar datos cuando ya no hay movimiento
    elif current_state == 0 and last_state == 1:
        data = generate_sensor_data(0)
        json_data = ujson.dumps(data)
        
        try:
            mqtt_client.publish(MQTT_TOPIC, json_data)
            print("👋 Presencia terminada")
            print("📤 Mensaje enviado:", json_data)
        except Exception as e:
            print("❌ Error publicando MQTT:", str(e))
    
    # Enviar datos periódicos incluso sin cambios de estado
    # Esto asegura un flujo constante de datos para Grafana
    elif current_time - last_publish_time >= 5:  # Cada 5 segundos
        # Simular detección aleatoria ocasionalmente
        simulate_detection = random.random() < 0.3  # 30% de probabilidad
        
        if simulate_detection:
            print("🔄 Simulando detección")
            data = generate_sensor_data(1)
        else:
            data = generate_sensor_data(current_state)
        
        json_data = ujson.dumps(data)
        
        try:
            mqtt_client.publish(MQTT_TOPIC, json_data)
            mqtt_client.ping()
            print("📊 Datos periódicos enviados:", json_data)
            last_publish_time = current_time
        except Exception as e:
            print("❌ Error publicando MQTT:", str(e))
            mqtt_client = connect_mqtt()
    
    last_state = current_state
    counter += 1
    utime.sleep(0.2)
```
#### Ejecucion 
![Sensor de prescencia IR](https://github.com/user-attachments/assets/466d5008-effd-4305-a205-38eb7d4a1c5c)
![Sensor de presencia IR](https://github.com/user-attachments/assets/6f8354b2-4f4e-47ba-b9a8-6a0ae04ab92e)

#### Loom
https://www.loom.com/share/d25cbc828d57469e9b2801393591ecfa

---


