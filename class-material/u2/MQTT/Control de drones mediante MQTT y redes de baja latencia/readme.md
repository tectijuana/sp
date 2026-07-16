# Control de Drones mediante MQTT y Redes de Baja Latencia
## Castillo Enriquez Hugo 22211532

## 1. Introducción
El control de vehículos aéreos no tripulados (UAVs) requiere **comunicaciones eficientes y confiables**, donde la **latencia** juega un papel crítico en la estabilidad y seguridad de vuelo. Protocolos tradicionales como HTTP presentan demasiado overhead para aplicaciones en tiempo real, lo que ha motivado la adopción de alternativas ligeras como **MQTT (Message Queuing Telemetry Transport)**.

MQTT, diseñado para redes de baja capacidad y dispositivos limitados, se basa en un modelo **publish/subscribe** y ofrece características orientadas a IoT. Con la llegada de **MQTT 5**, se incorporaron optimizaciones que lo hacen más competitivo para aplicaciones que requieren baja latencia, como el control de drones.

---

## 2. Marco Teórico

### 2.1 MQTT y el modelo cliente-broker
MQTT se apoya en el modelo **cliente-broker** sobre TCP/IP. Los clientes publican mensajes en *topics*, mientras que los suscriptores reciben la información mediante el broker, que actúa como intermediario.  
Ventajas: simplicidad, overhead reducido y amplia compatibilidad con plataformas IoT.  
Limitaciones: dependencia de TCP, lo que implica confirmaciones, reordenamiento y potencial aumento en latencia.

### 2.2 Características de MQTT 5 relevantes para baja latencia
- **QoS (Quality of Service):**  
  - **QoS 0**: entrega sin garantías, mínima latencia.  
  - **QoS 1**: garantiza entrega al menos una vez (mayor overhead).  
  - **QoS 2**: garantiza entrega exactamente una vez (latencia más alta) .

- **Flow Control (Receive Maximum):** regula el número de mensajes en vuelo para evitar saturación del cliente o broker .

- **Topic Alias:** sustituye nombres largos de *topics* por identificadores numéricos, reduciendo tamaño de paquetes y tiempo de transmisión .

- **Message y Session Expiry:** previenen la entrega de mensajes caducados, lo cual es crítico en sistemas de control donde un comando tardío puede ser peligroso .

- **User Properties:** permiten agregar metadatos a los mensajes, como marcas de tiempo o identificadores, útiles para trazabilidad y análisis de latencia .

- **Keep Alive y Client Take-Over:** mecanismos para detectar desconexiones rápidamente y recuperar la sesión sin pérdida prolongada de conectividad .

### 2.3 Importancia de la latencia en drones
En sistemas de control UAV, la latencia debe mantenerse en márgenes muy bajos para garantizar la estabilidad de los actuadores y la precisión en la navegación. Un retraso superior a decenas de milisegundos puede comprometer la seguridad, especialmente en maniobras críticas o en entornos con obstáculos.  

La elección de QoS, la cercanía del broker (edge vs cloud) y el uso de optimizaciones como **Topic Alias** y **Message Expiry** influyen directamente en el rendimiento.

### 2.4 Alternativas a MQTT
- **DDS (Data Distribution Service):** ofrece control fino de QoS y soporta multicast. Es más adecuado para tiempo real estricto, aunque más complejo y pesado .
- **MQTT-SN:** variante de MQTT sobre UDP, diseñada para redes de sensores y entornos con restricciones de energía y conectividad .
- **Otros protocolos (ZeroMQ, ROS2):** aplicados en robótica, con ventajas en entornos de comunicación interna de alta frecuencia.

---

## 3. Preguntas de Investigación
- **RQ1:** ¿Qué configuraciones de QoS en MQTT 5 permiten optimizar la latencia sin comprometer la fiabilidad en exceso?  
- **RQ2:** ¿Qué impacto tienen las nuevas características de MQTT 5 (flow control, topic alias, expiry) en escenarios de control UAV?  
- **RQ3:** ¿Cómo se posiciona MQTT 5 frente a alternativas como DDS y MQTT-SN en el contexto de baja latencia?  

---

## 4. Metodología Teórica
La investigación se desarrollará mediante:
1. **Análisis documental** de la especificación MQTT 5 y literatura académica sobre benchmarks de latencia.  
2. **Revisión comparativa** de estudios que enfrentan MQTT con protocolos alternativos (DDS, MQTT-SN).  
3. **Modelado teórico** de los tiempos de comunicación, considerando:  
   - Overhead de TCP.  
   - Diferencias de QoS en reintentos y confirmaciones.  
   - Reducción de tamaño de paquetes con Topic Alias.  
   - Efecto de Message Expiry en sistemas críticos.  
4. **Discusión crítica** sobre la aplicabilidad de MQTT 5 en UAVs de distintos escenarios:  
   - Redes locales de baja latencia (edge computing).  
   - Redes con mayor variabilidad (Wi-Fi, 4G/5G).  

---

## 5. Resultados Esperados
- **QoS 0** es la opción más adecuada para minimizar latencia, aunque con riesgo de pérdida en entornos no confiables.  
- **Topic Alias** reduce overhead en comunicaciones de alta frecuencia, siendo útil en telemetría continua.  
- **Message Expiry** garantiza consistencia evitando comandos obsoletos.  
- **Brokers en el edge** son preferibles a brokers en la nube para control UAV, debido a la reducción de RTT.  
- Frente a DDS, MQTT ofrece simplicidad y despliegue ágil, pero no garantiza tiempos deterministas <10 ms, por lo que su uso debe reservarse a control no crítico y telemetría.

---

## 6. Discusión
MQTT 5 puede considerarse un protocolo **viable para escenarios de baja latencia no estricta**, como monitoreo de drones, telemetría y control remoto no crítico. Sus optimizaciones (flow control, topic alias, expiry) mejoran sustancialmente la eficiencia frente a versiones anteriores.  

Sin embargo, para **control en tiempo real estricto**, la dependencia de TCP y las limitaciones del modelo de QoS hacen que DDS o soluciones basadas en UDP sean más adecuadas.  

Una posible solución híbrida consiste en utilizar **DDS/ROS2** para los lazos internos de control y **MQTT 5** para comunicación de alto nivel y monitoreo.

---

## 7. Conclusiones
- MQTT 5 introduce mejoras claves que permiten su aplicación en UAVs con requisitos de baja latencia, aunque no de tiempo real estricto.  
- Configuraciones con **QoS 0, brokers locales y uso de features como Topic Alias y Message Expiry** ofrecen el mejor equilibrio entre latencia y fiabilidad.  
- Para aplicaciones críticas en tiempo real, es recomendable complementar MQTT con protocolos especializados como DDS.  
- La investigación contribuye a delimitar el rol de MQTT en arquitecturas híbridas para control de drones.  

---

## 8. Referencias
- HiveMQ. (2020). *MQTT 5 Essentials*.  
- OASIS. (2019). *MQTT Version 5.0 Specification*.  
- Rahman, H., et al. (2022). *A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS*. arXiv.  
- RTI. *DDS vs MQTT: A Comparison for Real-Time Systems*.  
- Eclipse Foundation. *Eclipse Paho MQTT Client*.  
- MQTT-SN Specification. OASIS.  
- PX4 Autopilot Documentation. *Communication Protocols Overview*.  
