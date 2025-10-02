# Comparativa de Protocolos para IoT: MQTT, Modbus y REST

Este documento presenta una comparación entre tres protocolos relevantes para proyectos de IoT: **MQTT**, **Modbus** y **REST**, destacando sus características, ventajas, limitaciones y casos de uso más comunes.

---

## 🛰️ MQTT vs Modbus

### 🧩 MQTT (Message Queuing Telemetry Transport)

- Protocolo ligero basado en el modelo **publicador-suscriptor**.
- Diseñado para redes con **ancho de banda limitado**, alta latencia o conexiones poco confiables.
- Comunicación asíncrona y bidireccional a través de un **broker central**.
- Permite niveles de **Calidad de Servicio (QoS)** y persistencia de mensajes.
- Seguridad integrada con **TLS/SSL y autenticación**.
- Ideal para dispositivos con recursos limitados.

### ⚙️ Modbus

- Protocolo tradicional usado en automatización industrial.
- Modelo de comunicación **maestro-esclavo**.
- El maestro controla completamente la comunicación, los esclavos solo responden.
- Existen versiones como **Modbus RTU** (serial) y **Modbus TCP/IP** (Ethernet).
- Fácil de implementar y muy estable en entornos industriales.
- Limitado en capacidades de seguridad y escalabilidad.

### 🔍 Comparación MQTT vs Modbus

| Característica            | MQTT                             | Modbus                          |
|--------------------------|----------------------------------|---------------------------------|
| Modelo de comunicación   | Publicador-suscriptor            | Maestro-esclavo                |
| Arquitectura             | Basada en broker                 | Punto a punto                  |
| Escalabilidad            | Alta                             | Limitada                       |
| Seguridad                | TLS/SSL, autenticación integrada | Requiere medidas externas      |
| Ideal para               | IoT distribuido, redes inestables| Automatización industrial      |

> **Recomendación:** Usar MQTT para sistemas distribuidos, monitoreo remoto o cuando se necesite eficiencia en red. Usar Modbus en sistemas industriales tradicionales con equipos legados.

---

## 🌐 MQTT vs REST (HTTP)

### 🔗 REST (Representational State Transfer)

- Estilo arquitectónico usado en el desarrollo de APIs web.
- Basado en el modelo **cliente-servidor** con peticiones HTTP (GET, POST, etc.).
- Usa formatos como **JSON o XML**.
- Cada solicitud es independiente (**stateless**).
- Fácil de integrar con servicios web, paneles de control y bases de datos.

### 🌟 Ventajas de MQTT frente a REST

- Cabecera muy ligera (~2 bytes).
- Comunicación en **tiempo real** sin necesidad de solicitud activa.
- Mejor eficiencia en redes inestables.
- Ideal para dispositivos con recursos limitados.
- Soporte para **última voluntad** en caso de desconexión inesperada.

### ⚖️ Comparación MQTT vs REST

| Característica            | MQTT                              | REST (HTTP)                    |
|--------------------------|-----------------------------------|--------------------------------|
| Modelo de comunicación   | Publicador-suscriptor             | Cliente-servidor              |
| Eficiencia de red        | Alta (mínima sobrecarga)          | Baja (cabeceras HTTP pesadas) |
| Tiempo real              | Sí                                | No                            |
| Facilidad de integración | Media                             | Alta                          |
| Ideal para               | Dispositivos IoT en red constante | APIs web y dashboards         |

> **Recomendación:** MQTT es mejor para comunicaciones continuas o en tiempo real con muchos dispositivos. REST es adecuado para integraciones web tradicionales o comunicaciones esporádicas.

---

## 📄 Resumen del Artículo Académico: "Vista de MQTT: protocolo de comunicación en las IoT"

El artículo de la Universidad Autónoma del Estado de Hidalgo presenta una descripción técnica y práctica del protocolo **MQTT** en entornos de IoT.

### Puntos clave:

- MQTT permite comunicación eficiente en dispositivos con **recursos limitados**.
- Opera bajo una arquitectura **cliente-broker** que facilita el escalado.
- Soporta mecanismos de **seguridad, fiabilidad y gestión de mensajes**.
- Es ampliamente adoptado en **telemetría, sensores remotos y aplicaciones móviles**.

> El artículo destaca que MQTT es uno de los protocolos más recomendados para IoT debido a su bajo consumo de ancho de banda y su eficiencia en entornos con limitaciones técnicas.

---

## ✅ Conclusión

| Protocolo | Mejor para...                                     | Consideraciones                 |
|-----------|---------------------------------------------------|----------------------------------|
| MQTT      | Comunicaciones en tiempo real, IoT distribuido    | Requiere broker y configuración |
| Modbus    | Control industrial, dispositivos legacy            | Seguridad limitada              |
| REST      | Integraciones web, APIs, interfaces de usuario    | Mayor sobrecarga en red         |

> Elegir el protocolo adecuado dependerá del **tipo de aplicación**, **dispositivos involucrados**, **condiciones de red** y **necesidades de seguridad** del proyecto.

---

## 📚 Referencias

PUSR. (n.d.). *MQTT vs Modbus: An Analysis of IoT Gateway Protocol Differences*. PUSR IoT Blog. Recuperado el 30 de septiembre de 2025, de https://www.pusr.com/blog/MQTT-vs-Modbus-An-Analysis-of-IoT-Gateway-Protocol-Differences

Martínez Cabrera, A. J., & Reyes Cruz, E. A. (2023). Vista de MQTT: protocolo de comunicación en las IoT. *Revista ICBI*, 11(21), 64–75. Universidad Autónoma del Estado de Hidalgo. https://repository.uaeh.edu.mx/revistas/index.php/icbi/article/view/14698/12843

Cloud Studio. (n.d.). *MQTT vs REST: ¿Cuál es el mejor protocolo para IoT?*. Cloud Studio Blog. Recuperado el 30 de septiembre de 2025, de https://www.cloud.studio/mqtt-vs-rest-el-mejor-protocolo-para-iot/
