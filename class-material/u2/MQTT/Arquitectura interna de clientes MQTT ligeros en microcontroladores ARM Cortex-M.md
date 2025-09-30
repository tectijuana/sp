# Arquitectura interna de clientes MQTT ligeros en microcontroladores ARM Cortex-M-------Lopez Calvillo Angel Ivan

## Introducción
El **Internet de las Cosas (IoT)** requiere protocolos de comunicación que sean eficientes en consumo de recursos, seguros y de bajo ancho de banda. Uno de los protocolos más utilizados es **MQTT (Message Queuing Telemetry Transport)**, diseñado para entornos con recursos limitados y comunicaciones poco confiables.  

En el caso de los **microcontroladores ARM Cortex-M**, su uso resulta ideal debido a que estos dispositivos suelen contar con recursos reducidos (RAM, almacenamiento y capacidad de procesamiento), por lo que requieren clientes MQTT ligeros optimizados para estas condiciones.

Este documento analiza la arquitectura interna de los clientes MQTT ligeros en microcontroladores ARM Cortex-M.

---

## Características de los microcontroladores ARM Cortex-M
Los microcontroladores de la familia **Cortex-M** son ampliamente usados en aplicaciones embebidas por su:
- **Bajo consumo energético.**
- **Alto rendimiento en tareas de control.**
- **Soporte de interrupciones y periféricos integrados.**
- **Memoria limitada** (en algunos casos desde 64 KB de RAM).
- Compatibilidad con **RTOS** (como FreeRTOS, Zephyr) o ejecución en **bare-metal**.

Estas características hacen necesario implementar un cliente MQTT optimizado y modular.

---

## MQTT ligero: Conceptos básicos
- **Modelo de publicación/suscripción.**
- **Broker** como punto central de comunicación.
- **Mensajes pequeños** en formato binario.
- **Calidad de Servicio (QoS)** ajustable: 0 (al menos una vez), 1 (una vez) y 2 (exactamente una vez).
- **Encabezado mínimo** para optimizar ancho de banda.

---

## Arquitectura interna de un cliente MQTT ligero
Un cliente MQTT ligero para ARM Cortex-M debe optimizar **uso de memoria, procesamiento y energía**. Su arquitectura suele incluir:

### 1. Capa de Red
- Implementación de **TCP/IP ligero** (usualmente con **lwIP** u otros stacks embebidos).
- Manejo de **sockets no bloqueantes**.
- Opcionalmente, soporte de **TLS/DTLS** para seguridad (aunque consume más recursos).

### 2. Capa MQTT
- **Gestor de Conexiones**: maneja establecimiento, mantenimiento y reconexión con el broker.
- **Codificador/Decodificador de Paquetes**: serializa y deserializa mensajes MQTT (CONNECT, PUBLISH, SUBSCRIBE, etc.).
- **Gestión de Sesión**: almacenamiento de topics y QoS pendientes.
- **Cola de Mensajes**: buffer mínimo para manejar mensajes entrantes y salientes.

### 3. Interfaz de Aplicación
- **API simplificada** para publicar y suscribirse.
- Callbacks para eventos de red (mensaje recibido, desconexión).
- Manejo de **timeouts y watchdogs** para asegurar confiabilidad.

### 4. Optimización de Recursos
- Uso de **buffers estáticos** en lugar de dinámicos.
- Configuración de **límite de topics y conexiones simultáneas**.
- Opcional: integración con **RTOS** para multitarea, o ejecución en bucle principal (bare-metal).

---

## Implementaciones comunes de clientes MQTT ligeros
Algunas bibliotecas adaptadas a microcontroladores ARM Cortex-M incluyen:
- **Eclipse Paho Embedded MQTT**: cliente ligero en C optimizado para sistemas embebidos.
- **MQTT-C**: cliente escrito en C ANSI con bajo consumo de memoria.
- **lwMQTT**: diseñado específicamente para plataformas con recursos reducidos.
- **Mbed MQTT**: integración con Mbed OS y microcontroladores ARM.

---

## Casos de uso
- **Sensores IoT** que transmiten datos periódicos (temperatura, humedad, presión).
- **Dispositivos de automatización industrial** con conectividad inalámbrica.
- **Wearables y dispositivos médicos** que requieren comunicación confiable con bajo consumo de energía.

---

## Conclusiones
Los clientes MQTT ligeros en **microcontroladores ARM Cortex-M** permiten implementar sistemas IoT eficientes y confiables, gracias a una arquitectura modular que balancea **bajo consumo de recursos** con **conectividad robusta**.  
La clave está en la optimización de memoria, el manejo eficiente de la red y el soporte de calidad de servicio ajustable según las necesidades de la aplicación.

---

## Referencias
- Banks, A., Gupta, R., & Briggs, E. (2019). *MQTT Version 5.0*. OASIS Standard.  
- Eclipse Foundation. (2023). *Paho Embedded MQTT Client*. Recuperado de https://www.eclipse.org/paho  
- ARM. (2022). *Cortex-M processors*. Recuperado de https://developer.arm.com/  
- Dinculeană, D. (2018). *An Overview of MQTT for IoT*. *Informatica Economica*, 22(1), 47–54.  
