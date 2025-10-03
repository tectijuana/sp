# 📌 MQTT: Qué es, para qué sirve y cómo funciona

## 🔹 ¿Qué es MQTT?
MQTT (*Message Queuing Telemetry Transport*) es un **protocolo de comunicación ligero** que permite el intercambio de mensajes entre dispositivos de forma rápida y confiable.  

Se caracteriza por:
- Bajo consumo de red y energía (ideal para sensores).
- Fácil de implementar en dispositivos con recursos limitados.
- Ofrece niveles de calidad de servicio (QoS 0, 1 y 2).
- Muy utilizado en **Internet de las Cosas (IoT)** y **Machine to Machine (M2M)**.

---

## 🔹 ¿Cómo funciona?
MQTT utiliza un modelo **publicador/suscriptor (pub/sub)**:

- **Cliente (Publisher):** envía mensajes con datos (ejemplo: sensor de temperatura).  
- **Cliente (Subscriber):** recibe los mensajes si está suscrito al tema correspondiente.  
- **Broker:** servidor central que recibe los mensajes de los publicadores y los entrega a los suscriptores.  
- **Temas (Topics):** etiquetas jerárquicas que clasifican los mensajes, ej:  

---

## 🔹 Ventajas clave
✅ Bajo consumo de ancho de banda y batería.  
✅ Funciona en redes inestables.  
✅ Conexiones persistentes y mensajes retenidos.  
✅ Aviso de desconexiones inesperadas (*Last Will and Testament*).  
✅ Ideal para IoT, automatización industrial, domótica y agricultura.  

---

## 🔹 Ejemplo práctico
📡 Un sensor de temperatura publica en el tema:  

📱 Una aplicación móvil suscrita a ese tema recibe los valores en tiempo real.  

⚠️ Si el sensor se desconecta de golpe, el **broker** puede enviar un aviso automático con un mensaje especial (*Last Will*).  

---


✍️ **Conclusión:**  
MQTT es un protocolo simple, ligero y confiable que conecta sensores, aplicaciones y sistemas de control de manera eficiente. Es una de las tecnologías clave del **Internet de las Cosas**.

# 📚 Bibliografía

- HiveMQ. (2020). *MQTT Essentials - A comprehensive overview of MQTT facts and features for beginners and experts alike*.  
  Disponible en: [https://www.hivemq.com/mqtt-essentials](https://www.hivemq.com/mqtt-essentials)

- HiveMQ. (2021). *MQTT Sparkplug Essentials - Getting Started with this Open IIoT Specification*.  
  Disponible en: [https://www.hivemq.com/mqtt-sparkplug-essentials](https://www.hivemq.com/mqtt-sparkplug-essentials)

- OASIS. (2019). *MQTT Version 5.0 - OASIS Standard*.  
  Disponible en: [https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)

- Stanford-Clark, A., & Nipper, A. (1999). *MQ Telemetry Transport (MQTT) Protocol Specification*. IBM / Arcom.
