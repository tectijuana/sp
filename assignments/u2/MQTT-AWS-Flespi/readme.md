<img width="616" alt="Screenshot 2025-03-24 at 2 07 05 p m" src="https://github.com/user-attachments/assets/2ae4420a-41a1-4b4a-9f3f-5cc655030285" />


### Bloque 2:  Sistemas Programables e IoT con Raspberry Pi, flespi.com y AWS Academy

**Curso:** Sistemas Programables  
**Nivel:** Ingeniería en Sistemas Computacionales  
**Duración:** 3 sesiones (50  minutos c/u)

---

### 🎯 **Objetivos de la Lección:**

Al finalizar esta práctica, el estudiante será capaz de:

- Configurar dispositivos Raspberry Pi Zero 2W y Raspberry Pi Pico W para la captura de datos mediante sensores.
- Integrar y enviar información utilizando protocolos MQTT a la plataforma IoT flespi.com.
- Implementar soluciones básicas en AWS Academy para recibir, almacenar y visualizar datos IoT.
- Aplicar conocimientos prácticos sobre sistemas embebidos, comunicaciones inalámbricas y servicios en la nube.

---

### 📌 **Temas a Desarrollar:**

**Sesión 1:**

1. **Introducción a IoT y Sistemas Programables**
   - Conceptos clave: IoT, Sistemas Embebidos, MQTT.

2. **Configuración inicial del Hardware:**
   - Instalación y configuración de Raspberry Pi OS en Raspberry Pi Zero 2W.
   - Instalación y configuración de MicroPython en Raspberry Pi Pico W.

3. **Integración de sensores:**
   - Conexión y prueba de sensores ambientales (DHT22, BME280).

4. **Plataforma flespi.com:**
   - Creación y configuración de cuenta gratuita.
   - Configuración de broker MQTT.

**Sesión 2:**

5. **Envío de Datos a flespi.com:**
   - Desarrollo y ejecución de scripts Python/MicroPython para Raspberry Pi Zero 2W y Pico W.
   - Verificación y monitoreo de mensajes MQTT en flespi.

6. **AWS Academy para IoT:**
   - Configuración básica de instancia EC2 y entorno Cloud9.
   - Programación para consumo MQTT desde flespi a AWS.

7. **Visualización de Datos:**
   - Almacenamiento de datos recibidos en DynamoDB.
   - Creación básica de dashboard web para visualización de datos IoT.

---

### 🛠 **Actividades Prácticas:**

- Ensamblaje y configuración del hardware Raspberry. *
- Desarrollo de scripts Python/MicroPython para sensores y MQTT.
- Implementación en flespi y AWS Academy.

---

### 📝 **Evaluación:**

- Reporte técnico de implementación (50%) en gist markdown.
- Demostración en tiempo real de integración IoT (50%) con LOOM.com documentado en su GIST.

---

### 📚 **Materiales y Recursos:**

- Raspberry Pi Pico W y Raspberry Pi Zero 2W
- Sensores ambientales
- Plataforma flespi.com (https://flespi.com)
- AWS Academy (EC2 InfluxDB, Cloud9, DynamoDB)

---

Esta lección impulsa el aprendizaje integral y práctico, alineado con los objetivos profesionales de los estudiantes de Ingeniería en Sistemas Computacionales.

NOTA: Favor de crear bot de asistente de "flespi.com" es bien conocido

---

![Screenshot 2025-03-24 at 2 33 31 p m](https://github.com/user-attachments/assets/5b8e179c-0678-4b0a-ac3b-ae01d09cbd38)

Triptico: https://flespi.com/files/flespi-presentation.pdf

----

# Creacion de un Python "Fake Sensor"

Wokwi es un simulador gratuito y en línea diseñado especialmente para estudiantes, makers y desarrolladores que trabajan con microcontroladores. Destaca especialmente para quienes desean aprender o desarrollar proyectos con MicroPython utilizando la Raspberry Pi Pico W.


Portal de uso simulador MQTT empotrando microcontroladores https://wokwi.com/projects/315787266233467457

```python


