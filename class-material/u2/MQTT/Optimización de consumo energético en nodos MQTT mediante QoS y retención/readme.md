**Autor:** Ivan Gustavo Mendoza Suarez   
**No. Control:** 22210910   
**Nota:** *Investigación realizada con apoyo parcial de ChatGPT (GPT-5)*  

---

# 📡 Optimización de consumo energético en nodos MQTT mediante QoS y Retención

## 🔎 Introducción

En entornos de **Internet de las Cosas (IoT)**, el consumo energético es un factor crítico, especialmente en **nodos con recursos limitados** (sensores, actuadores, dispositivos alimentados por baterías).  
El protocolo **MQTT (Message Queuing Telemetry Transport)**, diseñado para comunicaciones livianas, ofrece mecanismos como los **niveles de Calidad de Servicio (QoS)** y la **retención de mensajes** que impactan directamente en el **uso eficiente de energía**.

Esta investigación analiza cómo estas características pueden optimizar el consumo energético en dispositivos IoT.

---

## ⚡ Relevancia del Consumo Energético en IoT

- La mayoría de los nodos IoT operan con **energía limitada** (baterías, energía solar, supercondensadores).  
- Reducir el **número de transmisiones** y **reintentos de comunicación** prolonga la vida útil del nodo.  
- MQTT, al trabajar sobre **TCP/IP**, requiere un balance entre **fiabilidad** y **eficiencia energética**.

---

## 🛠️ MQTT y Calidad de Servicio (QoS)

MQTT define tres niveles de **QoS (Quality of Service)**:

1. **QoS 0 – At most once ("como máximo una vez")**
   - El mensaje se envía **sin confirmación**.  
   - Menor consumo energético.  
   - Riesgo: pérdida de mensajes en caso de fallo de red.  
   - Ideal para sensores de bajo costo donde la pérdida de datos no es crítica (ej. temperatura en intervalos regulares).

2. **QoS 1 – At least once ("al menos una vez")**
   - El mensaje se entrega **con confirmación del broker**.  
   - Mayor consumo de energía por retransmisiones.  
   - Adecuado para datos relevantes donde la pérdida parcial no es aceptable.

3. **QoS 2 – Exactly once ("exactamente una vez")**
   - El nivel más seguro pero el más costoso energéticamente.  
   - Requiere múltiples intercambios entre cliente y broker.  
   - Usado solo en sistemas críticos donde la **duplicación o pérdida de datos es inaceptable** (ej. control médico).

📊 **Impacto energético:**  
- **QoS 0** consume menos energía, pero con baja confiabilidad.  
- **QoS 2** asegura integridad, pero puede agotar más rápido la batería.  
- **QoS 1** representa un **balance intermedio**.

---

## 🗂️ Retención de Mensajes en MQTT

- La opción **"Retained Message"** permite al broker guardar el último valor publicado en un tópico.  
- Cuando un nuevo cliente se suscribe, recibe **inmediatamente el último mensaje retenido**, sin necesidad de que el publicador esté activo.

🔋 **Ventajas en consumo energético:**
- Los nodos publicadores pueden **entrar en modo de bajo consumo** después de enviar un dato retenido.  
- Evita que múltiples clientes requieran datos redundantes.  
- Reduce la necesidad de **transmisiones periódicas innecesarias**.

Ejemplo:  
Un sensor de **estado ON/OFF** envía un mensaje retenido. Los nuevos clientes conocerán el estado actual sin necesidad de que el sensor vuelva a transmitir constantemente.

---

## 📊 Estrategias de Optimización

1. **Usar QoS según la criticidad del dato:**
   - Sensores ambientales → **QoS 0**.  
   - Alertas de seguridad → **QoS 1**.  
   - Aplicaciones críticas de control → **QoS 2** solo cuando sea indispensable.

2. **Aplicar Retained Messages en datos estáticos o de estado:**
   - Estados binarios (ON/OFF).  
   - Última medición de sensores que cambian lentamente.  

3. **Combinar Retención + QoS bajo:**
   - Publicar con **QoS 0 + Retain** puede ser suficiente para muchos casos de monitoreo, reduciendo drásticamente el consumo.

4. **Optimización del ciclo de actividad del nodo:**
   - Publicar → Retener → Entrar en **modo sleep**.  
   - Solo despertar cuando un valor cambia o en intervalos programados.

---

## 📉 Limitaciones y Riesgos

- **QoS bajo + Retain** puede generar **datos obsoletos** si el nodo muere sin actualizar el mensaje.  
- El uso excesivo de **QoS 2** degrada la vida útil de baterías.  
- Retained Messages mal gestionados pueden ocasionar **inconsistencias** en sistemas de control.

---

## ✅ Conclusión

La combinación de **QoS adecuado** y el uso estratégico de **retained messages** en MQTT representa una de las formas más efectivas de **optimizar el consumo energético en nodos IoT**:

- **QoS 0 + Retain**: excelente balance entre eficiencia y disponibilidad de datos.  
- **QoS 1**: recomendado para información importante pero no crítica.  
- **QoS 2**: reservar únicamente para sistemas altamente sensibles.

En definitiva, **la clave está en adaptar QoS y Retención al tipo de aplicación**, logrando así **comunicaciones confiables y eficientes** sin comprometer la energía disponible en los dispositivos.

---

## 🖼️ Imagen Representativa

![Consumo energético MQTT vs HTTP](https://www.mdpi.com/sensors/sensors-23-04896/article_deploy/html/images/sensors-23-04896-g006.png)

---

## 📚 Referencias

- OASIS MQTT Specification v5.0 (2019).  
- Hunkeler, U., Truong, H. L., & Stanford-Clark, A. (2008). *MQTT-S — A publish/subscribe protocol for Wireless Sensor Networks*.  
- Naik, N. (2017). *Choice of effective messaging protocols for IoT systems: MQTT, CoAP, AMQP and HTTP*. IEEE Systems Engineering Symposium.
