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

