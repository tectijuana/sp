# Implementación de MQTT sobre Wi-Fi y Bluetooth Low Energy (BLE): comparación de eficiencia en sistemas embebidos  
### Alumno: Aguayo Virgen Brisa Julianna  

## Introducción  
En el ámbito del Internet de las Cosas (IoT), el protocolo **MQTT** (Message Queuing Telemetry Transport) se ha consolidado como una de las herramientas más utilizadas para la transmisión de datos. Su modelo de publicación y suscripción facilita la comunicación entre dispositivos de manera ligera, confiable y eficiente. Sin embargo, la forma en que esos datos viajan depende de la tecnología de comunicación inalámbrica utilizada.  

Dos de las más comunes en sistemas embebidos son **Wi-Fi** y **Bluetooth Low Energy (BLE)**. Ambas presentan ventajas y desventajas: mientras Wi-Fi permite enviar grandes volúmenes de datos a alta velocidad, BLE se enfoca en reducir el consumo de energía y prolongar la vida útil de dispositivos pequeños y portátiles.  

Esta investigación analiza la implementación de MQTT sobre Wi-Fi y BLE, explorando cómo se comporta el protocolo en términos de eficiencia, consumo energético, velocidad y estabilidad en sistemas embebidos.  

## ¿Qué es MQTT? 
MQTT es un protocolo de comunicación diseñado para el intercambio de mensajes en dispositivos con recursos limitados y redes poco confiables.
Funciona bajo el esquema publicador–suscriptor, en el cual los dispositivos envían información a un broker (servidor central), y este la distribuye
a quienes estén suscritos a esos datos. Gracias a su ligereza, se utiliza ampliamente en IoT para conectar sensores, actuadores y aplicaciones en la nube.  

## ¿Qué es Wi-Fi?  
Wi-Fi es una tecnología de comunicación inalámbrica que permite conectar dispositivos a internet o a redes locales con altas velocidades de transmisión.  
 **Ventaja:** ofrece gran ancho de banda (capacidad de enviar muchos datos a la vez).  
 **Desventaja:** su consumo de energía es elevado, lo que lo hace menos ideal para sensores o dispositivos de bajo consumo.  

## ¿Qué es Bluetooth Low Energy (BLE)?  
Bluetooth Low Energy es una variante del Bluetooth tradicional que prioriza el bajo consumo energético.  
 **Ventaja:** ideal para dispositivos pequeños que transmiten datos de manera periódica, como relojes inteligentes o sensores médicos.  
 **Desventaja:** menor velocidad y alcance comparado con Wi-Fi.  

## Implementación de MQTT sobre Wi-Fi y BLE  
La integración de MQTT sobre estas tecnologías permite conectar dispositivos embebidos a sistemas de monitoreo y control en tiempo real.  

 **Wi-Fi + MQTT:** recomendado para aplicaciones que requieren transmitir datos grandes o continuos (ej. monitoreo de cámaras, datos ambientales en tiempo real).  
 **BLE + MQTT:** más adecuado para aplicaciones donde la prioridad es conservar energía y los datos transmitidos son pequeños (ej. sensores biomédicos, wearables).  

## Comparación de eficiencia  
 **Latencia (tiempo de respuesta):** Wi-Fi generalmente ofrece menor latencia que BLE, lo que lo hace más rápido en la entrega de mensajes.  
  **Consumo energético:** BLE consume mucha menos energía que Wi-Fi, lo que lo hace ideal para dispositivos con batería limitada.  
  **Estabilidad:** Wi-Fi ofrece conexiones más estables en entornos con buena cobertura, mientras que BLE es más sensible a interferencias.  
  **Casos de uso:** Wi-Fi destaca en sistemas con alta demanda de datos, mientras que BLE brilla en aplicaciones que buscan bajo consumo y portabilidad.  

## Impacto general  
La implementación de MQTT sobre Wi-Fi y BLE demuestra cómo la selección de la tecnología de comunicación afecta directamente la eficiencia de un sistema embebido. Wi-Fi es más eficiente en transmisión de datos masivos, pero BLE asegura mayor autonomía de dispositivos. Comprender estas diferencias es clave para diseñar aplicaciones IoT que equilibren velocidad, consumo energético y confiabilidad.  

## Referencias  
  OASIS. (2019). *MQTT Version 5.0*. OASIS Standard.  
  https://docs.oasis-open.org/mqtt/mqtt/v5.0/  
  Bluetooth SIG. (2024). *Bluetooth Low Energy Overview*.  
  https://www.bluetooth.com/learn-about-bluetooth/technology/bluetooth-low-energy/  
  IEEE Standards Association. (2023). *IEEE 802.11: Wireless LAN standards*.  
  https://standards.ieee.org/ieee/802.11/  
