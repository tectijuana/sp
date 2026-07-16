**Instituto Tecnológico de Tijuana**

**Ing. Sistemas Computacionales**

**Prof. René Solis Reyes**

**Sistemas Programables**

**Fonseca Novelo 22211562**

# Arquitectura Cliente-Servidor en MQTT  
## Análisis del rol del broker y los clientes  

# Índice  

- [Introducción](#introducción)  
- [El rol del broker](#el-rol-del-broker)  
- [El rol de los clientes](#el-rol-de-los-clientes)  
- [Interacción entre broker y clientes](#interacción-entre-broker-y-clientes)  
- [Ventajas del modelo cliente-servidor en MQTT](#ventajas-del-modelo-cliente-servidor-en-mqtt)  
- [Limitaciones y desafíos](#limitaciones-y-desafíos)  
- [Conclusión](#conclusión)  


### Introducción  
MQTT es un protocolo ligero de mensajería que se basa en una arquitectura cliente-servidor, donde el **broker** ocupa el rol central y los **clientes** (publicadores y suscriptores) interactúan a través de él. Esta estructura está pensada para resolver problemas de comunicación en redes inestables o con dispositivos de bajos recursos, como los que suelen encontrarse en el Internet de las Cosas (IoT). A diferencia de un modelo punto a punto, aquí los clientes nunca se comunican directamente entre sí, lo que reduce la complejidad y mejora la escalabilidad.  

### El rol del broker  
El broker puede entenderse como el “cerebro” de la red MQTT. Su trabajo es recibir todos los mensajes que los clientes publican y luego distribuirlos solo a aquellos clientes que estén interesados en ellos. Para esto utiliza el sistema de **topics**, que actúan como etiquetas o rutas jerárquicas que identifican cada mensaje. Además de enrutar, el broker también puede encargarse de verificar identidades, aplicar políticas de seguridad, almacenar mensajes en sesiones persistentes y enviar mensajes especiales como los de *Last Will and Testament*.  

La importancia del broker radica en que simplifica la comunicación. Sin él, cada cliente tendría que saber exactamente a qué otro cliente enviar información, lo que se volvería inmanejable en escenarios con cientos o miles de dispositivos. Gracias al broker, cada cliente solo necesita saber a qué servidor conectarse, sin preocuparse por quién recibirá el mensaje final.  

![mqtt](https://academy.nordicsemi.com/wp-content/uploads/2022/10/cellfund_less4_mqtt_protocol.png)

### El rol de los clientes  
Los clientes en MQTT pueden actuar como **publicadores**, **suscriptores**, o ambos al mismo tiempo. Un publicador envía mensajes a un *topic* sin necesidad de saber quién los recibirá. Un suscriptor, por su parte, se suscribe a ciertos *topics* para recibir los mensajes asociados. Esta división hace que los clientes sean livianos y fáciles de implementar en casi cualquier lenguaje de programación o dispositivo, desde un microcontrolador hasta un servidor en la nube.  

Los clientes también pueden definir parámetros importantes al conectarse al broker, como el nivel de **QoS (Quality of Service)**, que especifica cuánta garantía de entrega se requiere para un mensaje. Esto permite que un sensor barato pueda enviar datos sin importar si se pierden algunos paquetes, mientras que una aplicación crítica puede exigir entrega exacta de cada mensaje.  

### Interacción entre broker y clientes  
La interacción entre el broker y los clientes se da siempre sobre un canal de comunicación seguro y persistente, normalmente a través de **TCP/IP**. El proceso inicia cuando un cliente se conecta al broker enviando un mensaje especial de **CONNECT**. Si todo sale bien, el broker responde con un **CONNACK** que confirma la conexión. A partir de ese momento, el cliente puede publicar mensajes o suscribirse a los *topics* de su interés.  

Un detalle clave es que la conexión es mantenida abierta mientras ambos extremos estén activos, gracias a mecanismos como el **Keep Alive**, que envía pequeños mensajes de latido para evitar que la conexión “se congele”. Además, en caso de una desconexión inesperada, el broker puede notificar a los demás clientes con un mensaje de *Last Will and Testament*, lo que asegura que el sistema siempre tenga información del estado de cada dispositivo.  

![mqtt](https://cdn.prod.website-files.com/5ff66329429d880392f6cba2/6708f5b15374117c840d5fcc_6708ee20807b31c351ce6a22_7%2520-%252010.10-min.jpeg)

### Ventajas del modelo cliente-servidor en MQTT  
Una de las grandes ventajas de esta arquitectura es la **desacoplación**. Los publicadores y suscriptores no necesitan conocerse ni ejecutarse al mismo tiempo, lo que permite construir sistemas mucho más flexibles y escalables. Además, el broker centraliza funciones críticas como seguridad, control de acceso y almacenamiento de mensajes, evitando que cada cliente tenga que implementar estas funciones por separado.  

Otra ventaja es la **eficiencia**: al ser un protocolo ligero, los mensajes en MQTT tienen un encabezado mínimo y se transmiten con poco consumo de ancho de banda, lo que resulta esencial para redes móviles, dispositivos con baterías pequeñas o enlaces satelitales. También se presta bien para escenarios de gran escala, ya que un broker moderno puede manejar miles o millones de conexiones concurrentes mediante clustering y balanceo de carga.  

### Limitaciones y desafíos  
Aunque la arquitectura cliente-servidor con un broker central trae muchas ventajas, también tiene limitaciones. La principal es que el broker se convierte en un **punto único de fallo**: si el broker cae, toda la red de clientes queda incomunicada. Por eso, en sistemas críticos se implementan brokers redundantes o distribuidos para garantizar alta disponibilidad.  

Otro desafío es la **seguridad**. Como todos los mensajes pasan por el broker, es fundamental implementar cifrado (TLS/SSL), autenticación y autorización para evitar accesos no autorizados o fugas de datos. Además, aunque MQTT es muy eficiente, no siempre es la mejor opción para transmisión de archivos grandes o comunicaciones con baja latencia estricta, ya que fue diseñado principalmente para mensajes pequeños y frecuentes.  

### Conclusión  
La arquitectura cliente-servidor de MQTT, con el broker como eje central y los clientes como nodos que publican o reciben mensajes, ofrece un equilibrio entre simplicidad, eficiencia y escalabilidad. El modelo facilita la comunicación en entornos IoT y sistemas distribuidos, permitiendo que dispositivos con recursos limitados interactúen en tiempo real sin necesidad de conexiones directas.  

El rol del broker es crítico, pues asume la responsabilidad de gestionar las suscripciones, entregar mensajes con garantías de servicio y mantener la coherencia del sistema aun en escenarios de desconexiones. Los clientes, por su parte, se benefician de esta simplicidad al delegar en el broker la complejidad de la comunicación.  

En resumen, el diseño cliente-servidor en MQTT es un ejemplo de cómo una arquitectura bien pensada puede transformar la manera en que los dispositivos se comunican, haciendo posible el crecimiento explosivo de aplicaciones en el Internet de las Cosas.  

## Referencias  

1. [MQTT Version 5.0 – OASIS Open](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) — Especificación oficial de MQTT 5.  
2. [MQTT Essentials Part 8: Retained Messages (HiveMQ)](https://www.hivemq.com/blog/mqtt-essentials-part-8-retained-messages/) — Explicación de mensajes retenidos en MQTT.  
3. [MQTT Essentials Part 7: Persistent Session & Queuing Messages (HiveMQ)](https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/) — Manejo de sesiones persistentes y almacenamiento de mensajes.  
4. [Use of MQTT Will Message (EMQX)](https://www.emqx.com/en/blog/use-of-mqtt-will-message) — Descripción y ejemplo del Last Will & Testament en MQTT.  
5. [MQTT Essentials Part 3: Client, Broker & Connection Establishment (HiveMQ)](https://www.hivemq.com/blog/mqtt-essentials-part-3-client-broker-connection-establishment/) — Rol del broker y clientes, conexión CONNECT/CONNACK.  
6. [Essential MQTT Architecture Considerations for IoT Use Cases (HiveMQ)](https://www.hivemq.com/blog/essential-mqtt-architecture-considerations-iot-use-cases/) — Consideraciones de arquitectura para casos IoT.  
7. [Mosquitto man page: MQTT QoS levels](https://mosquitto.org/man/mqtt-7.html) — Definición de los niveles de QoS 0, 1 y 2.  
8. [A distributed architecture for MQTT messaging: the case of TBMQ (SpringerOpen)](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-025-01271-x) — Ejemplo de broker distribuido para escalabilidad.  
9. [Secure Data Distribution Architecture in IoT Using MQTT (ResearchGate)](https://www.researchgate.net/publication/368584936_Secure_Data_Distribution_Architecture_in_IoT_Using_MQTT) — Seguridad y arquitectura de datos en MQTT.  
10. [TLS Beyond the Broker: Enforcing Fine-grained Security and Trust in Publish/Subscribe Environments (arXiv)](https://arxiv.org/abs/2109.01169) — Seguridad y confianza en entornos pub/sub.  
11. [Security assessment of common open source MQTT brokers and clients (arXiv)](https://arxiv.org/abs/2309.03547) — Evaluación de seguridad en brokers y clientes MQTT.  
12. [MQTT Bridge Architectures in a Cross-Organizational Context (arXiv)](https://arxiv.org/abs/2501.14890) — Estudio sobre arquitecturas de puente MQTT en contextos distribuidos.  
