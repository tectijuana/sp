\# 📡 Lectura de Sensores Analógicos y Digitales y Envío de Datos mediante MQTT



👤 \*\*Alumno:\*\* JIMENEZ MONTES LUIS ALESSANDRO  

📅 \*\*Turno:\*\* 3PM TV  

🔗 \*\*Repositorio base:\*\* \[github.com/tectijuana/sp](https://github.com/tectijuana/sp)



---



\## 🎯 Objetivo

Implementar la lectura de sensores \*\*analógicos\*\* y \*\*digitales\*\*, procesar la información y enviarla de manera eficiente a través del protocolo \*\*MQTT\*\*, explorando conceptos de seguridad, eficiencia y arquitectura IoT.



---



\## 📖 Descripción del tema

En este tema se abordará:



1\. \*\*Lectura de sensores digitales\*\*  

&nbsp;  - Ejemplo: botón, PIR, sensor de movimiento.  

&nbsp;  - Uso de pines GPIO en modo entrada/salida.  



2\. \*\*Lectura de sensores analógicos\*\*  

&nbsp;  - Ejemplo: potenciómetro, sensor de temperatura (LM35), sensor de luz (LDR).  

&nbsp;  - Conversión analógica a digital (ADC).  



3\. \*\*Integración con MQTT\*\*  

&nbsp;  - Conexión con un broker MQTT (ejemplo: Mosquitto, HiveMQ).  

&nbsp;  - Publicación de datos desde los sensores.  

&nbsp;  - Suscripción a tópicos de control (ejemplo: encendido/apagado de LED).  



4\. \*\*Aplicaciones en la nube y edge computing\*\*  

&nbsp;  - Envío de datos a plataformas como \*\*Node-RED\*\*, \*\*ThingsBoard\*\* o \*\*AWS IoT Core\*\*.  

&nbsp;  - Procesamiento local en microcontroladores (ESP32, Raspberry Pi).  



---



\## 🛠️ Materiales sugeridos

\- ESP32 o Raspberry Pi Pico W.  

\- Sensores digitales: botón, PIR.  

\- Sensores analógicos: potenciómetro, LDR, LM35.  

\- Broker MQTT (local o en la nube).  

\- Cliente MQTT (MQTT Explorer, Node-RED o Python).  



---



\## 🔐 Seguridad en MQTT

\- Uso de \*\*credenciales de usuario/contraseña\*\*.  

\- Conexión segura con \*\*TLS/SSL\*\*.  

\- Restricción de tópicos para control de acceso.  



---



\## 📊 Ejemplo de tópicos

\- `sensores/analogico/temperatura`  

\- `sensores/digital/movimiento`  

\- `actuadores/led/control`  



---



\## 🚀 Resultados esperados

\- Captura y envío de datos de sensores en tiempo real mediante MQTT.  

\- Integración con aplicaciones en la nube para visualización.  

\- Demostración de un sistema IoT seguro y eficiente.  



---



\## 📎 Referencias

\- \[MQTT.org](https://mqtt.org/)  

\- \[HiveMQ MQTT Essentials](https://www.hivemq.com/mqtt-essentials/)  

\- \[Node-RED](https://nodered.org/)  



---

✨ Proyecto desarrollado como parte de la Unidad 2 – \*\*MQTT\*\*.



