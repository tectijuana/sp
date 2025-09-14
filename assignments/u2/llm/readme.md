
```┌─────────────────────────────🌦️ Dashboard Clima IoT + LLM─────────────────────────────┐
│                                                                                      │
│   📈 Temperatura (°C)         💧 Humedad (%)                 🌬️ Viento (km/h)        │
│   ──────────────────          ──────────────────            ──────────────────       │
│   30 ┤      ╭───╮             100 ┤ ╭╮                        40 ┤      ╭─╮         │
│   25 ┤   ╭──╯   ╰──╮           80 ┤ ││ ╭──╮                    30 ┤   ╭─╯ ╰─╮       │
│   20 ┤ ╭─╯        ╰─╮          60 ┤ │╰─╯  ╰╮                   20 ┤ ╭─╯     ╰─╮     │
│   15 ┤╯            ╰─           40 ┤ │      ╰──╮                10 ┤╯         ╰─    │
│                                                                                      │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 🤖 Asistente LLM (Chat)                                                               │
│ Usuario: ¿Cómo estuvo el clima esta semana?                                           │
│                                                                                      │
│ LLM: La temperatura promedio fue de 🌡️ 22°C, con máximas de 29°C el jueves.          │
│      La humedad bajó 📉 un 15% entre lunes y miércoles. El viento se mantuvo estable. │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
````



## 📊🔗 **Dashboard con API de LLM**

Un **dashboard con API de LLM** no solo muestra datos de sensores o sistemas, sino que también permite **interpretarlos, resumirlos y explicarlos** automáticamente usando un **modelo de lenguaje grande (LLM)** como GPT.

---

### 🔧 **Arquitectura típica**

```
🌡️ Sensores IoT / Sistemas
        │
        ▼
📨 Broker MQTT → 🗄️ InfluxDB / Prometheus (almacenamiento de series temporales)
        │
        ▼
📊 Grafana (dashboard interactivo con gráficas y alertas)
        │
        ▼
🤖 API de LLM (ej. GPT, LLaMA, Claude)
        │
        └──> Explicación en lenguaje natural + respuestas a consultas
```

---

### 🚀 **Cómo funciona en la práctica**

1. **Datos en tiempo real** llegan de sensores o sistemas a la base de datos (InfluxDB/Prometheus).
2. **Grafana** genera el dashboard visual (gráficas de temperatura, consumo de CPU, etc.).
3. El **LLM se integra como API** dentro de Grafana o un servicio adicional:

   * 📝 El usuario puede **preguntar en lenguaje natural**:

     > "¿Cuál fue la temperatura promedio esta semana?"
   * El **LLM interpreta la consulta**, genera una query (ej. en SQL o PromQL) hacia la base de datos.
   * Obtiene los datos y los **resume en lenguaje humano**.

---

### 💡 **Ejemplos de uso**

* 🌡️ **IoT:** El LLM analiza los datos de humedad y temperatura y te dice:

  > "La humedad bajó un 12% en los últimos 3 días, probablemente por el cambio de clima."
* 🖥️ **Sistemas:** En lugar de leer métricas técnicas, puedes preguntar:

  > "¿Por qué está lenta la aplicación?"
  > El LLM revisa datos de CPU, RAM y logs → responde:
  > "El servidor alcanzó el 95% de CPU entre las 3 y 4 PM por exceso de peticiones."
* 🧾 **Reportes automáticos:** El LLM genera un informe diario/semanal con texto narrativo y gráficas incrustadas del dashboard.

---

### ⚙️ **Tecnologías que pueden integrarse**

* **Grafana plugins**: usar paneles con chatbots conectados a APIs de LLM.
* **LangChain / LlamaIndex**: frameworks que convierten preguntas en queries hacia las BD de series temporales.
* **APIs de OpenAI, Anthropic, Meta (LLaMA), Mistral, etc.** para el motor LLM.

---

👉 En resumen:
Un **dashboard con API de LLM** no solo muestra gráficas, sino que **explica, responde y predice** con lenguaje natural, convirtiéndose en un **asistente inteligente de monitoreo**.


---

¡Excelente! 😃 Entonces podemos armar una **práctica guiada para estudiantes de Ingeniería en Sistemas** en el curso de **Sistemas Programables**, usando lo que ya saben (APIs como OpenWeatherMAP) y llevándolos a integrar un **dashboard + LLM**.

---

# 🛠️ Práctica: Dashboard Inteligente con LLM y OpenWeatherMAP

**Objetivo:** Desarrollar un dashboard que muestre datos del clima en tiempo real (API OpenWeatherMAP), almacenarlos en una base de datos de series temporales, visualizarlos en Grafana y usar un LLM (ej. GPT API) para interpretar los resultados en lenguaje natural.

---

## 🔗 Flujo de la práctica

```text
🌦️ OpenWeatherMAP API  →  📥 InfluxDB
                                  │
                                  ▼
                           📊 Grafana
                                  │
                                  ▼
                           🤖 API de LLM
```

---

## 🧩 Etapas de desarrollo

### 1️⃣ Captura de datos (API OpenWeatherMAP)

* Lenguaje sugerido: **Python** o **Node.js**.
* Los estudiantes ya saben obtener JSON de la API, ej:

  * Temperatura 🌡️
  * Humedad 💧
  * Velocidad del viento 🌬️

👉 Guardar estos datos en **InfluxDB** como series temporales.

---

### 2️⃣ Visualización en Grafana

* Conectar Grafana a InfluxDB.
* Crear paneles básicos:

  * Gráfica de temperatura en las últimas 24h.
  * Humedad promedio por día.
  * Mapa con la ciudad configurada.

---

### 3️⃣ Integración con un LLM

* Usar **OpenAI API** (o cualquier LLM disponible).
* Desarrollar un **módulo intermedio en Python**:

  * El estudiante envía una pregunta en lenguaje natural (ej. *"¿Cómo estuvo la temperatura esta semana?"*).
  * El programa traduce la pregunta en una consulta a InfluxDB.
  * Recupera los datos y los pasa al LLM.
  * El LLM devuelve un **resumen explicativo**.

---

### 4️⃣ Resultados esperados

* Dashboard de Grafana mostrando gráficas en tiempo real.
* Un chatbot (terminal o panel en Grafana) que responda:

  * "La temperatura promedio fue de 22°C y la máxima de 29°C el jueves."
  * "Hubo una caída de humedad de 15% entre el lunes y miércoles."

---

## 📚 Entregables de la práctica

1. **Script de captura** (API → InfluxDB).
2. **Dashboard en Grafana** con al menos 3 paneles.
3. **Módulo con API de LLM** que interprete preguntas en lenguaje natural.
4. **Informe final** explicando el flujo de datos y ejemplos de consultas/respuestas.

---

👉 Con esta práctica, los estudiantes aplican:

* Integración de APIs (OpenWeatherMAP).
* Manejo de series temporales (InfluxDB).
* Dashboards interactivos (Grafana).
* LLM aplicado como **intérprete de datos y asistente inteligente**.

---

## ANEXO: Ejemplo que debe mejorar 50% mas diferente.

```python
import requests
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from openai import OpenAI

# ----------------------------
# CONFIGURACIÓN
# ----------------------------
# 🔑 API Key de OpenWeatherMap (poner la suya)
OPENWEATHER_API_KEY = "TU_API_KEY"
CITY = "Tijuana,mx"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"

# 🔑 Configuración InfluxDB
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "TU_TOKEN_INFLUX"
INFLUX_ORG = "TU_ORG"
INFLUX_BUCKET = "clima"

# 🔑 Configuración LLM (ejemplo OpenAI GPT)
OPENAI_API_KEY = "TU_API_KEY_OPENAI"
client = OpenAI(api_key=OPENAI_API_KEY)

# ----------------------------
# 1. OBTENER DATOS DEL CLIMA
# ----------------------------
def obtener_clima():
    response = requests.get(URL)
    data = response.json()
    clima = {
        "temp": data["main"]["temp"],
        "humedad": data["main"]["humidity"],
        "viento": data["wind"]["speed"],
        "descripcion": data["weather"][0]["description"]
    }
    return clima

# ----------------------------
# 2. GUARDAR EN INFLUXDB
# ----------------------------
def guardar_in_influx(clima):
    with InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG) as clientdb:
        write_api = clientdb.write_api(write_options=None)

        point = (
            Point("clima")
            .tag("ciudad", CITY)
            .field("temperatura", clima["temp"])
            .field("humedad", clima["humedad"])
            .field("viento", clima["viento"])
            .time(datetime.utcnow(), WritePrecision.NS)
        )
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)

# ----------------------------
# 3. CONSULTAR Y PREGUNTAR A LLM
# ----------------------------
def preguntar_llm(pregunta, datos):
    prompt = f"""
    Eres un asistente que analiza datos de clima.
    Datos disponibles: {datos}
    Pregunta del usuario: {pregunta}
    Responde en español de forma clara y breve.
    """

    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return respuesta.choices[0].message.content

# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    # Paso 1: obtener datos
    clima = obtener_clima()
    print("Clima actual:", clima)

    # Paso 2: guardar en InfluxDB
    guardar_in_influx(clima)

    # Paso 3: ejemplo de consulta a LLM
    pregunta = "¿Cómo estuvo la temperatura y humedad en esta lectura?"
    resumen = preguntar_llm(pregunta, clima)
    print("🤖 LLM responde:", resumen)

```
