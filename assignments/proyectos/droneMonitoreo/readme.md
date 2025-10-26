
<img width="2560" height="1600" alt="screen" src="https://github.com/user-attachments/assets/77fa6d3f-dba5-48bd-8488-9127327af279" />


## 🛰️ Flespi Challenge: “SATNET AGRO DRONE SYSTEM” – Telemetría en Tiempo Real

### 🎯 Objetivo

Desarrollar una arquitectura IoT funcional que integre sensores en drones agrícolas para transmitir datos en tiempo real usando **Flespi MQTT broker**, con visualización vía dashboard o HTML UI como la que subiste (`code.html`).

---

## 🔧 Escenario

Un dron agrícola sobrevuela parcelas monitoreando temperatura, humedad y altura (altitud/barometría). La información debe transmitirse vía MQTT a Flespi y visualizarse en un dashboard web (como el que mostraste) con estilo moderno (Tailwind).

---

## 📦 Equipamiento virtual (Simulación)

* Microcontrolador: **Raspberry Pi Pico W (MicroPython)**
* Sensores simulados:

  * `BME280` (Temperatura, Humedad, Presión/Altitud)
  * `GPS NMEA stream` (simulado en formato JSON)
* Broker MQTT: [Flespi MQTT Broker](https://flespi.io/mqtt-broker)
* UI: `code.html` como plantilla para frontend

---

## 📚 Requisitos del Reto

### 1. Simulación de Sensores

Debe utilizar Wokwi.com para simular el GPS sensor y simula datos de sensores cada 5 segundos (formato JSON):

```json
{
  "timestamp": "2025-10-26T14:38:00Z",
  "temperature": 32.7,
  "humidity": 68.3,
  "altitude": 234.2,
  "gps": {
    "lat": -34.6123,
    "lon": -58.3772
  },
  "battery": 74
}
```

Introduce **anomalías** cada 30 lecturas:

* Temperatura fuera de rango (>45°C)
* Pérdida de GPS (`lat: null, lon: null`)
* Altitud negativa simulando caída

### 2. MQTT → Flespi Configuración

* Broker: `mqtt.flespi.io`
* Port: `1883`
* Topic: `satnet/agrodrone/telemetry`
* QoS: `1`
* Auth: token generado desde [flespi.io](https://flespi.io)

### 3. Código MicroPython Simulado

Envía los datos simulados por MQTT. Usa `umqtt.simple` o `mqtt_as`.

---

## 🖥️ Frontend HTML Adaptado (solo referencia es opcional)

Modifica tu `code.html` para:

* Mostrar las variables en tarjetas dinámicas (usando `WebSockets` o `MQTT over Web` si quieres ir más lejos)
* Resaltar valores anómalos en rojo (ej: altitud < 0m o temperatura > 45°C)

---

## 📊 Nivel Extra (Opcional)

* Integra **Grafana** usando **Flespi HTTP Stream** → InfluxDB → Grafana
* Mide rendimiento de transmisión (payload size, transmisión fallida vs exitosa)

---

## 🧠 Preguntas para Reflexión

1. ¿Qué frecuencia de muestreo sería óptima para balancear calidad vs consumo de energía?
2. ¿Cómo manejarías la pérdida de conexión con Flespi?
3. ¿Qué ventajas tiene usar Flespi sobre Mosquitto o AWS IoT Core en este contexto?

---

Puedes simular el flujo con herramientas como:

* [MQTT Explorer](https://mqtt-explorer.com)
* Wokwi (para código C con ESP32)
* Flespi MQTT test tool: [Try Now](https://flespi.io/mqtt-test)

---

¡Excelente elección! Vamos con ambas partes:
**1. Publicador MQTT en MicroPython (Raspberry Pi Pico W) usando Flespi**
**2. Detección local de anomalías antes de publicar los datos**

---

## 📡 1. Publicador MQTT en MicroPython (para Flespi)

**Requisitos previos:**

* WiFi SSID y contraseña
* Token de Flespi MQTT: crea uno desde [https://flespi.io](https://flespi.io) (Dashboard → Tokens → Create)

### 📁 Código: `main.py`

```python
import network
import time
import json
import random
from umqtt.simple import MQTTClient

# === CONFIGURACIÓN WIFI ===
WIFI_SSID = 'TU_SSID'
WIFI_PASSWORD = 'TU_PASSWORD'

# === CONFIGURACIÓN MQTT FLESPI ===
FLESPI_TOKEN = 'FlespiToken XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
MQTT_BROKER = 'mqtt.flespi.io'
MQTT_PORT = 1883
MQTT_TOPIC = 'satnet/agrodrone/telemetry'

# === Conectar WiFi ===
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Conectando a WiFi...")
        time.sleep(1)
    print("Conectado:", wlan.ifconfig())

# === Simulación de sensores ===
def simulate_data(counter):
    temperature = round(random.uniform(20, 40), 1)
    humidity = round(random.uniform(40, 90), 1)
    altitude = round(random.uniform(100, 300), 1)
    battery = random.randint(60, 100)
    gps = {
        "lat": -34.60 + random.uniform(-0.01, 0.01),
        "lon": -58.38 + random.uniform(-0.01, 0.01)
    }

    # Introducir anomalías cada 30 muestras
    if counter % 30 == 0:
        temperature = round(random.uniform(45, 55), 1)
        altitude = -10.0
        gps = {"lat": None, "lon": None}

    return {
        "timestamp": time.time(),
        "temperature": temperature,
        "humidity": humidity,
        "altitude": altitude,
        "gps": gps,
        "battery": battery
    }

# === Detección de anomalías ===
def check_anomalies(data):
    anomalies = []
    if data["temperature"] > 45:
        anomalies.append("🔥 Temperatura Alta")
    if data["altitude"] < 0:
        anomalies.append("📉 Altitud Negativa")
    if data["gps"]["lat"] is None or data["gps"]["lon"] is None:
        anomalies.append("🛰️ GPS Perdido")
    return anomalies

# === Main ===
def main():
    connect_wifi()
    client = MQTTClient("pico_client", MQTT_BROKER, port=MQTT_PORT, user="", password=FLESPI_TOKEN)
    client.connect()
    print("Conectado a Flespi MQTT")

    counter = 1
    while True:
        data = simulate_data(counter)
        anomalies = check_anomalies(data)

        if anomalies:
            data["anomalies"] = anomalies
            print("🚨 Anomalías detectadas:", anomalies)

        payload = json.dumps(data)
        client.publish(MQTT_TOPIC, payload)
        print(f"[{counter}] Publicado: {payload}")

        counter += 1
        time.sleep(5)

main()
```

---

## 💡 ¿Qué hace este código?

* Se conecta a WiFi y luego a Flespi usando el token MQTT.
* Simula valores realistas de sensores.
* Introduce anomalías cada 30 lecturas (altitud negativa, alta temperatura, pérdida de GPS).
* Detecta localmente esas anomalías antes de enviar los datos al broker.
* Publica el JSON en el topic `satnet/agrodrone/telemetry`.

---

## 🧩 **Rúbrica de Evaluación – Backend IoT con Flespi (Total: 100 pts)**

| **Criterio**                                            | **Descripción**                                                                                        | **Pts Máx.** |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| **1. Conectividad MQTT (Flespi)**                       | Conexión exitosa al broker Flespi usando token seguro y manejo adecuado del cliente MQTT               | 15 pts       |
| **2. Simulación de Sensores Realistas**                 | Simulación coherente de temperatura, humedad, altitud, batería y GPS. Valores dentro de rangos lógicos | 10 pts       |
| **3. Publicación de Datos MQTT**                        | Publicación periódica (cada 5 seg) en el topic `satnet/agrodrone/telemetry` con QoS adecuado           | 10 pts       |
| **4. Detección de Anomalías Local**                     | Identificación de condiciones anómalas (temp > 45°C, altitud < 0, GPS perdido)                         | 10 pts       |
| **5. Estructura del Payload JSON**                      | Payload limpio, estructurado y con `timestamp`, campos bien nombrados y parseables                     | 10 pts       |
| **6. Manejo de Errores (Red / MQTT / Sensor)**          | Reintentos, reconexión automática o manejo de excepciones por fallos de red o MQTT                     | 10 pts       |
| **7. Código Modular y Legible (MicroPython)**           | Uso de funciones limpias, documentación en comentarios, estilo claro                                   | 10 pts       |
| **8. Seguridad en el Token y Configuración**            | Token Flespi no hardcoded o uso de archivo externo / variables de entorno                              | 5 pts        |
| **9. Escalabilidad del Diseño (Multi-sensor / Drone)**  | Preparado para añadir múltiples sensores o nodos sin cambios drásticos al código                       | 10 pts       |
| **10. Prueba de Funcionamiento / Log de Publicaciones** | Registro serial de publicaciones con indicación de conexión, envío, errores y anomalías                | 10 pts       |

---

## 🧠 Bonus Extra (Opcional) - Hasta 10 pts

| **Criterio Bonus**                                      | **Descripción**                                                                        | **Pts** |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------- |
| Dashboard MQTT integrado en HTML o con WebSocket        | Frontend dinámico mostrando los datos recibidos en tiempo real                         | +5 pts  |
| Compresión del payload (ej. uso de CBOR o menos campos) | Uso de técnicas para reducir el tamaño del payload, pensando en LPWAN o edge computing | +5 pts  |

---

### 📊 Distribución Total

* **Obligatorios:** 100 pts
* **Bonus opcional:** +10 pts
* **Nota final:** Escalar sobre 100 (si hay bonus, pueden dar crédito adicional o sobresaliente pasará a otra practica de menor puntaje)

---
