### NICOLÁS LÓPEZ FÉLIX - C21212706

# 📡 Transmisión de datos DSP en tiempo real usando **MQTT** y análisis remoto

> **Resumen**
> Esta investigación explica cómo usar MQTT (especialmente MQTT 5.0) como transporte para datos de DSP en escenarios de baja latencia y análisis remoto. Cubre arquitectura recomendada, formatos de datos, compresión y codecs, técnicas de edge/feature extraction para reducir ancho de banda, consideraciones de latencia/jitter, seguridad, herramientas y patrones de despliegue. También ofrece una lista práctica de buenas prácticas para producción.

---

## 📘 Tabla de contenidos

1. [Contexto y alcance](#contexto-y-alcance)
2. [¿Por qué MQTT? cuándo usarlo (y cuándo NO)](#por-qué-mqtt-cuándo-usarlo-y-cuándo-no)
3. [Restricciones DSP y métricas clave (latencia, jitter, frame size)](#restricciones-dsp-y-métricas-clave-latencia-jitter-frame-size)
4. [Arquitectura recomendada (device → edge → broker → análisis)](#arquitectura-recomendada-device---edge---broker---análisis)
5. [Formatos de payload y serialización (JSON, CBOR, Protobuf)](#formatos-de-payload-y-serialización-json-cbor-protobuf)
6. [Compresión y codecs para audio/senales (Opus, ADPCM, DPCM)](#compresión-y-codecs-para-audiosenales-opus-adpcm-dpcm)
7. [Edge processing / feature extraction (por qué enviar características y no siempre raw)](#edge-processing--feature-extraction-por-qué-enviar-características-y-no-siempre-raw)
8. [QoS, persistencia y control de entrega en MQTT 5.0](#qos-persistencia-y-control-de-entrega-en-mqtt-50)
9. [Seguridad y autenticación (TLS, OAuth2, mTLS, ACLs)](#seguridad-y-autenticación-tls-oauth2-mtls-acls)
10. [Escalado y elección de broker / herramientas](#escalado-y-elección-de-broker--herramientas)
11. [Pipeline de ejemplo (producción): Mosquitto/EMQX → Telegraf → InfluxDB → Grafana](#pipeline-de-ejemplo-producción-mosquittoemqx--telegraf--influxdb--grafana)
12. [Checklist de buenas prácticas y recomendaciones rápidas](#checklist-de-buenas-prácticas-y-recomendaciones-rápidas)
13. [Limitaciones, riesgos y trabajos futuros](#limitaciones-riesgos-y-trabajos-futuros)
14. [Referencias (APA)](#referencias-apa)

---

# 1. Contexto y alcance

Este documento asume un caso típico: dispositivos que generan señales (audio, vibración, sensores de alta tasa) y desean transmitir *en tiempo cercano a real* para análisis remoto (detección de anomalías, clasificación, visualización en dashboards). El foco es en **arquitecturas prácticas** con MQTT como transporte — analizando ventajas, limitaciones y patrones para minimizar latencia y consumo de ancho de banda.

---

# 2. ¿Por qué MQTT? cuándo usarlo (y cuándo NO)

* **Ventajas**: MQTT es liviano, ampliamente soportado por brokers y bibliotecas (Eclipse Mosquitto, Paho, EMQX, HiveMQ) y tiene características útiles en v5 (topic aliases, message/session expiry, user properties, shared subscriptions) que ayudan en sistemas IoT/IIoT.
* **Limitaciones**: MQTT **no es un transporte de tiempo real determinista** (no proporciona garantías de latencia <~50 ms en redes públicas). Para ultra-baja latencia y media/audio interactiva, suele recomendarse WebRTC / WebTransport o protocolos RTP/SRTP. En cambio, MQTT es excelente para telemetría, telemetría de sensores, y transmisión de *frames/paquetes pequeños* o *features agregados*.

**Regla práctica**: si tu objetivo es audio interactivo (conversación en tiempo real o música con latencia humana crítica), prioriza WebRTC. Si tu objetivo es análisis remoto con tolerancia a decenas a cientos de ms, o envío de *features* o paquetes cortos (MFCCs, estadísticas por frame), MQTT es apropiado.

---

# 3. Restricciones DSP y métricas clave

* **Frame size (bloque de muestreo)**: determina latencia mínima: `frame_time = frame_samples / fs`. Ej.: 10 ms a 16 kHz → 160 muestras → cada frame introduce 10 ms de adquisición mínima.
* **Jitter**: paquetes intermitentes requieren *de-jitter buffers* en el receptor (aumentan latencia para mejorar estabilidad). Sistemas en tiempo cercano-a-real balancean jitter vs. latencia.
* **Presupuesto de latencia**: sumar latencias de ADC/encodificación → transmisión → colas/broker → deserialización → análisis → respuesta. Diseñar con margen (p. ej. objetivo final < 200 ms total) y medir cada etapa.

---

# 4. Arquitectura recomendada (device → edge → broker → análisis)

Patrón general:

1. **Device (sensado)** — adquisición ADC / microcontrolador / SoC.
2. **Edge gateway** (puede ser Raspberry Pi, gateway embebido) — tareas: framing, preprocesado, extracción de features, compresión, buffering, seguridad y puente MQTT-SN→MQTT si hay dispositivos muy limitados.
3. **Broker MQTT** — Mosquitto / EMQX / HiveMQ (gestiona pub/sub, QoS, shared subscriptions para balanceo).
4. **Procesamiento & almacenamiento** — consumidores (stream processors, funciones serverless, Apache Flink/Kafka Connect, o Telegraf → InfluxDB) que reciben mensajes MQTT y los envían a bases de datos/ML/alertas.
5. **Visualización/Análisis** — dashboards (Grafana), ML/serving (TF-Serving, TorchServe) y pipelines de offline training.

**Notas**:

* Para dispositivos muy limitados se puede usar **MQTT-SN** (UDP/encabezados reducidos) y un gateway que traduzca a MQTT estándar.
* En entornos industriales, usar **shared subscriptions** para balancear la carga de procesamiento entre múltiples consumidores.

---

# 5. Formatos de payload y serialización (JSON, CBOR, Protobuf)

* **JSON**: legible, fácil para debugging, pero con sobrecarga de bytes y parsing más lento.
* **CBOR (RFC 8949)**: formato binario compacto (ideal cuando quieres una estructura “tipo JSON” pero más pequeña).
* **Protocol Buffers (Protobuf)**: esquema + binario → baja latencia de parsing y tamaño reducido; ampliamente usado en IIoT (ej. Sparkplug B usa Protobuf). Útil cuando necesitas compatibilidad entre lenguajes y payloads compactos.

**Recomendación práctica**: para datos DSP de alta tasa (frames o múltiples sensores) usa **Protobuf** o **CBOR** (binario). Resguarda `topic` + `timestamp` + `sequence_id` + `payload` (payload = frame raw/compressed o vector de features).

---

# 6. Compresión y codecs (audio y señales)

* Para **audio interactivo** o de alta fidelidad: **Opus** (RFC 6716) es el codec de referencia de baja latencia y alta eficiencia; bien probado en aplicaciones VoIP/WebRTC. Para transmisión en paquetes sobre redes con pérdida, considere usar FEC/in-band FEC o envío de paquetes más pequeños.
* Para señales donde la fidelidad absoluta no es necesaria, técnicas como **DPCM / ADPCM** o compresión por subbanda pueden reducir el bitrate manteniendo la utilidad para análisis.
* Alternativa: **extraer features** (MFCC, espectrogramas reducidos) en edge y enviar vectores de características en vez de raw audio; esto reduce drásticamente el ancho de banda (ver sección 7).

---

# 7. Edge processing — por qué enviar features (y qué enviar)

Enviar características en vez de audio bruto **reduce ancho de banda** y preserva privacidad. Ejemplos comunes:

* **MFCCs** (coeficientes mel-cepstrales) — comunes en reconocimiento de voz y clasificación de sonidos.
* **Espectrograma comprimido** (frames reducidos).
* **Stat summaries**: RMS, ZCR, centroid, banda energía por banda.
  La literatura y trabajos recientes muestran que la compresión/feature-extraction en el edge puede ahorrar >80% de ancho de banda manteniendo rendimiento similar en tareas de detección/monitorización industrial.

---

# 8. QoS, persistencia y control de entrega en MQTT 5.0

* **QoS 0** = *at most once* (menor latencia, sin confirmación).
* **QoS 1** = *at least once* (retransmisión — posible duplicado).
* **QoS 2** = *exactly once* (mayor overhead).
* **Session Expiry / Message Expiry** (MQTT 5) permiten controlar cuánto tiempo el broker almacena estado/mensajes; útil para sistemas con desconexiones breves.

**Consejos prácticos**:

* Para telemetría de alta frecuencia prioriza QoS0 o QoS1 con *idempotencia* en el consumidor.
* Para mensajes críticos de control o alarmas usa QoS1/2 y persistencia.
* Usa **topic aliases** en publicaciones repetidas para reducir overhead de headers (MQTT 5).

---

# 9. Seguridad y autenticación

* **TLS (MQTT over TLS)**: imprescindible si los datos son sensibles o el broker es público. Validar cadenas de certificados y usar suites seguras.
* **Autenticación**: username/password, X.509 client certificates (mTLS) o tokens (OAuth2) según el ecosistema; HiveMQ y EMQX documentan patrones concretos.
* **Autorización/ACLs**: define qué topics puede publicar/suscribir cada identidad.
* **Cifrado de payload extremo a extremo**: si necesitas que ni siquiera el broker lea el payload, cifra el payload en origen y descífralo en destino (además de TLS).

---

# 10. Escalado y elección de broker / herramientas

* Brokers populares: **Eclipse Mosquitto** (liviano), **EMQX** (escala horizontal), **HiveMQ** (enterprise), **VerneMQ** (clustering). Elección depende de volumen, tolerancia a fallos, y características (bridge, plugins, autenticación).
* **Benchmarking**: estudios experimentales muestran que el rendimiento de brokers depende fuertemente del *tamaño de payload* y la mezcla de tráfico (pequeños vs grandes payloads). Prueba con tus cargas reales antes de dimensionar.

---

# 11. Pipeline de ejemplo (producción)

**Arquitectura ejemplo**:
Device → Edge (MFCC + CBOR) → Broker EMQX (TLS, shared subscriptions) → Workers (consumers) → **Telegraf (mqtt_consumer)** → **InfluxDB** → **Grafana** (live dashboards).

**Ventajas**:

* Telegraf simplifica ingestión desde MQTT y envío a InfluxDB.
* Shared subscriptions permiten escalar consumidores de análisis.
* InfluxDB / Grafana para visualización y almacenamiento temporal.

---

# 12. Checklist de buenas prácticas (rápido)

* [ ] Diseñar *frame size* y *buffering* para tu presupuesto de latencia.
* [ ] Preferir **features** en edge para ahorrar ancho de banda (MFCC, espectrogramas reducidos).
* [ ] Serializar con **Protobuf** o **CBOR** para payloads binarios compactos.
* [ ] Usar **TLS** + autenticación robusta (preferible mTLS o tokens con expiración).
* [ ] Balancear carga con **shared subscriptions** y monitorizar broker (latencia/CPU).
* [ ] Realizar pruebas de carga con patrones heterogéneos (mezcla de mensajes pequeños y grandes).

---

# 13. Limitaciones, riesgos y trabajos futuros

* **No determinismo estricto**: MQTT no sustituye a protocolos de baja latencia determinista (RTP/WebRTC) para audio interactivo.
* **Broker como punto único**: a menos que tengas cluster/replicación/bridge, el broker es punto de fallo — prediseña alta disponibilidad.
* **Pérdida de contexto por compresión**: al enviar solo features, podrías perder información útil para algunos tipos de análisis; mantén muestras temporales de raw para retraining.

---

# 14. Referencias (APA)

> Las entradas incluyen enlaces a los recursos técnicos más relevantes usados en este documento.

* OASIS. (2019). *MQTT Version 5.0* (OASIS Standard). Recuperado de [https://www.oasis-open.org/standard/mqtt-v5-0-os/](https://www.oasis-open.org/standard/mqtt-v5-0-os/).
* HiveMQ Team. (2024, March 6). *TLS/SSL - MQTT Security Fundamentals*. HiveMQ. Recuperado de [https://www.hivemq.com/blog/mqtt-security-fundamentals-tls-ssl/](https://www.hivemq.com/blog/mqtt-security-fundamentals-tls-ssl/).
* HiveMQ Team. (s.f.). *MQTT 5 Essentials — Shared Subscriptions; Session & Message Expiry; Topic Alias* (varios artículos). HiveMQ. Recuperado de [https://www.hivemq.com/blog/](https://www.hivemq.com/blog/).
* Valin, J., Maxwell, G., Vos, K., Terriberry, T., & Perrin, M. (2012). *RFC 6716 — Definition of the Opus Audio Codec*. IETF. Recuperado de [https://datatracker.ietf.org/doc/html/rfc6716](https://datatracker.ietf.org/doc/html/rfc6716).
* EMQX. (2025). *MQTT 5.0: 7 New Features and a Migration Checklist*. EMQX Blog. Recuperado de [https://www.emqx.com/en/blog/introduction-to-mqtt-5](https://www.emqx.com/en/blog/introduction-to-mqtt-5).
* Banno, R. (2023). *Performance Evaluation of MQTT Communication with Heterogeneous Traffic* (IEEE / COMPSAC). Recuperado de [https://www.rbanno.net/data/paper/202306_IEEE_COMPSAC.pdf](https://www.rbanno.net/data/paper/202306_IEEE_COMPSAC.pdf).
* InfluxData. (s.f.). *MQTT Consumer Telegraf Input Plugin*. InfluxData. Recuperado de [https://www.influxdata.com/integration/mqtt-telegraf-consumer/](https://www.influxdata.com/integration/mqtt-telegraf-consumer/).
* RFC 8949 (IETF). (2020). *Concise Binary Object Representation (CBOR)*. Recuperado de [https://datatracker.ietf.org/doc/html/rfc8949](https://datatracker.ietf.org/doc/html/rfc8949).
* Protocol Buffers. (s.f.). *Overview*. Google Developers. Recuperado de [https://protobuf.dev/overview/](https://protobuf.dev/overview/).
* Edge AI / Feature Extraction papers & reviews (selección): AI Flow at the Network Edge (2024), Compression-at-the-Edge audio studies (2025), y revisiones sobre extracción de features (varios). Estas referencias técnicas apoyan la recomendación de realizar feature extraction en edge para ahorro de ancho de banda y energía.

---
