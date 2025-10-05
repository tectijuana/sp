# SoC Heterogéneos como Nodos MQTT

## Introducción y Fundamentos Arquitectónicos del Edge IoT

El Internet de las Cosas (IoT) ha evolucionado desde simples dispositivos de detección hasta complejos nodos de procesamiento en el borde (*Edge*).  
Esta arquitectura se basa en la infraestructura global de Internet, con el propósito de facilitar el intercambio de información y servicios, afectando la seguridad y privacidad de las cadenas de suministro.  

El término *Internet of Things* fue acuñado en **1999** por **Kevin Ashton**, impulsado por tecnologías como la identificación por radiofrecuencia (**RFID**) y la detección emergente.  

La arquitectura IoT suele dividirse en **cuatro capas**:

1. **Capa de detección:** sensores y adquisición de datos.  
2. **Capa de intercambio de datos:** transmisión transparente a través de redes.  
3. **Capa de integración de información:** procesamiento y filtrado de datos.  
4. **Capa de aplicación:** servicios e interfaces para el usuario final.  

Uno de los resultados más notables del crecimiento de IoT es la **enorme generación de datos**, que requiere:  
- Almacenamiento masivo.  
- Procesamiento en tiempo real.  
- Redes de banda ancha eficientes.  

Inicialmente, los nodos IoT usaban microcontroladores ARM Cortex-M y **RTOS** (sistemas operativos de tiempo real), priorizando bajo costo y consumo.  
Sin embargo, las nuevas demandas —como **Machine Learning local**, **seguridad avanzada (TLS)** y **gestión compleja de red**— han llevado a una transición hacia arquitecturas más potentes.  

Aquí surgen los **Sistemas en Chip Heterogéneos (HSoC)**, que combinan:  
- Un **Cortex-A** (alto rendimiento, ejecuta Linux y aplicaciones ricas).  
- Uno o más **Cortex-M** (bajo consumo, ejecuta RTOS para tareas deterministas).  

Esto permite un entorno **Edge Computing** optimizado: rendimiento + eficiencia.

### MQTT como Protocolo Ubicuo para HSoC  

El **MQTT (Message Queuing Telemetry Transport)** es un protocolo ligero y eficiente para entornos de bajo ancho de banda o energía limitada.  
Opera bajo el patrón **publicar/suscribir (Pub/Sub)**, reduciendo tráfico y mejorando latencia respecto a modelos punto a punto.  

#### Niveles de Calidad de Servicio (QoS)

| Nivel | Descripción | Garantía |
|-------|--------------|----------|
| **QoS 0** | “A lo sumo una vez” | Entrega rápida sin garantía |
| **QoS 1** | “Al menos una vez” | Garantiza recepción, puede haber duplicados |
| **QoS 2** | “Exactamente una vez” | Garantiza recepción única |

MQTT también incluye:  
- **Mensajes retenidos:** el *broker* entrega el último mensaje guardado a nuevos suscriptores.  
- **Última Voluntad y Testamento (LWT):** mensaje enviado si un cliente se desconecta abruptamente.  

#### Novedades de MQTT 5.0  
MQTT 5.0 introduce mejoras clave:  
- **Códigos de Razón:** diagnóstico rápido de fallos de comunicación.  
- **Propiedades de Usuario:** adjuntar metadatos (ID de máquina, datos de sensor, etc.).  
- **Suscripciones Compartidas:** balanceo de carga y tolerancia a fallos.  

Se recomienda adoptar **MQTT 5.0** para nuevos proyectos por su mejor escalabilidad y diagnóstico avanzado.

---

### Implicaciones de Diseño y *Trade-offs* para el HSoC  

Los nodos MQTT basados en HSoC deben balancear **Linux (Cortex-A)** y **RTOS (Cortex-M)**.  
Linux ofrece flexibilidad, pero no elimina la necesidad de control determinista con RTOS.  

Desafíos:
- Coordinación entre núcleos.  
- Minimización de la sobrecarga de comunicación (*IPC*).  
- Implementación segura de transporte criptográfico (TLS).  

El reto principal es equilibrar:
- El **rendimiento de red (Cortex-A/Linux)**  
con  
- La **baja latencia y determinismo (Cortex-M/RTOS)**  