# DANIEL ROMERO BRAVO

```text
Asistencia de IA: El usuario fue apoyado con la asistencia para acomodar las referencias en APA 
y realizar correcciones ortográficas, ajustes de redacción y obtener unas fuentes de información.
Herramienta: ChatGPT (GPT-5 Thinking mini)
Fecha: 30 de septiembre de 2025
Plataforma de hardware utilizada: N/A
```
# Persistencia de datos y sesiones en MQTT para sistemas con memoria limitada

## Resumen

En entornos con memoria limitada (microcontroladores, dispositivos *edge*), diseñar la persistencia de datos y el manejo de sesiones en MQTT requiere equilibrar fiabilidad (entrega de mensajes, recuperación tras desconexión) con restricciones físicas: tamaño de RAM/flash, *endurance* de memoria no volátil, consumo de energía y latencias de escritura/erase.  

Las decisiones clave incluyen:  

- Cuándo confiar en la persistencia en el broker (sesiones persistentes, mensajes retenidos y colas de entrega).  
- Cuándo mantener colas locales en el dispositivo (flash circular, SQLite ligero, buffers en RAM).  
- Cómo usar QoS y *retained messages* para reducir sobrecarga.  
- Cómo usar las opciones de MQTT v5 (Session Expiry, Message Expiry) para controlar el estado retenido por el broker.  
([HiveMQ](https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/); [HiveMQ - MQTT5](https://www.hivemq.com/blog/mqtt5-essentials-part4-session-and-message-expiry/))

---

## Conceptos esenciales y definiciones

### Sesión persistente / Clean Start (MQTT v3.1.1 vs MQTT 5)

- **Sesión persistente**: si el cliente se conecta con `cleanSession=false` (v3) o `Clean Start=0` + *Session Expiry Interval* apropiado (v5), el broker guarda las suscripciones y las colas de mensajes pendientes para entregarlos cuando el cliente vuelva a conectarse. Útil para dispositivos que se desconectan con frecuencia.  
([HiveMQ](https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/); [HiveMQ - MQTT5](https://www.hivemq.com/blog/mqtt5-essentials-part4-session-and-message-expiry/))  

- **Clean Start / Clean Session**: crear una sesión nueva y descartar el estado anterior — reduce carga en broker pero pierde mensajes enviados durante la desconexión. En MQTT v5 se controla con *Clean Start* + *Session Expiry Interval*.

---

### Retained messages (mensajes retenidos)

Un mensaje publicado con `retain = 1`.  

- El broker guarda el último mensaje retenido por tópico.  
- Lo entrega inmediatamente a nuevos suscriptores del tópico.  
- No es equivalente a la cola de mensajes pendientes para clientes *offline* (QoS 1/2).  
- Es una forma simple de almacenar el “estado actual” de un tópico.  
- La persistencia del *retained* depende de cómo el broker guarda sus datos (memoria vs disco).  ([Cedalo](https://cedalo.com/blog/mqtt-retained-messages-explained/))

<img width="662" height="240" alt="image" src="https://github.com/user-attachments/assets/f60bdc6c-2842-4f2b-9dbd-3b857dbec91c" />

---

### QoS y entrega para clientes *offline*

- **QoS 0**: mejor esfuerzo, no persistencia.  
- **QoS 1**: entrega al menos una vez; el broker almacena `PUBLISH` hasta recibir `PUBACK` del suscriptor (para sesiones persistentes y clientes *offline*).  
- **QoS 2**: entrega exactamente una vez; implica más estado y *handshake* adicional.  

La selección de QoS es un equilibrio entre fiabilidad y almacenamiento/estado en el broker.

---

## ¿Qué hace el broker y qué hace el dispositivo?

### Broker (ideal)

- Mantiene sesiones persistentes, colas de mensajes (para QoS ≥1) y mensajes retenidos.  
- La administración de sesiones en el broker reduce la complejidad del dispositivo, pero impone requerimientos de almacenamiento en el broker.  
- Configurar la persistencia en brokers como **Mosquitto, EMQX, HiveMQ** es crítico.  
([PageFault](https://pagefault.blog/2020/02/05/how-to-set-up-persistent-storage-for-mosquitto-mqtt-broker/); [EMQX](https://www.emqx.com/en/blog/the-easiest-guide-to-getting-started-with-mqtt))

### Dispositivo (memorias limitadas)

- Mantener una cola local pequeña y persistente (log circular en flash o archivo SQLite reducido).  
- Persistir solo metadatos esenciales (ID de cliente, contadores de mensajes pendientes, último ACK por tópico).  
- Evitar confiar únicamente en broker cuando hay pérdida frecuente de conectividad o riesgo de borrado de sesiones.

---

## Impacto de la memoria limitada

Problemas comunes:  

- **Endurance**: escrituras constantes en Flash/EEPROM reducen la vida útil.  
- **Latencias de escritura**: afectan el rendimiento en tiempo real.  
- **Capacidad**: obliga a purgar, compactar logs o usar compresión ligera.  
- **Consumo de energía**: escrituras en memoria no volátil gastan más energía, crítico en dispositivos a batería.
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/2c944c3e-597e-4dfc-8075-5e7fc594034f" />

---

## Técnicas y patrones recomendados

1. **Política híbrida**: persistencia local mínima + sesiones en broker.  
   - Guardar en el dispositivo solo lo necesario para reintentos inmediatos.  
   - Usar *Session Expiry Interval* en MQTT v5 para limitar cuánto tiempo el broker retiene el estado.  
   ([HiveMQ - MQTT5](https://www.hivemq.com/blog/mqtt5-essentials-part4-session-and-message-expiry/))

2. **Selección inteligente de QoS**  
   - Telemetría poco crítica → QoS 0.  
   - Comandos críticos → QoS 1 o QoS 2.  

3. **Uso de retained messages para “estado”**  
   - Publicar estado actual del dispositivo con `retain=1`.  
   - Evitar usarlo para lecturas frecuentes.  
   ([Cedalo](https://cedalo.com/blog/mqtt-retained-messages-explained/))

4. **Batching y compresión**  
   - Agrupar lecturas pequeñas en un solo mensaje.  
   - Usar compresión ligera si el procesador lo permite.  

5. **Cola circular en flash + checksum**  
   - Implementar log circular con índices en RAM.  
   - Reintentar publicaciones en orden tras reconexión.  

6. **Base de datos embebida ligera**  
   - SQLite, littlefs, o un archivo binario simple.  

7. **Control de expiración (Message Expiry Interval)**  
   - Configurar en MQTT v5 para que mensajes pendientes caduquen.  
   ([HiveMQ - MQTT5](https://www.hivemq.com/blog/mqtt5-essentials-part4-session-and-message-expiry/))

8. **Monitoreo y límites en broker**  
   - Configurar `persistence true` y `max_queued_messages` en Mosquitto.  
   - Validar si la persistencia es en disco o solo en memoria.  
   ([PageFault](https://pagefault.blog/2020/02/05/how-to-set-up-persistent-storage-for-mosquitto-mqtt-broker/))

---

## Estrategia práctica de implementación

1. Definir requisitos de fiabilidad.  
2. Elegir política de sesión (*Session Expiry Interval*).  
3. Dimensionar buffer local (N mensajes o T segundos).  
4. Decidir entre retained vs queued.  
5. Reintentar publicaciones en reconexión y eliminar tras ACK.  
6. Establecer límites (máx mensajes, máx reintentos).  
7. Probar con fallos (reinicios, desconexiones largas).  

---

## Medición y *benchmarking* sugeridos

- **Latencia de persistencia local**: medir tiempo por escritura en flash.  
- **Jitter**: verificar impacto en interrupciones periódicas.  
- **Endurance**: calcular ciclos/día y vida útil de memoria.  
- **Pruebas en broker**: simular desconexiones largas, medir retención de mensajes y expiración.  

---

## Ejemplos y notas sobre brokers

- **Mosquitto**: requiere `persistence true` y `persistence_file` para sesiones en disco. ([PageFault](https://pagefault.blog/2020/02/05/how-to-set-up-persistent-storage-for-mosquitto-mqtt-broker/))  
- **EMQX / HiveMQ**: soporte completo de MQTT v5, permiten políticas de expiración y administración centralizada. ([EMQX](https://www.emqx.com/en/blog/the-easiest-guide-to-getting-started-with-mqtt))  

---

## Consideraciones de seguridad

- No guardar credenciales en texto plano en flash.  
- Usar TLS para proteger sesiones persistentes.  
- Configurar autenticación estricta para prevenir ataques DoS por exceso de sesiones.  

---

## Referencias

- HiveMQ. (s. f.). *MQTT Essentials — Part 7: Understanding Persistent Sessions and Clean Sessions*. HiveMQ. [https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/](https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/)  

- HiveMQ. (s. f.). *MQTT 5 Essentials — Session and Message Expiry*. HiveMQ. [https://www.hivemq.com/blog/mqtt5-essentials-part4-session-and-message-expiry/](https://www.hivemq.com/blog/mqtt5-essentials-part4-session-and-message-expiry/)  

- PageFault blog. (2020, 5 de febrero). *How to set up persistent storage for Mosquitto MQTT broker*. PageFault. [https://pagefault.blog/2020/02/05/how-to-set-up-persistent-storage-for-mosquitto-mqtt-broker/](https://pagefault.blog/2020/02/05/how-to-set-up-persistent-storage-for-mosquitto-mqtt-broker/)  

- Cedalo. (2023, 11 de agosto). *MQTT Retained Messages Explained*. Cedalo Blog. [https://cedalo.com/blog/mqtt-retained-messages-explained/](https://cedalo.com/blog/mqtt-retained-messages-explained/)  

- EMQX. (2025, 26 de febrero). *Mastering MQTT: The Ultimate Beginner's Guide for 2025*. EMQX Blog. [https://www.emqx.com/en/blog/the-easiest-guide-to-getting-started-with-mqtt](https://www.emqx.com/en/blog/the-easiest-guide-to-getting-started-with-mqtt)  
