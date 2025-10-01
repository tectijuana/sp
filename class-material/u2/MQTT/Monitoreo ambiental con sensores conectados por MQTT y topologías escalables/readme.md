# Monitoreo Ambiental con Sensores conectados por MQTT y Topologías Escalables

**Alumno:** Solano Cortéz Iván Israel

**Materia:** Sistemas Programables

**Fecha:** 30 de septiembre del 2025


## 📌 Resumen
Esta investigación describe la aplicación de sensores para **monitoreo ambiental** (aire, agua, ruido y clima), cómo se integran mediante **MQTT**, y las **topologías y prácticas** para escalar sistemas desde decenas hasta miles de nodos. Se incluyen ejemplos prácticos, arquitecturas recomendadas y referencias bibliográficas.

---

## 1. Introducción
El protocolo **MQTT** es ligero y se basa en el modelo *publish/subscribe*, lo que lo hace ideal para **IoT** y **monitoreo ambiental**. Permite separar los **sensores (publishers)** de los **consumidores de datos (subscribers)** y soporta tópicos jerárquicos, QoS y retención de mensajes. Esto lo hace especialmente útil en redes distribuidas con limitaciones de energía y ancho de banda.

---

## 2. Variables Ambientales y Sensores

| Variable              | Sensores comunes                      | Consideraciones |
|-----------------------|----------------------------------------|-----------------|
| **Calidad del aire**  | SDS011, PMS5003 (PM2.5/PM10); MQ-x, SCD30 (CO₂) | Los sensores de partículas requieren calibración; los NDIR son preferibles para CO₂. |
| **Clima**             | BME280, SHT3x (T°, humedad, presión)  | Bajo consumo y fácil integración con ESP32/Arduino. |
| **Calidad del agua**  | pH, turbidez, conductividad, DO        | Requieren mantenimiento frecuente por biofouling. |
| **Ruido ambiental**   | Micrófonos calibrados (SPL)            | Útiles para mapas de contaminación acústica. |

---

## 3. Arquitectura Típica

[Sensores] ---> [Gateway local/Edge] ---> [Broker MQTT] ---> [DB/Analytics/Dashboards]

En esta arquitectura:

* Los sensores recolectan datos (ej. temperatura, CO₂, humedad).

* El gateway local se encarga de la agregación de datos y puede incluir funciones de preprocesamiento.

* El broker MQTT centraliza la comunicación y asegura que los mensajes lleguen a los clientes interesados.

* Finalmente, los datos se almacenan en una base de datos, se procesan mediante analytics y se visualizan en dashboards.

## 4. Topologías Escalables

Para garantizar que un sistema de monitoreo ambiental funcione de forma eficiente incluso con miles de sensores, es necesario implementar topologías escalables.

## 4.1 Topología Jerárquica

* Sensores distribuidos en diferentes regiones.

* Cada región cuenta con un gateway que se comunica con un broker intermedio.

* Los brokers intermedios se conectan a un broker central para consolidar la información.

## 4.2 Topología Distribuida con Balanceo de Carga

* Uso de múltiples brokers MQTT trabajando en conjunto.

* Implementación de balanceadores de carga que distribuyen las conexiones de los sensores.

* Garantiza tolerancia a fallos y mayor disponibilidad.

## 4.3 Edge Computing + MQTT

* Procesamiento preliminar de datos en el borde (edge).

* Reducción de la latencia y del tráfico hacia la nube.

* Ideal para sistemas que requieren respuestas rápidas (ej. alertas de contaminación).

## 5. Ventajas del Monitoreo Ambiental con MQTT

* Escalabilidad: Puede manejar desde pocos hasta miles de sensores.

* Eficiencia energética: Los sensores consumen menos energía en la transmisión de datos.

* Flexibilidad: Integración con sistemas de almacenamiento, análisis de datos y dashboards en la nube.

* Interoperabilidad: Soporta diferentes plataformas y lenguajes de programación.

* Confiabilidad: Opciones de QoS aseguran la entrega de mensajes.

## Conclusiones

El uso de sensores conectados mediante MQTT en arquitecturas escalables es una estrategia sólida para el monitoreo ambiental moderno.
Este enfoque permite la recolección eficiente, segura y en tiempo real de datos, garantizando una mejor toma de decisiones en ámbitos como la agricultura, las ciudades inteligentes y la protección ambiental.

## Referencias

* Banks, A., & Gupta, R. (2014). MQTT Version 3.1.1. OASIS Standard. https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html

* Hunkeler, U., Truong, H. L., & Stanford-Clark, A. (2008). MQTT-S — A publish/subscribe protocol for Wireless Sensor Networks. 2008 3rd International Conference on Communication Systems Software and Middleware and Workshops (COMSWARE), 791–798. https://doi.org/10.1109/COMSWA.2008.4554519

* Serrano, M., & Serrano, J. (2019). MQTT IoT Protocol and Edge Computing: A Perfect Match for Environmental Monitoring Systems. IEEE Internet of Things Journal, 6(2), 3668–3675.

* IBM. (2020). What is MQTT? IBM Developer. https://developer.ibm.com/articles/iot-mqtt-why-good-for-iot/
