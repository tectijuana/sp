# 📡 Análisis del uso de MQTT para transmisión de datos de visión desde plataformas embebidas (incluyendo FPGA)

**Autor:** Gómez Aguilar Jared Emmanuel  
**Número de Control:** 22210309  
**GitHub:** JaredEmmanuelGomezAguilar - JaredEmmanuelGomez

---

## 📋 Resumen
Este documento analiza el uso del protocolo **MQTT** como medio eficiente para la **transmisión de datos de visión** en sistemas embebidos, incluyendo plataformas basadas en **FPGAs**.  
El objetivo es evaluar cómo este protocolo ligero permite comunicar dispositivos con recursos limitados, garantizando eficiencia, bajo consumo de energía y escalabilidad en aplicaciones de visión por computadora.

---

## 🔑 Introducción
La visión por computadora en dispositivos embebidos implica retos como:
- **Limitación de recursos** (procesador, memoria, batería).  
- **Necesidad de baja latencia** en transmisión de imágenes o metadatos.  
- **Confiabilidad** en redes inestables o de bajo ancho de banda.

En este contexto, **MQTT (Message Queuing Telemetry Transport)** surge como una solución viable gracias a su modelo **publicar/suscribirse**, simplicidad y flexibilidad en la entrega de mensajes.

---

## ⚙️ Fundamentos de MQTT
- **Arquitectura:** basada en **Clientes** y un **Broker** que gestiona la comunicación.  
- **Modelo Pub/Sub:** separación entre productores (sensores de visión) y consumidores (servidores de análisis o dashboards).  
- **Calidad de Servicio (QoS):**
  - `0` – entrega sin garantía.  
  - `1` – entrega al menos una vez.  
  - `2` – entrega exactamente una vez.  
- **Funciones clave:**
  - Mensajes retenidos (retained).  
  - Última Voluntad y Testamento (LWT).  
  - Sesiones persistentes.  
  - Keep Alive para verificar disponibilidad.
 
  <img width="767" height="400" alt="image" src="https://github.com/user-attachments/assets/4fdfea26-53be-4da9-911e-589c9c0e6d80" />

---

## 📷 Transmisión de datos de visión
1. **Datos completos:** envío de imágenes o frames comprimidos.  
2. **Metadatos:** coordenadas de objetos detectados, etiquetas o estadísticas.  
3. **Eventos:** alertas de movimiento, reconocimiento de patrones o fallos en el sensor.  

El uso de MQTT permite decidir **qué datos enviar** y **con qué nivel de garantía**, optimizando recursos.

---

## 🔬 Uso en plataformas embebidas
### 🔹 Microcontroladores y SBC (ej. Raspberry Pi)
- Publican resultados de visión procesados localmente.  
- Ideales para enviar metadatos y eventos.  

### 🔹 FPGAs
- Ejecutan **procesamiento paralelo** en tiempo real (detección de objetos, filtros de imagen).  
- Publican datos procesados mediante clientes MQTT integrados o pasarelas hacia el broker.  
- Combinan **alto rendimiento** en procesamiento con **eficiencia** en comunicación.

<img width="1352" height="758" alt="image" src="https://github.com/user-attachments/assets/d73d0508-29b3-4b30-ae38-f95bdb4bbb4f" />


---

## 🚀 Beneficios de MQTT en visión embebida
- **Bajo consumo de ancho de banda:** ideal para redes IoT.  
- **Flexibilidad en entrega:** QoS ajustable según el tipo de dato (crítico o no crítico).  
- **Escalabilidad:** múltiples suscriptores (ejemplo: un servidor en la nube y un panel local reciben la misma información).  
- **Compatibilidad:** integración con **MQTT 5** permite control de flujo, alias de tópicos y expiración de mensajes.  

---

## ⚠️ Desafíos
- MQTT no está diseñado para transmisión continua de video de alta resolución.  
- Requiere **compresión previa** o **procesamiento local** para enviar solo datos relevantes.  
- La seguridad debe fortalecerse con **TLS/SSL** y control de accesos.  

---

## 🧭 Conclusiones
El uso de **MQTT** en transmisión de datos de visión desde plataformas embebidas, incluyendo **FPGAs**, representa una opción eficiente para:
- Reducir consumo de red.  
- Integrar sistemas heterogéneos en tiempo real.  
- Escalar soluciones IoT aplicadas a vigilancia, robótica o control industrial.  

No obstante, para transmisión de video en crudo es recomendable combinar MQTT con otros protocolos optimizados para **streaming multimedia**.

---

## 📝 Aprendizajes
En esta investigación se analizó el uso del **MQTT** como protocolo de comunicación para la transmisión de datos de visión en sistemas embebidos, incluyendo FPGAs.

Se explicó que MQTT funciona bajo un modelo llamado **publicar y subiscribir**, en donde los dispositivos que generan información (como sensores o cámaras) publican datos en un **broker**, y los sistemas que necesitan la información se suscriben para obtenerla.
El documento detalla en general:

-Las ventajas de MQTT: bajo consumo de recursos, escalabilidad y confiabilidad en redes poco estables.
-El uso de calidad de servicio (QoS) para ajustar la seguridad de la entrega según la importancia de los datos.
-Funciones clave como mensajes retenidos, últimas voluntades (LWT), sesiones persistentes y el mecanismo de keep-alive.
-La integración con plataformas embebidas como Raspberry Pi o microcontroladores, y con FPGAs, que permiten procesar imágenes en tiempo real gracias a su capacidad de paralelismo.
Se aclaró también que MQTT es altamente eficiente para transmitir metadatos de visión (como coordenadas, estados o alertas), pero no es el protocolo más adecuado para transmitir video en crudo. Para esos casos, se recomienda usarlo en combinación con otros protocolos de streaming.

---

## 📝 Aprendizajes
En esta investigación se analizó el uso del **MQTT** como protocolo de comunicación para la transmisión de datos de visión en sistemas embebidos, incluyendo FPGAs.

Se explicó que MQTT funciona bajo un modelo llamado **publicar y subiscribir**, en donde los dispositivos que generan información (como sensores o cámaras) publican datos en un **broker**, y los sistemas que necesitan la información se suscriben para obtenerla.
El documento detalla en general:

-Las ventajas de MQTT: bajo consumo de recursos, escalabilidad y confiabilidad en redes poco estables.
-El uso de calidad de servicio (QoS) para ajustar la seguridad de la entrega según la importancia de los datos.
-Funciones clave como mensajes retenidos, últimas voluntades (LWT), sesiones persistentes y el mecanismo de keep-alive.
-La integración con plataformas embebidas como Raspberry Pi o microcontroladores, y con FPGAs, que permiten procesar imágenes en tiempo real gracias a su capacidad de paralelismo.
Se aclaró también que MQTT es altamente eficiente para transmitir metadatos de visión (como coordenadas, estados o alertas), pero no es el protocolo más adecuado para transmitir video en crudo. Para esos casos, se recomienda usarlo en combinación con otros protocolos de streaming.

---

## 📚 Referencias
- *MQTT 5 Essentials* – HiveMQ (2020).  
- Eclipse Foundation. [MQTT.org](https://mqtt.org)  
- OASIS Standard: MQTT Version 5.0 (2019).  
- S. Mittal, “FPGA-based Accelerators for Convolutional Neural Networks,” *ACM Computing Surveys*, 2018.  
