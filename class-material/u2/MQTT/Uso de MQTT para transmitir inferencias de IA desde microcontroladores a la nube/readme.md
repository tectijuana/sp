# Revisión de herramientas para inferencia de IA en microcontroladores con MQTT
- Materia: Sistemas Programables
- Carrera: Ingeniería en Sistemas Computacionales
- Estudiante: Bautista Lagunas Jose Daniel
- No. Control: 22211527

---
## MQTT como eje de comunicación inteligente

La convergencia entre el Internet de las Cosas (IoT) y la Inteligencia Artificial (IA), especialmente con la irrupción de modelos ligeros (TinyML) y modelos de lenguaje extensos (LLMs), ha impulsado un nuevo paradigma: dispositivos físicos que no solo miden el entorno, sino que también **razonan localmente y comunican sus inferencias en tiempo real** hacia la nube. En este contexto, **MQTT (Message Queuing Telemetry Transport)** se consolida como el protocolo ideal para integrar microcontroladores con servicios de IA distribuidos.

MQTT fue diseñado para entornos con recursos limitados, redes intermitentes y alta dispersión geográfica. Su arquitectura **publicador/suscriptor (pub/sub)** desacopla completamente a los dispositivos que generan datos (publicadores) de los que los procesan (suscriptores), permitiendo escalar sistemas sin modificar el firmware de cada sensor.  
Características como **bajo overhead**, **mensajes retenidos**, **niveles de calidad de servicio (QoS)** y **reconexión automática** lo hacen especialmente adecuado para aplicaciones de inferencia o respuesta instantánea, donde los datos deben procesarse apenas llegan sin depender de ciclos de consulta.  

En un flujo típico, **los sensores publican datos (telemetría, estado o eventos)**, los **servicios de IA/LLM suscritos procesan la información**, y luego publican sus resultados o decisiones en tópicos de retorno (por ejemplo, `alerts/deviceID`). Esta dinámica **event-driven** habilita la interacción continua entre el entorno físico y los modelos inteligentes.  

### Arquitectura general

1. **Microcontroladores y sensores (publicadores):** ejecutan mediciones o inferencias locales y envían resultados vía MQTT.  
2. **Gateways de borde:** filtran o agregan datos antes de publicarlos a la nube, optimizando tráfico y latencia.  
3. **Broker MQTT (local o en nube):** enruta mensajes entre los distintos actores del sistema.  
4. **Servicios IA/LLM (suscriptores):** procesan los datos entrantes, ejecutan inferencia o razonamiento y publican respuestas.  
5. **Actuadores o sistemas downstream:** reciben los resultados (alertas, comandos, predicciones) y ejecutan acciones en el entorno físico.

Gracias a esta estructura, **nuevos modelos o módulos de IA pueden añadirse sin reprogramar los dispositivos**, lo que favorece la escalabilidad y la evolución tecnológica.

---

## Inferencia de IA en microcontroladores: herramientas y casos prácticos

En el ámbito del **TinyML**, varias herramientas permiten ejecutar modelos de IA directamente en microcontroladores y comunicarse por MQTT con la nube o brokers intermedios.

---

### TensorFlow Lite for Microcontrollers (TFLM)

**TensorFlow Lite Micro** permite desplegar modelos de IA cuantizados (por ejemplo, int8) en microcontroladores como el **ESP32**, ejecutando inferencia local sin requerir un sistema operativo. Aunque no incluye nativamente MQTT, puede integrarse con librerías como **esp-mqtt** o **lwIP MQTT**, enviando solo los resultados al broker.  
Ejemplos prácticos incluyen **monitoreo de baterías inteligentes** o **detección de anomalías**, donde la inferencia local genera una alerta que se publica mediante MQTT. Esta estrategia reduce drásticamente el tráfico y mejora la latencia.

**Ventajas:**
- Baja latencia al ejecutar inferencia en el borde.  
- Menor consumo de red (solo se transmiten resultados).  

**Desafíos:**
- Limitación de memoria (requiere cuantización).  
- Implementación manual del cliente MQTT y de la seguridad TLS.

---

### Edge Impulse

**Edge Impulse** ofrece un entorno completo de desarrollo TinyML: adquisición de datos, entrenamiento, optimización y despliegue en hardware.  
Aunque no integra MQTT de forma nativa, numerosos proyectos lo emplean para **publicar resultados de inferencia** a través de brokers locales o servicios como **AWS IoT Core**. Por ejemplo, se han implementado soluciones con **Arduino Nano 33 IoT** o **ESP32**, donde Edge Impulse realiza la inferencia y MQTT envía los resultados a dashboards o sistemas de automatización.

**Ventajas:**
- Despliegue rápido y soporte multiplataforma.  
- Actualización OTA de modelos y runners.  

**Desafíos:**
- Adaptar el cliente MQTT al SDK del dispositivo.  
- Gestión de compatibilidad entre versiones del modelo.

---

### Otras herramientas emergentes

Frameworks como **MicroAI** y **MCUNet** buscan optimizar el rendimiento de modelos en microcontroladores aún más pequeños mediante **búsqueda automática de arquitecturas (NAS)** y **motores de inferencia especializados (TinyEngine)**.  
Estos enfoques pueden combinarse con MQTT para enviar inferencias más precisas o compactas a la nube, permitiendo una jerarquía de IA: **inferencias rápidas en el borde + razonamiento profundo en la nube**.

---

## Casos de uso combinando MQTT e inferencia de IA

- **Manufactura inteligente:** sensores publican datos de vibración o temperatura; modelos TinyML locales detectan anomalías y publican alertas MQTT que un servicio en la nube verifica o amplía.  
- **Vehículos definidos por software:** módulos embebidos usan IA local para diagnóstico y transmiten conclusiones por MQTT hacia servicios de mantenimiento predictivo.  
- **Hogar inteligente:** dispositivos con ESP32 y modelos de detección local publican comandos o eventos para asistentes basados en LLM (como control de voz).  
- **Salud y energía:** wearables o medidores publican inferencias (frecuencia cardíaca anómala, sobrecarga eléctrica) que una capa IA supervisa y actúa en tiempo real.

---

## Desafíos técnicos y evolución

- **Latencia y rendimiento:** la conversión de datos y la publicación MQTT deben optimizarse para no generar cuellos de botella.  
- **Seguridad:** es esencial usar MQTT con **TLS, autenticación fuerte y control de tópicos** para evitar accesos indebidos.  
- **Gestión de modelos (OTA):** se requieren mecanismos seguros para actualizar modelos en dispositivos remotos.  
- **Estandarización de mensajes:** el uso de formatos ligeros como **CBOR o Protobuf** permite transmitir inferencias de forma eficiente.  
- **Brokers inteligentes:** propuestas como **MQTT+** introducen procesamiento y filtrado directamente en el broker, reduciendo carga en los microcontroladores.  

En el futuro, se espera que MQTT evolucione hacia un **protocolo de comunicación entre agentes de IA**, gracias a las nuevas funciones del estándar **MQTT 5**, que facilitan respuestas directas (request–reply) y colaboración entre modelos o servicios distribuidos

El uso combinado de **TinyML y MQTT** constituye la base para sistemas de **inteligencia distribuida**: los microcontroladores procesan información localmente y envían inferencias mediante un canal ligero, eficiente y escalable hacia servicios de IA o LLM en la nube.  
Herramientas como **TensorFlow Lite Micro**, **Edge Impulse** y nuevos frameworks optimizados habilitan esta simbiosis entre hardware embebido e inteligencia conectada. Con el respaldo de MQTT como columna vertebral de mensajería, estos sistemas logran integrar **eficiencia energética, baja latencia y comunicación inteligente**, marcando un paso clave hacia el IoT cognitivo del futuro.

---

### Referencias

1. MQTT.org. *MQTT Version 5.0 Specification*. [https://mqtt.org](https://mqtt.org)  
2. Google TensorFlow. *TensorFlow Lite for Microcontrollers*. [https://www.tensorflow.org/lite/microcontrollers](https://www.tensorflow.org/lite/microcontrollers)  
3. Edge Impulse Documentation. *Deploying Machine Learning Models on Embedded Devices*. [https://docs.edgeimpulse.com](https://docs.edgeimpulse.com)  
4. MicroAI. *Edge-native Machine Learning for IoT*. [https://micro.ai](https://micro.ai)  
5. Lin, J. et al. (2021). *MCUNet: Tiny Deep Learning on IoT Devices*. MIT CSAIL.  
6. AWS IoT Core. *Integrating MQTT with AI Workloads*. [https://aws.amazon.com/iot-core](https://aws.amazon.com/iot-core)



