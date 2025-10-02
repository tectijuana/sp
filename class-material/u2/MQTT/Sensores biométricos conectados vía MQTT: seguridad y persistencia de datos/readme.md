# Sensores biométricos conectados vía MQTT: seguridad y persistencia de datos

##
**Alumno:** Diego Huerta Espinoza  
**No. Control:** 20212411
## Introducción

El uso de sensores biométricos en sistemas de monitoreo médico y aplicaciones de salud ha crecido exponencialmente gracias al Internet de las Cosas (IoT). Protocolos como MQTT (Message Queuing Telemetry Transport) permiten una comunicación eficiente entre dispositivos de bajo consumo, como microcontroladores y sensores biomédicos. Esta investigación explora cómo se integran sensores biométricos con MQTT, abordando los desafíos de seguridad y persistencia de datos.

## Arquitectura del Sistema

- **Sensores Biométricos**: Dispositivos como el MAX30102 (pulsioxímetro y monitor de frecuencia cardíaca) se conectan a microcontroladores como el ESP32 mediante interfaces como I2C.
- **Microcontroladores**: El ESP32 actúa como nodo maestro o esclavo, recolectando datos biométricos y transmitiéndolos vía MQTT.
- **Broker MQTT**: Gestiona la comunicación entre dispositivos mediante el modelo de publicación/suscripción.
- **Aplicaciones de visualización**: Herramientas como Grafana o Home Assistant permiten visualizar los datos en tiempo real.

## Seguridad en MQTT

MQTT es un protocolo ligero, ideal para dispositivos IoT, pero presenta vulnerabilidades si no se implementan medidas de seguridad adecuadas:

- **Problemas comunes**:
  - Falta de cifrado en tránsito.
  - Autenticación débil.
  - Riesgo de ataques MITM (Man-in-the-Middle).

- **Soluciones recomendadas**:
  - Uso de TLS/SSL para cifrado de datos.
  - Autenticación mediante certificados digitales.
  - Implementación de cifrado autenticado con datos asociados (AEAD), como ChaCha20-Poly1305.

## Persistencia de Datos

La persistencia de datos biométricos es crucial para garantizar trazabilidad y continuidad en el monitoreo:

- **Almacenamiento local y en la nube**: Los datos pueden ser almacenados temporalmente en el microcontrolador y luego enviados al servidor o nube.
- **Bases de datos**: Se recomienda el uso de bases de datos como InfluxDB para datos temporales y MongoDB para registros históricos.
- **Redundancia y respaldo**: Implementar copias de seguridad automáticas y redundancia en el sistema para evitar pérdida de información.

## Aplicaciones y Beneficios

- **Monitoreo en tiempo real**: Permite seguimiento continuo de constantes fisiológicas en hospitales o entornos prehospitalarios.
- **Toma de decisiones clínicas**: Mejora la eficiencia médica al proporcionar datos oportunos.
- **Escalabilidad**: MQTT permite conectar múltiples sensores sin sobrecargar la red.

## Conclusión

La integración de sensores biométricos con MQTT ofrece una solución eficiente para el monitoreo de salud, pero requiere una implementación cuidadosa en términos de seguridad y persistencia de datos. Con protocolos adecuados y buenas prácticas de desarrollo, es posible construir sistemas robustos, seguros y escalables para aplicaciones biomédicas.

## Referencias

-Becerra Tapia, Víctor, Téllez Victoria, Victoria, Ramos Medina, José Mariano, Peñaloza Mendoza, Guillermo Rey, & Castro Zenil, Mario Salvador. (2023). Sistema de transferencia de datos biomédicos con protocolos de comunicación de bajo consumo. Revista de ciencias tecnológicas, 6(4), e284. Epub 25 de junio de 2024.https://doi.org/10.37636/recit.v6n4e284  
-Suarez, J. E. P. (2025, 1 marzo). Articulo SEGURIDAD EN PROTOCOLO MQTT. studylib.es. https://studylib.es/doc/9100674/articulo--seguridad-en-protocolo-mqtt  
-Carli, M. (2025, July 17). Seguridad en MQTT en entornos de Ciberseguridad Industrial - Centro de Ciberseguridad Industrial. Centro de Ciberseguridad Industrial. https://www.cci-es.org/seguridad-en-mqtt-en-entornos-de-ciberseguridad-industrial/  
-Cdsentec. (2023, November 4). How MQTT protocol application in wireless pressure and temperature sensor ? - SenTec. SenTec. https://cdsentec.com/es/how-mqtt-protocol-application-in-wireless-pressure-or-temperature-sensor/
