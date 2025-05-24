# 📡 Sensor de presión barométrica(BMP280) y Visualizarlo en Flespi

- **Nombre:** Garcia Santos Jonathan  
- **GitHub:** [JONATHAN-GARCIA20]
- **Matrícula:** 22210307  

# 📌 Sensor de presión barométrica(BMP280)

# 📌 Introducción

El sensor de presión barométrica BMP280 es un módulo de alta precisión diseñado para medir la presión atmosférica y la temperatura. Gracias a su bajo consumo de energía y alta sensibilidad, es ampliamente utilizado en aplicaciones como estaciones meteorológicas, altímetros, drones y monitoreo ambiental.

En este proyecto, utilizaremos un ESP32 para leer los datos del BMP280 a través del protocolo I2C y enviarlos a un servidor MQTT en la nube. La simulación se realizará en Wokwi, donde generaremos valores aleatorios para representar los datos del sensor en ausencia de hardware real.

# 🛠️ Codigo en Wokwi
```
import network
import random  # Solo para la simulación en Wokwi
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
TOPIC = "wokwi/sensor/bmp280"
client = MQTTClient("esp32", BROKER)
client.connect()

# Bucle infinito para enviar datos cada 3 segundos
while True:
    try:
        # Simulación en Wokwi (generar valores aleatorios en lugar de leer del sensor real)
        presion = random.uniform(95000, 105000)  # Presión en Pa
        temperatura = random.uniform(15, 30)  # Temperatura en C (sin símbolo especial)
        
        mensaje = f"Presion: {presion:.2f} Pa, Temp: {temperatura:.2f} C"  # Sin caracteres especiales
        client.publish(TOPIC, mensaje.encode('utf-8'))  # Codificar en UTF-8
        print("📤 Enviado:", mensaje)
    
    except Exception as e:
        print("⚠️ Error simulando el sensor:", e)
    
    time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato


```

![image](https://github.com/user-attachments/assets/cbf537b1-8917-48e5-a037-2a4b91ca439c)

# 📌Visualizar datos en Flespi

![image](https://github.com/user-attachments/assets/03101277-da08-4cc1-8666-df66b081bf66)

