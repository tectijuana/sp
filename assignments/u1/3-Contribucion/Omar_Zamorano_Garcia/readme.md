### Omar Zamorano Garcia #22211676
## Sistemas programables
# Comunicación por Radio Frecuencia en microcontroladores (XBee, Zigbee, etc).

## Introducción
La comunicación por radiofrecuencia es parte de la nueva tecnología en el desarrollo de sistemas modernos, permitiendo eliminar cualquier tipo de conexión por cable, esto gracias a la transmisión de datos por ondas.

Desde el punto de vista del autor, siendo un estudiante de ingeniería en sistemas computacionales, conocer el como funcionan estas tecnologías implica comprender tanto el nivel físico (frecuencia, potencia de transmisión, alcance) como el nivel lógico (protocolos de comunicación, direccionamiento de nodos, seguridad), esto con el fin de poder desarrollar sistemas que se integren con componentes físicos capaces de enviar información.

## Tecnologías que usan comunicación por radiofrecuencia
Actualmente la mayoría de los dispositivos utilizados por las personas utilizan mínimo un tipo de comunicación por radio frecuencia. Las siguientes son algunos de los tipos de comunicaciones por radiofrecuencia:

1. ***Bluetooth***: Es una de las más conocidas y más usadas por las personas. Es el principal medio de transferencia de archivos vía inalámbrica, además, es muy usada para dispositivos de audio como audífonos y bocinas. Existen 2 categorías:
   1. Bluetooth Clásico (BR/EDR) usado para transmisión de audio (audífonos, bocinas, micrófonos) y datos con mayor velocidad.
   2. Bluetooth Low Energy (BLE): optimizado para bajo consumo y conexiones rápidas, ideal para IoT, wearables y sensores.
- **Otras características:**
  - Utiliza una frecuencia de 2.4 GHz, permitiendo un alcance promedio de 10 metros.
  - **Velocidad de transmisión:** BR/EDR hasta 3 Mbps y BLE entre 125 Kbps y 2 Mbps.
  - **Topología:** Soporta conexiones punto a punto y piconets, que se basa en un dispositivo principal y hasta 7 dispositivos esclavos.
  - Es muy utilizado por su bajo consumo pero esta limitado en aplicaciones por su poco alcance, es por eso que su uso recomendable es en el hogar.

2. ***Zigbee:*** Zigbee es en teoría es de las tecnologías más nuevas. Por lo general cuando se habla de una comunicación con Zigbee, se habla de una red donde existe un coordinador que inicializa y gestiona la red, routers que retransmiten datos ampliando el alcance y dispositivos finales que envían o reciben información. Zigbee permite crear redes escalables, donde los nodos se comunican de manera directa o a través de otros nodos intermedios en caso de que el receptor esté muy lejos.
- **Características principales**:
  - Su topología se basa en la de malla pero también puede adaptarse a una de árbol o estrella.
  - Funciona en una frecuencia de 2.4 GHz, aunque también puede usar 868/915 MHz.
  - Tiene un alcance promedio de 10–100 m (dependiendo de la cantidad de epetidores en la malla).
  - Velocidad de transmisión promedio es de 20–250 Kbps (dependiendo de la banda usada).
  - Su consumo es extremadamente bajo, ideal para dispositivos que operan con batería durante meses o años. Es por eso que su aplicación principal es para la comunicación entre dispositivos domésticos como luces, cerraduras inteligentes, sensores de temperatura, humedad, termostatos, etc.
![Estructura del protocolo Zigbee](https://www.guiahardware.es/wp-content/uploads/2022/10/capaz-ZigBee-1024x648.png)

4. ***XBee:***
