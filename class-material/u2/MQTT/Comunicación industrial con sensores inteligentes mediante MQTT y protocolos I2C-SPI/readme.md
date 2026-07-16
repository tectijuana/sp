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

 ## Cómo funciona
  1)  Tiene 2 Líneas que son SCL (línea de reloj en serie) y SDA (puerto de aceptación de la línea de datos en serie)
  2)  CL es la línea de reloj para sincronizar la transmisión. SDA es la línea de datos a través de la cual se envían o reciben bits de datos.
  3)  El dispositivo maestro inicia la transferencia de datos en autobús y genera un reloj para abrir el dispositivo transferido y cualquier dispositivo dirigido se considera un dispositivo esclavo.
  4)  La relación entre los dispositivos ama y esclavistas, la transmisión y la recepción en el autobús no es constante. Depende de la dirección de la transferencia de datos en ese momento.
  5)  Si el amo quiere enviar datos al esclavo, el amo primero debe dirigirse al esclavo antes de enviar cualquier dato.
  6)  El maestro terminará la transferencia de datos. Si el amo quiere recibir datos del esclavo, el amo debe dirigirse de nuevo al esclavo primero.
  7)  El anfitrión entonces recibe los datos enviados por el esclavo y finalmente, el receptor termina el proceso de recepción. El anfitrión también es responsable de generar el reloj de sincronización y de poner fin a la transferencia de datos.

## Protocolo de trabajo de I2C
### Método de transmisión de datos
1) El maestro envía la señal de transmisión a cada esclavo conectado cambiando la línea SDA de un nivel de alta tensión a un nivel de baja tensión y línea SCL de alto a bajo después de cambiar la línea SDA.
2) El amo envía a cada esclavo la dirección de 7 o 10 bits del esclavo y una lectura/escritura a la esclava con la que quiere comunicarse.
3) El esclavo comparará entonces la dirección con la suya. Si la dirección coincide, el esclavo devuelve una parte de ACK que cambia la línea SDA bajo por un bit. Si la dirección no coincide con su dirección, el esclavo deja la línea SDA alta
4) El maestro entonces enviará o recibirá el marco de datos. Después de la transferencia de cada marco de datos, el dispositivo receptor devuelve otro bit ACK al remitente para reconocer la transmisión exitosa.
5) Para detener la transmisión de datos, el maestro envía una señal de alto al esclavo cambiando SCL antes de cambiar SDA alto
    También es necesario conectar la fuente de alimentación a través de una resistencia de tracción. Cuando el autobús está ocioso, ambas líneas operan a un alto nivel de potencia.
6) La capacitancia en la línea afectará a la velocidad de transmisión del autobús. Como la potencia actual en el autobús es pequeña, cuando la capacitancia es demasiado grande, puede causar errores de transmisión. Así, su capacidad de carga debe ser de 400pF, por lo que se puede estimar la longitud permitida del autobús y el número de dispositivos conectados.

## Modos de transmisión
### Modo rápido:
    Los dispositivos de modo rápido pueden recibir y transmitir a 400kbit/s. Tienen que ser capaces de sincronizarse con una transmisión de 400kbit/s y ampliar el período bajo de la señal SCL para ralentizar la transmisión.
    Los dispositivos de modo rápido son compatibles con la marcha atrás y pueden comunicarse con dispositivos de modo estándar de los sistemas de autobuses I2C de 0 a 100 kbit/s. Sin embargo, como los dispositivos de modo estándar no son compatibles con alza, no pueden operar en un sistema de bus I2C rápido. La especificación de bus I2C de modo rápido tiene las siguientes características en comparación con el modo estándar:
        La tasa máxima de bits se aumenta a 400 kbit/s;
        Ajustó el momento de las señales de los datos serie (SDA) y de los relojes serie (SCL).
        Tiene la función de suprimir el fallo y las entradas SDA y SCL tienen gatillos Schmitt. 
        El buffer de salida tiene una función de control de pendiente para los bordes de caída de las señales SDA y SCL
        Una vez que se apaga el suministro de alimentación del dispositivo de modo rápido, los pines de E/S de SDA y SCL deben quedar inactivos y no pueden bloquear el autobús.
        El dispositivo de tracción exterior conectado al autobús debe sintonizarse para acomodar el tiempo máximo de elevación más corto permitido del autobús I2C de modo rápido. Para los autobuses con una carga máxima de 200pF, el dispositivo de tracción de cada autobús puede ser una resistencia. Para un autobús con una carga entre 200pF y 400pF, el dispositivo de tracción puede ser una fuente de corriente (máximo 3mA) o un circuito de resistencia conmutado.
### Ventajas de usar I2C

    Tiene un conteo de pines/señal bajo incluso con numerosos dispositivos en el autobús
    Flexible, ya que apoya la comunicación multimaestro y multiesclavo.
    Simple ya que solo utiliza 2 cables bidireccionales para establecer la comunicación entre múltiples dispositivos.
    Adaptable ya que puede adaptarse a las necesidades de varios dispositivos esclavistas.
    Apoya a múltiples maestros.

### Desventajas de usar I2C

    Velocidad más lenta, ya que requiere resistencias de pull-up en lugar de resistencias push-pull utilizadas por SPI. También tiene un diseño de drenaje abierto = velocidad limitada.
    Requiere más espacio a medida que las resistencias consumen bienes raíces de PCB valiosos.
    Puede llegar a ser complejo a medida que aumenta el número de dispositivos. 
# Interfaz SPI
## Qué es SPI

    Stands para Interfaz Periférico Serial (SPI)
    Es similar a I2C y es una forma diferente de protocolo de comunicaciones en serie especialmente diseñado para que los microcontroladores se conecte.
    Opera a pleno rendimiento donde los datos se pueden enviar y recibir simultáneamente.
    Operar a velocidades de transmisión de datos más rápidas = 8Mbits o más
    Normalmente es más rápido que el I2C debido al protocolo simple. Incluso si las líneas de datos/reloj se comparten entre dispositivos, cada dispositivo requerirá un cable de dirección único.
    Se utiliza en lugares donde la velocidad es importante. (por ejemplo. Tarjetas SD, módulos de visualización o cuando la información actualiza y cambia rápidamente como termómetros)

## Cómo funciona

    Comunicarse de dos maneras:
        Seleccionar cada dispositivo con una línea Chip Select. Para cada dispositivo se requiere una línea separada de Chip Select. Esta es la forma más común en que los RPi utilizan actualmente SPI.
        Encadenamiento Daisy donde cada dispositivo está conectado al otro a través de sus datos hacia los datos en línea del siguiente.
    No hay límite al número de dispositivos SPI que se pueden conectar. Sin embargo, hay límites prácticos debido al número de líneas de selección de hardware disponibles en el dispositivo principal con el método de selección de chip o la complejidad de pasar datos a través de dispositivos en el método de cadena de margaritas.
    En la comunicación punto a punto, la interfaz SPI no requiere operaciones de abordaje y es comunicación completa, que es sencilla y eficiente. 

## Protocolo de trabajo SPI

    El SPI se comunica a través de 4 puertos que son:
        MOSI - Salida de datos maestro, entrada de datos esclavos
        MISO - entrada de datos maestros, producción de datos esclavistas
        La señal de reloj SCLK, generada por el dispositivo maestro, hasta fPCLK/2, la frecuencia del modo de esclavo hasta fCPU/2
        Señales activadas por el esclavo, controlada por el dispositivo maestro, algunos IC serán etiquetados como CS (Seleccione Chip)
    En un sistema multiesclavo, cada esclavo requiere una señal de habilitación separada, que es un poco más complicada en el hardware que el sistema I2C.
    La interfaz SPI es en realidad dos simples registros de cambios en el hardware interno. Los datos transmitidos son de 8 bits. Se transmite poco a poco bajo el esclavo permite la señal y el pulso de desplazamiento generado por el dispositivo maestro. La parte alta está en la parte delantera y la parte baja está en la parte trasera.
    La interfaz SPI es la transmisión de datos serie sincrónicos entre la CPU y el dispositivo periférico de baja velocidad. Bajo el pulso de turno del dispositivo maestro, los datos se transmiten bit por bit. La parte alta está en la parte delantera y la parte baja está en la parte trasera. Es una comunicación completa, y la velocidad de transmisión de datos es en general más rápida que el autobús I2C y puede alcanzar velocidades de unos pocos Mbps.

## Ventajas de usar SPI

    El protocolo es sencillo ya que no hay un sistema complicado de tratamiento de esclavos como el I2C.
    Es el protocolo más rápido en comparación con UART e I2C.
    No inicio y detenga bits a diferencia de UART, lo que significa que los datos se pueden transmitir continuamente sin interrupción
    Líneas separadas MISO y MOSI, lo que significa que los datos pueden ser transmitidos y recibidos al mismo tiempo

## Desventajas del uso IPC

    Más puertos de Pin están ocupados, el límite práctico a una serie de dispositivos.
    No se especifica el control del flujo, y ningún mecanismo de reconocimiento confirma si los datos se reciben a diferencia de I2C
    Utiliza cuatro líneas MOSI, MISO, NCLK, NSS
    No hay forma de comprobación de error a diferencia de en UART (usando bit de paridad)
    Sólo 1 maestro

# Biliografia

Team, H. (2015, January 12). Introducing the MQTT Protocol – MQTT Essentials: Part 1. Translate.goog; HiveMQ. https://www-hivemq-com.translate.goog/blog/mqtt-essentials-part-1-introducing-mqtt/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

‌Welcome To Zscaler Directory Authentication. (2025). Translate.goog. https://www-hashstudioz-com.translate.goog/blog/connecting-internet-of-things-iot-with-mqtt/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

‌yida. (2019, September 25). UART vs I2C vs SPI – Communication Protocols and Uses - Latest News from Seeed Studio. Latest News from Seeed Studio. https://www.seeedstudio.com/blog/2019/09/25/uart-vs-i2c-vs-spi-communication-protocols-and-uses/?srsltid=AfmBOopIU4uTAhVVHxwnHDfQ-IN7mXfULEZFA8BWFh4jXVnwC2JtzpCG

‌
