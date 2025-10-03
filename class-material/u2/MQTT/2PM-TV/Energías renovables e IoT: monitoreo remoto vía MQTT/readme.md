
# Energías renovables e IoT: monitoreo remoto vía MQTT

**Autor:** Meza Rodriguez Eduardo Manuel  
**Institución:** Instituto Tecnológico de Tijuana  
**Materia:** Sistemas Programables  
**Profesor:** Rene Solis Reyes  
**Fecha:** 30 de Septiembre del 2025  

## ¿Qué es MQTT?
MQTT (Message Queuing Telemetry Transport) es un protocolo ligero de mensajería diseñado para la comunicación máquina a máquina (M2M) y para el Internet de las Cosas (IoT).  
- Se basa en el modelo publicar/suscribirse, lo cual permite mayor flexibilidad en el envío y recepción de datos.  
- Fue pensado para dispositivos con recursos limitados (sensores, microcontroladores) y conexiones poco confiables (redes móviles, WiFi rural o enlaces satelitales).  
- En este modelo, los dispositivos solo necesitan conectarse a un **broker**, que funciona como intermediario, reduciendo la dependencia directa entre sensores y aplicaciones.  

## Flujo de comunicación en monitoreo remoto de energías renovables

### Publicadores (sensores IoT)
Los sensores son los encargados de tomar mediciones del entorno y del funcionamiento de los equipos de energía renovable.  
- **Paneles solares:** voltaje, corriente, temperatura de celdas, radiación solar.  
- **Turbinas eólicas:** velocidad del viento, rpm del rotor, potencia generada, temperatura de rodamientos.  
- Cada dato capturado se envía a un *topic* organizado jerárquicamente, por ejemplo:  
  - energia/solar/panel1/voltaje = 32.5V  
  - energia/eolica/turbina2/potencia = 450kW  

### Broker MQTT
El broker es el núcleo de la comunicación:  
- **Función principal:** recibir los mensajes de los publicadores y distribuirlos a los suscriptores que lo requieran.  
- Puede implementarse en la nube para soluciones escalables, o en servidores locales para aprovechar baja latencia en entornos aislados.  
- Algunos brokers populares son **Eclipse Mosquitto**, **HiveMQ** y **EMQX**.  

### Suscriptores (sistemas de control y usuarios)
Los suscriptores reciben mensajes del broker y los utilizan de diversas formas:  
- **Visualización:** plataformas web y móviles que muestran la producción en tiempo real.  
- **Almacenamiento:** bases de datos que guardan el histórico de producción.  
- **Gestión inteligente:** sistemas SCADA o dashboards que generan reportes de eficiencia y predicciones.  
- **Alertas:** notificaciones automáticas si un panel presenta baja eficiencia o si una turbina se detiene.  

## Características de MQTT útiles en IoT energético
- **Ligereza y eficiencia:** bajo consumo de ancho de banda, esencial para zonas rurales sin fibra óptica.  
- **Calidad de servicio (QoS):**  
  - QoS 0: entrega mejor esfuerzo.  
  - QoS 1: al menos una vez, garantizando llegada.  
  - QoS 2: exactamente una vez, usado donde no debe haber duplicados.  
- **Persistencia de mensajes:** útil cuando un sensor se desconecta y luego vuelve a transmitir.  
- **Retained Messages:** siempre disponible el último dato crítico, como el voltaje de una batería.  
- **Last Will & Testament (LWT):** informa sobre fallas de sensores desconectados, lo que mejora el mantenimiento.  

## Ejemplo de arquitectura típica
1. **Sensores IoT** en los equipos renovables envían datos mediante WiFi, LoRa o 4G.  
2. **Broker MQTT** centraliza la información.  
3. **Base de datos** (MySQL, InfluxDB) almacena el histórico.  
4. **Dashboard** (Grafana, Node-RED) visualiza tendencias de energía.  
5. **Sistema de alarmas** envía correos o mensajes de texto cuando ocurre una anomalía.  

## Retos y consideraciones
- **Seguridad:** los datos deben cifrarse (TLS/SSL) para evitar accesos malintencionados.  
- **Escalabilidad:** un sistema debe estar preparado para manejar cientos o miles de sensores.  
- **Mantenimiento preventivo:** detectar fallos en paneles y turbinas antes de que se vuelvan críticos.  
- **Optimización energética:** usar los datos recolectados para planificar mejor el consumo y almacenamiento en baterías.  

## Impacto en energías renovables
El uso de IoT con MQTT representa una gran ventaja para el sector energético:  
- Permite **monitoreo en tiempo real** de plantas solares y parques eólicos, incluso en regiones remotas.  
- Ayuda a reducir costos de operación gracias al mantenimiento predictivo.  
- Mejora la **eficiencia energética**, ya que los datos en vivo permiten ajustar la distribución de energía en redes inteligentes (*smart grids*).  
- Contribuye a una gestión más sostenible al integrar tecnologías limpias con comunicación eficiente.  

***

