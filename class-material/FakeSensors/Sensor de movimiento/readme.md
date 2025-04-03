# Sensor de Movimiento con Radar (RCWL-0516)  
**Autor:** Brandon Orozco Hernandez  

## 📡 **Requisitos**  
- **ESP32** con MicroPython  
- **Broker MQTT** (Mosquitto o Flespi)  
- **Conexión WiFi**
- ---

## 📸 **Captura de Pantalla de Terminal de Python**
![image](https://github.com/user-attachments/assets/4fdbd15f-5e29-4c0a-a7b5-ccdfd2877561)
## 📸 **Captura de Pantalla de Terminal de Wokwi**
![image](https://github.com/user-attachments/assets/360c5533-73b7-4bc0-a922-b1ee77268391)
## 📸 **Captura de Pantalla de Terminal de Flepsi**
![image](https://github.com/user-attachments/assets/2c8d9357-a172-4ce0-9bd5-d14d7e869109)


## Código en wokwi y en python

```python
import time
import network
from umqtt.simple import MQTTClient
from machine import Pin

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
TOPIC_MOVIMIENTO = "ebike/movimiento"
client = MQTTClient("esp32", BROKER)
client.connect()

# Configurar sensor de movimiento (RCWL-0516)
sensor_movimiento = Pin(34, Pin.IN)  # RCWL-0516 conectado al GPIO 34

# Bucle infinito para detectar y enviar datos
while True:
    if sensor_movimiento.value() == 1:  # Detecta movimiento
        mensaje = "Movimiento detectado"
        client.publish(TOPIC_MOVIMIENTO, mensaje)
        print("📤 Publicado en MQTT:", mensaje)
        time.sleep(2)  # Espera para evitar spam de mensajes

    time.sleep(0.1)  # Pequeña pausa para evitar sobrecarga
## ⚡ **Código en Python**  

```python
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "ebike/movimiento"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "ebike/movimiento"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "JsEaMID8LzTRfmwfWDGY5FA8JIghV3I9BokckxocuIXM0cavcwjB5dekB1kJHKyG"  # Reemplaza con tu token de Flespi

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
        
        # Enviar directamente a Flespi
        flespi_client.publish(FLESPI_TOPIC, payload)
        print(f"📤 Enviado a Flespi: {payload}")
            
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



