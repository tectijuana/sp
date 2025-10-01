# Implementación de comunicación UART–MQTT bridge en sistemas embebidos

## Resumen
La presente investigación aborda el diseño e implementación de un puente de comunicación entre UART y MQTT en sistemas embebidos. Este mecanismo, conocido como **UART–MQTT bridge**, permite conectar dispositivos que utilizan comunicación serie asíncrona con infraestructuras modernas de mensajería basadas en el protocolo MQTT. El propósito es facilitar la integración de sensores y microcontroladores con plataformas IoT, servicios en la nube y aplicaciones de monitoreo remoto. Se describen los fundamentos de ambos protocolos, las arquitecturas más comunes para implementar el puente, las opciones de hardware y software disponibles, así como aspectos de seguridad, pruebas de rendimiento, casos de uso reales y conclusiones derivadas de su aplicación práctica.

## Introducción
En los sistemas embebidos resulta común emplear UART (Universal Asynchronous Receiver/Transmitter) debido a su bajo costo y simplicidad en la transmisión de datos entre dispositivos. Sin embargo, este tipo de comunicación se limita a enlaces punto a punto y no ofrece mecanismos de distribución a gran escala. En contraposición, MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería liviano diseñado para redes poco confiables y equipos con recursos limitados. A través de un broker central, permite la publicación y suscripción de mensajes de manera eficiente. La implementación de un **UART–MQTT bridge** hace posible enlazar ambas tecnologías, transformando los datos provenientes de UART en publicaciones MQTT y permitiendo que mensajes provenientes del broker se envíen de regreso al dispositivo serial.

## Protocolos y fundamentos técnicos
UART es un protocolo de comunicación serie asíncrona que transmite datos en formato de bits, organizados en tramas que incluyen velocidad en baudios, bits de datos, paridad y bits de parada. Su simplicidad lo hace muy utilizado en dispositivos embebidos, aunque carece de mecanismos de control de sesión, enrutamiento o fiabilidad a nivel de transporte. En este sentido, los desarrolladores suelen diseñar protocolos de aplicación sobre UART que incluyan delimitadores de mensajes, sumas de comprobación o confirmaciones.  

MQTT, por el contrario, fue creado para aplicaciones de telemetría y control en entornos con recursos limitados. Se basa en un modelo cliente-servidor donde el broker actúa como intermediario. Los dispositivos pueden publicar en un tema (topic) o suscribirse a él, lo que permite un esquema de comunicación desacoplado. Además, MQTT ofrece diferentes niveles de calidad de servicio (QoS 0, 1 y 2), que permiten definir la fiabilidad en la entrega de mensajes, desde una transmisión sin confirmación hasta una entrega garantizada y sin duplicados.

## Arquitectura de un UART–MQTT bridge
La arquitectura básica de un UART–MQTT bridge está conformada por tres bloques principales. El primero es la interfaz UART, encargada de establecer la comunicación física y lógica con el dispositivo serial. El segundo corresponde al módulo de conversión y parsing, el cual interpreta la información recibida y la adapta a un formato estructurado como JSON o CBOR. Finalmente, el tercer bloque corresponde al cliente MQTT, responsable de conectarse al broker, publicar datos en los topics adecuados y suscribirse a topics específicos para reenviar comandos al dispositivo a través de UART.  

En implementaciones más complejas, se incluyen mecanismos de buffering para almacenar datos cuando la red está caída, colas de reenvío para asegurar que los mensajes críticos no se pierdan y reglas de transformación que permiten mapear de forma flexible los datos seriales en diferentes topics del broker.

## Implementación
Existen diferentes enfoques para implementar un UART–MQTT bridge. Una primera opción consiste en el uso de microcontroladores con conectividad inalámbrica, como el ESP32 o ESP8266, que permiten leer datos desde UART y enviarlos directamente a un broker MQTT utilizando Wi-Fi. Esta solución es económica, de bajo consumo energético y elimina la necesidad de un gateway intermedio.  

Otra alternativa es utilizar una computadora de placa reducida como la Raspberry Pi, en la cual se pueden ejecutar herramientas como `serial2mqtt` o scripts en Python que combinan librerías como `pyserial` y `paho-mqtt`. Esta opción es más potente, admite múltiples puertos seriales y puede alojar un broker local como Mosquitto, lo que permite tener control completo de la infraestructura IoT.  

Una tercera opción es recurrir a frameworks comerciales como Mongoose OS, que ofrecen módulos de gateway UART listos para conectarse a servicios en la nube, como AWS IoT o Azure IoT Hub. Estas soluciones son especialmente útiles en entornos industriales donde se requiere rapidez en el desarrollo y certificaciones de seguridad.

## Seguridad
La seguridad en un UART–MQTT bridge debe considerarse desde su diseño. En el enlace MQTT es fundamental implementar cifrado mediante TLS/SSL para proteger la comunicación contra accesos no autorizados. Asimismo, se recomienda habilitar autenticación de clientes y control de acceso a topics desde el broker. En cuanto a la comunicación UART, se pueden añadir mecanismos de verificación de integridad, como sumas de comprobación o códigos CRC, que garanticen la validez de los datos recibidos. También resulta importante limitar el acceso físico a los puertos serie para prevenir manipulaciones no autorizadas.  

En aplicaciones críticas, es recomendable aislar físicamente los circuitos de UART mediante conversores optoacoplados, lo cual protege al sistema de interferencias eléctricas o ataques de hardware.

## Pruebas y métricas de rendimiento
La evaluación de un UART–MQTT bridge debe contemplar métricas como la latencia extremo a extremo, es decir, el tiempo que transcurre desde que un mensaje es enviado por UART hasta que es recibido a través del broker MQTT. Otra métrica relevante es el throughput, que corresponde a la cantidad de mensajes procesados por segundo. También debe verificarse la robustez del sistema ante desconexiones, caídas de red y reconexiones, garantizando que los mensajes críticos no se pierdan.  

Además, se recomienda medir el consumo de recursos del dispositivo, incluyendo memoria, CPU y energía, sobre todo en microcontroladores alimentados por batería. En entornos industriales, el análisis de escalabilidad también es importante, verificando que el sistema soporte decenas o cientos de dispositivos UART conectados simultáneamente a un mismo broker.

## Casos de uso
La implementación de un UART–MQTT bridge tiene múltiples aplicaciones prácticas. En sistemas de monitoreo ambiental, sensores conectados por UART pueden enviar datos de temperatura, humedad o calidad del aire a un broker MQTT, permitiendo visualización en tiempo real mediante dashboards como Grafana. En entornos industriales, equipos heredados que solo disponen de comunicación serial pueden integrarse a plataformas de gestión en la nube mediante un gateway UART–MQTT. En el ámbito doméstico, microcontroladores Arduino con sensores pueden comunicarse con plataformas de domótica como Home Assistant gracias a este tipo de puente.

## Ejemplo práctico
En el caso del ESP32, la implementación de un UART–MQTT bridge requiere configurar uno de sus puertos UART secundarios, establecer la conexión Wi-Fi y emplear una librería MQTT como PubSubClient. Una vez leído el flujo serial, los datos se transforman en un formato como JSON y se publican en un topic específico, mientras que los mensajes recibidos desde el broker se envían nuevamente al puerto UART.  

En una Raspberry Pi, el proceso implica instalar un broker Mosquitto, conectar el dispositivo serial por USB y configurar un servicio como `serial2mqtt` que actúe como traductor entre UART y MQTT. Este servicio puede ejecutarse de manera automática mediante systemd, lo cual garantiza que el bridge esté disponible de forma persistente. Adicionalmente, se pueden integrar herramientas como Node-RED para orquestar flujos de datos, aplicar transformaciones y enviar información a aplicaciones web o servicios en la nube.

## Conclusiones
El uso de un **UART–MQTT bridge** constituye una solución eficaz para integrar dispositivos seriales en arquitecturas IoT modernas. La elección de la plataforma depende de los requisitos de la aplicación: los microcontroladores como el ESP32 ofrecen simplicidad y bajo costo, mientras que soluciones basadas en Raspberry Pi o frameworks especializados proporcionan mayor potencia y flexibilidad. La correcta implementación de protocolos de seguridad, manejo de fallos y normalización de mensajes asegura un sistema confiable y escalable, capaz de responder a las demandas de aplicaciones tanto domésticas como industriales.  

En conclusión, el **UART–MQTT bridge** es un elemento clave para la convergencia entre tecnologías tradicionales de comunicación serial y el paradigma IoT basado en mensajería ligera, permitiendo extender la vida útil de equipos existentes y potenciar la interoperabilidad en sistemas heterogéneos.

## Referencias
EMQX. (2024). *MQTT on ESP32: A Beginner's Guide*.  
Random Nerd Tutorials. (2024). *ESP32 UART Communication (Serial)*.  
vortex314. (s. f.). *serial2mqtt* [Repositorio GitHub].  
Mongoose OS. (s. f.). *UART gateway / UART Bridge*.  
Random Nerd Tutorials. (2021). *How to install Mosquitto Broker on Raspberry Pi*.  
