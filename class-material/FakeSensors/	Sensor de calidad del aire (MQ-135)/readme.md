# 🏭 **Monitor de Calidad del Aire con ESP32 y MQ-135**

📍 *Autor: [Arias Verdin Vivian -C20211692]*  
📅 *Fecha: [03/04/2025]*  
📌 *Descripción:* Este proyecto utiliza un ESP32 en Wokwi para leer datos del sensor MQ-135 y enviarlos mediante **MQTT** a **Flespi**, permitiendo su visualización remota.

---

## 📡 **Código para Wokwi (ESP32 con MQ-135)**
Este código configura el ESP32 en Wokwi para leer el sensor de calidad del aire MQ-135 y enviar los datos a **Flespi MQTT**.

```python
import time
import network
from umqtt.simple import MQTTClient
from machine import ADC

# Configuración WiFi en Wokwi
SSID = "Wokwi-GUEST"
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Conectando a WiFi...")
    time.sleep(1)

print("✅ WiFi Conectado. IP:", wifi.ifconfig()[0])

# Configuración de MQTT (Flespi)
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "sensor/airquality"
FLESPI_TOKEN = "2VC5YWysyF4nfepE5hyDUN7S6VZPjx0M1ZofavRZErTlvnThcwnvFIgd9WDZDjSb"  # Reemplaza con tu token de Flespi

client = MQTTClient("esp32", FLESPI_BROKER, port=FLESPI_PORT, user=FLESPI_TOKEN, password="")
client.connect()

# Configuración del sensor MQ-135
mq135 = ADC(34)  # Pin analógico donde está conectado el sensor

# Bucle infinito para enviar datos cada 3 segundos
while True:
    air_quality = mq135.read()  # Leer valor del sensor
    message = f'{{"mq135_value": {air_quality}}}'  # Formato JSON
    
    client.publish(FLESPI_TOPIC, message)
    print("📤 Enviado a Flespi:", message)
    
    time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato
```

---

## 📊 **Código para visualizar datos en Python (Flespi)**
Este script recibe los datos enviados por MQTT y los muestra en la consola.

```python
import paho.mqtt.client as mqtt

# Configuración de MQTT (Flespi)
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "sensor/airquality"
FLESPI_TOKEN = "2VC5YWysyF4nfepE5hyDUN7S6VZPjx0M1ZofavRZErTlvnThcwnvFIgd9WDZDjSb"  # Reemplaza con tu token de Flespi

# Función cuando se recibe un mensaje
def on_message(client, userdata, msg):
    air_quality = msg.payload.decode()
    print(f"📥 Calidad del Aire Recibida: {air_quality}")

# Configurar cliente MQTT para Flespi
client = mqtt.Client()
client.username_pw_set(FLESPI_TOKEN)
client.on_message = on_message

client.connect(FLESPI_BROKER, FLESPI_PORT)
client.subscribe(FLESPI_TOPIC)

print("📡 Esperando datos del sensor MQ-135 en Flespi...")
client.loop_forever()
```

---

## 🚀 **Pasos para probar en Wokwi**
1. Abre [Wokwi](https://wokwi.com).
2. Crea un nuevo proyecto con un **ESP32**.
3. Agrega el sensor **MQ-135** y conéctalo al **pin 34**.
4. Copia el código de Wokwi y ejecútalo.
5. Corre el código de **visualización en Python** para recibir los datos desde **Flespi**.

# Screenshots
![image](https://github.com/user-attachments/assets/9f1e4948-1af3-4b7a-82b5-cac507d777ea)
![image](https://github.com/user-attachments/assets/ed298307-95ee-4a47-a203-a031d4764ec7)
![image](https://github.com/user-attachments/assets/bcc00685-eb7d-4a6e-afff-8c40e1b990d3)
