# MQTT

<img width="1200" height="627" alt="image" src="https://github.com/user-attachments/assets/5db04b10-b24a-4c0c-97e8-f3d68fb9b5a1" />



# ¿Qué es MQTT?

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero basado en el modelo publicador/suscriptor.
Se diseñó para comunicaciones M2M (Machine-to-Machine) e IoT (Internet of Things).
Opera sobre TCP/IP, usando normalmente el puerto 1883 (o 8883 con TLS/SSL).

# Caracteristicas Principales 

*Ligero y eficiente* → bajo consumo de ancho de banda y CPU (ideal para microcontroladores, ARM y Raspberry Pi).
Arquitectura cliente-servidor → un broker MQTT (ej. Mosquitto, EMQX) administra los mensajes.

Modelo Pub/Sub:

*Publisher (publicador)* → envía mensajes a un "topic".

*Subscriber (suscriptor)* → recibe mensajes de ese "topic".

*Broker* → intermedia entre ellos.

*QoS (Quality of Service)* → 3 niveles de confiabilidad:

*QoS 0* → "at most once" (sin confirmación).

*QoS 1* → "at least once" (el receptor recibe al menos una vez, con posible duplicado).

*QoS 2* → "exactly once" (entrega garantizada una sola vez).



# Caso de usos 
En un Raspberry Pi, MQTT se suele usar para conectar sensores o dispositivos IoT a servicios en la nube (ej. AWS IoT Core, Azure IoT Hub, Mosquitto local).

Ejemplo de instalación de Mosquitto broker en Raspberry Pi OS:

```
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
```
Ejemplo de uso rápido:

Publicar un mensaje:

```
mosquitto_pub -h localhost -t "casa/sala/temperatura" -m "25°C"
```
Suscribirse a un tema:
```
mosquitto_sub -h localhost -t "casa/sala/temperatura"
```


# Integracion C / ARM Assembly
Aunque MQTT normalmente se maneja desde Python, Node.js o C, también se puede integrar con programas en C y desde ahí invocar funciones en ensamblador ARM64.

En C se usa la librería paho-mqtt de Eclipse.

En ARM64 Assembly podrías crear rutinas de comunicación (por ejemplo, para empaquetar mensajes o procesar buffers) y llamarlas desde C.


# Ventajas de MQTT frente a otros protocolos (HTTP, CoAP)
*Menor consumo de energía y ancho de banda que HTTP.*

*Persistencia de mensajes (el broker guarda mensajes para clientes desconectados).*

*Escalabilidad → muchos clientes suscritos a los mismos topics.*
