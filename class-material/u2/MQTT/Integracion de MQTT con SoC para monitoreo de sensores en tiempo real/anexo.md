# Anexo – Integración de MQTT con SoC para Monitoreo de Sensores en Tiempo Real  
**Autor:** Alonso Villela Iker Saúl – 22211517  

## Asistencia de IA  

Para la investigación sobre **integración de MQTT con SoC para el monitoreo de sensores en tiempo real**, utilicé **ChatGPT (GPT-5)** como apoyo únicamente para:  

- Identificar **casos de uso documentados** en IoT donde se aplica MQTT en dispositivos embebidos.  
- Recibir ejemplos de **diagramas de arquitectura** mostrando la interacción entre sensores, SoC, broker MQTT y dashboards.  
- Sugerir la estructura del documento en **formato académico/Markdown** para un README de GitHub.  
- Elaborar **tablas comparativas** sobre protocolos de comunicación (MQTT, CoAP, AMQP) y sus ventajas/desventajas.  
- Redactar de forma más clara los apartados de **ventajas, limitaciones y conclusiones** sobre el uso de SoC con MQTT.  

El contenido final fue redactado, organizado y revisado manualmente por el autor, garantizando la **coherencia académica y técnica**.  

---

## Herramientas Utilizadas  
- **ChatGPT (GPT-5, modo investigador técnico).**  
- **Fecha de asistencia:** 2025-09-30.  
- **Plataforma:** Recomendaciones sobre integración de MQTT en sistemas embebidos.  
- **Otras herramientas:**  
  - VS Code para edición de Markdown y control de versiones en GitHub.  
  - Eclipse Mosquitto (documentación oficial) para confirmar configuración de brokers.  
  - Navegadores web para consulta de documentación técnica (MQTT.org, EMQX, HiveMQ).  

---

## Prompts Utilizados (ejemplos)  
1. *“Genera un informe académico en Markdown sobre integración de MQTT en SoC para monitoreo de sensores en tiempo real.”*  
2. *“Haz una tabla comparativa entre MQTT, CoAP y AMQP con ventajas, limitaciones y aplicaciones.”*  
3. *“Explícame cómo representar en un diagrama de flujo la arquitectura típica de sensores + SoC + MQTT broker + nube.”*  
4. *“Incluye casos de uso de MQTT en IoT (smart cities, industria 4.0, monitoreo ambiental).”*  
5. *“Redacta conclusiones sobre los beneficios de integrar MQTT en sistemas embebidos.”*  

---
## Referencias (Formato APA)  

- Banks, A., & Gupta, R. (2014). *MQTT Version 3.1.1*. OASIS Standard. https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html  
- ARM Ltd. (2023). *Cortex-M Processor Technical Reference Manual*. ARM. https://developer.arm.com/  
- Espressif Systems. (2023). *ESP32 Technical Reference Manual*. Espressif. https://www.espressif.com/  
- Eclipse Foundation. (2023). *Eclipse Mosquitto - An Open Source MQTT Broker*. https://mosquitto.org/  
- NVIDIA. (2023). *Jetson Developer Guide*. NVIDIA. https://developer.nvidia.com/embedded/jetson  
- Sysgo. (2022). *Embedded Systems Design and Optimization*. Sysgo. https://www.sysgo.com/  
- Lee, E. A., & Seshia, S. A. (2020). *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. MIT Press.   daemlo que se vea y no hala fallas
---
## Ejemplos de Información Integrada  

### Comparación de Protocolos de Comunicación
| Protocolo | Características | Ventajas | Desventajas |
|-----------|-----------------|----------|-------------|
| MQTT | Basado en TCP, modelo pub-sub, QoS configurable | Ligero, ideal para IoT, eficiente en tiempo real | Requiere broker central |
| CoAP | Basado en UDP, enfoque REST | Bajo overhead, integración con web | Menor fiabilidad que MQTT |
| AMQP | Mensajería empresarial robusta | Alto nivel de seguridad, colas avanzadas | Complejidad y mayor consumo |

### Arquitectura típica MQTT + SoC
```mermaid
flowchart TD
    A[Sensor IoT] --> B[SoC con Cliente MQTT]
    B --> C[Broker MQTT]
    C --> D[Servidor en la Nube]
    D --> E[Dashboard en Tiempo Real]



