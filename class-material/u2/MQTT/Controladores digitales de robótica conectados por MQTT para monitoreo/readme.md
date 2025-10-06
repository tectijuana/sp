# TEMA: Controladores digitales de róbotica conectados por MQTT para monitoreo

**Nombre:** Belen Perez Villa 

**Número de control:** 21212579

**Fecha:** 30/09/25
---
## ¿Qué son los controladores digitales?
Un controlador digital en robotica es el "cerebro" que recibe datos de sensores (posición, temperatura, velocidad, corriente de motores, etc),
los procesa y envia ordenes a los actuados (motores, pinzas, brazos roboticos). Ejemplos:  `` PLC, microcontroladores
(Arduino, ESP32, Raspberry pi Pico w) `` o incluso controladores industriales dedicados.
<img width="1136" height="639" alt="image" src="https://github.com/user-attachments/assets/ecac2556-5165-434b-bec9-0a6993b8bc9e" /> 
Figura 1


---
## Conexion mediante MQTT 
- `` MQTT (Message Queuing Telemetry Transport)`` es un protocolo ligero de mensajeria que es muy usado en `` IoT `` y en los sistemas distribuidos.
- Funciona con un modelo `` publicador-suscritor`` a traves de un boker (ej. Mosquitto, HiveMQ):
- El ``Controlador robotico`` publica datos: estado de motores, posicion, energia y alarmas.
- Otro disposito (PC, servidor en la nube (AWS), dashboard en Gafana o Node-RED) se suscribe a esos datos para monitorearlos en tiempo real.
- Tambien puede haber comunicacion inversa: evitar comandos al robot desde un panel remoto
---
## Ventajas de usar MQTT en robotica
1. ``Ligero y eficiente`` --> ideal para microcontroladores con pocos recursos.
2. ``Escalable`` --> se pueden conectar muchos robots/sensores a un mismo broker.
3. ``Bajo consumo de ancho de banda`` --> util si los robots estan en red Wi-Fi o incluso LTE.
4. ``Monitoreo en tiempo real`` --> datos de telemetria accesibles desde cualquier parte.
---
## Ejemplo de aplicacion practica
Imaginamos que tenemos un brazo de robotico que es controlado por un ESP32:
- El ESP32 recibe datos de un sensor de torque y de posicion.
- Publica cada 200 ms la informacion en un topico MQTT:
   - ``robot/estado/posicion``
   - ``robot/estado/torque``
- Un servidor con Node-RED y Grafana recibe datos y los muestra en dashboards con graficas.
- Desde la interfaz tambien se pueden enviar comandos (ej. ``robot/control/start``, ``robot/control/stop``).
---
## Monitoreo y seguridad
- ``QoS (Quality of Service)`` en MQTT asegura que los mensajes lleguen incluso si hay fallos de red.
- Se pueden añadir ``TLS/SSL`` y autenticacion para que nadie externo controlo los robots.
- En el entorno industrial, suele integrarse con ``Sistemas SCADA``.
---
## Referencias
- Banks, J., Carson, J. S., Nelson, B. L., & Nicol, D. M. (2019). *Discrete-Event System Simulation* (6.ª ed.). Pearson.  

- Eclipse Foundation. (2023). *MQTT: The Standard for IoT Messaging*. Recuperado de https://mqtt.org/  

- Hunkeler, U., Truong, H. L., & Stanford-Clark, A. (2008). MQTT-S — A publish/subscribe protocol for Wireless Sensor Networks. *IEEE 3rd International Conference on Communication Systems Software and Middleware*, 791–798. https://doi.org/10.1109/COMSWA.2008.4554519  

- Ochoa, S., & Mejía, R. (2021). *Internet de las Cosas: Fundamentos y Aplicaciones*. Alfaomega.  

- Villalobos, J., & García, E. (2020). Controladores digitales aplicados a la robótica industrial. *Revista Iberoamericana de Automática e Informática Industrial*, 17(4), 413–424. https://doi.org/10.4995/riai.2020.12443  

- Eclipse Mosquitto. (2023). *An Open Source MQTT Broker*. Recuperado de https://mosquitto.org/  

- Node-RED. (2023). *Low-code programming for event-driven applications*. Recuperado de https://nodered.org/ 
