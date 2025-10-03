# Publicación de Eventos del Sistema Linux Embebido vía MQTT (DBus + Mosquitto)

**Nombre:** Juan Carlos Maya Pino  
**No. Control:** 22211611  
**Materia:** Sistemas Programables  
**Fecha:** 30/09/2025  

## Introducción

En los sistemas embebidos modernos, es importante poder **comunicar en tiempo real los eventos del sistema** hacia otros dispositivos o aplicaciones.  
Ejemplo: que un dispositivo envíe una alerta cuando **se apaga la red, se conecta un USB o baja la batería**.

Para lograr esto, se utilizan tres herramientas clave:

- **DBus** → Detecta eventos internos en Linux.  
- **MQTT** → Protocolo ligero de mensajería para IoT.  
- **Mosquitto** → El broker que distribuye los mensajes a los clientes suscritos.  

De esta forma, un **sistema embebido Linux** puede integrarse fácilmente a proyectos de **IoT, monitoreo y automatización**.

## Conceptos Básicos

### ¿Qué es un Sistema Embebido?
Un sistema embebido es una computadora pequeña diseñada para una tarea específica.  
Ejemplos:  
- Un **Raspberry Pi** en un proyecto IoT.  
- El **router WiFi** de casa.  
- El sistema de control de un **elevador**.  

### ¿Qué es DBus?
DBus es como un **autobús de información** dentro del sistema operativo Linux.  
Los servicios o aplicaciones pueden **emitir mensajes (señales)** y otros pueden **escucharlos**.  

Ejemplo de eventos en DBus:  
- Conexión/desconexión de red.  
- Estado de batería.  
- Conexión de un dispositivo USB.  

### ¿Qué es MQTT?
MQTT es un **protocolo ligero de mensajería** diseñado para dispositivos con recursos limitados.  
Funciona con el modelo **publicador-suscriptor**:

- **Publicador:** quien envía un mensaje (ej. sensor de temperatura).  
- **Suscriptor:** quien recibe el mensaje (ej. app en el celular).  
- **Topic:** el canal donde se envían los mensajes (ej. `casa/sala/temp`).  

Ejemplo:  
Un sensor publica `25°C` en el topic `casa/sala/temperatura`, y cualquier cliente suscrito lo recibe.

### ¿Qué es Mosquitto?
Mosquitto es un **broker MQTT** que funciona como intermediario.  
Recibe los mensajes de los publicadores y los distribuye a los suscriptores.  
Sin Mosquitto, los mensajes no sabrían a dónde ir.

## Flujo Completo: DBus + MQTT + Mosquitto

1. **DBus detecta un evento** en Linux (ej. desconexión de red).  
2. **Un programa escucha DBus** y crea un mensaje de texto.  
3. **El cliente MQTT publica el mensaje** en un topic.  
4. **Mosquitto recibe y reenvía** el mensaje a los clientes suscritos.  
5. **Los suscriptores reaccionan** (ej. guardar en base de datos o mostrar alerta).


## Características Principales

Esta arquitectura (DBus + MQTT) presenta una serie de características que la hacen ideal para sistemas embebidos modernos:

- **Desacoplamiento:** El componente que genera el evento (vía DBus) no necesita saber nada sobre los clientes que consumirán la información. Simplemente publica el mensaje en el broker, y este se encarga de la distribución.
- **Monitoreo en Tiempo Real:** La naturaleza de bajo retardo de MQTT permite que los eventos se publiquen y reciban casi instantáneamente, lo cual es crítico para aplicaciones de monitoreo y alerta.
- **Bajo Consumo de Recursos:** Tanto MQTT como un cliente ligero que escuche DBus están diseñados para ser eficientes, consumiendo un mínimo de CPU, memoria y ancho de banda, algo esencial en hardware con recursos limitados.
- **Escalabilidad:** Es muy sencillo añadir nuevos suscriptores (dispositivos, aplicaciones, bases de datos) que reaccionen a los eventos del sistema. El broker Mosquitto puede manejar miles de conexiones simultáneas sin problema.
- **Interoperabilidad:** Al utilizar estándares abiertos como DBus en Linux y MQTT en IoT, la solución es altamente compatible con una infinidad de plataformas, lenguajes de programación y aplicaciones de terceros.

## Ventajas de esta Arquitectura

Implementar este sistema ofrece beneficios claros:

1.  **Centralización de la Información:** Todos los eventos importantes del sistema se pueden canalizar a través de un único punto (el broker MQTT), facilitando el monitoreo, el registro (logging) y la depuración.
2.  **Flexibilidad:** Puedes cambiar fácilmente el componente que reacciona al evento. Por ejemplo, hoy una alerta puede ser un email, pero mañana puede ser una notificación push a una app móvil, sin necesidad de modificar el sistema embebido.
3.  **Fiabilidad en la Entrega:** MQTT ofrece diferentes **Niveles de Calidad de Servicio (QoS)** que garantizan la entrega de mensajes, incluso en redes inestables:
    - **QoS 0 (At most once):** "Dispara y olvida". El mensaje se envía una vez, sin confirmación.
    - **QoS 1 (At least once):** Se garantiza que el mensaje llega al menos una vez.
    - **QoS 2 (Exactly once):** Se garantiza que el mensaje llega exactamente una vez.
4.  **Desarrollo Simplificado:** En lugar de implementar sockets complejos o APIs personalizadas, los desarrolladores pueden usar librerías de MQTT bien documentadas y robustas, acelerando el tiempo de desarrollo.

## Limitaciones y Desventajas

Aunque es una solución potente, es importante considerar sus posibles inconvenientes:

- **Punto Único de Fallo (Single Point of Failure):** Si el broker Mosquitto se detiene, toda la comunicación se interrumpe. En entornos críticos, esto puede requerir configuraciones de alta disponibilidad (clustering), lo cual añade complejidad.
- **Dependencia de la Red:** La publicación de eventos depende completamente de la conectividad de red entre el dispositivo embebido y el broker. Si la red falla, los mensajes no se enviarán (a menos que se implemente una lógica de almacenamiento y reenvío).
- **Complejidad de DBus:** Para quienes no están familiarizados con él, la sintaxis y las herramientas para inspeccionar y escuchar los eventos de DBus pueden tener una curva de aprendizaje.
- **Seguridad:** Si no se configura correctamente, un broker MQTT puede ser un punto vulnerable. Es fundamental implementar mecanismos de autenticación y cifrado para proteger los datos.
