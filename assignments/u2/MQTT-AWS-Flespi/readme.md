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

![Screenshot 2025-03-25 at 2 35 38 p m](https://github.com/user-attachments/assets/3f3070d9-5c8e-484b-af38-575fb5d321ca)


# Creacion de un Python "Fake Sensor"

Wokwi es un simulador gratuito y en línea diseñado especialmente para estudiantes, makers y desarrolladores que trabajan con microcontroladores. Destaca especialmente para quienes desean aprender o desarrollar proyectos con MicroPython utilizando la Raspberry Pi Pico W.


Portal de uso simulador MQTT empotrando microcontroladores https://wokwi.com/projects/315787266233467457


En Wokwi,  permite enviar solicitudes MQTT a brokers como Flespi. Flespi es un broker MQTT público y gratuito que soporta MQTT 5.0, ofreciendo características como conexiones seguras SSL/TLS y un sistema flexible de control de acceso. Puedes simular microcontroladores como el ESP32 o el Raspberry Pi Pico W ejecutando MicroPython y establecer conexiones MQTT con Flespi. Un ejemplo de esto es un proyecto en Wokwi que utiliza un ESP32 para medir la frecuencia cardíaca y enviar los datos a Flespi a través de MQTT.

Para conectar tu simulació, necesitarás crear una cuenta en Flespi para obtener un token de autorización. Luego, en tu código de MicroPython, puedes utilizar este token como el nombre de usuario al configurar la conexión MQTT. Asegúrate de que tu simulación en Wokwi tenga acceso a Internet y que las bibliotecas necesarias para MQTT estén instaladas y correctamente importadas en tu entorno de MicroPython. 

Como por ejemplo:
- 🌦️ **Estación Meteorológica Agrícola:** Envía temperatura, humedad y velocidad del viento cada minuto para monitoreo agrícola.
-  🚗 **Tracker GPS Vehicular:** Reporta coordenadas, velocidad y estado del vehículo cada 30 segundos.
-  ⚡ **Medidor Inteligente de Energía Eléctrica:** Reporta consumo en tiempo real cada minuto para gestión de consumo residencial.
-  🏭 **Sensor de Nivel Industrial:** Envía niveles de tanque y alertas de rebosamiento cada 10 segundos.


---

🛰️ **Práctica MQTT IoT con Flespi, Wokwi y/o AWS Academy** 🌐

 🚀 En esta práctica temática exploraremos MQTT en profundidad utilizando las plataformas Flespi, Wokwi y/o AWS Academy para simular escenarios realistas de integración de dispositivos IoT. Cada uno de UDs. seleccionará un caso del mundo real (ficticio, pero basado en situaciones reales), integrando 10 dispositivos MQTT específicos a ese contexto. Usara ChatGTP bot para que puede amplificar las condiciones de la simulacion para determinar los 10 devices donde acomodarlos para una tematica profesional.

📡 **Escenarios disponibles (cada uno debe integrar 10 dispositivos IoT MQTT):**

1. 🌾 Agricultura Inteligente / pythonC
2. 🚛 Logística y Transporte / diegotescodehub
3. 🏭 Industria 4.0 - brandon0216
4. 🏥 Salud Inteligente - cesarr777
5. 🏙️ Ciudad Inteligente
6. 🏡 Hogar Inteligente / saidtm
7. 🛍️ Retail Inteligente
8. 🎓 Campus Universitario Inteligente
9. 🛳️ Puerto Inteligente / eduardojs7
10. 🏟️ Estadio Inteligente - aagramon
11. 🎢 Parque Temático Inteligente - noelgalgo
12. 🌊 Acuicultura Inteligente
13. ⚡ Redes Eléctricas Inteligentes-PaulScholl
14. 🏨 Hotelería Inteligente / Sh0cko
15. 🚴 Movilidad Inteligente
16. 🌲 Gestión Forestal Inteligente - urieluna17
17. 🚉 Ferrocarriles Inteligentes - molinaedgr
18. 🏢 Edificios Inteligentes / vivianar
19. 🏋️‍♂️ Gimnasios Inteligentes - castiilejo16
20. 🍽️ Restaurantes Inteligentes -jonathan-garcia20
21. 🏖️ Turismo Inteligente-(abnerorterga98)
22. 🎮 Centros de Entretenimiento Inteligentes
23. 🐾 Monitoreo Inteligente de Fauna Silvestre
24. 📦 Almacenes Inteligentes/ 22210329
25. 🎬 Producción Audiovisual Inteligente
26. Gestion vehiculos (uber) / juanuz

📋 **Tareas a realizar:**
- Seleccionar un escenario y diseñar los tópicos MQTT adecuados para cada dispositivo.
- Simular la conexión y comunicación MQTT usando MicroPython en Wokwi y/o AWS Academy.
- Conectar cada dispositivo al broker MQTT Flespi.
- Crear dashboards básicos en Flespi para monitoreo en tiempo real.
- Generar imágenes temáticas para la presentación del proyecto utilizando Adobe Firefly o herramientas similares.
- Documentar claramente los tópicos, mensajes y frecuencias de publicación y suscripción.

📌 **Objetivos de aprendizaje:**
- Comprender y aplicar el protocolo MQTT en distintos escenarios reales.
- Desarrollar habilidades en configuración y gestión de redes IoT heterogéneas.
- Potenciar la capacidad de resolución de problemas mediante simulaciones realistas.
- Aplicar herramientas creativas para la generación visual temática en proyectos técnicos.



