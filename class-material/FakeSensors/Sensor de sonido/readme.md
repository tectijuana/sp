# 📡 Sensor de sonido (MAX4466) y Visualizarlo en Flespi

- **Nombre:** Garcia Santos Jonathan  
- **GitHub:** [JONATHAN-GARCIA20]
- **Matrícula:** 22210307  

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
