# Gonzalo Cortez Huerta 22210761

## Fuentes

- [Qué es MQTT y cómo funciona](https://mqtt.org/)  
- [Arquitectura de memoria en sistemas embebidos (BBVA)](https://www.bbva.com/es/que-son-los-sistemas-embebidos-y-para-que-sirven/)  
- [Jerarquía de memoria - GeeksforGeeks](https://www.geeksforgeeks.org/memory-hierarchy-design-and-its-characteristics/)  
- [Uso de memoria en IoT y MQTT - ResearchGate](https://www.researchgate.net/publication/343413737_The_Design_and_Implementation_of_MQTT_Based_IoT_Application)  
- [IBM Developer - Introducción a MQTT](https://developer.ibm.com/articles/iot-mqtt-why-good-for-iot/)  

# Jerarquías de memoria en dispositivos que usan MQTT para telemetría

## Descripción
Lo que pedí a la IA: un documento en formato **Markdown** sobre jerarquías de memoria en dispositivos IoT que usan **MQTT** para telemetría.  
Lo que modifiqué: se adaptó la información al contexto de **telemetría IoT**, destacando cómo la jerarquía de memoria influye en el rendimiento, consumo de energía y confiabilidad en la transmisión de datos.

---

## Introducción
En sistemas de **telemetría IoT**, los dispositivos recopilan datos de sensores y los transmiten mediante el protocolo **MQTT (Message Queuing Telemetry Transport)** hacia un broker o servidor.  
La **jerarquía de memoria** en estos dispositivos es clave para optimizar:
- **Velocidad de respuesta**  
- **Consumo energético**  
- **Almacenamiento local vs en la nube**  
- **Fiabilidad de los datos transmitidos**

---

## Jerarquía de Memoria en IoT con MQTT

1. **Registros del procesador (nivel más rápido)**  
   - Se usan para operaciones inmediatas de la CPU.  
   - Guardan valores temporales como mediciones instantáneas de sensores.  

2. **Memoria caché (si está disponible en SoC avanzados)**  
   - Permite un acceso rápido a datos que se usan frecuentemente.  
   - Reduce la latencia al procesar datos para enviarlos por MQTT.  

3. **Memoria RAM (volátil)**  
   - Almacena temporalmente datos de sensores antes de empaquetarlos en mensajes MQTT.  
   - Maneja colas de mensajes cuando la conexión con el broker es inestable.  

4. **Memoria Flash / EEPROM (no volátil)**  
   - Guarda configuraciones del dispositivo (credenciales MQTT, tópicos, QoS).  
   - Almacena datos críticos cuando no hay conectividad, para retransmitirlos luego.  

5. **Almacenamiento externo (SD, NAND, etc.)**  
   - Usado en gateways o dispositivos con mayor capacidad.  
   - Permite almacenar grandes volúmenes de datos antes de enviarlos.  

6. **Nube / Servidor MQTT (nivel externo)**  
   - El broker MQTT organiza y distribuye la información a clientes suscritos.  
   - Garantiza la entrega dependiendo del nivel de **QoS** configurado.  

---

## Diagrama en Mermaid

```mermaid
graph TD
    A[Dispositivo IoT con MQTT] --> B1[Registros CPU]
    B1 --> B2[Memoria Caché]
    B2 --> B3[Memoria RAM]
    B3 --> B4[Memoria Flash/EEPROM]
    B4 --> B5[Almacenamiento externo]
    B5 --> C[Nube / Broker MQTT]
