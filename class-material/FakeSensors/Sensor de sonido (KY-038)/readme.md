# 📌 Integración del Sensor de Sonido KY-038 con ESP32 y Flespi

**Alumno**: Lennyn Alejandro Castillejo Robles  
**Materia**: Sistemas Programables

---

## 📖 Descripción
Este proyecto documenta la integración de un **ESP32** con un **Sensor de Sonido KY-038** para la monitorización de niveles de sonido en tiempo real.  
Los datos son enviados mediante **MQTT** desde **Wokwi** a **Visual Studio Code**, donde se procesan y reenvían a **Flespi** para su visualización en un **dashboard interactivo**.

---

## 🛠️ Tecnologías y Herramientas Utilizadas
- **ESP32** (Simulado en Wokwi)
- **MicroPython** (en ESP32 para lectura del sensor)
- **Mosquitto MQTT** (para comunicación entre dispositivos)
- **Paho MQTT (Python en VS Code)** (para recibir y reenviar datos)
- **Flespi MQTT** (para almacenamiento y visualización)
- **Wokwi** (Simulación del ESP32 y sensor KY-038)

---

## 🏗️ Implementación

### **1️⃣ Configuración del ESP32 en Wokwi**
Se programó un **ESP32 en Wokwi** con **MicroPython** para leer datos del **Sensor de Sonido KY-038** y enviarlos a **Mosquitto MQTT**.

```python
import machine
import network
import time
from umqtt.simple import MQTTClient

# Configuración WiFi en Wokwi
SSID = "Wokwi-GUEST"
PASSWORD = ""
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(1)

print("✅ WiFi Conectado.")

# Configurar MQTT
BROKER = "test.mosquitto.org"
TOPIC = "geps/sensor"
client = MQTTClient("esp32", BROKER)
client.connect()

# Configuración del sensor KY-038
adc = machine.ADC(machine.Pin(34))

while True:
    sonido = adc.read()  # Leer valor analógico
    client.publish(TOPIC, str(sonido))
    print(f"📤 Enviado: {sonido}")
    time.sleep(2)
    
  ```
  
![image](https://github.com/user-attachments/assets/afab46e4-2a3a-469f-b5fc-2a814e19781d)

  ## Código en python en visual code 
  ```
  import paho.mqtt.client as mqtt
import json

# Configuración de MQTT para Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "geps/sensor"

# Configuración de MQTT para Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "geps/sensor"
FLESPI_TOKEN = "9nMgowguNbbC43z3PaqxN22gqgSNCzz6cUeefWheFpXSTpAbBNA5eMHSkmAK7ogL"  #

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado a Wokwi MQTT Broker.")
        client.subscribe(WOKWI_TOPIC)
    else:
        print(f"❌ Error al conectar: {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Recibido de Wokwi: {payload}")
        
        # Convertir mensaje JSON
        data = json.loads(payload)
        sound_level = data.get("sound_level", 0)
        
        # Enviar datos a Flespi
        json_payload = json.dumps({"sound_level": sound_level})
        flespi_client.publish(FLESPI_TOPIC, json_payload)
        print(f"📤 Enviado a Flespi: {json_payload}")

    except Exception as e:
        print(f"⚠ Error procesando mensaje: {e}")

# Cliente MQTT para Wokwi
wokwi_client = mqtt.Client()
wokwi_client.on_connect = on_connect
wokwi_client.on_message = on_message

# Cliente MQTT para Flespi
flespi_client = mqtt.Client()
flespi_client.username_pw_set(FLESPI_TOKEN)
flespi_client.connect(FLESPI_BROKER, FLESPI_PORT)

# Conectar a los brokers
wokwi_client.connect(WOKWI_BROKER, WOKWI_PORT)
wokwi_client.loop_start()
flespi_client.loop_start()

print("📡 Esperando datos de Wokwi...")

# Mantener el script corriendo
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n🔌 Desconectando...")
    wokwi_client.disconnect()
    flespi_client.disconnect()

```
![image](https://github.com/user-attachments/assets/fe83e8d6-f1de-4b8e-83a5-80bcf672d447)


## Board en Flespi

![image](https://github.com/user-attachments/assets/b3f30971-85b0-417f-8531-70c930055e0b)

