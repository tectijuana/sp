#  Anexo – Información Adicional
## 1. Propósito del Anexo

- Proporcionar detalles complementarios que no caben directamente en el cuerpo del `README.md`.
- Incluir abreviaciones, supuestos, aspectos de diseño y posibles extensiones.
- Servir como referencia técnica para quien revise o expanda el proyecto.

---

## 2. Abreviaturas y Términos Técnicos

| Abreviatura / Término | Significado / Descripción |
|------------------------|-----------------------------|
| FPGA                   | Field‑Programmable Gate Array |
| MQTT                   | Message Queuing Telemetry Transport |
| PWM                    | Pulse‑Width Modulation (modulación por ancho de pulso) |
| H‑Bridge                | Puente en H (control bidireccional de motor) |
| TLS                    | Transport Layer Security |
| QoS                    | Quality of Service (niveles de calidad en MQTT) |
| ADC                    | Analog-to-Digital Converter (convertidor analógico a digital) |
| Uptime                 | Tiempo de disponibilidad operativa continua |
| SoC                    | System on Chip (cuando la FPGA incorpora procesador) |

---

## 3. Supuestos del Diseño

1. La red Ethernet o canal de comunicación tiene **baja latencia** y jitter controlado.  
2. Los sensores tienen tiempos de muestreo compatibles con la frecuencia de control requerida.  
3. La carga mecánica del motor varía dentro de rangos esperados, sin abruptas transiciones imposibles de controlar.  
4. El broker MQTT se encuentra en una red confiable con buena disponibilidad (alta uptime).  
5. Los niveles eléctricos (voltajes, corrientes) y requisitos de aislamiento están dimensionados correctamente para el motor y los sensores.  
6. El hardware y la FPGA tienen recursos suficientes (memoria, lógica) para soportar el cliente MQTT, buffers y control en paralelo.

---

## 4. Seguridad, Robustez y Buenas Prácticas

- **Cifrado de datos (TLS):** Asegurar que la comunicación MQTT esté cifrada para proteger la confidencialidad e integridad.  
- **Autenticación:** Uso de credenciales seguras (usuario/contraseña) para el acceso al broker.  
- **QoS y reintentos:** Usar QoS = 1 o 2 en MQTT para garantizar que los mensajes críticos lleguen, con reintentos automáticos en fallos transitorios.  
- **Watchdog interno en FPGA:** Mecanismo de supervisión que reinicia el sistema si se detecta bloqueo o condición anómala.  
- **Validación de datos entrantes:** Verificar valores sensoriales atípicos antes de actuar (evitar errores catastróficos por señales corruptas).  
- **Actualización segura:** Si se habilita actualización remota (FOTA), debe hacerse con validación de firma para evitar código malicioso.  
- **Registro de eventos (logging):** Mantener logs de fallos, reconexiones, límites excedidos para diagnóstico post-mortem.

---

## 5. Extensiones Futuras (Ideas para mejorar)

- Control de **múltiples motores** desde una única FPGA, con escalabilidad modular.  
- Soporte adicional para protocolos alternativos como **CoAP** o **AMQP**, permitiendo comparación con MQTT.  
- Despliegue de **broker MQTT redundante** en cluster para tolerancia a fallos.  
- Integración de **actualizaciones OTA (Over-The-Air)** mediante MQTT con firma y verificación.  
- Uso de **machine learning o modelos predictivos** para anticipar fallas mecánicas a partir de la telemetría capturada.  
- Interfaz gráfica local en la FPGA (si dispone de pantalla) para monitoreo y control autónomo offline.

---

## 6. Artefactos de Referencia

- Diagrama conceptual y diagrama detallado de la arquitectura del sistema.  
- Tablas con métricas propuestas (latencia, precisión, consumo, disponibilidad).  
- Manuales y especificaciones técnicas usados: Nios II, MQTT, diseño digital, etc.  
- Códigos de ejemplo o pseudocódigo para cliente MQTT, generación PWM, manejo de sensores.

---

## 7. Guía de Estilo y Uso (Inspirada en AI_GUIDANCE)

Para asegurar que la documentación y el código del proyecto mantengan coherencia y calidad, aquí tienes algunas recomendaciones de estilo:

- Utiliza **Markdown limpio y estructurado**: encabezados (niveles), tablas, listas, negritas y cursivas según convenga.  
- Si incluyes fragmentos de código o secuencias, usa bloques de código con especificación de lenguaje (```c, ```vhdl, etc.).  
- Introduce comentarios y explicaciones mínimas en cada sección para que quien lea entienda el flujo y propósito.  
- En versiones futuras, considera un sistema de **plantillas (template)** para generar documentos uniformes si amplías el proyecto.  
- Define convenciones para nombres de módulos, señales y temas de red/seguridad desde un inicio, y documenta estas convenciones aquí.  
- Cada vez que actualices el proyecto, actualiza también el anexo para mantener sincronía entre la documentación y el diseño real.

---

## 8. Referencias

1. Intel (Altera). (2020). *Nios II processor reference handbook*.  
2. OASIS. (2014). *MQTT version 3.1.1 specification*.  
3. Roth, C. H., & John, L. K. (2008). *Diseño digital con VHDL*.  
4. Pellerin, D., & Thibault, S. (2005). *Practical FPGA programming in C*.  
5. TechTarget. (2021). *IoT protocols comparison: MQTT, CoAP, AMQP and more*.  

---
