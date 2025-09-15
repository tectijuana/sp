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
  
  ![Bluetooth](https://www.afrodigimag.com/wp-content/uploads/2020/03/technologie-bluetooth-un-progres-dusage-quotidien-afrodigimag.jpg)

---

2. ***Zigbee:*** Zigbee es un protocolo de comunicación inalámbrica estandarizado que define cómo se organizan y comunican los nodos en una red. Por lo general cuando se habla de una comunicación con Zigbee, se habla de una red donde existe un coordinador que inicializa y gestiona la red, routers que retransmiten datos ampliando el alcance y dispositivos finales que envían o reciben información. Zigbee permite crear redes escalables, donde los nodos se comunican de manera directa o a través de otros nodos intermedios en caso de que el receptor esté muy lejos.
- **Características principales**:
  - Su topología se basa en la de malla pero también puede adaptarse a una de árbol o estrella.
  - Funciona en una frecuencia de 2.4 GHz, aunque también puede usar 868/915 MHz.
  - Tiene un alcance promedio de 10–100 m (dependiendo de la cantidad de epetidores en la malla).
  - Velocidad de transmisión promedio es de 20–250 Kbps (dependiendo de la banda usada).
  - Su consumo es extremadamente bajo, ideal para dispositivos que operan con batería durante meses o años. Es por eso que su aplicación principal es para la comunicación entre dispositivos domésticos como luces, cerraduras inteligentes, sensores de temperatura, humedad, termostatos, etc.

![Estructura del protocolo Zigbee](https://www.guiahardware.es/wp-content/uploads/2022/10/capaz-ZigBee-1024x648.png)

---

3. ***XBee:*** Es una familia de módulos de comunicación inalámbrica que permiten a microcontroladores transmitir y recibir datos por radiofrecuencia. Dependiendo del modelo, estos pueden usar distintos protocolos, como Zigbee, Bluetooth, etc., funcionando como intermediarios que facilitan la creación de redes inalámbricas punto a punto, en estrella o en malla.
XBee puede llegar a sonar lo mismo cuando se compara con Zigbee, sin embargo, la principal diferencia es que Zigbee es un protocolo o estándar de comunicación inalámbrica que define cómo se organizan y transmiten los datos en una red, mientras que XBee es un dispositivo físico (hardware) que puede implementar Zigbee u otros protocolos de comunicación.
- **Características princiaples**
  - Es compatible con Zigbee, 802.15.4, DigiMesh, Wi-Fi y Bluetooth según el modelo.
  - Opera como un reemplazo de cable serial.
  - Tiene un alcance de decenas de metros hasta varios kilómetros, pero todo dependiendo de la antena y modelo.
  - Tiene un bajo consumo energético, ideal para aplicaciones de internet de las cosas y sensores que funcionan con batería.

![XBee](https://cdn-shop.adafruit.com/640x480/128-01.jpg)

---

4. ***Wi-Fi:*** Es una de las tecnologías de comunicación inalámbrica más famosas que permite a los dispositivos conectarse a redes de área local, y a través de un routers a internet. Las personas que desconocen el tema, creen que el wifi es intenet, pero wifi es el medio de comunicación para llegar a diferentes redes o solo tranferir datos en una misma red.
- **Características principales:**
  - Opera principalmente en frecuencias de 2.4 GHz y 5 GHz.
  - Alcance promedio de 30–100 m, dependiendo del entorno.
  - Velocidad de transmisión alta, desde Mbps hasta Gbps.
  - Su topología puede variar ya que se usa para acceder a distintas redes, por lo que su topologías no puede ser definida. 
  - Su consumo energético es mayor, por lo que su uso es ideal en aplicaciones que no dependan únicamente de batería.

![WiFi](https://okdiario.com/img/2023/11/10/senal-wifi.jpg)

---

5. ***LTE (Long Term Evolution):*** LTE es un estándar de comunicación celular de alta velocidad diseñado para transmisión de datos y voz sobre redes móviles. 
- **Características principales:**
  - Opera en frecuencias asignadas por cada país, principalmente entre 700 MHz y 2600 MHz, según la red y el operador.
  - Descarga de hasta 300 Mbps.
  - Subida de hasta 75 Mbps.
  - Alcance entre torres y el usuario es de 1–5 km en áreas urbanas y hasta 10–15 km en áreas rurales, pero si se necesita llegar más lejos, las antenas sirven de repetidoras de señal.
  - Su topología principal es de celda, es decir, las torres estan ubicadas en ciertos puntos para formar hexágonos como en un panal de abeja.
  - Sus principales aplicaciones son navegación por internet, streaming de video y audio, videollamadas, etc.

![Frecuencias LTE](https://tse2.mm.bing.net/th/id/OIP.Mxk4l6iXSX8R81RSl-Bi2wHaEt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3)

---

6. ***LoRa (Long Range):*** LoRa es una tecnología de comunicación inalámbrica de largo alcance y bajo consumo, diseñada principalmente para aplicaciones de internet de las cosas y sensores distribuidos donde no exiteste la posibilidad de poner repetidores tan cercanos. Lo que hace que tenga un mayor alcance es su forma de transmitir los datos usando la técnica Chirp Spread Spectrum. Lo que hace es enviar la información en pequeños paquetes en distintas frecuencias para que en caso de interferencia, las señales que superan la frecuencia de los obstáculos puedan llegar mínimo a un nodo para que se vuelve a enviar a otro punto. Además, las señales se envian en distintas direcciones para tratar de esquivar las interferencias.
Una vez que los datos llegan al gateway o nodo central, este los envía a un servidor en la nube, donde pueden almacenarse, procesarse y analizarse. Desde la nube, también se pueden enviar comandos de regreso a los nodos para ajustar sensores, activar actuadores o cambiar parámetros del sistema, completando así el ciclo de comunicación de manera eficiente y centralizada.
- **Características principales:**
  - Opera en bandas libres o licenciadas según el país.
  - Tiene un muy buen alcance. En áreas urbanas de 2–5 km y en lo rural de 15–30 km.
  - Al tener un gran alcance, su velocidad es baja, entre 0.3 y 50 Kbps, suficiente para sensores que envían datos esporádicos.
  - Sus principales aplicaciones son la agricultura inteligente, ciudades inteligente, sistemas de logística en aereopuertos, etc.

![Arquitectura de LoRa](https://www.cardinalpeak.com/wp-content/uploads/2020/05/LoRaWAN-Network-Architecture.png)

## Referencias
- Comofuncionaexplicado.com. (s.f.). Descubre cómo funciona el bluetooth. [https://comofuncionaexplicado.com/tecnologia-y-electronica/bluetooth/](https://comofuncionaexplicado.com/tecnologia-y-electronica/bluetooth/)
- Rosagro, J. (2024, abril 16). ZigBee: ¿Qué es y para qué sirve? GuiaHardware. [https://www.guiahardware.es/zigbee/](https://www.guiahardware.es/zigbee/)
- XBee.cl. (s.f.). ¿Qué es XBee? [https://xbee.cl/que-es-xbee/](https://xbee.cl/que-es-xbee/)
- Gallego, G. (2025, febrero 4). Qué es el WiFi y cómo funciona para conectar todo a Internet. ADSLZone. [https://www.adslzone.net/reportajes/tecnologia/que-es-wifi-como-funciona/](https://www.adslzone.net/reportajes/tecnologia/que-es-wifi-como-funciona/)
- UNIR Revista. (2025, febrero 13). LTE: qué es, cómo funciona y diferencias con 4G y 5G. Universidad Internacional de La Rioja. [https://www.unir.net/revista/ingenieria/lte-que-es/](https://www.unir.net/revista/ingenieria/lte-que-es/)
- Semtech Corporation. (s.f.). ¿Qué es LoRa? [https://www.semtech.com/lora/what-is-lora?utm_source=chatgpt.com](https://www.semtech.com/lora/what-is-lora?utm_source=chatgpt.com)
- The Things Network. (s.f.). Spreading Factors. [https://www.thethingsnetwork.org/docs/lorawan/spreading-factors/?utm_source=chatgpt.com](https://www.thethingsnetwork.org/docs/lorawan/spreading-factors/?utm_source=chatgpt.com)
