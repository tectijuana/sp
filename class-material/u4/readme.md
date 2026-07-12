# U04 — Comunicaciones avanzadas e integración con IA

Esta unidad formaliza la **capa de orquestación con LLM** del [AI-IoT-Stack](../../docs/ai-iot-stack.md): el microcontrolador ya no solo publica datos por MQTT, también puede consultar un modelo de lenguaje para razonar sobre ellos.

---

## 4.1 Conectividad: de WiFi/BT a bajo consumo

| Tecnología | Cuándo usarla | Notas |
|---|---|---|
| **WiFi** (ESP32, RP Pico W) | Hay alimentación estable y red disponible | La opción por defecto del curso hasta ahora |
| **Bluetooth / BLE** | Corto alcance, bajo consumo, sin infraestructura de red | Útil para wearables o pares de dispositivos |
| **LoRaWAN** | Largo alcance, muy bajo consumo, poca frecuencia de datos | Estaciones remotas (agricultura, monitoreo ambiental — ver `class-material/u2/desafio`) |

La elección de conectividad no cambia el resto del stack: sigue siendo MQTT/EdgeX → InfluxDB → dashboard. Lo que cambia es el costo energético y la latencia con la que los datos llegan a la capa de inteligencia.

---

## 4.2 De la simulación a la integración real con un LLM

`class-material/u3/3.4` planteó la idea con una respuesta de ChatGPT **simulada** (un diccionario fijo). Esta unidad la lleva al siguiente nivel: una llamada HTTP real a una API de LLM, con las mismas consideraciones que se usarían en producción.

**Flujo:**

```
Sensor(es) ──▶ Microcontrolador (ESP32 / RP Pico W)
                     │  arma un prompt con el estado leído
                     ▼
              API de un LLM (HTTPS + API key)
                     │  responde en lenguaje natural o JSON estructurado
                     ▼
        Actuador / pantalla / publicación MQTT del resultado
```

**Ejemplo (MicroPython, `urequests`) — sensor de temperatura pide una recomendación:**

```python
import urequests
import ujson

LLM_API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "TU_API_KEY"  # nunca la escribas en el código en un repo público; usa una variable de entorno o secretos del curso

def pedir_recomendacion(temperatura, humedad):
    prompt = (
        f"Lectura de sensor: temperatura={temperatura}C, humedad={humedad}%. "
        "Responde en una sola frase corta con una recomendación de acción."
    )
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 60,
    }
    r = urequests.post(LLM_API_URL, headers=headers, data=ujson.dumps(body))
    respuesta = r.json()["choices"][0]["message"]["content"]
    r.close()
    return respuesta

recomendacion = pedir_recomendacion(38.4, 22)
print("Recomendación:", recomendacion)
```

> ⚠️ En Wokwi no hay salida real a Internet: para probar la llamada real se necesita hardware físico (ESP32/Pico W) o correr el mismo código en una PC. Wokwi sigue siendo válido para probar la lógica de sensores/actuadores antes de integrar el LLM.

---

## 4.3 Buenas prácticas al integrar un LLM en el stack

- **El prompt debe pedir una salida corta y estructurada** (una frase, un JSON), no un ensayo — el microcontrolador tiene que mostrarlo o actuar sobre él.
- **Nunca subas tu API key al repositorio.** Usa variables de entorno, un archivo `secrets.py` ignorado por git, o las claves que proporcione el docente para prácticas.
- **El LLM es la capa de razonamiento, no la de control en tiempo real.** Las decisiones críticas de seguridad (apagar un actuador por sobrecalentamiento, por ejemplo) deben resolverse localmente; el LLM aporta contexto y lenguaje natural, no reemplaza un `if` de seguridad.
- **Registra la llamada y su costo/latencia.** Parte de evaluar si el LLM aporta valor real es medir cuánto tarda y cuánto cuesta contra la alternativa de una regla fija.

---

## 4.4 Práctica sugerida

Extiende la práctica de `3.4`: en vez de simular la respuesta, conecta un ESP32 o RP Pico W real (o un backend intermedio en Flask, ver `class-material/u1/4-Flask`) que reciba el dato del sensor, llame a la API del LLM, y publique la recomendación por MQTT para que aparezca en el dashboard de Grafana/ThingsBoard junto con el dato crudo.

Ver rúbrica general de prácticas en [GRADING.md](../../GRADING.md).
