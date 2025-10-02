<div align="center">
  
# Comparativa de plataformas para proyectos con MQTT
  
[![IoT](https://img.shields.io/badge/IoT-MQTT-blue)](https://mqtt.org/)
[![ESP32](https://img.shields.io/badge/Platform-ESP32-red)](https://www.espressif.com/)
[![STM32](https://img.shields.io/badge/Platform-STM32-green)](https://www.st.com/)
[![Raspberry Pi](https://img.shields.io/badge/Platform-Raspberry%20Pi-pink)](https://www.raspberrypi.org/)
  
![mqtt_shared_subscriptions_wildcard](https://github.com/user-attachments/assets/980179bf-4927-48de-86b3-02e4d5048b09)

  
</div>

---

## Datos del alumno:
- **Nombre:** Morales Hernandez Christian Gahel
- **Número de control:** 22210323
- **Fecha:** Octubre 01 2025

---

## I. ESP32 + MQTT
Los microcontroladores STM32, de arquitectura ARM Cortex, ofrecen una amplia gama de potencia y recursos según la familia elegida. A diferencia del ESP32, no cuentan con conectividad integrada, por lo que se requiere añadir módulos externos de red (Ethernet, WiFi o celulares) y configurar la pila de red, normalmente con LwIP y FreeRTOS.

El STM32 puede funcionar como cliente MQTT, publicando y recibiendo datos de un broker. Para ello se integran librerías de MQTT embebido adaptadas al entorno, como las versiones ligeras de Paho MQTT. Estos clientes permiten enviar información de sensores o estados de control hacia un broker externo.

Existen ejemplos prácticos donde se configura el microcontrolador para publicar mensajes periódicos a un broker, así como para recibir comandos de control remoto. En entornos de simulación, como Wokwi, es posible emular este comportamiento antes de implementarlo en hardware real.

El STM32 se destaca en aplicaciones que requieren tiempo real y determinismo, donde además del intercambio de mensajes MQTT se deben controlar periféricos de forma precisa. Su mayor reto es la complejidad de integración, ya que el desarrollador debe gestionar tanto la pila de red como las librerías MQTT y los recursos de hardware.

---

## II. STM32 + MQTT
Los microcontroladores STM32, de arquitectura ARM Cortex, ofrecen una amplia gama de potencia y recursos según la familia elegida. A diferencia del ESP32, no cuentan con conectividad integrada, por lo que se requiere añadir módulos externos de red (Ethernet, WiFi o celulares) y configurar la pila de red, normalmente con LwIP y FreeRTOS.

El STM32 puede funcionar como cliente MQTT, publicando y recibiendo datos de un broker. Para ello se integran librerías de MQTT embebido adaptadas al entorno, como las versiones ligeras de Paho MQTT. Estos clientes permiten enviar información de sensores o estados de control hacia un broker externo.

Existen ejemplos prácticos donde se configura el microcontrolador para publicar mensajes periódicos a un broker, así como para recibir comandos de control remoto. En entornos de simulación, como Wokwi, es posible emular este comportamiento antes de implementarlo en hardware real.

El STM32 se destaca en aplicaciones que requieren tiempo real y determinismo, donde además del intercambio de mensajes MQTT se deben controlar periféricos de forma precisa. Su mayor reto es la complejidad de integración, ya que el desarrollador debe gestionar tanto la pila de red como las librerías MQTT y los recursos de hardware.

---

## III. Raspberry Pi + MQTT
La Raspberry Pi funciona como un ordenador de bajo coste con sistema operativo Linux. Gracias a su potencia y conectividad integrada (Ethernet y WiFi en la mayoría de los modelos), puede desempeñar roles tanto de cliente como de servidor.

El uso más habitual es instalar el broker Mosquitto directamente en la Raspberry Pi. Esto se logra con el gestor de paquetes y permite tener un broker MQTT funcional en pocos minutos. Una vez instalado, se puede configurar para aceptar conexiones locales o remotas, habilitar usuarios y contraseñas, y definir parámetros como puertos y seguridad.

Con herramientas como mosquitto_pub y mosquitto_sub es posible realizar pruebas de publicación y suscripción directamente desde la terminal. Además, se integra fácilmente con Node-RED, lo que permite crear flujos visuales para conectar la Raspberry Pi con otros dispositivos como ESP32 o Arduino, y visualizar datos en tiempo real.

Gracias a su sistema operativo completo, la Raspberry Pi puede funcionar como gateway central de un sistema IoT, albergando no solo el broker MQTT sino también bases de datos, dashboards, servidores web y otros servicios que enriquecen el ecosistema. Su principal limitación es el mayor consumo energético y que no es adecuada para tareas de control en tiempo real estricto.

---

### Comparativa hasta ahora

| Plataforma | Lo que muestran las fuentes / ventajas | Limitaciones / retos evidentes |
|------------|----------------------------------------|-------------------------------|
| **ESP32** | Amplio soporte de ejemplos con PubSubClient y AsyncMqttClient; modularización del código; uso de JSON; reconexión automática; ejemplos prácticos con sensores; conexión con brokers públicos | No hay análisis de límites (mensajes por segundo, escalabilidad); no se ve rendimiento bajo carga pesada; manejo de reconexiones requiere cuidado |
| **STM32** | Posibilidad de usar MQTT cliente mediante integración con LwIP/HAL/RTOS; ejemplos comunitarios y foros; simulaciones (Wokwi) permiten probar sin hardware físico | No hay ejemplos completos de broker en STM32; requiere mayor esfuerzo para integrar red y librerías MQTT; menos ejemplos "listos para usar" que ESP32 |
| **Raspberry Pi** | Excelentes guías para instalar Mosquitto broker; configurar clientes; permitir acceso remoto; uso de Node-RED junto con MQTT; pruebas con comandos mosquitto | No se tratan límites de rendimiento, latencia, comportamiento bajo carga, ni comparaciones con MCU |

---

# Versión ampliada / enriquecida

## Información externa destacada (adicional)

- En el foro de ST, usuarios reportan dificultad para conectar STM32F407G con MQTT sobre Ethernet + ENC28J60, con errores como `mqtt_connect return -10`, problemas de desconexión y publicación fallida
- GitHub "eziya/STM32F4_HAL_ETH_MQTT_CLIENT" es un ejemplo concreto de STM32 + FreeRTOS + LwIP + MQTT cliente usando Paho MQTT, adaptado para HAL y ETH
- En STM32F7, intentos de correr un broker MQTT completo directamente en el microcontrolador muestran que las librerías estándar (LwIP/FreeRTOS) solo ofrecen clientes, no servidores broker completos
- En STM32 se pueden usar librerías como **Tuxera MQTT** (implementación comercial/certificada) con soporte TLS y compatibilidad MISRA
- Es común advertir que aunque técnicamente se puede implementar un broker en MCU, el esfuerzo y las limitaciones hacen que se prefiera usar dispositivos Linux (como Raspberry Pi) como brokers principales
  > "MQTT is designed to be small on the client side, but can be quite demanding on the broker side … you can get some simple, small server running on an STM32, but it may not be worth the effort."
- Para ESP32, Random Nerd Tutorials muestra cómo publicar y suscribir tópicos, manejo de reconexión, uso de librerías y ejemplos con sensores
- En proyectos de ESP32 y Raspberry Pi, muchas guías usan la Raspberry Pi como broker Mosquitto mientras los ESP32 actúan como clientes publicadores y/o suscriptores

---

## Comparativa técnica combinada

Versión enriquecida de la comparación entre ESP32, STM32 y Raspberry Pi para proyectos con MQTT:

| Criterio / aspecto | ESP32 | STM32 | Raspberry Pi |
|-------------------|-------|-------|--------------|
| **Función típica en el ecosistema MQTT** | Cliente publicador/suscriptor de sensores, nodos remotos | Cliente embebido para control, adquisición, actuadores | Broker principal o gateway, cliente de alto nivel, procesamiento de datos |
| **Disponibilidad de ejemplos / código** | Muy abundante (PubSubClient, AsyncMqttClient, ejemplos con sensores, JSON) | Menos ejemplos "listos para usar", pero hay portaciones Paho + ejemplos HAL + FreeRTOS (ej. proyecto STM32F4_HAL_ETH_MQTT_CLIENT) | Muchas guías para instalar Mosquitto, conectar clientes, usar Node-RED |
| **Dificultad de configuración / integración** | Relativamente sencilla: WiFi integrado, librerías bien documentadas | Interfaz de red debe escogerse/integrarse (Ethernet, módulo WiFi, LwIP, drivers), ajuste manual de pila y librerías | Bastante directa: instalar broker con apt, configurar, usar clientes |
| **Rendimiento / escalabilidad** | Buen desempeño para cantidad moderada de mensajes; posibilidad de saturación si muchos mensajes por segundo | Buena según hardware (MCU de gama alta), pero requiere optimización; clientes más simples | Puede manejar múltiples conexiones y publicar/subscribe de muchos clientes, aunque bajo carga intensa puede haber latencias |
| **Broker embebido en el dispositivo** | Generalmente no (ESP32 actúa como cliente) | En teoría posible en MCU potentes, pero complejidad alta y recursos limitados; pocas bibliotecas maduras para broker completo en STM32 | Sí, Raspberry Pi puede correr broker (Mosquitto u otras) con sistema operativo completo y recursos disponibles |
| **Manejo de fallos / reconexión / robustez** | Buen soporte en librerías (reconexión automática, librerías asíncronas) | Requiere manejo explícito de reconexión, buffers, errores de red, gestión de memoria | El entorno Linux ofrece herramientas avanzadas, logs, reinicios automáticos de procesos |
| **Consumo energético** | Bajo (módulos en modo de sueño), apto para dispositivos alimentados con batería | Potencialmente bajo si se aprovechan modos de bajo consumo del MCU, pero la interfaz de red puede aumentar consumo | Alto consumo relativo por tener sistema operativo completo, periféricos activos |
| **Latencia / determinismo** | Bastante bueno para tareas embebidas | Muy fuerte para tareas de control deterministas (microcontroladores con RTOS) | Latencia mayor debido al sistema operativo, procesos, multitarea |
| **Costo y hardware necesario adicional** | WiFi + Bluetooth integrados en muchos modelos (menos componentes extra) | Puede requerir chip externo (módulo WiFi, PHY Ethernet, transceptores) | Ya incluye conectividad (según modelo) y hardware completo; menor necesidad de módulos adicionales |
| **Flexibilidad en procesamiento de datos** | Limitada por recursos integrados | Intermedia (depende del MCU) | Muy alta: puede ejecutar algoritmos pesados, análisis local, almacenar historiales, servir dashboards |
| **Escenario ideal de uso** | Sensores remotos, nodos IoT, actuadores simples que se comunican con broker | Controladores embebidos críticos (temporización, control en tiempo real) que también requieren comunicación MQTT | Broker local, gateway, nodo central, procesamiento local, integrar con otros servicios locales o en la nube |

---

## Ejemplos ilustrativos / casos prácticos

- **Proyecto común:** Usar **Raspberry Pi como broker Mosquitto** y tener varios ESP32 como nodos sensores que publican datos (temperatura, humedad, etc.). Muchas guías siguen esta arquitectura (RPi + ESP32)
- **STM32 con conectividad celular:** Implementar MQTT cliente en STM32 junto con un módulo de conectividad (por ejemplo SIM7600, módulo GSM), para publicar datos desde un microcontrolador con conectividad celular
- **Proyecto "STM_IoT_3":** Conectar STM32 al broker MQTT, publicar un mensaje y mostrar el estado de conexión en un display

---

# Conclusiones y recomendaciones

## 1. Complementar roles

Lo más común (y eficiente) es usar **ESP32 (o STM32)** como nodos clientes ligeros y usar una **Raspberry Pi** como broker central o gateway de alto nivel. En casos donde el MCU debe operar de forma autónoma sin broker externo, podría intentar alojar un broker embebido, pero eso conlleva complejidad y límites.

## 2. Elección según los requisitos del proyecto

- Si tu aplicación exige **tiempos de respuesta, control en tiempo real** o interacción con muchos periféricos, **STM32** puede ser más adecuado como cliente
- Si tu aplicación principal es **recopilación/publicación de datos** con conectividad WiFi, con mínima lógica extra, **ESP32** ofrece un camino más directo
- Si además quieres **procesamiento local, análisis de datos, dashboards** locales o gestionar múltiples conexiones, **Raspberry Pi** como nodo central es muy fuerte

## 3. Evaluar rendimiento, límites y consumo en contexto real

En tu proyecto concreto, realiza pruebas de:
- **Latencia**
- **Número de clientes activos**
- **Tamaño de mensajes**
- **Reconexiones repetidas**
- **Consumo energético** (especialmente si algún nodo será alimentado por batería)

## 4. Uso de librerías confiables

- **Para ESP32:** `PubSubClient` es un clásico, y `AsyncMqttClient` mejora el manejo asíncrono
- **Para STM32:** Bibliotecas como Paho Embedded MQTT adaptadas a HAL + FreeRTOS + LwIP tienen ejemplos comunitarios (como el repositorio `eziya/STM32F4_HAL_ETH_MQTT_CLIENT`)
- **Para Raspberry Pi:** Mosquitto es muy fiable y ampliamente usado en el ecosistema IoT

## 5. Precaución al intentar que un MCU actúe como broker completo

⚠️ Aunque técnicamente es posible (sobre todo en MCUs más potentes), muchas fuentes advierten que un broker MQTT exige más recursos (memoria, concurrencia, buffers) de lo que un MCU pequeño puede manejar con facilidad.

---
