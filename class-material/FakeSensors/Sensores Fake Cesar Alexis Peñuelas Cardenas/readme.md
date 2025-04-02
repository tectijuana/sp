# Sensor de vibración piezoeléctrico

**Nombre: Cesar Alexis Peñuelas Cardenas**

**Matricula: 22210335**

**Github: Cesarr777**

**Gist de GPS WOKWI: https://gist.github.com/Cesarr777/70ae0e49088ecaae7da736c26ab9b719**

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

![image](https://gist.github.com/user-attachments/assets/c5f6c9e8-9363-469b-8fb6-3fbc078b9df7)


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
 ![image](https://gist.github.com/user-attachments/assets/82f25bc7-1531-40b4-ad57-a0b74b34b3b1)

  # Datos en Flespi 
![image](https://gist.github.com/user-attachments/assets/2dd32f6a-8499-47c3-b8ac-ece67ca9518d)

# Sensor de CO (MQ-7)	

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
TOPIC = "wokwi/sensor2"
client = MQTTClient("esp32", BROKER)
client.connect()

# Bucle infinito para enviar datos cada 3 segundos
while True:
    co_value = random.uniform(0.1, 10.0)  # Simular lectura del sensor MQ-7 (CO en ppm)
    client.publish(TOPIC, str(co_value))
    print("📤 Enviado:", co_value, "ppm")
    time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato
```

![image](https://gist.github.com/user-attachments/assets/668403fe-620e-4caa-bd7e-986827063410)

 # Codigo python que sirve como puente
 ```
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "wokwi/sensor2"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "wokwi/sensor2"  # Puedes cambiarlo según tus necesidades
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
![image](https://gist.github.com/user-attachments/assets/8d68b106-715c-4da5-88cc-6c8a456ab4d7)

  # Datos en Flespi 
  
![image](https://gist.github.com/user-attachments/assets/780e73bf-3687-448d-916d-4e3d40f2cb5c)

# GPS DE WOKWI A MQTT
# Puente MQTT: De Wokwi a Flespi

**Nombre: Cesar Alexis Peñuelas Cardenas**

**Matricula: 22210335**

**Github: Cesarr777**

## 📌 Descripción
Script Python que funciona como puente MQTT para:
1. Recibir datos GPS en formato NMEA que vienen desde Wokwi
2. Parsear y transformar los datos a JSON
3. Reenviar la información estructurada a Flespi

## Codigo de Woski donde se envian los datos
```
import time
import network
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
TOPIC = "wokwi/gps"
client = MQTTClient("esp32", BROKER)
client.connect()

# Datos GPS simulados
gps_data = [
    "$GPGGA,000001,1223.2062,S,1758.2865,E,1,08,0.9,0.0,M,0.0,M,,*47",
    "$GPGGA,000002,0669.3645,S,3417.3205,E,1,08,0.9,0.0,M,0.0,M,,*47",
    "$GPGGA,000003,0000.4581,S,3790.7421,E,1,08,0.9,0.0,M,0.0,M,,*47"
]

# Bucle infinito para enviar datos cada 3 segundos
while True:
    for sentence in gps_data:
        client.publish(TOPIC, sentence)
        print("📤 Enviado:", sentence)
        time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato
```

![image](https://gist.github.com/user-attachments/assets/90f814b0-ba5e-4e4d-b2c3-4e51d8d1761a)

 
 # Codigo python que sirve como puente
 ```
 import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "wokwi/gps"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "wokwi/gps"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "S5nwLfn6PTi0T0KPXssvsXARXOkX2Hzhj72axFIIotsKNnDvuGAiI8CqpF3Bgbtz"  # Reemplaza con tu token de Flespi

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
  ![image](https://gist.github.com/user-attachments/assets/42996463-0445-4410-9fb3-729be696623c)

  # Datos en Flespi 
  ![image](https://gist.github.com/user-attachments/assets/c3ef97a6-cb0b-4e71-a584-bfe671521c3d)
 







