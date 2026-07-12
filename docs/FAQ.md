# Preguntas frecuentes (FAQ)

## Sobre el curso

**¿Necesito comprar hardware?**
No necesariamente. El curso usa simuladores (Wokwi, Proteus, Fritzing) y sensores simulados (`class-material/FakeSensors`) para la mayoría de las prácticas. Tener un ESP32 o Raspberry Pi Pico W real ayuda en U04–U06, pero hay rutas alternativas (backend Flask intermedio) para quien no lo tenga.

**¿Qué lenguajes se usan?**
Principalmente MicroPython y C/C++ para microcontroladores; Python para backend y herramientas del stack.

**¿Qué es el AI-IoT-Stack?**
La innovación del ciclo 2027: el pipeline IoT del curso (sensores → MQTT → InfluxDB → dashboards) extendido con una capa de inteligencia — TinyML en el borde y LLMs en la nube. Ver [`docs/ai-iot-stack.md`](./ai-iot-stack.md).

## Sobre entregas y evaluación

**¿Dónde entrego mis prácticas?**
Vía GitHub, según indique cada práctica (pull request a este repo o enlace a tu repositorio). Ver [`docs/guidelines.md`](./guidelines.md).

**¿Puedo entregar tarde?**
Hay un periodo de gracia de 48 horas con penalización del 10%. Después no se aceptan entregas. Ver [`POLICIES.md`](../POLICIES.md).

**¿Cómo se califica el proyecto final?**
Con la rúbrica de [`GRADING.md`](../GRADING.md); desde el ciclo 2027 incluye el criterio "Capa de inteligencia" — el proyecto debe demostrar TinyML o integración LLM funcionando. Requisitos en [`class-material/u6`](../class-material/u6/readme.md).

## Sobre el uso de IA

**¿Puedo usar ChatGPT/Copilot/Claude en mis trabajos?**
Sí, es bienvenido y de hecho el curso lo enseña — pero cada entrega debe incluir la declaración de asistencia de IA ([`ANEXO.md`](../ANEXO.md)) y tú debes poder defender y explicar todo lo entregado. Ver [`AI_GUIDANCE.md`](../AI_GUIDANCE.md).

**¿Qué pasa si uso IA y no lo declaro?**
Se trata como falta de integridad académica, con las consecuencias descritas en [`POLICIES.md`](../POLICIES.md).

**¿Es obligatoria una API key de pago para las prácticas con LLM?**
No. Las prácticas iniciales usan respuestas simuladas (Wokwi), y para las llamadas reales el docente indica las opciones disponibles cada ciclo.
