## Quintero Angulo Roberto carlos
## 22210784

---
# Alta disponibilidad y tolerancia a fallos en topologías MQTT distribuidas  

## Introducción  
La comunicación máquina a máquina (M2M) y el Internet de las Cosas (IoT) han crecido exponencialmente en la última década, impulsando la necesidad de sistemas de mensajería confiables, escalables y resilientes. Entre los protocolos más adoptados se encuentra MQTT (Message Queuing Telemetry Transport), diseñado para ser ligero y eficiente en redes con recursos limitados. Sin embargo, cuando se implementa a gran escala, surge el reto de garantizar la **alta disponibilidad (HA)** y la **tolerancia a fallos (FT)** dentro de arquitecturas distribuidas, asegurando que los datos sigan fluyendo incluso frente a interrupciones.  

## Conceptos fundamentales  

### Alta disponibilidad  
Se refiere a la capacidad del sistema para permanecer operativo durante el mayor tiempo posible, minimizando las interrupciones. En el contexto de MQTT, significa que los **brokers** deben seguir aceptando y distribuyendo mensajes sin importar si uno de los nodos falla.  

### Tolerancia a fallos  
Consiste en la habilidad de un sistema de mantener su funcionamiento correcto aun cuando se presenten errores de hardware, software o red. En topologías MQTT, esto se logra con **mecanismos de replicación, recuperación automática y balanceo de carga** entre brokers.  

## Topologías distribuidas en MQTT  
Para implementar HA y FT en MQTT, se suelen usar varias arquitecturas:  

- **Cluster de brokers**: múltiples instancias de MQTT trabajan en paralelo, compartiendo suscripciones y estados de clientes. Ejemplo: EMQX y HiveMQ soportan clustering nativo.  
- **Federación de brokers**: los brokers están interconectados, pero no comparten estado en tiempo real, lo que permite segmentar dominios de red.  
- **Arquitectura maestro-esclavo (primario-secundario)**: un broker primario gestiona el tráfico y otro está en espera para tomar el control en caso de fallo.  

## Mecanismos para garantizar HA y FT  

- **Balanceo de carga**: uso de balanceadores TCP/HTTP que distribuyen conexiones de clientes entre brokers disponibles.  
- **Persistencia de mensajes**: almacenamiento en disco o bases de datos distribuidas (Kafka, Redis, Cassandra) para evitar pérdida de datos.  
- **Replicación de estado**: sincronización de sesiones y colas de mensajes entre brokers, reduciendo la pérdida en caso de caída de nodos.  
- **Supervisión y orquestación**: uso de herramientas como Kubernetes, Docker Swarm o sistemas de monitoreo (Prometheus, Grafana) para reinicio automático y escalabilidad.  
- **Protocolos de consenso**: algunos brokers distribuidos implementan algoritmos como Raft o Paxos para garantizar consistencia y liderazgo en el clúster.  

## Beneficios de aplicar HA y FT en MQTT  

- Reducción de interrupciones en servicios críticos como domótica, transporte inteligente, salud digital e industria 4.0.  
- Escalabilidad horizontal para manejar millones de conexiones simultáneas.  
- Garantía de entrega de mensajes en diferentes niveles de QoS (0, 1 y 2) aun en presencia de fallos.  
- Resiliencia frente a fallos de hardware, desconexiones de red o errores de software.  

## Retos y consideraciones  

- **Complejidad de configuración**: montar un clúster distribuido requiere mayor conocimiento técnico.  
- **Costos de infraestructura**: la redundancia implica más recursos de hardware y software.  
- **Latencia y consistencia**: la replicación puede introducir retardos y posibles conflictos en la entrega de mensajes.  
- **Seguridad**: al distribuir brokers, se amplía la superficie de ataque y se deben reforzar protocolos TLS, autenticación y control de acceso.  

## Conclusión  
La alta disponibilidad y la tolerancia a fallos en topologías MQTT distribuidas aseguran que los sistemas IoT funcionen sin interrupciones. Mediante clústeres, balanceo de carga y replicación, se logra una comunicación confiable y resiliente, aunque con mayores retos de configuración, costos y seguridad.

## Referencias
https://www.hivemq.com/blog/clustering-mqtt-introduction-benefits/


https://www.mdpi.com/1424-8220/22/9/3162
