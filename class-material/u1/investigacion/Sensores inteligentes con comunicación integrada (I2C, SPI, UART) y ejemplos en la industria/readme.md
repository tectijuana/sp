 # Sensores inteligentes con comunicación integrada (I2C, SPI, UART) y ejemplos en la industria
En 2024, protocolos de comunicación como I2C, SPI y UART siguen siendo componentes esenciales del mundo tecnológico. Utilizados para la comunicación entre diversos dispositivos electrónicos, estos protocolos son el núcleo invisible que mantiene nuestros sistemas integrados y periféricos interconectados funcionando óptimamente.

En este artículo, analizaremos estos tres protocolos para brindarte una comprensión clara y práctica de sus características, beneficios y limitaciones. 

# ¿Qué es una interfaz periférica en serie (SPI)?

SPI (Interfaz Periférica Serie) destaca por su alta velocidad, lo que la convierte en la opción preferida para comunicaciones rápidas. A diferencia de I₂C, SPI funciona con cuatro cables: MISO (Entrada Maestro-Salida Esclavo), MOSI (Salida Maestro-Entrada Esclavo), SCK (Reloj Serie) y SS (Selección Esclavo), lo que permite una comunicación full-duplex (envío y recepción simultánea). A pesar de su simplicidad y velocidad, SPI requiere más pines que I₂C, lo cual puede ser un factor a considerar en el diseño de circuitos.

## Etapas de la transmisión SPI :

    1. Generación de señal de reloj : el maestro inicia la comunicación generando una señal de reloj que sincroniza el intercambio de datos. 
    2. Selección de esclavo : el maestro activa el esclavo deseado bajando la línea SS a un nivel de voltaje bajo. 
    3. Intercambio de datos : El maestro comienza enviando datos al esclavo a través de la línea MOSI, bit a bit, a menudo comenzando por el bit más significativo. Al mismo tiempo, el esclavo también puede enviar datos al maestro a través de la línea MISO, generalmente comenzando por el bit menos significativo. 
    4. Comunicación simultánea : A diferencia de un modelo simple de comando y respuesta, SPI permite la comunicación bidireccional simultánea. Mientras la línea SS permanezca habilitada, el maestro y el esclavo pueden continuar intercambiando datos simultáneamente, lo que permite una transmisión de datos eficiente y rápida en ambas direcciones. 

<img width="828" height="496" alt="image" src="https://github.com/user-attachments/assets/8151dd3e-3d36-42d8-a5ab-be1392383463" />





## Ventajas, desventajas y aplicaciones

## Beneficios :

    • Transferencias de datos rápidas y eficientes. 
    • Comunicación full-duplex para envío y recepción simultáneos. 
    • Simplicidad de diseño e implementación. 
    
## Desventajas :

    • Uso de múltiples pines, lo que puede ser un problema en diseños con espacio limitado. 
    • Menos eficiente para gestionar múltiples esclavos en comparación con I2C. 
    • Susceptible a interferencias a altas velocidades o largas distancias. 

# SPI en microcontroladores

## Controlador/adaptador SPI

Es una herramienta sencilla para controlar dispositivos SPI. Es compatible con todos los sistemas operativos. El analizador lógico en tiempo real muestra el tráfico SPI en pantalla. El voltaje de funcionamiento del controlador SPI es de 3,3 V a 5 V.

## MCP 3008

Es un ADC de 10 bits con 8 canales. Además, se conecta a la Raspberry Pi mediante una conexión serie SPI. 

# ¿Qué es I2C?

El protocolo de comunicación serial (I²C) es eficaz para sensores y módulos, pero no para la comunicación entre dispositivos PCB. El bus transmite información bidireccionalmente entre dispositivos conectados mediante dos cables. Con este protocolo, se pueden conectar hasta 128 dispositivos a la placa base, manteniendo una comunicación fluida entre ellos. Son ideales para proyectos que requieren la interacción de diversos componentes (p. ej., sensores, pines, expansiones y controladores). Además, la velocidad de I²C depende de la velocidad de los datos, la calidad de los cables y la cantidad de ruido externo. I²C también utiliza interfaces de dos cables para conectar dispositivos de baja velocidad, convertidores A/D en vivo, microcontroladores, interfaces de E/S, etc. 

# Protocolo de trabajo I2C 

Los dispositivos maestros envían la señal a cada uno de los esclavos conectados. Esto se realiza conmutando las líneas SDA y SCL de alto a bajo voltaje. 
El dispositivo maestro es responsable de enviar 7 o 10 bits de la dirección, incluido el bit de lectura/escritura, al esclavo para comunicarse.
El esclavo compara la dirección y, si coincide, devuelve el bit de confirmación ACK. Esto activaría la línea SDA por un bit; de lo contrario, no se produce ningún cambio en la línea SDA, manteniéndola activa.
El maestro también transceptor la trama de datos, y el dispositivo receptor confirma la transmisión exitosa enviando un bit ACK. El dispositivo maestro envía una señal de parada para detener la transmisión de datos, donde el interruptor SCL se activa antes que el SDA. 

<img width="626" height="209" alt="image" src="https://github.com/user-attachments/assets/4d0f26f8-bd0c-46e8-8b52-981086460ff6" />


# Pros y contras de I2C

## Ventajas
    • Admite varios dispositivos maestros.  
    • Ofrece comunicación multi-esclavo y multi-maestro. 
    • Este protocolo también es flexible y adaptable. 
## Contras
    • I2C es un protocolo un poco más lento debido a la necesidad de resistencias pull-up. 
    • Ocupa más espacio. 
    • La arquitectura es más compleja a medida que aumenta el número de dispositivos. 
    • Este protocolo es semidúplex, lo que es bastante problemático y requiere diferentes dispositivos para una comunicación completa. 

# ¿Qué es UART?

La Recepción y Transmisión Asíncrona Universal (UART) es la interfaz de comunicación serie que conecta el host con el dispositivo auxiliar. Este protocolo permite la comunicación serie full-duplex. Los UART son chips diseñados para la comunicación asíncrona.

Mediante bits de inicio y parada, transmite bits de datos ordenados del más pequeño al más grande. Los circuitos controladores controlan los niveles de señalización eléctrica externos al UART. 

Por lo tanto, este protocolo UART admite la transmisión de datos bidireccional, serial y asíncrona. Mediante las líneas de datos 0 y 1, conectadas a los pines digitales 0 y 1, esta interfaz consta de dos líneas de datos: transmisión y recepción.

El UART puede gestionar fácilmente el problema de sincronización entre dispositivos serie y ordenadores. El UART transmite datos de forma asíncrona, lo que significa que el UART emisor no sincroniza su salida con el UART receptor. Los UART envían paquetes de datos sin señal de reloj mediante la adición de bits de inicio y fin. Para que el UART receptor sepa cuándo empezar a leer los bits, estos definen el inicio y el final del paquete de datos. 

<img width="610" height="293" alt="image" src="https://github.com/user-attachments/assets/bffd5aa5-5b2e-4303-9993-2046af7128f5" />


# Pros y contras de UART

## Ventajas

    Solo utiliza dos líneas o cables ayudando a limpiar los circuitos.
    No requiere una señal de reloj.
    Tiene un bit de paridad para comprobar errores.
    Es un método de comunicación fácil y ampliamente utilizado.

## Contras

    Tiene un tamaño de datos limitado a solo 9 bits.
    No admite varios dispositivos maestros y esclavos.
    La tasa de baudios o la velocidad de transmisión de datos debe ser inferior al 10 % o una de la otra.
    La velocidad de transmisión de datos es menor en comparación con el resto de protocolos. 

# Ejemplo de UART en microcontrolador

## USB a UART 5 V

Diseñadas para simplificar la comunicación USB-serie, estas interfaces UART USB-serie proporcionan una conexión USB-serie. El uso de un controlador host USB reduce eficientemente la cantidad de componentes externos, minimizando el ancho de banda USB. Basado en el convertidor de bus USB CH340, puede convertir archivos USB a archivos serie. Es compatible con convertidores USB-UART de 5 V.

## Convertidor serie USB CP2102

Los diseños RS-232 se pueden actualizar fácilmente a USB con este controlador de puente USB a UART altamente integrado. Se proporciona conectividad USB a dispositivos equipados con UART. Las placas Arduino/Seeeduino se pueden actualizar por ordenador con este convertidor serie USB CP2102.

## UART Seeduino V4.2

Las placas Arduino contienen al menos un puerto serie que suele comunicar los pines digitales Tx y Rx mediante USB. Es compatible con la placa Arduino. Esta placa se puede programar mediante un cable microUSB. 


## bibliografia en formato apa

NextPCB. (2024, 30 agosto). SPI vs. I2C vs. UART: Differences Between These Communication Interfaces. https://www-nextpcb-com.translate.goog/blog/spi-i2c-uart?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

Samba, N. (2024, 5 enero). Understanding and Selecting in 2024: I2C, SPI, UART Explained. Parlez-vous Tech. https://www-parlezvoustech-com.translate.goog/en/comparaison-protocoles-communication-i2c-spi-uart/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc


