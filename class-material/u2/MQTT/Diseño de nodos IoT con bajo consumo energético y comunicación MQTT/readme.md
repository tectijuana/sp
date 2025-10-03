--- 
# Jorge Luis Castro Alvarado
2 PM
---
# Diseño de nodos IoT con bajo consumo energético y comunicación MQTT

## Introducción
El Internet de las Cosas (IoT) está revolucionando sectores como la agricultura, la logística, la salud, las ciudades inteligentes y el monitoreo ambiental. Sin embargo, uno de los mayores retos para la adopción masiva de dispositivos es la **autonomía energética**.  
Un nodo IoT debe funcionar durante meses o incluso años sin intervención humana, lo que reduce costos de mantenimiento y permite despliegues en entornos remotos. Para lograrlo, se requiere un **diseño integral** que combine:

1. **Hardware de ultra bajo consumo**  
2. **Software optimizado para eficiencia energética**  
3. **Protocolos de comunicación ligeros, como MQTT**  

---

## 1. Arquitectura de Hardware de Mínimo Consumo
El hardware es la base de la eficiencia energética. Cada componente del nodo debe seleccionarse considerando su impacto en el consumo.

### 1.1. Componentes principales
- **Microcontrolador (MCU):** es el cerebro del nodo. Se debe priorizar MCUs con múltiples modos de sueño y tiempos rápidos de despertar (ej. ESP32, STM32L4, nRF52, PSoC 6).  
- **Módulos de comunicación:**  
  - *Wi-Fi*: alto ancho de banda, pero elevado consumo. Útil en transmisiones poco frecuentes.  
  - *Bluetooth Low Energy (BLE):* muy eficiente para comunicaciones cortas.  
  - *LPWAN (LoRaWAN, NB-IoT):* ideal para sensores remotos de bajo tráfico de datos.  
- **Sensores y actuadores:** deben permitir apagado o estados de bajo consumo cuando no están en uso.  
- **Sistema de alimentación:** la elección de reguladores de voltaje y baterías es crítica; la corriente de reposo (Iq) puede llegar a ser el mayor consumidor de energía si no se selecciona correctamente.

### 1.2. Selección de MCU de bajo consumo
- **Criterios:** consumo en reposo, modos de sueño, eficiencia al despertar, memoria integrada y periféricos autónomos (ej. DMA).  
- **Ejemplos:**  
  - *ESP32*: popular y versátil.  
  - *MSP430*: diseñado para consumo ultrabajo.  
  - *PSoC 6*: arquitectura dual-core para gestión granular de energía.  

---

## 2. Estrategias de Software para la Optimización Energética
El firmware debe estar diseñado para que el dispositivo pase la mayor parte del tiempo en **reposo**.

### 2.1. Ciclo de trabajo
El modelo más eficiente es: **Despertar → Medir → Procesar/Transmitir → Dormir**.  
Este patrón minimiza tanto el tiempo como la intensidad de consumo.

### 2.2. Modos de sueño profundo
Ejemplo con ESP32:  
- **Modem-Sleep:** CPU activa, radio apagada.  
- **Light-Sleep:** CPU suspendida, RAM retenida, consumo en miliamperios.  
- **Deep-Sleep:** CPU y periféricos apagados, solo RTC activo (10-150 µA).  
- **Hibernación:** consumo mínimo (<5 µA), solo temporizador de despertar.  

En *deep sleep*, el reinicio es total, por lo que el estado debe guardarse en memoria RTC o almacenamiento persistente.

### 2.3. Gestión eficiente de periféricos y código
- Apagar explícitamente módulos de radio y sensores.  
- Optimizar algoritmos y evitar procesos innecesarios.  
- **Batching de datos:** agrupar varias lecturas antes de transmitir, reduciendo el número de reconexiones y el tiempo de radio activa.

---

## 3. MQTT como protocolo de comunicación eficiente
### 3.1. Fundamentos
- **Modelo publicar/suscribir (Pub/Sub):** los nodos publican mensajes en temas, y los suscriptores los reciben a través de un *broker*.  
- **Ventajas:** bajo consumo de ancho de banda, encabezados mínimos (2 bytes), simplicidad en dispositivos con recursos limitados.  

### 3.2. Configuración eficiente
- **QoS:**  
  - *QoS 0:* más eficiente, adecuado para telemetría periódica.  
  - *QoS 1:* mayor fiabilidad, recomendado para comandos críticos.  
  - *QoS 2:* entrega exacta, pero muy costoso energéticamente.  
- **Keep Alive:** establecer intervalos largos para evitar reconexiones innecesarias.  
- **Sesiones persistentes:** (Clean Session = false) para conservar suscripciones y evitar gastos extra al reconectar.  
- **Last Will and Testament (LWT):** permite detectar desconexiones inesperadas de nodos.  

### 3.3. Comparación con otros protocolos
- **HTTP:** ineficiente en IoT, consumo alto debido a encabezados y conexiones repetidas.  
- **CoAP:** ligero y basado en UDP, pero requiere manejo de fiabilidad en la aplicación. MQTT es más maduro y confiable.

---

## 4. Implementación práctica y seguridad
### 4.1. Caso de estudio: ESP32 con MQTT
Un nodo con ESP32 puede:  
1. Conectarse a Wi-Fi.  
2. Enviar lecturas de sensores a un broker MQTT.  
3. Entrar en *deep sleep*.  
La lógica se concentra en `setup()`, ya que tras cada despertar el MCU reinicia.

### 4.2. Seguridad con TLS
- MQTT por sí solo no cifra datos, por lo que se recomienda **MQTTS (MQTT sobre TLS)**.  
- **Costo energético:** el *handshake TLS* inicial es muy demandante.  
- **Solución:** usar **reanudación de sesión TLS**, evitando repetir el costoso proceso criptográfico en cada ciclo.

---

## Conclusión
El diseño de nodos IoT de bajo consumo energético y comunicación MQTT requiere una visión holística que integre:

- **Hardware:** selección de MCUs de ultra bajo consumo, sensores apagables y reguladores eficientes.  
- **Software:** ciclos de trabajo optimizados, uso intensivo de *deep sleep*, y gestión cuidadosa de periféricos.  
- **MQTT:** configuraciones ajustadas (QoS, Keep Alive, sesiones persistentes) para reducir la sobrecarga en las reconexiones.  
- **Seguridad:** implementación de TLS con reanudación de sesión para proteger datos sin comprometer la batería.  

Un nodo bien diseñado puede operar durante años con una sola batería, equilibrando **autonomía, eficiencia y seguridad** en entornos IoT.

---

## Fuente
Este resumen se basa en el documento:  
**Diseño de Nodos IoT con Bajo Consumo Energético y Comunicación MQTT** (2025).  
[Documento completo aquí](https://www.globalstar.com/getmedia/68f9aab4-3c7f-4caf-918a-c7f49a921a06/ebook-beyond-power-constraints-es.pdf?ext=.pdf)
