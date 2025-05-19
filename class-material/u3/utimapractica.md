<img width="644" alt="Screenshot 2025-05-19 at 2 02 39 p m" src="https://github.com/user-attachments/assets/4cd3db35-b377-467b-8444-68190a53f3d9" />


📘 **Práctica: Conexión de una Raspberry Pi Pico W a la API de ChatGPT para generar respuestas automáticas sobre una tema en soluciones IoT Sensores**
🔧 *Plataforma: Wokwi + MicroPython*
📡 *Tecnología: Wi-Fi, HTTP, JSON*

---

🎯 **Objetivo General**
Que el estudiante comprenda cómo integrar una Raspberry Pi Pico W con servicios externos usando peticiones HTTP (REST) y analice la interacción básica con APIs de IA como ChatGPT.

---

📦 **Materiales (simulados en Wokwi)**

* Raspberry Pi Pico W
* Pantalla  OLED Display (con salida de consola para depurar) NOTA: Puede utilizar otras pantallas de WOKWI.com
* Sensor de botón o entrada por REPL (mas complementos libre de actuar)
* Otros sensore de Wokwi para que involucrarlos en la idea de la proyeccion de esta microcontroladora con un grado de inteligencia..
* Conexión a Internet (emulada en Wokwi)

> Recuerde el modificar el "prompt" que sea el retorno solicitado y no una gran enunciado que no puea entender la condición, debe decidir la validación por ChatGTP.

---

🧠 **Descripción de la Actividad**
El estudiante implementará un programa en MicroPython que envía un mensaje a la API de ChatGPT (mediante una URL dummy en Wokwi) y recibe una respuesta que se muestra en pantalla. Aunque Wokwi no tiene salida real a internet, se simulará la llamada usando una función que devuelve un texto fijo (imitando a ChatGPT).

Posteriormente, el mismo código puede migrarse a una Raspberry Pi Pico W real para hacerlo funcional con conexión real y una clave de API de OpenAI.

---

🧪 **Código Base Simulado (Wokwi)**

```python
import time

def fake_chatgpt_response(prompt):
    # Simula la respuesta de la API
    respuestas = {
        "Hola": "¡Hola! ¿Cómo estás? 😊",
        "¿Qué es Python?": "Python es un lenguaje de programación de alto nivel.",
        "¿Quién eres?": "Soy una IA simulada como ChatGPT en Wokwi."
    }
    return respuestas.get(prompt, "Lo siento, no entendí la pregunta.")

def main():
    print("Bienvenido a ChatGPT en Pico W (simulado)")
    while True:
        entrada = input("Escribe tu pregunta: ")
        if entrada.lower() in ["salir", "exit"]:
            print("Adiós 👋")
            break
        print("Enviando pregunta a ChatGPT...")
        respuesta = fake_chatgpt_response(entrada)
        print("Respuesta de ChatGPT: ", respuesta)
        time.sleep(2)

main()
```

---

🌐 **Migración a una Pico W real**

Para una Pico W conectada a internet real:

1. Instala `urequests`.
2. Usa la API oficial de OpenAI.
3. Agrega tu clave de API y endpoint.

Ejemplo de código con API real (resumido):

```python
import urequests
import network

API_KEY = "sk-..."  # Tu clave real
URL = "https://api.openai.com/v1/chat/completions"

def enviar_a_chatgpt(mensaje):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": mensaje}]
    }
    response = urequests.post(URL, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
```

---

📋 **Evaluación**

| Criterio                           | Puntos |
| ---------------------------------- | ------ |
| Código limpio y bien documentado   | 20     |
| Simulación funcional en Wokwi      | 20     |
| Correcta emulación de respuestas   | 20     |
| Capacidad de migrar a entorno real | 20     |
| Reflexión sobre uso de IA          | 20     |

---

📝 **Conclusión esperada**
El estudiante podrá explicar cómo funciona una API, cómo se simulan procesos en Wokwi y cómo se puede conectar una Pico W real a servicios modernos como OpenAI.


