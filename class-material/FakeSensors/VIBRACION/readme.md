# Sensor de vibración piezoeléctrico

**Nombre: Cesar Alexis Peñuelas Cardenas**

**Matricula: 22210335**

**Github: Cesarr777**

## 📌 Descripción
Script Python que funciona como puente MQTT para:
1. Recibir datos del sensor que vienen desde Wokwi
2. Parsear y transformar los datos a JSON
3. Reenviar la información estructurada a Flespi

## Codigo de Woski donde se envian los datos
```
import time
import network
import random
from umqtt.simple import MQTTClient

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
TOPIC = "wokwi/sensor1"
client = MQTTClient("esp32", BROKER)
client.connect()

# Bucle infinito para enviar datos cada 3 segundos
while True:
    vibration_value = random.randint(0, 1023)  # Simular lectura del sensor piezoeléctrico
    client.publish(TOPIC, str(vibration_value))
    print("📤 Enviado:", vibration_value)
    time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato
```

![image](https://github.com/user-attachments/assets/0b8b9d69-b72b-4a46-ac5a-a1d44e3d4dec)


 # Codigo python que sirve como puente
 ```
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "wokwi/sensor1"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "wokwi/sensor1"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "CbGNcrGPnhcZoghrbCPkVhenEey1qeTPs1AkacRFcbC3uFNm11gr1stlduUMyzjg"  # Reemplaza con tu token de Flespi

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
    
  ```
![image](https://github.com/user-attachments/assets/d33bd141-127d-4333-b0bb-1caa927c55a6)

  # Datos en Flespi 
![image](https://github.com/user-attachments/assets/83dbf7a4-7e0c-4ead-a9ec-98da17de71c6)
