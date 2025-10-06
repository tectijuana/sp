# Reducción de consumo energético mediante MQTT con sesiones persistentes

### Peralta Vigil Fernando Yael

***
![Imagen referente al MQTT](https://www.cloud.studio/wp-content/uploads/2025/04/MQTT-LOGO-BLOG.webp)
Una sesión persistente permite que un cliente “desaparezca” (se desconecte) y luego reanude sin tener que rehacer completamente su estado, lo cual reduce overhead en el cliente en reconexiones.

El broker recuerda las suscripciones y guarda los mensajes pendientes mientras el cliente está desconectado. Lo que es clave para dispositivos alimentados por batería, porque pueden entrar en modo de bajo consumo, desconectarse del broker y luego reconectarse sin gastar energía en reestablecer todo el contexto.

### Como es que ayudan con respecto a reducir el consumo energetico

* Un cliente no necesita reenviar suscripciones cada vez que se reconecta. Esto ahorra mensajes extra y ciclos de CPU en el dispositivo.

* El broker almacena mensajes pendientes mientras el cliente está desconectado. Así, el dispositivo puede entrar en modo de bajo consumo y solo despertar para reconectarse y recibir lo acumulado.

* El uso de sesiones persistentes permite al cliente evitar el “handshake completo” en cada reconexión, reduciendo el tráfico de red y el uso de energía


## Referencias
1. HiveMQ. (s.f.). Persistent Session & Queuing Messages | MQTT Essentials Part 7. Recuperado de https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/
