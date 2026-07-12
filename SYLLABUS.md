# Syllabus — Sistemas Programables

**Carrera:** Ingeniería en Sistemas Computacionales  
**Institución:** Tecnológico Nacional de México (TECNM)  
**Duración:** 16 semanas  
**Modalidad:** Teórico–práctico con laboratorio  
**Créditos:** 6  
**Revisión del temario:** 2027

---

## Descripción del curso

El curso de **Sistemas Programables** proporciona los fundamentos teóricos y prácticos para el diseño, programación e integración de sistemas embebidos con arquitecturas de nube e IoT. Se abordan microcontroladores, interfaces de entrada/salida, protocolos de comunicación, mensajería y persistencia de datos, visualización, inteligencia artificial en el borde (Edge AI) e integración con modelos de lenguaje (LLM), así como el desarrollo de un proyecto integrador con sensores, actuadores y plataformas IoT reales.

> La innovación del ciclo 2027 es el **AI-IoT-Stack**: el mismo pipeline de datos IoT del curso, con una capa de inteligencia (Edge AI/TinyML y orquestación con LLM) que razona sobre los datos en vez de solo graficarlos. Ver [`docs/ai-iot-stack.md`](./docs/ai-iot-stack.md).

---

## Resultados de aprendizaje

Al finalizar el curso, el estudiante será capaz de:

1. Comprender la arquitectura y funcionamiento de microcontroladores y microprocesadores comunes.
2. Programar sistemas embebidos utilizando lenguajes como C/C++ y MicroPython, apoyado en entornos de nube (AWS Academy) y simuladores (Wokwi, Proteus, Fritzing).
3. Diseñar y simular circuitos digitales que integren sensores y actuadores.
4. Implementar protocolos de comunicación (UART, SPI, I²C, MQTT) y desplegar un stack IoT (broker MQTT, EdgeX Foundry) para la ingesta de datos.
5. Persistir y visualizar datos de sensores en series temporales (InfluxDB) mediante dashboards (Grafana, Prometheus, ThingsBoard).
6. Integrar sistemas embebidos con servicios en la nube, APIs externas y modelos de IA (Edge AI/TinyML y LLMs) aplicando buenas prácticas de eficiencia y seguridad.
7. Desarrollar un proyecto final que resuelva un problema real mediante un sistema programable conectado.

---

## Unidades temáticas

- **U01 — Fundamentos y entorno cloud-embebido**
  - Arquitectura básica de un microcontrolador
  - Entorno de desarrollo, simuladores (Wokwi, Proteus, Fritzing)
  - AWS Academy, instancias EC2 y despliegue de un backend ligero (Flask)
- **U02 — Sensores, actuadores y mensajería IoT**
  - Lenguaje C/C++ y MicroPython; manejo de pines digitales y analógicos
  - Protocolos UART, SPI, I²C
  - Mensajería pub/sub con MQTT (Mosquitto/EMQX) y procesamiento en el borde con EdgeX Foundry
  - Desafíos de diseño IoT con impacto social y ambiental
- **U03 — Persistencia y visualización de datos**
  - Bases de datos de series temporales (InfluxDB)
  - Dashboards y monitoreo (Grafana, Prometheus, ThingsBoard)
  - Tipos de dashboards (estratégico, táctico, operacional, informativo)
- **U04 — Comunicaciones avanzadas e integración con IA**
  - Conectividad WiFi y Bluetooth (ESP32, RP Pico W) y opciones de bajo consumo (LoRaWAN)
  - Consumo de APIs externas (REST/HTTP) desde microcontroladores
  - Integración de asistentes LLM (ChatGPT, Copilot) en flujos de sensores
- **U05 — Edge AI, seguridad y eficiencia**
  - Inteligencia artificial en el borde (TinyML)
  - Seguridad en sistemas embebidos e IoT (autenticación, cifrado, buenas prácticas)
  - Eficiencia energética y contenerización ligera en el borde
- **U06 — Proyecto integrador**
  - Diseño, implementación, documentación y presentación de un sistema programable conectado de extremo a extremo

---

## Evaluación

- **Prácticas de laboratorio (5–6):** 40%  
- **Quizzes y evaluaciones parciales:** 15%  
- **Participación y revisiones por pares:** 10%  
- **Proyecto final:** 35%  

> Detalles y rúbricas en [GRADING.md](./GRADING.md).

---

## Bibliografía y recursos

- Mazidi, Muhammad Ali. *Microcontrollers and Embedded Systems*.
- Simon Monk. *Programming Arduino: Getting Started with Sketches*.
- Elecia White. *Making Embedded Systems*.
- *TinyML for Edge Intelligence in IoT and LPWAN Networks*.
- *Building IoT Visualizations using Grafana*.
- *Mastering LoRaWAN: Comprehensive Guide to Low-Power IoT Communication*.
- Ver catálogo completo en [`resources/bibliography.md`](./resources/bibliography.md).
- Documentación oficial:
  - [ESP32 — Espressif Docs](https://docs.espressif.com/)
  - [Raspberry Pi Pico — Docs](https://www.raspberrypi.com/documentation/microcontrollers/)
  - [EdgeX Foundry Docs](https://docs.edgexfoundry.org/)
  - [ThingsBoard Docs](https://thingsboard.io/docs/)

---

## Políticas del curso

- **Asistencia:** obligatoria en laboratorios.
- **Integridad académica:** todos los proyectos deben ser originales.
- **Colaboración:** se permite discutir soluciones, pero los entregables son individuales salvo indicación contraria.
- **Entregas:** cada práctica indica fecha y hora límite.
- **Accesibilidad:** materiales disponibles en repositorio GitHub para consulta permanente.

---

## Notas finales

- La programación de sistemas embebidos requiere tanto **práctica en hardware real** como uso de **simuladores**.  
- Los estudiantes deberán documentar cada práctica en el repositorio siguiendo las guías de contribución.

