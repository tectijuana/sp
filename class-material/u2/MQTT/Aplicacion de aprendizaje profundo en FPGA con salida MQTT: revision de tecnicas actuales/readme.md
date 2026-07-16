### Omar Zamorano Garcia
### No.Control: 22211676
# Aplicación de aprendizaje profundo en FPGA con salida MQTT: revisión de técnicas actuales

## Introducción
Actaulmente el desarrollo de sistemas inteligentes en el área del Internet de las Cosas (IoT) ha impulsado la integración de algoritmos de aprendizaje profundo (IA) en dispositivos de bajo consumo y alta eficiencia, como las Field Programmable Gate Arrays (FPGAs). Estos dispositivos permiten la ejecución paralela de programas instalados en el hardware y a su vez el entrenamiento y uso de sistemas inteligentes. 

La combinación de aprendizaje profundo en FPGA con salida vía MQTT abre un panorama de aplicaciones en áreas como la visión artificial, el monitoreo industrial, la salud, los sistemas autónomos y cualqueier tipo de sistemas en los que la IA puede resultar beneficiosa. A continuación, se revisarán las características del protocolo MQTT, su relevancia en sistemas programables, y las técnicas actuales que integran FPGA, deep learning y comunicación IoT.

## MTQQ
El Message Queuing Telemetry Transport (MQTT) es un protocolo de mensajería basado en el modelo ***publicador/suscriptor***, diseñado para comunicaciones en redes con recursos limitados o condiciones poco confiables. 

El modelo ***publicador/suscriptor*** consta de comunicación por medio de un intermediario. El publicador envía datos a un intermediario llamado broker el cual sirve como servidor, despuués el suscriptor accede al broker para rescatar cualquier dato que haya llegado. Este modelo permite que dispositivos de bajos recursos se puedan comunicar ya que en realidad no existe una comunicación directa, sino que existe un repositorio de datos donde otro dispositivo los rescata.

### Principios básicos:

- Modelo publish/subscribe: Los clientes publican mensajes en “temas” (topics), y otros clientes se suscriben a dichos temas para recibir los mensajes.
- Broker central: Actúa como intermediario entre publicadores y suscriptores, gestionando la distribución de datos.
- Ligereza: Su sobrecarga mínima (encabezados de apenas 2 bytes) lo hace ideal para dispositivos con recursos limitados como sensores, microcontroladores o FPGA.
- Calidad de servicio (QoS): Ofrece tres niveles de entrega de mensajes:
  - QoS 0: al menos una vez, sin confirmación.
  - QoS 1: entrega garantizada al menos una vez.
  - QoS 2: entrega exactamente una vez (mayor fiabilidad).

![MTQQ](https://taufikcrisnawan.dev/_next/image?url=https:%2F%2Fik.imagekit.io%2Ftaufik%2Fblog%2Fhow-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-debian-11%2Fthumbnail.png&w=1920&q=75)

### Aplicaciones actuales:
Hoy en día MQTT se utiliza en:
- **IoT doméstico:** domótica, sensores de temperatura, cámaras inteligentes.
- **Industria 4.0:** monitoreo de maquinaria y control remoto de procesos.
- **Transporte y logística:** seguimiento de vehículos y carga en tiempo real.
- **Salud digital:** transmisión de datos biométricos desde dispositivos médicos portátiles.

![IoT](https://img.freepik.com/premium-vector/iot-internet-things-devices-connectivity-concepts-network-flat-style-with-people_194782-1655.jpg?w=2000)

## ¿Qué es un FPGA?
Un Field Programmable Gate Array (FPGA) es un circuito integrado digital programable por el usuario después de su fabricación. A diferencia de los microcontroladores o procesadores tradicionales, que tienen una arquitectura fija, los FPGA permiten configurar su estructura interna para implementar distintos tipos de circuitos y sistemas digitales.

### La arquitectura básica de un FPGA está compuesta por:
- **Bloques lógicos programables (CLBs):** unidades que pueden configurarse para implementar puertas lógicas, registros y funciones combinacionales o secuenciales.
- **Interconexiones programables:** permiten enlazar los bloques lógicos entre sí para formar sistemas complejos.
- **Bloques de memoria embebida (BRAM):** utilizados para almacenamiento temporal de datos o buffers.
- **Elementos dedicados:** como multiplicadores, DSPs y controladores de E/S, diseñados para acelerar operaciones específicas.

![FPGA](https://image.slideserve.com/604529/basic-fpga-architecture-l.jpg)

## Aprendizaje profundo en FPGA
El aprendizaje profundo se caracteriza por el uso de redes neuronales profundas (DNN, CNN, RNN, entre otras), que requieren altas capacidades de cómputo. Las FPGAs representan una alternativa intermedia entre GPUs y microcontroladores, ya que:

- Permiten la paralelización masiva de operaciones matemáticas.
- Son reconfigurables, adaptándose a distintos modelos de redes neuronales.
- Consumen menos energía que las GPU, lo cual es crítico en entornos embebidos.

Actualmente, existen herramientas como Xilinx Vitis AI e Intel OpenVINO que facilitan la implementación de modelos de deep learning en FPGA, optimizando capas convolucionales, operaciones de pooling y funciones de activación.

## Integración FPGA + Deep Learning + MQTT

El flujo de trabajo típico en un sistema de aprendizaje profundo con salida MQTT es el siguiente:

1- **Captura de datos:** sensores o cámaras conectados al FPGA.

2- **Procesamiento local:** la FPGA ejecuta el modelo de red neuronal para clasificar, detectar o inferir patrones en tiempo real.

3- **Generación de resultados:** salida en forma de etiquetas, probabilidades o alertas.

4- **Transmisión vía MQTT:** el FPGA, actuando como cliente MQTT, publica los resultados en un broker para que aplicaciones externas los consuman.

![Deep Learning](https://tse1.mm.bing.net/th/id/OIP.NqFoz0tlweyC8n8j2gVqLwHaCy?rs=1&pid=ImgDetMain&o=7&rm=3)

### Ejemplos de aplicación:
- **Visión artificial en drones:** detección de obstáculos con CNN en FPGA, enviando alertas al centro de control por MQTT.
- **Monitoreo industrial:** análisis de vibraciones en maquinaria mediante redes neuronales, con notificaciones MQTT a un panel de supervisión.
- **Sistemas médicos portátiles:** FPGA procesando señales de ECG en tiempo real y publicando los diagnósticos vía MQTT a una app móvil.
- **Ciudades inteligentes:** detección de tráfico o incidentes a través de FPGA con salida MQTT hacia sistemas de gestión urbana.

## Referencias

MQTT. (s. f.). MQTT: The standard for IoT messaging. [https://mqtt.org/](https://mqtt.org/)

Amazon Web Services. (s. f.). ¿Qué es MQTT? Explicación del protocolo MQTT. [https://aws.amazon.com/es/what-is/mqtt/](https://aws.amazon.com/es/what-is/mqtt/)

Topologías de Red. (s. f.). Protocolo MQTT: Guía completa para principiantes y expertos. [https://topologiasdered.com/blog/protocolo-mqtt/](https://topologiasdered.com/blog/protocolo-mqtt/)

Bing. (s. f.). Qué es FPGA. [https://www.bing.com/search?q=que%20es%20fpga&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=que%20es%20fpga&sc=12-11&sk=&cvid=8FA14C2E3FD94534B9F165493E4FC53B](https://www.bing.com/search?q=que%20es%20fpga&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=que%20es%20fpga&sc=12-11&sk=&cvid=8FA14C2E3FD94534B9F165493E4FC53B)

Encuentra el significado. (s. f.). FPGA: ¿Qué significa y cómo funciona este componente electrónico? [https://www.encuentraelsignificado.com/que-significa-fpga/](https://www.encuentraelsignificado.com/que-significa-fpga/)

Khaki, A. M. Z., & Choi, A. (2025). Optimizing Deep Learning Acceleration on FPGA for Real-Time and Resource-Efficient Image Classification. Applied Sciences, 15(1), 422. [https://www.mdpi.com/2076-3417/15/1/422](https://www.mdpi.com/2076-3417/15/1/422)
