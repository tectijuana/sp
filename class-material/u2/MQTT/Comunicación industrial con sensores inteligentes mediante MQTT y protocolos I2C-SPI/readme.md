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
