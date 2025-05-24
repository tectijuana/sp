# 📡 Sensor de Lluvia - MQTT  
**Autor:** Brandon Orozco Hernández  

Este código en Python permite recibir datos del **sensor de lluvia** a través de **Wokwi** y reenviarlos a **Flespi** mediante MQTT.  

## 🔧 Configuración  
- **Broker Wokwi:** `test.mosquitto.org`  
- **Broker Flespi:** `mqtt.flespi.io`  
- **Tópico MQTT:** `ebike/lluvia`  
![image](https://github.com/user-attachments/assets/1a4456bb-3591-4fd9-a7d6-68932b068cd8)
![image](https://github.com/user-attachments/assets/32a1c2c2-bab8-4520-a401-730e61ba59b4)
![image](https://github.com/user-attachments/assets/c0f6a4ea-5c8c-49d3-8e9c-20bfa82c234b)

## 📜 Código en Python  
```python
import time
import network
from umqtt.simple import MQTTClient
from machine import Pin, ADC

# Configurar WiFi en Wokwi
SSID = "Wokwi-GUEST"
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Conectando a WiFi...")
    time.sleep(1)

print("✅ WiFi Conectado. IP:", wifi.ifconfig()[0])

# Configurar MQTT
BROKER = "test.mosquitto.org"
TOPIC_LLUVIA = "ebike/lluvia"
client = MQTTClient("esp32", BROKER)
client.connect()

# Configurar sensor de lluvia (YL-83)
sensor_lluvia = ADC(Pin(34))  # Pin analógico 34
divisor = 4095  # ADC de 12 bits

# Bucle infinito para enviar datos cada 3 segundos
while True:
    # Leer sensor de lluvia
    valor_agua = sensor_lluvia.read()
    porcentaje = 100 - (valor_agua / divisor * 100)
    mensaje_lluvia = f"{porcentaje:.2f}% humedad"
    
    # Publicar datos
    client.publish(TOPIC_LLUVIA, mensaje_lluvia)
    
    print("📤 Lluvia Enviada:", mensaje_lluvia)
    
    time.sleep(3)

## 📜 Código en Wokwi

import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "ebike/lluvia"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "ebike/lluvia"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "W5Wy01hB7cD5DeenObhpdWnlExEBWtLSKzMy41hujkVvxMDbLfBTBvU5JjAH5Zv0"  # Reemplaza con tu token de Flespi

# Solución para la advertencia de deprecación
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado correctamente")
    else:
        print(f"❌ Error de conexión: {rc}")

def on_message_wokwi(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Recibido de Wokwi: {payload}")
        
        # Verificar si es un mensaje NMEA
        if payload.startswith('$GPGGA'):
            # Procesamiento básico de NMEA
            parts = payload.split(',')
            nmea_data = {
                'type': 'GPGGA',
                'time': parts[1],
                'latitude': f"{parts[2]} {parts[3]}",
                'longitude': f"{parts[4]} {parts[5]}",
                'fix_quality': parts[6],
                'satellites': parts[7],
                'hdop': parts[8],
                'altitude': f"{parts[9]} {parts[10]}",
                'raw': payload
            }
            
            # Convertir a JSON para enviar a Flespi
            json_payload = str(nmea_data).replace("'", '"')
            
            # Enviar a Flespi
            flespi_client.publish(FLESPI_TOPIC, json_payload)
            print(f"📤 Enviado a Flespi: {json_payload}")
        else:
            # Si no es NMEA, enviar tal cual
            flespi_client.publish(FLESPI_TOPIC, payload)
            print(f"📤 Enviado a Flespi (raw): {payload}")
            
    except Exception as e:
        print(f"⚠️ Error al procesar mensaje: {e}")

# Configurar cliente Wokwi (versión actualizada para evitar warning)
wokwi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
wokwi_client.on_message = on_message_wokwi
wokwi_client.on_connect = on_connect

# Configurar cliente Flespi
flespi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
flespi_client.username_pw_set(FLESPI_TOKEN)
flespi_client.on_connect = on_connect

try:
    # Conectar a Flespi
    flespi_client.connect(FLESPI_BROKER, FLESPI_PORT)
    flespi_client.loop_start()
    
    # Conectar a Wokwi
    wokwi_client.connect(WOKWI_BROKER, WOKWI_PORT)
    wokwi_client.subscribe(WOKWI_TOPIC)
    print("📡 Esperando datos de Wokwi...")
    
    # Mantener el script corriendo
    wokwi_client.loop_forever()
    
except KeyboardInterrupt:
    print("\n🔌 Desconectando...")
    wokwi_client.disconnect()
    flespi_client.disconnect()
except Exception as e:
    print(f"❌ Error crítico: {e}")

