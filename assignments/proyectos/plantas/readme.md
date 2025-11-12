![](screen.png)

## 🌿 **Práctica IoT: Sistema Inteligente para el Cuidado de Plantas con Wokwi, Flespi y Dashboard Web**

### 🎯 **Objetivo**

Diseñar un sistema IoT que simule un entorno real de agricultura doméstica inteligente. Se utilizarán **5 sensores simulados**, conectados a unas Raspberry Pi Pico W emuladas en **Wokwi**, que transmitirán datos a **Flespi IoT portal MQTT** como si estuviera operando en un sistema de control remoto distribuido. Los datos serán visualizados en un **dashboard web dinámico** tipo "Plant Care Pro" según su propuesta.

---

## 🌐 **Descripción del Escenario**

Imagina que esta app está **conectada a una red de controladores remotos en tiempo real** a través de **Flespi**, un broker MQTT que actúa como intermediario entre tus dispositivos (Pico W) y el sistema de monitoreo.
Cada dispositivo puede estar ubicado en una macetas distintas dentro de un invernadero o una casa.
La app representa un **centro de monitoreo de plantas**, visualizando el estado de cada una mediante sus sensores como si estuviera conectada remotamente a varias estaciones IoT.

---

## 🧩 **Componentes del Proyecto**

### ✅ Hardware virtual (simulado en Wokwi):

Utilizando el simulador Wokwi con Raspberry Pi Pico W:

1. 🌱 **Humedad del Suelo** – variable simulada
2. 🌡️ **Temperatura y Humedad** – DHT22
3. 💡 **Sensor de Luz** – LDR
4. 🫁 **Calidad de Aire** – MQ135 simulado con potenciómetro
5. 💧 **Nivel de Agua** – digital (0/1) o con potenciómetro

> Cada sensor representa una entrada de datos crítica para la planta.

---

## 📡 **Conexión a Flespi (Control Remoto Simulado)**

* El **Pico W simulado en Wokwi** se conecta a **Flespi MQTT**, funcionando como una estación remota.
* Se publica cada lectura a un tópico diferente con el siguiente esquema:

```bash
plantcare/{planta_id}/soil
plantcare/{planta_id}/temp
plantcare/{planta_id}/light
plantcare/{planta_id}/air
plantcare/{planta_id}/water
```

* Esto simula que el sistema **recibe datos desde múltiples plantas distribuidas en el hogar o jardín**, cada una identificada por su `planta_id`.

---

## 🧠 **Lógica del Dispositivo (Edge Computing)**

* El Pico W lee sensores cada 10 segundos.
* Publica al broker Flespi solo si hay cambios significativos.
* Usa reconexión automática si se pierde conexión MQTT.
* Incluye fallas intencionales como:

  * Pico aleatorio de temperatura a 80 °C.
  * Valor `None` en humedad del suelo.
  * Sensor de agua siempre en 0.

---

## 📺 **Dashboard Web (HTML + Tailwind + JS)**

Basado en tu archivo `code.html`, los alumnos deben:

* Mostrar tarjetas por planta/sensor.
* Cambiar colores o íconos según umbral crítico.
* Mostrar alertas (como un "controlador remoto" avisando al usuario).
* Simular múltiples plantas escuchando de varios tópicos (`plantcare/1/...`, `plantcare/2/...`).

> Se puede consumir desde Flespi vía:

* API REST (Flespi REST Streams)
* WebSocket → si intermedio con Flask o Node.js

---

## 🧪 **Extras de Simulación**

* Simular múltiples plantas con diferentes sensores conectados.
* Agregar botón de riego manual (solo visual).
* Usar un archivo JSON para mostrar histórico local.
* Visualización en tiempo real como si fuera un **panel de control remoto industrial**.

---

## 📐 **Rúbrica de Evaluación**

| Criterio                                               | Puntos |
| ------------------------------------------------------ | ------ |
| Uso de 5 sensores físicos o virtuales en Wokwi         | 30     |
| Conexión funcional MQTT con Flespi como control remoto | 20     |
| Dashboard responsivo que consume datos                 | 20     |
| Alertas visuales + simulación de múltiples plantas     | 10     |
| Estética, lógica, modularidad del código               | 10     |
| **Total**                                              | **90** |

---

## 📘 **Material de apoyo sugerido**

* Simulador: [https://wokwi.com](https://wokwi.com)
* Broker: [https://flespi.io](https://flespi.io)
* JS MQTT: [Paho MQTT JS](https://www.eclipse.org/paho/)
* Libro de apoyo: *IoT Visualizations using Grafana*

---

## 🧠 1. **Código MicroPython para Wokwi con Pico W + MQTT (Flespi)**

> ✅ Este código envía datos simulados de 5 sensores al broker MQTT de **Flespi** desde un **Raspberry Pi Pico W** emulado en **Wokwi**.

### 🧪 Simulación de sensores: valores aleatorios para temperatura, humedad, luz, CO₂ y agua.

```python
# micropython_flespi_wokwi.py
import network
import time
import ubinascii
import machine
import ujson
from umqtt.simple import MQTTClient
from random import randint

# ======= WiFi Configuration =======
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# ======= Flespi MQTT Config =======
FLESPI_TOKEN = "FlespiToken YOUR_TOKEN_HERE"
MQTT_BROKER = "mqtt.flespi.io"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())

# ======= MQTT Topics =======
BASE_TOPIC = "plantcare/1/"
TOPICS = {
    "soil": BASE_TOPIC + "soil",
    "temp": BASE_TOPIC + "temp",
    "light": BASE_TOPIC + "light",
    "air": BASE_TOPIC + "air",
    "water": BASE_TOPIC + "water"
}

# ======= Connect to WiFi =======
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("Connected to WiFi:", wlan.ifconfig())

# ======= Simulate Sensor Data =======
def read_sensors():
    return {
        "soil": randint(20, 60),
        "temp": randint(18, 35),
        "light": randint(300, 1000),
        "air": randint(400, 800),
        "water": randint(0, 1)
    }

# ======= Connect to MQTT =======
def connect_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, user="", password=FLESPI_TOKEN)
    client.connect()
    print("Connected to Flespi MQTT")
    return client

# ======= Main Loop =======
connect_wifi()
client = connect_mqtt()

while True:
    data = read_sensors()
    for key, topic in TOPICS.items():
        value = data[key]
        client.publish(topic, str(value))
        print(f"Published {key}: {value} to {topic}")
    time.sleep(5)
```

> ⚠️ **Reemplaza** `"YOUR_TOKEN_HERE"` por tu **token real de Flespi**.

---

## 🌐 2. **Código JavaScript para el Dashboard (HTML) que escucha Flespi**

> ⚠️ Esta es una forma *simple* que requiere tener un backend intermedio (Flask, Node.js o Replit) que consuma Flespi y exponga una API REST o WebSocket.

### Opción rápida: Simula el consumo con JSON estático (para pruebas de frontend)

```html
<script>
async function fetchSensorData() {
  // Simulación de API REST que sirve valores desde Flespi o local
  const response = await fetch("https://mi-api.intermedia.io/sensores"); // cambia por tu endpoint real
  const data = await response.json();

  document.getElementById("soil").innerText = data.soil + "%";
  document.getElementById("temp").innerText = data.temp + "°C";
  document.getElementById("light").innerText = data.light + " lx";
  document.getElementById("air").innerText = data.air + " ppm";
  document.getElementById("water").innerText = data.water === 1 ? "OK" : "VACÍO";

  // Cambiar colores o íconos si hay alertas
  if (data.soil < 30) {
    document.getElementById("soil").style.color = "red";
  } else {
    document.getElementById("soil").style.color = "green";
  }
}

setInterval(fetchSensorData, 5000); // cada 5 segundos
</script>
```

> Para usarlo con Flespi **directamente**, se recomienda un backend Python como Flask que consuma MQTT y reexponga los datos como REST para el dashboard.

---
¡Excelente decisión! Aquí tienes un ejemplo de **backend en Python con Flask** que:

1. **Se conecta al broker MQTT de Flespi** como suscriptor.
2. Guarda los últimos datos recibidos de los sensores.
3. Expone una **API REST** (`/sensores`) para que el dashboard en HTML pueda leerlos fácilmente.

---

## 🧠 Backend Flask + MQTT (Python 3.x)

> Requisitos:

* `flask`
* `paho-mqtt`

Instala con:

```bash
pip install flask paho-mqtt
```

---

### `app.py` (servidor Flask)

```python
from flask import Flask, jsonify
import paho.mqtt.client as mqtt
import threading

app = Flask(__name__)

# Flespi MQTT config
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_TOKEN = "FlespiToken YOUR_TOKEN_HERE"
TOPICS = [
    ("plantcare/1/soil", 0),
    ("plantcare/1/temp", 0),
    ("plantcare/1/light", 0),
    ("plantcare/1/air", 0),
    ("plantcare/1/water", 0)
]

# Data store
sensor_data = {
    "soil": None,
    "temp": None,
    "light": None,
    "air": None,
    "water": None
}

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to Flespi with result code", rc)
    for topic in TOPICS:
        client.subscribe(topic)
        print("Subscribed to", topic[0])

def on_message(client, userdata, msg):
    key = msg.topic.split("/")[-1]
    try:
        val = int(msg.payload.decode())
        sensor_data[key] = val
    except Exception as e:
        print("Error decoding message:", e)

# MQTT Thread
def start_mqtt():
    client = mqtt.Client()
    client.username_pw_set(FLESPI_TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(FLESPI_BROKER, 1883, 60)
    client.loop_forever()

# Start MQTT client in background
mqtt_thread = threading.Thread(target=start_mqtt)
mqtt_thread.daemon = True
mqtt_thread.start()

# REST endpoint
@app.route("/sensores")
def get_sensores():
    return jsonify(sensor_data)

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```
---
## 📺 Pico W con Display OLED

La pantalla OLED se encargará de desplegar los datos de una sexta planta simulada en la Pico W
El siguiente codigo muesta como se simulan estos datos y se envian al display OLED

```
# plant6_local_oled.py
# Simula sensores de "Planta 6" y los muestra en OLED SSD1306 (MicroPython, Pico W)
# NO envía datos a ningún broker.

from machine import Pin, I2C
import time
import random
import ssd1306

# ===== CONFIGURACIÓN DEL OLED =====
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

PLANT_NAME = "Planta 6"

# ===== UMBRALES PARA ALERTAS =====
SOIL_THRESHOLD = 25      # % por debajo → riego urgente
LIGHT_THRESHOLD = 100    # lux por debajo → baja luz
AIR_THRESHOLD = 800      # valor por encima → mala calidad / alerta

# ===== FUNCIONES =====
def read_sensors():
    """Simula lecturas de sensores."""
    return {
        "soil": round(random.uniform(18.0, 60.0), 1),   # humedad suelo %
        "temp": round(random.uniform(16.0, 32.0), 1),   # temperatura °C
        "light": random.randint(20, 900),               # lux
        "air": random.randint(300, 950),                # índice/ppm
        "water": random.choice([0, 1])                  # 0 = vacío, 1 = OK
    }

def evaluate_status(data):
    """Evalúa las condiciones y devuelve un texto de estado."""
    msgs = []
    if data["soil"] < SOIL_THRESHOLD:
        msgs.append("RIEGO!")
    if data["light"] < LIGHT_THRESHOLD:
        msgs.append("Luz baja")
    if data["air"] > AIR_THRESHOLD:
        msgs.append("Aire malo")
    if data["water"] == 0:
        msgs.append("Agua BAJA")
    if not msgs:
        return "ESTADO: SANO"
    return " ".join(msgs)

def show_display(data, status):
    """Muestra las lecturas y estado en el OLED."""
    oled.fill(0)
    oled.text(PLANT_NAME, 0, 0)
    oled.text("T:{:.1f}C S:{:.0f}%".format(data["temp"], data["soil"]), 0, 16)
    oled.text("L:{:d}lx A:{:d}".format(data["light"], data["air"]), 0, 32)
    water_txt = "Agua:OK" if data["water"] == 1 else "Agua:BAJO"
    oled.text(water_txt, 0, 48)
    oled.show()

    # Si hay alertas, mostrar una segunda pantalla de estado por 1s
    if status != "ESTADO: SANO":
        time.sleep(1)
        oled.fill(0)
        oled.text("ALERTA!", 0, 0)
        oled.text(status[:16], 0, 16)
        if len(status) > 16:
            oled.text(status[16:32], 0, 32)
        oled.show()
        time.sleep(1)

# ===== PROGRAMA PRINCIPAL =====
def main():
    try:
        while True:
            data = read_sensors()
            status = evaluate_status(data)
            show_display(data, status)

            # Mostrar también por consola (Thonny Shell)
            print("Datos:", data, "|", status)

            time.sleep(5)

    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()
        print("Programa detenido por usuario.")

# ===== Ejecutar =====
main()
```
---

## 🌐 Cómo probar

1. Ejecuta `app.py` (tu Flask + MQTT listener)
2. En tu frontend HTML (tu dashboard), actualiza:

```javascript
const response = await fetch("http://localhost:5000/sensores");
```

> O cámbialo a tu IP pública si estás desplegando en Replit o servidor.

---

## ✅ ¿Qué logras con este sistema?

* Conexión **remota en tiempo real** entre sensores virtuales (Wokwi Pico W) y tu dashboard web.
* Flespi actúa como un **sistema de control distribuido**.
* Dashboard puede recibir actualizaciones cada pocos segundos usando REST o incluso WebSockets (para refrescar en tiempo real no esta incluido en esta practica, pero lo puede hacer Ud.).


NOTA: Esta invitado para PullRequest de errores o omisiones, esta practica no esta probada.
