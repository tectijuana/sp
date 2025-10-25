
<img width="780" height="2110" alt="screen" src="https://github.com/user-attachments/assets/5d7fadb7-821c-4af2-ae38-8000c44b334b" />


# 🚚 PRÁCTICA IoT: Simulación de Flota de Vehículos con Backend en Flespi MQTT + Wokwi

### 🎯 Objetivo Docente

El propósito de esta práctica es que los estudiantes construyan un **backend funcional para IoT vehicular**, comprendiendo el flujo completo de:

* Simulación de sensores en **Wokwi con MicroPython** o Python local.
* Transmisión de datos a **Flespi MQTT** como broker en la nube.
* Posprocesamiento y visualización opcional vía **Node-RED, Grafana o EC2 con herramientas open source**.

> ⚠️ **No se desarrollarán portales web ni UI visuales**. Esta práctica se centra en el **modelo de datos, el flujo MQTT y el backend de telemetría**, fomentando la creatividad en la simulación, análisis y modelado de eventos.

---

## 🔧 Escenario:

Eres parte del equipo técnico de **Galgo Transportes**, una empresa que busca digitalizar su flota de 10 vehículos de carga. Se requiere una solución para:

* 🛰️ Localización GPS.
* ⛽ Nivel de combustible.
* 🌡️ Temperatura del motor.
* 🛑 Eventos de frenado brusco.

Cada vehículo enviará estos datos simulados cada **15 segundos** vía MQTT a **Flespi**, usando un tópico por vehículo.

---

## 🧱 Requisitos Técnicos:

### 1. Simulación de Sensores

Plataformas válidas:

* ✅ Python local (con `paho-mqtt`)
* ✅ MicroPython en **Wokwi** con **ESP32 o Pico W**

Cada vehículo debe simular:

* Latitud / Longitud (movimiento simulado).
* Nivel de combustible (disminuye progresivamente).
* Temperatura del motor (con picos aleatorios).
* Evento de frenado brusco aleatorio (cada 30–60 segundos).

---

### 2. Tópico MQTT por vehículo

Formato:

```
fleet/vehicle/{vehicle_id}/telemetry
```

Ejemplo de Payload:

```json
{
  "timestamp": "2025-10-25T14:33:00Z",
  "lat": -34.6037,
  "lon": -58.3816,
  "fuel": 67.3,
  "temp": 91.2,
  "brake_event": false
}
```

---

### 3. Backend MQTT en Flespi

* Crea cuenta gratuita en [https://flespi.io](https://flespi.io)
* Define un canal MQTT.
* Crea un **token único por vehículo**.
* Usa TLS o puerto 1883 según la librería que uses (Python o MicroPython).

---

### 4. Visualización (Opcional, no evaluado directamente)

Si se desea explorar más:

* Conecta Flespi a Node-RED vía MQTT-IN.
* Visualiza los datos con InfluxDB y Grafana.
* **AWS EC2** puede utilizarse como entorno de despliegue backend con software open-source (Mosquitto, Telegraf, InfluxDB, Grafana).

---

## 📌 Actividades clave

1. ✅ Modela 10 vehículos con diferentes rutas.
2. ✅ Envía datos MQTT cada 15s por tópico estructurado.
3. ✅ Simula eventos realistas (picos, desconexión, frenos).
4. ✅ Opcional: crea alertas por temperatura o freno.
5. ✅ Documenta arquitectura y pruebas.

---

## 🧪 Restricciones y Retos

* Simular picos de temperatura aleatorios en al menos 3 vehículos.
* Simular pérdida de conexión de un vehículo por 2 minutos.
* No exceder los **100 mensajes por minuto por vehículo** (tasa máxima de Flespi gratuito).
* Documentar cada error, anomalía o evento generado.

---

## 📈 Datos Simulados – Ejemplo

| Vehículo | Timestamp | Latitud | Longitud | Combustible (%) | Temp (°C) | Freno Brusco |
| -------- | --------- | ------- | -------- | --------------- | --------- | ------------ |
| V001     | 14:00Z    | -34.60  | -58.38   | 87.5            | 89.2      | false        |
| V002     | 14:00Z    | -34.62  | -58.40   | 76.4            | 91.7      | true         |
| V003     | 14:00Z    | -34.63  | -58.35   | 92.8            | 88.1      | false        |

---

## 📁 Entregables esperados

* Código fuente (`fleet_simulator.py` o `main.py` en MicroPython).
* Evidencia de publicación en Flespi (pantallazo, logs).
* Captura de Dashboard (si se hace Node-RED o Grafana).
* Diagrama de arquitectura (`Mermaid.js`).
* Archivo `.json` de ejemplo con payload simulado.

---

### 🌐 Arquitectura del Sistema (Mermaid.js)

<img width="1317" height="1082" alt="GalgoTrabsortes diagrama" src="https://github.com/user-attachments/assets/9bcbad32-f1a1-45fb-b575-38bd9856ec41" />

---

## 🛠️ Backend en Python (simulador)

Ya incluido arriba (`fleet_simulator.py`). Puedes adaptarlo fácilmente a:

* `MicroPython` + `umqtt.simple` para correr en Wokwi o Pico W.
* `paho-mqtt` en PC o EC2.

---

## 🚀 Extensiones posibles

Para estudiantes avanzados:

* 🛰️ Simular sensores reales como MPU6050, DHT22, etc.
* 🔐 Agregar autenticación con JWT al mensaje.
* 📦 Crear endpoint en Flask para consultar última ubicación.
* 📉 Analizar consumo de combustible por distancia recorrida.

---

## 🚗 MicroPython en Wokwi + MQTT (Flespi)

Este script simula **un vehículo** que publica cada 15 segundos:

* GPS (lat/lon) simulado
* Nivel de combustible decreciente
* Temperatura del motor con picos
* Evento de frenado brusco aleatorio

> ✅ Lo puedes correr en Wokwi: selecciona **Raspberry Pi Pico W** o **ESP32 con Wi-Fi**
> 🔐 Necesitas un **token de Flespi MQTT** y red Wi-Fi simulada (Wokwi la soporta)

---

## 📄 `main.py` para Wokwi

```python
import network
import time
import random
import ujson
from umqtt.simple import MQTTClient

# 🛠️ Configuración WiFi (simulada en Wokwi)
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""

# 📡 Configuración MQTT (Flespi)
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOKEN = "FlespiToken xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # ← Reemplaza este token

VEHICLE_ID = "V001"
TOPIC = f"fleet/vehicle/{VEHICLE_ID}/telemetry"
PUBLISH_INTERVAL = 15  # segundos

# 📍 Coordenadas base
lat = -34.6037
lon = -58.3816
fuel = 100.0
temp = 90.0

last_brake = time.time()

# 🌐 Conectar Wi-Fi
def connect_wifi():
    print("🔌 Conectando a Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("✅ Conectado:", wlan.ifconfig())

# 🔗 Conectar MQTT
def connect_mqtt():
    client = MQTTClient(client_id=VEHICLE_ID,
                        server=FLESPI_BROKER,
                        port=FLESPI_PORT,
                        user=FLESPI_TOKEN,
                        password="")
    client.connect()
    print("📡 Conectado a Flespi MQTT")
    return client

# 🧪 Generar datos
def generate_data():
    global lat, lon, fuel, temp, last_brake

    lat += random.uniform(-0.0003, 0.0003)
    lon += random.uniform(-0.0003, 0.0003)

    fuel = max(0, fuel - random.uniform(0.1, 0.5))

    if random.random() < 0.05:
        temp = min(130, temp + random.uniform(5, 10))
    else:
        temp = max(80, temp - random.uniform(0.2, 0.5))

    brake_event = False
    if time.time() - last_brake > random.randint(20, 40):
        brake_event = random.choice([True, False])
        last_brake = time.time()

    return {
        "timestamp": time.time(),
        "lat": round(lat, 6),
        "lon": round(lon, 6),
        "fuel": round(fuel, 2),
        "temp": round(temp, 2),
        "brake_event": brake_event
    }

# 🚀 Programa principal
connect_wifi()
client = connect_mqtt()

while True:
    data = generate_data()
    payload = ujson.dumps(data)
    client.publish(TOPIC, payload)
    print(f"🚚 Enviado → {TOPIC}: {payload}")
    time.sleep(PUBLISH_INTERVAL)
```

---

## 🧰 Wokwi Setup

1. Abre [https://wokwi.com/new](https://wokwi.com/new)
2. Elige `Raspberry Pi Pico W` o `ESP32`
3. Agrega archivo `main.py` con el código anterior
4. Asegúrate que el proyecto tenga Internet (Wokwi lo simula)
5. Reemplaza el `FlespiToken` en el código

---

## 🧪 ¿Cómo validar?

* Revisa en Flespi el canal MQTT → mensajes entrantes
* Si usas Node-RED o MQTT Explorer, también verás los datos
* Puedes duplicar este código para múltiples dispositivos en simulación (copiar proyecto)

---

## 🧠 Extensiones recomendadas

* Simula sensores reales: DHT22, MPU6050 (solo lectura aleatoria)
* Agrega botón en Wokwi como interruptor de emergencia (puerta abierta)
* Usa múltiples `client_id` para simular varios vehículos

---


## ✅ EJEMPLO FINAL – Wokwi / MicroPython – 10 Vehículos Simulados, en Wokwi con MicroPython (usando un solo script con IDs alternos) + una **rúbrica de evaluación docente** clara y estructurada.

> ⚠️ Wokwi no soporta múltiples instancias de hardware en paralelo en un solo proyecto.
> Por eso, esta versión **simula los 10 vehículos en un solo script** (ideal para pruebas, no para dispositivos físicos independientes).

---

### 📄 `main.py` (10 Vehículos, un solo script)

```python
import network
import time
import random
import ujson
from umqtt.simple import MQTTClient

# 🛜 WiFi (simulado por Wokwi)
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""

# 📡 Flespi MQTT
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOKEN = "FlespiToken xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 🚚 Configuración
NUM_VEHICLES = 10
PUBLISH_INTERVAL = 15  # segundos
START_LAT = -34.6037
START_LON = -58.3816

# 📍 Vehículos simulados
vehicles = []
for i in range(NUM_VEHICLES):
    vehicle = {
        "id": f"V{str(i+1).zfill(3)}",
        "lat": START_LAT + random.uniform(-0.01, 0.01),
        "lon": START_LON + random.uniform(-0.01, 0.01),
        "fuel": random.uniform(60, 100),
        "temp": random.uniform(80, 90),
        "last_brake": time.time()
    }
    vehicles.append(vehicle)

# 🔌 Wi-Fi
def connect_wifi():
    print("🔌 Conectando a Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("✅ Conectado:", wlan.ifconfig())

# MQTT
def connect_mqtt():
    client = MQTTClient(client_id="fleet_sim",
                        server=FLESPI_BROKER,
                        port=FLESPI_PORT,
                        user=FLESPI_TOKEN,
                        password="")
    client.connect()
    print("📡 MQTT conectado")
    return client

# Simulación por vehículo
def simulate(vehicle):
    vehicle["lat"] += random.uniform(-0.0003, 0.0003)
    vehicle["lon"] += random.uniform(-0.0003, 0.0003)
    vehicle["fuel"] = max(0, vehicle["fuel"] - random.uniform(0.05, 0.2))

    if random.random() < 0.05:
        vehicle["temp"] = min(130, vehicle["temp"] + random.uniform(5, 15))
    else:
        vehicle["temp"] = max(80, vehicle["temp"] - random.uniform(0.1, 0.5))

    brake_event = False
    if time.time() - vehicle["last_brake"] > random.randint(20, 40):
        brake_event = random.choice([True, False])
        vehicle["last_brake"] = time.time()

    return {
        "timestamp": time.time(),
        "lat": round(vehicle["lat"], 6),
        "lon": round(vehicle["lon"], 6),
        "fuel": round(vehicle["fuel"], 2),
        "temp": round(vehicle["temp"], 2),
        "brake_event": brake_event
    }

# 🚀 Main
connect_wifi()
client = connect_mqtt()

while True:
    for v in vehicles:
        data = simulate(v)
        topic = f"fleet/vehicle/{v['id']}/telemetry"
        payload = ujson.dumps(data)
        client.publish(topic, payload)
        print(f"📤 {v['id']} → {topic}: {payload}")
    time.sleep(PUBLISH_INTERVAL)
```

---

## 📊 RÚBRICA DE EVALUACIÓN – Backend de Simulación IoT Vehicular

| Criterio                           | Descripción                                                                 | Puntos      |
| ---------------------------------- | --------------------------------------------------------------------------- | ----------- |
| **Configuración Flespi**           | Uso correcto del token, conexión exitosa al broker                          | 10 pts      |
| **Simulación de sensores**         | Publicación de: GPS, combustible, temperatura, frenado brusco               | 20 pts      |
| **Formato MQTT**                   | Uso correcto del tópico: `fleet/vehicle/{ID}/telemetry` y JSON estructurado | 15 pts      |
| **Picos/anomalías**                | Simulación de picos de temperatura y frenado realista                       | 10 pts      |
| **Gestión de múltiples vehículos** | Simulación concurrente de 10 vehículos                                      | 15 pts      |
| **Documentación técnica**          | Comentarios en el código, estructura clara                                  | 10 pts      |
| **Evidencia de pruebas**           | Capturas de Flespi, consola, logs de transmisión                            | 10 pts      |
| **Creatividad / Extensión**        | Uso de sensores adicionales, mejoras propias                                | 10 pts      |
| **TOTAL**                          |                                                                             | **100 pts** |

---

## 📝 Recomendaciones para UD.

* Permite que los estudiantes **adapten este código a MicroPython real** en Pico W.
* Incentiva el uso de Flespi como base para flujos Node-RED, InfluxDB, o AWS opcional.
* Refuerza que esto **no es frontend**: están trabajando **el backend IoT, modelado y lógica de negocio**.
* Valora si implementan **algoritmos de interpretación**: picos anómalos, patrones de frenado, predicción de falla.

-
