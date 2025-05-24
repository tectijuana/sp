# Proyecto: Simulación de Sensor DHT22 en Wokwi con MQTT

**Autor:** [Arias Verdin Vivian C20211692]  
**Fecha:** [03/04/2025]  
**Descripción:** Este proyecto simula un sensor de temperatura y humedad DHT22 en Wokwi y envía los datos a un servidor MQTT.

---

# Código Wokwi

```python
import time
import network
from umqtt.simple import MQTTClient
import dht
import machine

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
TOPIC = "fake/dht22"
client = MQTTClient("esp32", BROKER)
client.connect()

# Configurar sensor DHT22
dht_sensor = dht.DHT22(machine.Pin(4))

# Bucle infinito para enviar datos cada 3 segundos
while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        payload = f"{{'temperature': {temp}, 'humidity': {hum}}}"
        client.publish(TOPIC, payload)
        print("📤 Enviado:", payload)
    except Exception as e:
        print("⚠️ Error al leer el sensor:", e)
    time.sleep(3)
```

# Código de Visualización en Python

```python
import paho.mqtt.client as mqtt

# Configuración de MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "fake/dht22"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado correctamente")
        client.subscribe(TOPIC)
    else:
        print(f"❌ Error de conexión: {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"📥 Recibido: {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
print("📡 Esperando datos...")
client.loop_forever()
```

#screenshot
![image](https://github.com/user-attachments/assets/575ed038-c5da-4640-9cb9-35c217fad97e)
![image](https://github.com/user-attachments/assets/981be6d2-1005-4c4e-a87f-adb3f4ab0650)
![image](https://github.com/user-attachments/assets/3933bdfa-7aee-46bc-ab27-a8e75ced8335)


