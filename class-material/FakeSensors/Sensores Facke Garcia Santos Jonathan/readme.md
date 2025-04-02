# 📡 Práctica: Simulación de Sensor GPS y tambien funsionamiento de sensores: Sensor de presión barométrica (BMP280), Sensor de sonido (MAX4466) y Visualizarlo en Flespi

- **Nombre:** Garcia Santos Jonathan  
- **GitHub:** [JONATHAN-GARCIA20]
- **Matrícula:** 22210307  

# 📌 Sensor GPS

# 📌 Introducción
La práctica consiste en generar manualmente los trazos de una ruta utilizando la herramienta geojson.io (https://geojson.io/#map=1.75/24.3/-147.7). A través de esta plataforma, se crea un código que representa la ruta, el cual luego debe ser formateado en el estándar de coordenadas EMEA. Una vez que las coordenadas estén adecuadamente estructuradas, se utilizará Wokwi (https://wokwi.com/) para emular una placa y trabajar con sensores, simulando su funcionamiento en un entorno controlado.

# 🛠️ Codigo en Wokwi
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
TOPIC = "gps/wokwi"
client = MQTTClient("esp32", BROKER)
client.connect()

# Datos GPS simulados
gps_data = [
    "$GPGGA,000001,3231.7212,S,11253.7894,O,1,08,0.9,0.0,M,0.0,M,,*47",
    "$GPGGA,000002,2950.7210,S,11050.7061,O,1,08,0.9,0.0,M,0.0,M,,*47",
    "$GPGGA,000003,2914.4374,S,10725.6086,O,1,08,0.9,0.0,M,0.0,M,,*47"
]

# Bucle infinito para enviar datos cada 3 segundos
while True:
    for sentence in gps_data:
        client.publish(TOPIC, sentence)
        print("📤 Enviado:", sentence)
        time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato
```
![image](https://github.com/user-attachments/assets/ab8c1895-2573-4530-a3cd-c89e167a0800)

Podemos apreciar como aqui se mandan los datos correctamnete de las cordenadas.

# 💾 **Codigo en Python para recibir los datos que nos envia Wokwi para poder mandarlo a flespi**  

Guardamos el archivo con la extencion NombreArchivo.py
```python
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "gps/wokwi"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "wokwi/gps"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "NrYSDc8w7sl9NRRd73b3a4ubtdIAyLbplrrsBpuyvsYbP4hx9BgQCGlWQaGn5r7c"  # Reemplaza con tu token de Flespi

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
        print(f"⚠ Error al procesar mensaje: {e}")

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
    print(f"❌ Error crítico: {e}")
```
Ejecutamons el archivo ( Nos aparecera lo siguiente en la Terminal)

![image](https://github.com/user-attachments/assets/12fecd8b-e730-47ca-8513-8fab420651c1)

Podemos apreciar qui que estamos resiviendo los datos correctamnte que nos envia Wokwi

# 📌Visualizar datos en Flespi

- Accede a Flespi y ve a MQTT Board.
- Suscríbete al TOPIC que declaramos el el codigo en este caso ( gps/wokwi )
![image](https://github.com/user-attachments/assets/312bff13-ddc7-412e-8266-6754afed0c71)

- Aqui lo vemos de una forma rapida pero igual lo podemos ver de una forma mas visual.
- Esto agregando un Widget para verlo de forma grafica en tiempo Real

![image](https://github.com/user-attachments/assets/58e660ef-e7c6-41ae-b330-e5992ccb3410)

# 📌 Sensor de presión barométrica (BMP280)



# 📌 Sensor de sonido (MAX4466)

# 📌 Introducción

El sensor de sonido MAX4466 es un amplificador de micrófono de alta ganancia diseñado para capturar variaciones en el nivel de sonido y convertirlas en señales analógicas. Este tipo de sensor es útil para aplicaciones como monitoreo de ruido ambiental, detección de voz y activación por sonido.

En este proyecto, utilizaremos un ESP32 para leer los datos del MAX4466 a través de su conversor analógico-digital (ADC) y enviarlos a un servidor MQTT en la nube. La simulación se realizará en Wokwi, donde generaremos valores aleatorios para representar los datos del sensor en ausencia de hardware real.

# 🛠️ Codigo en Wokwi
```
import time
import network
import random  # Solo para la simulación en Wokwi
from umqtt.simple import MQTTClient
from machine import ADC, Pin

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
TOPIC = "wokwi/sensor/max4466"
client = MQTTClient("esp32", BROKER)
client.connect()

# Configurar el sensor de sonido MAX4466 (entrada analógica en pin 34)
sound_sensor = ADC(Pin(34))
sound_sensor.atten(ADC.ATTN_11DB)  # Configurar el rango de entrada (hasta 3.6V)

# Bucle infinito para enviar datos cada 3 segundos
while True:
    sonido = sound_sensor.read()  # Leer valor analógico (0 - 4095 en ESP32)
    
    # Simulación en Wokwi (si no tienes el sensor físico, usa valores aleatorios)
    if not sonido:
        sonido = random.randint(1000, 3000)
    
    mensaje = f"Nivel de sonido: {sonido}"
    client.publish(TOPIC, mensaje)
    print("📤 Enviado:", mensaje)
    
    time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato

```

![image](https://github.com/user-attachments/assets/52ee818b-5a6c-40bc-8052-545d6b31ae75)

# 📌Visualizar datos en Flespi

![image](https://github.com/user-attachments/assets/7f4de2e5-00ba-4f60-8cff-ee75166b2790)


