# Simulación de Redes MQTT para Pruebas de Sistemas Distribuidos Embebidos
### Introducción
La simulación de redes MQTT da la posibilidad de probar, validar y optimizar sistemas distribuidos embebidos sin necesidad de desplegar el hardware completo.
Normalmente tiene el objetivo de evaluar el rendimiento, la confiabilidad y la seguridad de aplicaciones IoT y sistemas embebidos en un entorno controlado.

**MQTT BROKER**
El broker MQTT actúa como intermediario central entre los clientes que publican y los que se suscriben. Su función principal es recibir los mensajes publicados en un tópico y distribuirlos únicamente a los clientes suscritos a ese tópico, garantizando la entrega según el nivel de QoS (Quality of Service) configurado. De esta manera, desacopla a los emisores de los receptores y asegura que la comunicación suceda en los sistemas distribuidos.

**Objetivos**
- Validar la comunicación entre nodos antes de implementar en hardware real.
- Analizar latencias y pérdidas de paquetes bajo distintas condiciones de red.
- Probar QoS (Quality of Service) de MQTT en diferentes escenarios.
- Simular escalabilidad: número de clientes, tópicos y frecuencia de publicación.
- Evaluar la consistencia de datos en sistemas distribuidos.

**Herramientas de Simulación**
1. Brokers MQTT para pruebas
- Eclipse Mosquitto: ligero, usa autenticación y TLS.
- EMQX: escalabilidad y uso de métricas.
- HiveMQ CE: ideal para pruebas con dashboards y monitoreo.
2. Simuladores de clientes
- MQTT.fx: es una herramienta gráfica para pruebas manuales.
- MQTT Explorer: visualización de tópicos y cargas.
- Scripts en Python (Paho-MQTT): para generar clientes y escenarios de tráfico.
3. Entornos de red simulada
- Docker: crear topologías distribuidas con múltiples contenedores.
- Mininet: simular condiciones de red (latencia, pérdida, ancho de banda).
- NS-3: simulación avanzada de protocolos de red.

### Escenarios de Prueba
1. Topología Básica

Varios clientes embebidos (sensores) publican en un broker central.
Un cliente suscriptor recibe y procesa los mensajes.

2. Topología Distribuida

Gateways locales conectados a un broker central en la nube.
Simulación de desconexiones y reintentos automáticos.

3. Pruebas de Estrés

Decenas o cientos de clientes simulados publicando al mismo tiempo.
Medición de uso de CPU, memoria y latencia del broker.

4. Pruebas de Seguridad

Conexiones MQTT con TLS/SSL.

Autenticación con usuario/contraseña o certificados.

### Métricas a Evaluar

- Latencia: tiempo entre publicación y recepción.
- Throughput: cantidad de mensajes procesados por segundo.
- Uso de recursos: CPU, RAM y red en broker y clientes.
- Confiabilidad: pérdida de mensajes bajo distintas condiciones.
- Escalabilidad: comportamiento con cientos/miles de clientes.

### Beneficios
- Reducción de costos antes de desplegar hardware real.
- Mayor control de pruebas (condiciones de red y carga ajustables).
- Detección temprana de cuellos de botella.
- Facilidad para enseñanza y experimentación académica.

### Conclusión
La simulación de redes MQTT constituye una herramienta esencial para el desarrollo de sistemas distribuidos embebidos, ya que permite anticipar problemas, mejorar el rendimiento y aumentar la seguridad antes de la implementación en dispositivos físicos.

- Alumno: Roldan Castro Luis Alberto (22211648)
- Docente: Rene Reyes Solis
- Grupo: SC7B
