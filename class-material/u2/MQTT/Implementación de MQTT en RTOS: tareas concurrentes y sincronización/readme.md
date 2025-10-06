<div align="center">

# 🎓 Implementacion de MQTT en RTOS: 
### Tareas Concurrentes Y Sincronizacion
## Sistemas Programables
### Castro Balbuena Angel Andres - 22211534

**Instituto Tecnologico De Tijuana**

*01/10/25*

---

</div>
Asistencia de IA: Utilicé chatgpt para que me diera mi texto en formato Markdown Herramienta: ChatGPT Fecha: 01 de Octubre 2025
# Implementación de MQTT en RTOS: Tareas Concurrentes y Sincronización

## Introducción

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero basado en el patrón publicación-suscripción, diseñado específicamente para dispositivos con recursos limitados y redes con ancho de banda restringido. Cuando se implementa en sistemas operativos de tiempo real (RTOS), surgen desafíos particulares relacionados con la gestión de tareas concurrentes y la sincronización de recursos compartidos.

La integración de MQTT en entornos RTOS permite desarrollar aplicaciones IoT robustas donde múltiples tareas pueden comunicarse de manera eficiente con brokers remotos, manteniendo las garantías de tiempo real que estos sistemas requieren.

## MQTT en Sistemas Embebidos

### Características del Protocolo MQTT

MQTT opera sobre el protocolo TCP/IP y fue diseñado con un "pequeño código footprint", haciéndolo ideal para dispositivos embebidos. El protocolo sigue el estándar ISO/IEC PRF 20922 y se basa en un modelo cliente-servidor donde un broker central gestiona todas las comunicaciones entre clientes (MQTT.org, s.f.).

### Implementaciones para RTOS

Las implementaciones más comunes de MQTT para RTOS incluyen bibliotecas optimizadas que consideran las restricciones de memoria y procesamiento. FreeRTOS, uno de los RTOS más utilizados, ofrece la biblioteca coreMQTT, que proporciona una implementación cliente del estándar MQTT 3.1.1 específicamente diseñada para dispositivos embebidos (Amazon Web Services, s.f.).

## Arquitectura de Tareas Concurrentes

### Modelo de Múltiples Tareas

En una implementación típica de MQTT sobre RTOS, se emplean múltiples tareas concurrentes que operan de manera paralela:

- **Tarea MQTT Agent**: Gestiona la conexión MQTT y procesa las solicitudes entrantes de otras tareas
- **Tareas Productoras**: Generan datos y publican mensajes MQTT
- **Tareas Consumidoras**: Suscriben a topics y procesan mensajes recibidos
- **Tarea de Red**: Maneja la pila TCP/IP y las operaciones de socket

### Compartición de Conexión MQTT

Un desafío crítico es permitir que múltiples tareas compartan una única conexión MQTT sin conflictos. La biblioteca coreMQTT-Agent de FreeRTOS resuelve esto implementando un patrón de agente (daemon) que proporciona APIs thread-safe, permitiendo que diferentes hilos compartan una conexión MQTT sin que la aplicación deba gestionar primitivas de sincronización directamente (FreeRTOS, s.f.-a).

## Mecanismos de Sincronización

### Semáforos

Los semáforos son objetos de sincronización fundamentales en RTOS que mantienen un contador y se utilizan principalmente para:

- **Señalización de eventos**: Un semáforo binario puede indicar cuándo los datos MQTT están listos para procesarse
- **Gestión de recursos finitos**: Los semáforos contadores controlan el acceso a un número limitado de buffers o conexiones

Los semáforos binarios tienen solo dos estados: disponible (count = 1) e indisponible (count = 0), siendo ideales para señalización entre tareas (Texas Instruments, s.f.). Los semáforos son particularmente útiles para señalar eventos, como cuando los datos están listos para ser procesados (InTechHouse, s.f.).

### Colas (Queues)

Las colas son el mecanismo principal de comunicación entre tareas en RTOS. Funcionan como buffers FIFO (First In First Out) thread-safe y permiten:

- Enviar solicitudes MQTT desde múltiples tareas al agente MQTT
- Pasar datos entre productores y consumidores
- Comunicación segura entre interrupciones y tareas

Las colas típicamente tienen un receptor específico y uno o varios emisores. En el contexto de MQTT, una tarea puede enviar continuamente solicitudes a la cola del agente hasta que esta se llene y la tarea productora se bloquee, permitiendo entonces que el agente procese las solicitudes pendientes (Amazon Web Services, s.f.; FreeRTOS, s.f.-b).

### Mutexes

Los mutex (mutual exclusion) son esenciales para proteger recursos compartidos como:

- Variables globales de estado MQTT
- Buses de comunicación
- Estructuras de datos compartidas

Los mutex implementan herencia de prioridad en RTOS bien diseñados, evitando el problema de inversión de prioridad donde una tarea de baja prioridad bloquea indefinidamente a una de alta prioridad (López, 2025; InTechHouse, s.f.).

## Patrones de Implementación

### Patrón Agent/Daemon

El patrón más robusto consiste en una tarea dedicada (MQTT Agent) que:

1. Mantiene la conexión MQTT activa
2. Recibe comandos de otras tareas mediante una cola
3. Ejecuta operaciones MQTT (publicar, suscribir, desuscribir)
4. Notifica resultados mediante callbacks o semáforos

Este diseño centraliza la gestión de la conexión y elimina race conditions al serializar todas las operaciones MQTT a través de un único punto de control.

### Tareas Concurrentes por Cliente

Una alternativa para brokers embebidos es asignar una tarea dedicada a cada cliente conectado, donde cada tarea escucha su propio socket TCP en paralelo. Este método permite que el broker escuche a todos los clientes MQTT simultáneamente, mejorando la eficiencia temporal mediante concurrencia (Cajas, s.f.).

### Gestión de Prioridades

En sistemas RTOS es crucial establecer prioridades apropiadas:

- **Alta prioridad**: Tareas críticas de tiempo real que publican datos sensibles al tiempo
- **Media prioridad**: Tarea MQTT Agent para garantizar procesamiento oportuno
- **Baja prioridad**: Tareas de mantenimiento y procesamiento no crítico

## Consideraciones de Diseño

### Prevención de Inanición

El agente MQTT debe protegerse contra inanición (starvation) cuando tareas de mayor prioridad envían solicitudes continuamente. Esto se logra mediante:

- Limitación del tamaño de la cola de comandos
- Implementación de timeouts en operaciones bloqueantes
- Balanceo de prioridades entre tareas

### Uso Eficiente de Memoria

Los RTOS tienen memoria limitada, por lo que es importante:

- Dimensionar apropiadamente las colas (número y tamaño de elementos)
- Reutilizar buffers mediante pools de memoria
- Evitar asignaciones dinámicas frecuentes durante operación normal
- Optimizar el tamaño de stack de cada tarea

### Manejo de Desconexiones

La implementación debe gestionar:

- Reconexiones automáticas con backoff exponencial
- Reenvío de mensajes pendientes tras reconexión
- Notificación a tareas cuando la conexión se pierde
- Almacenamiento temporal de mensajes críticos

## Ejemplo de Flujo de Trabajo

1. **Tarea Productora** genera datos del sensor
2. Envía comando PUBLISH a la cola del MQTT Agent
3. **MQTT Agent** extrae comando de la cola
4. Ejecuta MQTT_Publish() sobre la conexión
5. Envía confirmación mediante callback a la tarea productora
6. **Tarea Productora** continúa su operación

Este flujo asegura que múltiples tareas pueden publicar mensajes MQTT sin interferir entre sí ni corromper el estado de la conexión.

## Conclusiones

La implementación de MQTT en RTOS requiere un diseño cuidadoso que balancee los requisitos de tiempo real con la naturaleza asíncrona de las comunicaciones de red. Los mecanismos de sincronización como semáforos, colas y mutex son fundamentales para coordinar tareas concurrentes que comparten recursos MQTT.

El patrón agent/daemon se ha consolidado como la mejor práctica, proporcionando thread-safety sin imponer carga de sincronización a las aplicaciones. Las implementaciones modernas como coreMQTT-Agent demuestran que es posible crear sistemas robustos y eficientes donde múltiples tareas RTOS interactúan con brokers remotos manteniendo las garantías deterministas que estos sistemas requieren.

La correcta asignación de prioridades, dimensionamiento de recursos y manejo de errores son aspectos críticos que determinan el éxito de estas implementaciones en aplicaciones IoT de producción.

## Referencias

Amazon Web Services. (s.f.). *coreMQTT library - FreeRTOS*. AWS Documentation. https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt.html

Amazon Web Services. (s.f.). *Intertask coordination - FreeRTOS*. AWS Documentation. https://docs.aws.amazon.com/freertos/latest/userguide/inter-task-coordination.html

Cajas, A. (s.f.). *EmbeddedMqttBroker: This is a Mqtt broker for embedded devices, developed in C++, FreeRTOS to use advanced multitasking capabilities, and arduino core*. GitHub. https://github.com/alexCajas/EmbeddedMqttBroker

FreeRTOS. (s.f.-a). *coreMQTT-Agent: Implements an MQTT agent (or daemon) task for simple MQTT connection sharing among different threads of execution*. GitHub. https://github.com/FreeRTOS/coreMQTT-Agent

FreeRTOS. (s.f.-b). *coreMQTT-Agent-Demos: Demonstrates use of coreMQTT-Agent for simple MQTT connection sharing among different threads of execution*. GitHub. https://github.com/FreeRTOS/coreMQTT-Agent-Demos

InTechHouse. (s.f.). *Advanced Inter-Task Communication in RTOS*. https://intechhouse.com/blog/advanced-inter-task-communication-in-rtos/

López, J. (2025, 17 de mayo). *Demystifying FreeRTOS: A Practical Guide to Semaphores, Queues, and Mutexes*. Medium. https://medium.com/@joaquinlopezm/demystifying-freertos-a-practical-guide-to-semaphores-queues-and-mutexes-4113b9bb338c

MQTT.org. (s.f.). *Comparison of MQTT implementations*. Wikipedia. https://en.wikipedia.org/wiki/Comparison_of_MQTT_implementations

Percepio. (2023, 23 de mayo). *RTOS 101: Semaphores and Queues*. https://percepio.com/rtos-101-semaphores-and-queues/

Texas Instruments. (s.f.). *Thread Synchronization — SimpleLink™ CC13XX/CC26XX SDK BLE5-Stack User's Guide*. https://software-dl.ti.com/simplelink/esd/simplelink_cc13xx_cc26xx_sdk/8.30.01.01/exports/docs/ble5stack/ble_user_guide/html/freertos/synchronization.html
