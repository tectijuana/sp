# Estado del arte: Seguridad de datos en FPGA con MQTT (TLS, QoS, cifrado en hardware)

---

## 1. Introducción y alcance

La creciente expansión del Internet de las Cosas (IoT) ha impulsado la necesidad de transmisión segura y confiable de datos entre dispositivos embebidos. En este contexto, las Field Programmable Gate Arrays (FPGAs) ofrecen una plataforma flexible para implementar módulos de cifrado y procesamiento paralelo.
El protocolo MQTT se ha posicionado como uno de los más utilizados en IoT por su ligereza y eficiencia, mientras que las tecnologías TLS (Transport Layer Security) y el cifrado en hardware proporcionan mecanismos de protección ante ataques de interceptación o manipulación de datos.

![Placa FPGA](https://m.media-amazon.com/images/I/71u4+xT+zUL._UF1000,1000_QL80_.jpg)

---

## 2. MQTT y QoS 2: transmisión confiable y retos en hardware

El protocolo MQTT ofrece tres niveles de calidad de servicio (QoS):

-QoS 0: entrega al menos una vez, sin confirmación.

-QoS 1: entrega garantizada al menos una vez, con posible duplicado.

-QoS 2: garantiza entrega exactamente una vez, siendo el más confiable, pero también el más costoso en procesamiento y tiempo.

El nivel QoS 2 utiliza un intercambio de cuatro mensajes (PUBLISH → PUBREC → PUBREL → PUBCOMP), lo que garantiza que el receptor reciba cada mensaje una sola vez. Sin embargo, en sistemas embebidos o basados en FPGA, este proceso puede generar sobrecarga en memoria y latencia.

![Diagrama del flujo](https://i0.wp.com/i.imgur.com/7sC1vzn.png)

---

## 3. TLS y mTLS: protección del canal de comunicación

Para proteger la transmisión de datos, MQTT puede funcionar sobre TLS (MQTTS). Este protocolo proporciona confidencialidad, integridad y autenticación mediante certificados digitales. La versión mTLS (mutual TLS) permite que tanto el cliente como el servidor se autentiquen mutuamente.

En el contexto de FPGA, implementar una pila completa de TLS directamente en hardware es complejo debido al consumo de recursos lógicos. Por ello, una estrategia común consiste en delegar la gestión de TLS a un microcontrolador (MCU) o soft-core processor (como MicroBlaze o Nios II) que se comunica con la FPGA a través de una interfaz segura (SPI, AXI, UART).

![Handshake](https://www.researchgate.net/publication/372804861/figure/fig2/AS:11431281178403147@1690899772011/TLS-handshake-for-MQTT-authenticated-using-digital-signatures.ppm)

---

## 4. Cifrado en hardware: AES y ChaCha20-Poly1305

Las FPGAs permiten implementar algoritmos criptográficos en hardware paralelo, logrando menor latencia y mayor seguridad frente a ataques por software.
Los algoritmos más utilizados son:

AES (Advanced Encryption Standard): ampliamente estandarizado; su modo GCM (Galois Counter Mode) permite cifrado y autenticación simultánea.

ChaCha20-Poly1305: adoptado en TLS 1.3, ofrece rendimiento comparable con menor consumo energético y mayor resistencia a ataques por canal lateral.


---

## 5. Amenazas y contramedidas en hardware

A pesar de la robustez criptográfica, los ataques de canal lateral (SCA) siguen siendo un desafío. Estos ataques explotan fugas físicas como consumo de energía, radiación electromagnética o tiempos de ejecución para inferir claves secretas.

Entre las contramedidas más efectivas se encuentran:

Aleatorización (masking): introduce ruido o variabilidad controlada en los datos procesados.

Balanceo de consumo energético: evita que las transiciones lógicas revelen información.

Reconfiguración parcial dinámica: cambia la disposición del circuito durante la operación, complicando el análisis.


---

## 6. Gestión de claves y autenticación

Una parte esencial de la seguridad es la protección y manejo de las claves criptográficas. Las FPGAs modernas permiten el uso de:

Memoria segura (eFUSE) para almacenar claves permanentes.

Módulos TPM o ATECC para autenticación basada en hardware.

Certificados X.509 para la verificación en mTLS.

En aplicaciones IoT, la rotación de claves y la actualización remota (OTA) son fundamentales para mantener la seguridad a largo plazo, aunque siguen siendo retos abiertos por las limitaciones de conectividad y recursos.

---

## 7. Integración FPGA – MQTT – TLS: arquitecturas modernas

El enfoque más adoptado en la actualidad combina:

FPGA como acelerador criptográfico (AES-GCM, ChaCha20).

MCU o CPU embebida para manejar la pila TCP/TLS y la lógica MQTT.

Broker MQTT remoto con soporte TLS y control de QoS.

Este modelo híbrido equilibra rendimiento y seguridad, reduciendo la carga de software y aumentando la confiabilidad de la comunicación.

---

## 8. Evaluaciones de rendimiento y tendencias

Estudios comparativos (Gavriilidis et al., 2025) muestran que:

El uso de TLS incrementa el consumo de CPU y memoria entre 25 % y 40 %.

La aceleración de cifrado en FPGA reduce significativamente la latencia del procesamiento de datos (hasta 60 % menos).

La implementación de QoS 2 eleva el tiempo de entrega, pero asegura fiabilidad total, crucial en sistemas críticos (financieros, industriales o médicos).


---

## 9. Retos actuales y líneas de investigación

Diseño de TLS liviano para FPGA con menor uso de recursos lógicos.

Gestión automatizada de claves con actualización segura en campo (OTA).

Optimización de QoS 2 para enlaces intermitentes o redes con alta latencia.

Defensas avanzadas contra ataques SCA en implementaciones paralelas.

Cifrado de extremo a extremo (E2E) sobre MQTT, preservando la privacidad incluso ante brokers intermediarios.


---

## 10. Conclusión

El estado actual demuestra que las FPGA son plataformas ideales para implementar seguridad a nivel de hardware, especialmente cuando se integran con protocolos ligeros como MQTT y capas seguras como TLS. Sin embargo, aún existen desafíos en la gestión de recursos, protección de claves y mitigación de ataques físicos.
La tendencia hacia arquitecturas híbridas FPGA–MCU y el uso de mecanismos AEAD (Authenticated Encryption with Associated Data) representa la evolución natural hacia sistemas IoT más seguros, eficientes y confiables.


---

## 11. Referencias

Asistencia de IA: Solicité a la IA lo siguiente “Necesito una investigación sobre Estado del arte de la seguridad de datos en FPGA con MQTT (TLS, QoS, cifrado en hardware)  y opciones de imagenes que podría adjuntar"
Herramienta: ChatGPT Fecha: Viernes 3 de Octubre de 2025
