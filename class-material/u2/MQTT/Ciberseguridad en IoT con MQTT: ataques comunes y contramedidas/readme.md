# Ciberseguridad en IoT con MQTT: Ataques Comunes y Contramedidas

## Introducción

El protocolo MQTT (Message Queuing Telemetry Transport) es ampliamente utilizado en dispositivos IoT debido a su ligereza y eficiencia.

Sin embargo, su uso también introduce riesgos de seguridad que deben ser abordados.

## Objetivo de la Investigación

El objetivo de esta investigación es identificar los ataques más comunes que afectan a sistemas IoT que utilizan MQTT y proponer contramedidas efectivas para mitigar estos riesgos.

## Metodología

**Revisión**: Análisis de artículos académicos, blogs técnicos y documentación oficial.

**Estudio de casos**: Evaluación de incidentes reales relacionados con MQTT.

**Pruebas prácticas**: Simulación de ataques y evaluación de contramedidas.

## Ataques Comunes en MQTT

**Intercepción de mensajes**:
   - Descripción: Un atacante intercepta y modifica mensajes entre dispositivos.
   - Impacto: Pérdida de confidencialidad e integridad de los datos.

**Suplantación de identidad**:
   - Descripción: Un atacante se hace pasar por un dispositivo legítimo.
   - Impacto: Acceso no autorizado y posibles daños al sistema.

**Ataques de denegación de servicio**:
   - Descripción: Sobrecarga del broker MQTT para interrumpir el servicio.
   - Impacto: Indisponibilidad del sistema.

## Contramedidas

**Cifrado de comunicaciones**:
   - Implementar TLS/SSL para proteger los datos en tránsito.

**Autenticación y autorización**:
   - Uso de credenciales seguras y políticas de acceso basadas en roles.

**Configuración segura del broker**:
   - Limitar el número de conexiones simultáneas y establecer límites de ancho de banda.

## Conclusión

La seguridad en IoT con MQTT requiere un enfoque proactivo que combine buenas prácticas de configuración, monitoreo constante y la implementación de tecnologías de seguridad.

## Referencias

HiveMQ Team. (2020). MQTT essentials: The ultimate guide to the MQTT protocol. HiveMQ. https://www.hivemq.com/static/ebooks/hivemq-ebook-mqtt-essentials.pdf



