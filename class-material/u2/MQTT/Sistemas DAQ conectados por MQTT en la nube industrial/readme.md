## Adan Eric Ojeda Quintero - 22211625

# Sistemas DAQ conectados por MQTT en la nube industrial

Un sistema de adquisición de datos (DAQ) en la industria se encarga de medir variables físicas (voltaje, temperatura, presión, vibración, etc.) usando sensores y módulos especiales, conectados a controladores lógicos programables (PLC) o pasarelas. Estos datos permiten supervisar y optimizar procesos productivos. Tradicionalmente se almacenan localmente, pero con el Internet Industrial de las Cosas (IIoT) ahora se envían a la nube para su análisis avanzado. Por ejemplo, NI define el DAQ como “el proceso de medir fenómenos eléctricos o físicos… mediante sensores, hardware de medición y software programable”.
Para trasladar esos datos al cloud, el protocolo MQTT resulta muy útil en entornos industriales.

# ¿Qué es MQTT y por qué es útil en la industria?
MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero basado en el modelo publicar/suscribir. En lugar de usar conexiones punto a punto tradicionales, los dispositivos (sensores, PLCs, etc.) publican sus datos en “topics” o canales y otros sistemas se suscriben a esos topics para recibir la información. Esto desacopla totalmente a productores y consumidores de datos.

Al ser binario y tener encabezados muy pequeños (tan solo ~2 bytes de base), MQTT minimiza el uso de ancho de banda.
Además, opera sobre una sola conexión TCP persistente, lo que permite enviar grandes volúmenes de datos rápidos sin crear muchas conexiones nuevas
En la práctica esto significa que es ideal para redes industriales con anchos de banda limitados o inestables. Entre sus características clave están los niveles de calidad de servicio (QoS), que garantizan la entrega fiable de mensajes aun en redes celulares o intermitentes, y su compatibilidad con cifrado TLS y autenticación de certificados, lo que ayuda a proteger la información crítica

Gracias a su simplicidad y eficacia, MQTT se ha vuelto un estándar en IIoT y Industria 4.0, permitiendo conectar desde grandes fábricas hasta dispositivos con baterías limitadas.Incluso sistemas de control industrial (SCADA) populares como Ignition usan MQTT para transmitir datos de planta hacia la nube.
Comunicación entre DAQ y plataformas en la nube.

En una arquitectura típica, los datos de plantas industriales (sensores, PLCs, estaciones de monitoreo) se envían a un broker MQTT que puede estar en la nube o en el borde (edge). Por ejemplo, un PLC puede exponer variables vía Modbus y un gateway o software de adquisición lee esos datos y los publica en el broker MQTT. Las aplicaciones en la nube, dashboards o sistemas analíticos luego se suscriben a los topics correspondientes para recibir esos datos en tiempo real.

Figura: Ejemplo de arquitectura de adquisición de datos (DAQ) usando MQTT. Varios dispositivos industriales (PLCs, I/O analógicas/digitales, etc.) envían sus mediciones a un módulo de adquisición o pasarela, que convierte y publica la información a un broker MQTT. Luego, aplicaciones y servicios en la nube se suscriben a esos topics para visualizar y procesar los datos al instante. 
Esta vía permite centralizar el monitoreo y control sin necesidad de conexiones punto a punto, ya que el broker actúa como intermediario único. En la práctica existen varias formas de conectar el DAQ a MQTT. Algunos PLC modernos pueden conectarse directamente a Internet (con módulos LTE, por ejemplo) y hablar MQTT. Más comúnmente, se utilizan gateways industriales o software como Node-RED que actúan de puente: leen variables del PLC (usando Modbus, OPC UA, etc.) y las publican a MQTT. Node-RED, en particular, es una herramienta visual de código abierto muy usada en IIoT para este fin.

De este modo se logra un flujo de datos escalable y de bajo costo, compatible con muchos equipos existentes.

# Plataformas y herramientas comunes
Existen numerosos brokers y plataformas que soportan MQTT en entornos industriales:
Brokers MQTT: Softwares como Mosquitto, HiveMQ, EMQX o RabbitMQ (con plugin MQTT) son servidores que reciben las publicaciones y las distribuyen a suscriptores. Pueden instalarse en la nube o localmente. También hay servicios gestionados en la nube (AWS IoT Core, Azure IoT Hub, Google Cloud IoT Core) que incluyen un broker MQTT integrado.

**Plataformas IoT industriales:** Muchos fabricantes ofrecen plataformas completas de IIoT. Por ejemplo, AWS IoT, Azure IoT Hub y Google Cloud IoT permiten conectar miles de dispositivos vía MQTT y ofrecen administración de dispositivos, bases de datos y análisis.

También hay soluciones de software especializadas (como Siemens MindSphere, PTC ThingWorx, IBM Watson IoT, Ubidots, etc.) que usan MQTT para la ingesta de datos.
SCADA y software de borde: Herramientas de supervisión/SCADA integran MQTT para enviar datos a la nube. Ignition, Chariot o Edge Intelligence de Cognex, por ejemplo, reenvían datos de producción y visión industrial mediante MQTT. 

Del mismo modo, bibliotecas de código abiertas en Python, C/C++, Node.js, etc., facilitan implementar clientes MQTT en aplicaciones personalizadas.
Normas de interoperabilidad: Para que distintos sistemas entiendan los datos, existen especificaciones como Sparkplug B, que definen cómo estructurar los temas y la carga útil MQTT en la industria.

Estas normas simplifican la interoperabilidad entre equipos heterogéneos y plataformas de nube.

En resumen, se dispone de una gran variedad de software que permite crear flujos donde los datos de los DAQ (PLC, medidores de energía, sensores) van por MQTT a la nube, y luego se visualizan en dashboards o se procesan en servicios de análisis.
Ventajas de MQTT en DAQ industrial
Eficiencia de red: MQTT usa encabezados muy pequeños y solo envía mensajes cuando hay cambio de datos, lo que ahorra ancho de banda. 

Además, mantiene una única conexión persistente TCP para todos los dispositivos, reduciendo la sobrecarga de conexión.

**Escalabilidad:** Es posible conectar miles o incluso millones de sensores al mismo broker MQTT sin necesidad de conexiones directas entre cada par de dispositivos. Plataformas como AWS IoT Core, basadas en MQTT, gestionan millones de conexiones simultáneas.

**Desacoplamiento (pub/sub):** Productores y consumidores de datos no necesitan conocerse ni comunicarse directamente. Esto permite agregar o cambiar dispositivos sin afectar al sistema completo.

**Fiabilidad:** MQTT ofrece tres niveles de QoS para asegurar la entrega de mensajes aun en redes móviles o inestables. De este modo se minimiza la pérdida o duplicado de datos.

**Seguridad:** Soporta cifrado TLS/SSL y autenticación por certificados o tokens modernos. Los brokers gestionados en la nube suelen incluir políticas avanzadas de autorización, lo que protege la información crítica.

**Ligereza:** Requiere muy pocos recursos en el dispositivo cliente (RAM/CPU), por lo que funciona en microcontroladores o PLCs sencillos.
Esto también prolonga la vida de batería en dispositivos inalámbricos.
Todas estas ventajas convierten a MQTT en una opción ideal para aplicaciones industriales como monitoreo de máquinas en tiempo real, control remoto y análisis predictivo, donde se generan grandes volúmenes de datos desde el campo hacia la nube.

## Retos y consideraciones
Integración TI/OT: Uno de los mayores desafíos es unificar los sistemas de Tecnología de la Información (TI) con los de Operaciones (OT). Los sistemas TI (bases de datos, analítica) y OT (PLC y control real) manejan datos y protocolos distintos. Se requiere normalizar formatos y protocolos para que los datos fluyan correctamente entre ambos entornos
bevywise.com
. Por ejemplo, se suelen usar gateways o software de integración que transforman Modbus/OPC-UA a MQTT.
Interoperabilidad de datos: MQTT por sí mismo no define la estructura de los mensajes. Sin estándares adicionales, cada proveedor podría usar formatos diferentes. Para evitar problemas, han surgido marcos como Sparkplug B, que establecen patrones comunes de temas y payloads MQTT en la industria
tulip.co
.
Conectividad de red: Las redes industriales pueden sufrir interferencias o cortes. Hay que prever mecanismos de reintento, almacenamiento local en los gateways (almacenes buffer) o QoS adecuados para que la información no se pierda si se cae la conexión.
Seguridad: Aunque MQTT soporta cifrado y autenticación, su configuración correcta es esencial. Se deben usar certificados válidos y políticas de acceso estrictas, ya que un broker mal asegurado podría exponer datos sensibles de la planta.
Gestión y monitoreo: Al escalar a miles de dispositivos, es necesario administrar y monitorear el broker MQTT (logs, métricas de rendimiento). Sin una buena supervisión, podrían generarse cuellos de botella o fallos no detectados.
Capacitación: El equipo de ingeniería debe aprender a programar en pub/sub y a usar estas nuevas plataformas en la nube. Esto puede requerir tiempo y pruebas piloto.
A pesar de estos desafíos, las soluciones modernas están maduras y permiten implementar MQTT en entornos industriales con altos estándares de fiabilidad y seguridad.
Integración en arquitecturas industriales
MQTT encaja naturalmente en arquitecturas de borde (edge) e industriales modernas. Normalmente, los sensores y PLCs en planta se conectan a un dispositivo de borde o gateway que actúa de puente. Dicho dispositivo recoge datos locales y los envía al broker MQTT en la nube o centro de datos
cloud.google.com
. En Google Cloud, por ejemplo, se describe cómo las puertas de enlace de borde publican telemetría de los dispositivos al broker MQTT central usando MQTT sobre TLS
cloud.google.com
. Así se aísla la red local de la infraestructura cloud, manteniendo redundancia y control. Un concepto emergente es el Espacio de Nombres Unificado (UNS), en el que MQTT actúa como eje central para unificar datos OT y TI
tulip.co
tulip.co
. En este enfoque, todos los datos relevantes (producción, calidad, energía, mantenimiento) se publican en un gran topic compartido o estructura de topics. Esto elimina miles de conexiones punto a punto internas. Al cumplir MQTT los requisitos (arquitectura abierta, informe por excepción, eficiente en ancho de banda), se considera ideal para implementar un UNS empresarial
tulip.co
. Por último, muchas arquitecturas industriales combinan MQTT con otros protocolos: por ejemplo, un PLC puede seguir usando OPC-UA o Modbus en la planta, pero envía sus datos hacia el cloud vía MQTT. De esta forma se mantiene la compatibilidad con equipos existentes mientras se aprovecha la nube para análisis avanzado y visualización centralizada. Figura: Desafíos TI/OT en la industria. Los sistemas de control (OT) y las plataformas informáticas (TI) suelen tener objetivos diferentes. La imagen ilustra la necesidad de integrar ambos mundos unificando datos y protocolos. Según Bevywise, una integración efectiva requiere normalizar formatos y protocolos para que los datos de TI y OT sean capturados y usados correctamente
bevywise.com
.
Aplicaciones reales
MQTT ya se emplea en numerosos casos industriales reales, entre ellos:
Monitoreo de maquinaria: Sensores de vibración, temperatura o presión instalados en motores y bombas publican sus lecturas vía MQTT en tópicos como “estado_equipo”. Los sistemas de mantenimiento se suscriben y detectan cambios inusuales para realizar mantenimiento predictivo antes de que ocurra una falla
come-star.com
.
Optimización de producción: Se envían métricas de producción (por ejemplo, OEE, tasa de calidad, disponibilidad) de las máquinas a la nube. Esto permite a los gerentes ajustar en tiempo real parámetros de la línea. Plataformas IoT aprovechan esta información para mejorar la eficiencia de fábrica
ubidots.com
.
Gestión energética: Medidores inteligentes de consumo (corriente, voltaje) se conectan por MQTT a la nube. Por ejemplo, Phoenix Contact describe medidores que “se conectan directamente a una plataforma en la nube […] a través de Ethernet y MQTT” en modo Plug & Play
phoenixcontact.com
. Esto facilita a los responsables de energía ver consumos y generar reportes sin tocar la infraestructura OT tradicional.
Logística y seguimiento: En operaciones logísticas, cámaras de visión y lectores de códigos de barras publican datos a la nube mediante MQTT. Cognex señala que su herramienta Edge Intelligence “ofrece funciones de reenvío de datos MQTT” para sistemas de logística, aprovechando su baja sobrecarga para enviar imágenes y lecturas hacia análisis en la nube
cognex.com
.
Otros casos: Agricultura inteligente (sensores de riego publican humedad de suelo vía MQTT), energía renovable (turbinas eólicas reportan datos de estado), o distribución inteligente (sensores de calidad de agua) son ejemplos adicionales donde se emplea MQTT para llevar datos al cloud y mejorar la toma de decisiones.
En resumen, la combinación DAQ + MQTT + nube permite monitorear máquinas, procesos de producción y recursos (como energía) en tiempo real. Esto da lugar a sistemas más inteligentes, con mantenimiento predictivo, optimización continua y visualización global de la planta.
