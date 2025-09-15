
---

# 🌦️ Práctica: Dashboard en terminal con **Dashing** y datos de OpenWeatherMap

## 🎯 Objetivo

Consumir datos en tiempo real desde la API pública de **OpenWeatherMap (OWM)** y mostrarlos en un **dashboard en terminal** usando **Dashing** dentro de una instancia **AWS EC2 con Ubuntu**.

---

## 🔹 Parte 1: Preparación del entorno

1. **Conectar a la instancia EC2 (Ubuntu)**

   ```bash
   ssh -i "tu-clave.pem" ubuntu@ec2-X-X-X-X.compute.amazonaws.com
   ```

2. **Actualizar sistema**

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

3. **Instalar Python 3 y pip**

   ```bash
   sudo apt install python3 python3-pip -y
   ```

4. **Instalar librerías necesarias**

   ```bash
   pip install dashing requests
   ```

---

## 🔹 Parte 2: Obtener una API Key de OpenWeatherMap

1. Crear una cuenta gratuita en 👉 [https://openweathermap.org/](https://openweathermap.org/)
2. Ir a **API Keys** y copiar tu clave personal.
3. La usaremos en el código para autenticar las peticiones.

---

## 🔹 Parte 3: Crear el script del dashboard

1. **Crear archivo `clima.py`**

   ```bash
   nano clima.py
   ```

2. **Código de ejemplo**

   ```python
   import time, requests
   from dashing import VSplit, HSplit, HGauge, VGauge, Log, Text

   # Configuración
   API_KEY = "TU_API_KEY"  # <--- reemplazar con tu clave
   CIUDAD = "Tijuana,mx"
   URL = f"http://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&appid={API_KEY}&units=metric"

   # Panel
   ui = HSplit(
       VSplit(
           Text(f"🌍 Clima en {CIUDAD}", border_color=3),
           HGauge(val=0, title="🌡️ Temp (°C)"),
           VGauge(val=0, title="💧 Humedad (%)"),
       ),
       VSplit(
           Log(title="📜 Eventos de clima"),
           Text("", border_color=2, color=2, title="Descripción"),
       )
   )

   log = ui.items[1].items[0]
   desc_box = ui.items[1].items[1]
   temp_gauge = ui.items[0].items[1]
   hum_gauge = ui.items[0].items[2]

   # Bucle principal
   while True:
       try:
           resp = requests.get(URL)
           data = resp.json()

           temp = data["main"]["temp"]
           humedad = data["main"]["humidity"]
           descripcion = data["weather"][0]["description"]

           # Actualizar dashboard
           temp_gauge.value = int(temp)
           hum_gauge.value = int(humedad)
           desc_box.text = f"Condición: {descripcion}"

           log.append(f"[{time.strftime('%H:%M:%S')}] {descripcion}, {temp}°C, {humedad}%")

           ui.display()
           time.sleep(10)  # refresca cada 10 segundos
       except Exception as e:
           log.append(f"⚠️ Error: {e}")
           ui.display()
           time.sleep(10)
   ```

---

## 🔹 Parte 4: Ejecutar el panel

```bash
python3 clima.py
```

👉 En la terminal se verá un **dashboard dinámico** con:

* 🌡️ **Temperatura actual (°C)**
* 💧 **Humedad (%)**
* 📜 **Log de condiciones climáticas** con hora de registro
* ☁️ **Descripción textual del clima**

---

## 🔹 Sugerencias de extensión

* 📊 Agregar **gráficas en tiempo real** con `HChart` para mostrar la evolución de la temperatura.
* 🌍 Cambiar la ciudad y monitorear varias ubicaciones en paneles distintos.
* 🔌 Integrar con **MQTT** para enviar alertas cuando la temperatura o humedad superen cierto umbral.

---

## ✅ Conclusión

Con esta práctica, los estudiantes aprenden a:

* Usar **APIs públicas (REST)** en Python.
* Construir un **dashboard en terminal** con **Dashing**.
* Implementar un **sistema de monitoreo en tiempo real** dentro de un **servidor remoto (AWS EC2 Ubuntu)**.
------

| Criterio                                     | Excelente (100%)                                                                | Satisfactorio (80%)                                              | Insuficiente (50%)                           | Nulo (0%)               |
| -------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------- | ----------------------- |
| **Configuración de entorno en AWS EC2**      | EC2 configurada correctamente, Python y dependencias instaladas sin errores     | Configuración incompleta, pero entorno funcional                 | Errores importantes que afectan la ejecución | No se realizó           |
| **Implementación del dashboard con Dashing** | Dashboard con temperatura, humedad, log y descripción funcionando correctamente | Dashboard incompleto pero con funcionalidad básica               | Script con errores que limitan su uso        | No se entregó           |
| **Integración con OpenWeatherMap**           | API Key configurada y datos reales consumidos                                   | API Key configurada, pero datos limitados o con errores          | API no configurada, solo datos simulados     | Sin integración con API |
| **Evidencia en Asciinema**                   | Grabación clara, incluye bloque con nombre, número de control y fecha           | Grabación realizada pero con datos de identificación incompletos | Grabación con errores o ilegible             | No se entregó grabación |

