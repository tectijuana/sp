###  📌 Simulador de Sensor de Distancia Láser y Sensor de Voltaje con Representación en Flespi 📌

**Nombre:** Carlos Alberto Iñiguez Gallego  
**Número de Control:** 19211660  
**GitHub:** [CarlosAlberto193](https://github.com/CarlosAlberto193)

---
# Sensor de voltaje (ZMPT101B)	
<p align="center">
  <img src="https://uelectronics.com/wp-content/uploads/2019/10/AR1197-ZMPT101B-800x800.jpg" width="400">
</p>

Es un módulo diseñado para medir voltajes de corriente alterna (CA) de manera precisa y segura. Utiliza un pequeño transformador de medida (ZMPT101B) junto con un circuito de acondicionamiento de señal para convertir la señal de CA en un voltaje adecuado para microcontroladores como Arduino o ESP32.

**Características principales:**
- Rango de medición: 0V - 250V CA (depende de la calibración).
- Alta precisión en la detección de voltaje.
- Salida analógica proporcional al voltaje de entrada.
- Aislamiento eléctrico seguro gracias al transformador integrado.
## 1️⃣ Planeacion del Proyecto
La mayor dificultad para mi persona al momento de desarrollar este trabajo, viene del hecho de que no habia trabajo nunca con Flespi o propiamente con Wokwi (Comprendia su funcion pero nunca su uso), el mayor complejo resulto ser el aprender a trabajar con plataformas con una limitada lista de recursos par ami estudio.

Dicho esto, al momento de formalizar y plantear el proyecto me di cuenta que no era dificil demas, y la utilidad que se busca cumplir con Wokwi es solamente resultado de no tener la capacidad por parte de la Universidad para aprender apartir de Sensores o Placas de la propia institucion

Otro punto que cabe aclarar es que el trabajo pasado (Fake GPS) me dejo en perfecta condicion para continuar con Flespi, la cual es una plataforma con la que nunca tuve que trabajar en el pasado.

De igual manera, las misma regla continue, en donde trabaje con Python de manera local para enviar la informacion, añadiendo un paso mas a mi desarrollo.

## 2️⃣ Codigo del Proyecto
### Codigo de Wokwi:
```python
import time
import network
from umqtt.simple import MQTTClient
from machine import ADC, Pin

# Configuración del Wi-Fi
SSID = "Wokwi-GUEST"
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Conectando a WiFi...")
    time.sleep(1)

print("✅ WiFi Conectado. IP:", wifi.ifconfig()[0])

# Configuración MQTT
BROKER = "test.mosquitto.org"
TOPIC = "voltaje/sensor"
client = MQTTClient("esp32", BROKER)
client.connect()

# Configurar el sensor de voltaje en el GPIO34
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB) 

# Bucle infinito para leer y enviar datos cada 3 segundos
while True:
    valor_analogico = adc.read()
    voltaje = valor_analogico * (3.3 / 4095)  

    payload = "{:.2f}".format(voltaje)  
    client.publish(TOPIC, payload)
    print("📤 Enviado:", payload)
    time.sleep(3)
```
### Código Python
```python
import paho.mqtt.client as mqtt # type: ignore

# Configuración del broker de Wokwi (Mosquitto)
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_TOPIC = "voltaje/sensor"

# Configuración del broker de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_TOPIC = "voltaje"
FLESPI_TOKEN = "N1jjPhpPJOlsDOb67SCRqfRDpiNNfsETkHn8ioNoJbJK2kchzca0e0FlU9mMviwg"

# Función cuando se recibe un mensaje desde Wokwi
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Recibido de Wokwi: {payload}")

        # Enviar a Flespi
        flespi_client.publish(FLESPI_TOPIC, payload)
        print(f"📤 Enviado a Flespi: {payload}")

    except Exception as e:
        print(f"⚠ Error al procesar mensaje: {e}")

wokwi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
wokwi_client.on_message = on_message
flespi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
flespi_client.username_pw_set(FLESPI_TOKEN)

try:
    # Conectar a Flespi
    flespi_client.connect(FLESPI_BROKER, 1883)
    flespi_client.loop_start()

    # Conectar a Wokwi
    wokwi_client.connect(WOKWI_BROKER, 1883)
    wokwi_client.subscribe(WOKWI_TOPIC)
    print("📡 Escuchando datos de Wokwi...")
    wokwi_client.loop_forever()

except KeyboardInterrupt:
    print("\n🔌 Desconectando...")
    wokwi_client.disconnect()
    flespi_client.disconnect()
except Exception as e:
    print(f"❌ Error crítico: {e}")
```

## 3️⃣ Pruebas de Desarrollo
<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/A.PNG" width="600">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/B.PNG" width="600">
</p>

## 4️⃣ Aplicacion en Flespi
<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/C.PNG" width="600">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/D.PNG" width="600">
</p>

## 5️⃣ Video en Loom del Funcionamiento
<p align="center">
<a href="https://www.loom.com/share/d544fdf5d93245758e49ce623a323241?sid=2b7c42d7-2dc0-407f-accf-9288e8f6c0d5">
  <img src="https://cdn.loom.com/sessions/thumbnails/d544fdf5d93245758e49ce623a323241-1084cc11e6b8f4e6.jpg" width="750">
</a>
</p>

---

# 🔍 Sensor de Distancia Láser - VL53L0X 🔍
<p align="center">
  <img src="https://uelectronics.com/wp-content/uploads/2018/07/AR0493-VL53L0X.jpg" width="400">
</p>

El **VL53L0X** es un sensor láser basado en tecnología **Time-of-Flight** que permite medir distancias con alta precisión sin contacto. Ideal para robótica, IoT y automatización.

**🔧 Características principales:**
- Rango de medición: 30 mm - 2000 mm (dependiendo de la superficie y luz)
- Precisión de hasta 1 mm
- Comunicación I2C
- Bajo consumo energético y tiempo de respuesta rápido

## 1️⃣ Planeación del Proyecto
La necesidad de realizar el trabajo con ambos sensores para poder entregar el trabajo me corrigio de mi esperada simplicidad, sin embargo la entrega de la prueba con el sensor de Distancia Láser sigue las mismas reglas con las que he trabajado y he tenido que aprender; dicho esto hubo una complicacion no logre ver a primera vista: De manera general; una placa ESP32 en Wokwi no almacena la biblioteca para un sensor VL53L0X

Si uno quiere hacer uso de las capacidades de la plataforma para de manera automatica añadir las bibliotecas que uno necesita para cada proyecto, no cuento con tanta suerte debido a que esta es de paga; Sin embargo me vi con la suerte de encontrar una biblioteca que operara en .py de este sensor.
## 2️⃣ Código del Proyecto

### 💻 Código para ESP32 en Wokwi

```python
import time
import network
from umqtt.simple import MQTTClient
from machine import Pin, I2C
import VL53L0X

# Configuración Wi-Fi
SSID = "Wokwi-GUEST"
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Conectando a Wi-Fi...")
    time.sleep(1)

print("✅ Conectado a Wi-Fi. IP:", wifi.ifconfig()[0])

# Configuración MQTT
BROKER = "test.mosquitto.org"
TOPIC = "distancia/sensor"
client = MQTTClient("esp32", BROKER)
client.connect()

# Inicializar el sensor VL53L0X
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sensor = VL53L0X.VL53L0X(i2c)

# Bucle principal
while True:
    distancia = sensor.read()
    distancia_cm = distancia / 10
    payload = "{:.2f}".format(distancia_cm)
    client.publish(TOPIC, payload)
    print("📤 Enviado:", payload)
    time.sleep(3)
```

### 🐍 Código Python (Puente entre Wokwi y Flespi)

```python
import paho.mqtt.client as mqtt

# Configuración MQTT
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_TOPIC = "distancia/sensor"

FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_TOPIC = "distancia"
FLESPI_TOKEN = "TU_TOKEN_DE_FLESPI"

# Función para manejar mensajes entrantes
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Recibido de Wokwi: {payload}")
        flespi_client.publish(FLESPI_TOPIC, payload)
        print(f"📤 Enviado a Flespi: {payload}")
    except Exception as e:
        print(f"⚠ Error: {e}")

# Clientes MQTT
wokwi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
wokwi_client.on_message = on_message

flespi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
flespi_client.username_pw_set(FLESPI_TOKEN)

try:
    flespi_client.connect(FLESPI_BROKER, 1883)
    flespi_client.loop_start()

    wokwi_client.connect(WOKWI_BROKER, 1883)
    wokwi_client.subscribe(WOKWI_TOPIC)

    print("📡 Escuchando datos de Wokwi...")
    wokwi_client.loop_forever()

except KeyboardInterrupt:
    print("\n🔌 Desconectando...")
    wokwi_client.disconnect()
    flespi_client.disconnect()

except Exception as e:
    print(f"❌ Error crítico: {e}")
```

## 3️⃣ Pruebas de Desarrollo

<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/I.PNG" width="600">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/II.PNG" width="600">
</p>

## 4️⃣ Visualización en Flespi

<p align="center">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/III.PNG" width="600">
  <img src="https://raw.githubusercontent.com/CarlosAlberto193/GPSRuta/main/Imagenes/IV.PNG" width="600">
</p>

---

## 5️⃣ 🎥 Video del Funcionamiento

<p align="center">
<a href="https://www.loom.com/share/0d9059122437448ea6a69cadac07e5d0?sid=b8c2a7d5-d41c-49e3-a4b6-1dc6bff5fa8a">
  <img src="https://cdn.loom.com/sessions/thumbnails/71c11acc4538480fadf84b376de30c20-fdd36f698e4ab127.jpg" width="750">
</a>
</p>


---
**Referencias**

Uceeatz. (n.d.). VL53L0X.py [Python script]. GitHub. https://github.com/uceeatz/VL53L0X/blob/master/VL53L0X.py

ElectroNOOBS. (2020, September 27). ESP32 VL53L0X Laser TOF sensor Arduino tutorial [Video]. YouTube. https://www.youtube.com/watch?v=SWBI6_rxmT8
