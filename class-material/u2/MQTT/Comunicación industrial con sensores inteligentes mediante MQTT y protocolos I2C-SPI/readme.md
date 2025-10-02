# MQTT 
MQTT es un protocolo de transporte de mensajes de publicación/suscripción cliente-servidor. Es ligero, abierto, sencillo y está diseñado para facilitar su implementación. Estas características lo hacen ideal para su uso en diversas situaciones, incluyendo entornos con limitaciones como la comunicación máquina a máquina (M2M) y el Internet de las Cosas (IoT), donde se requiere un código reducido o el ancho de banda de la red es limitado.

Cuando se describe a MQTT como "ligero", significa que ha sido diseñado para ser simple, eficiente y con un consumo mínimo de recursos. MQTT se creó con el objetivo de enviar pequeñas cantidades de datos a través de redes poco fiables con ancho de banda y conectividad limitados. En comparación con otros protocolos, MQTT tiene una huella de código reducida, baja sobrecarga y bajo consumo de energía. Gracias a su mínima sobrecarga de paquetes, MQTT destaca en la transferencia de datos por cable en comparación con protocolos como HTTP. Esto también lo hace ideal para su uso en dispositivos con capacidad de procesamiento, memoria y duración de batería limitadas, como sensores y otros dispositivos IoT.

## ¿Cuáles son los componentes de una arquitectura MQTT?
En resumen, MQTT es uno de los protocolos de mensajería más populares, además del protocolo TCP/IP. La abreviatura de MQTT significa Message Queueing Telemetry Transport (Transporte de Telemetría de Cola de Mensajes). Para comprender el concepto de MQTT, es necesario comprender los siguientes términos:

1) ### Publicar/Suscribirse:
   Es un protocolo donde un dispositivo puede publicar un mensaje y otro dispositivo puede suscribirse a temas para recibir los mensajes.
   ![](https://www-hashstudioz-com.translate.goog/blog/wp-content/uploads/2020/04/mqtt-element-1.png?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)
   
3) ### Mensajes:
   Los mensajes son intercambios de información entre dispositivos, pueden ser comandos o datos.
4) ### Tema:
   Un tema es el lugar donde un dispositivo quiere colocar o desde donde quiere recuperar un mensaje.
5) ### Broke:
   El broker es responsable de recibir todos los mensajes, filtrarlos y publicarlos para todos los clientes suscritos.     

## ¿Cómo funciona MQTT en proyectos de IoT?
Como se mencionó anteriormente, MQTT está diseñado como un protocolo de mensajería liviano que utiliza operaciones de publicación/suscripción para intercambiar datos entre clientes y el servidor.

Es el protocolo más adecuado para proyectos de domótica e Internet de las Cosas . Si quieres empezar a crear tus propios proyectos con MQTT, aquí te explicamos cómo implementarlo en cuatro etapas:

. Conexión : un cliente comienza creando una conexión de Protocolo de control de transmisión/Protocolo de Internet (TCP/IP) con el broker utilizando un puerto estándar o un puerto personalizado        definido por los operadores del broker.
. Autenticación: La autenticación forma parte del transporte y proporciona seguridad a nivel de aplicación. Con la Seguridad de la Capa de Transporte (TLS), la validación correcta de un                certificado de cliente se utiliza para autenticar al cliente ante el servidor. A nivel de aplicación, el protocolo MQTT permite el uso de un nombre de usuario y una contraseña para la                autenticación.
. Comunicación : Durante la fase de comunicación, un cliente puede realizar operaciones de publicación, suscripción, cancelación de suscripción y ping. Normalmente, los mensajes tienen cargas          útiles. Los desarrolladores deben definirlas, que pueden ser datos binarios, texto sin formato, JSON, XML u otros. Los mensajes MQTT tienen otros atributos: calidad de los servicios y                mantenimiento de la bandera.
. Terminación : Cuando un publicador o suscriptor desea terminar una sesión MQTT, envía un mensaje de DESCONEXIÓN al broker y cierra la conexión. Esto se denomina cierre ordenado porque permite al     cliente reconectarse fácilmente proporcionando su identidad y reanudando la conexión donde la dejó.
## Los beneficios de MQTT

1)  Huella de código semidad: los dispositivos solos necesitan unas pocas líneas de código para funcionar con el protocolo MQTT.

2)  Paquetes de datos minimizados: MQTT es muy eficiente en energía. Esto lo hace ideal para conectarse con dispositivos que están alimentados por batería o tienen poca potencia de CPU.

3)  Velocidad: MQTT opera en tiempo real, sin retrasos fuera de QoS.

4)  Facilidad de implementación: MQTT ya cuenta con bibliotecas en lenguajes de programación como Elixir y Python.

5)  Ultima voluntad y testamento : Si un cliente se desconecta inesperadamente, puede configurar instrucciones para enviar mensajes a todos los suscriptores para remediar la situación.

6) Mensajes retenidos: Cada tema puede tener un mensaje retenido que un cliente recibe automáticamente cuando se suscribe (como una publicación fija en las redes sociales).

# Interfaz I2C

## Qué es I2C?
1)    Estancias para el circuito interintegrado (I2C)
2)    Es un protocolo de comunicaciones en serie de manera similar a UART. Sin embargo, no se utiliza para la comunicación PC-dispositivo, sino con módulos y sensores.
3)    Es un simple autobús en serie sincronizado de dos hilos bidireccionales y requiere sólo dos cables para transmitir información entre dispositivos conectados al autobús.
4)    Son útiles para proyectos que requieren muchas partes diferentes (por ejemplo, sensores, pin, expansiones y conductores) trabajando juntos ya que pueden conectar hasta 128 dispositivos a la placa principal, manteniendo una vía de comunicación clara.
5)    Esto se debe a que I2C utiliza un sistema de direcciones y un bus compartido = muchos dispositivos diferentes se pueden conectar usando los mismos cables y todos los datos se transmiten en un solo cable y tienen un bajo conteo de pines. Sin embargo, la compensación por este cableado simplificado es que es más lento que SPI.
6)    Velocidad de I2C también depende de la velocidad de los datos, calidad del alambre y ruido externo
7)    El protocolo I2C también se utiliza como interfaz de dos hilos para conectar dispositivos de baja velocidad como microcontroladores, EEPROM, convertidores A/D y D/A, interfaces de E/S y otros periféricos similares en sistemas integrados. 

 
