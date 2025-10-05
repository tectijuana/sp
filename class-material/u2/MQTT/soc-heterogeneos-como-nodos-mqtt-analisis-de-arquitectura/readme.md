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