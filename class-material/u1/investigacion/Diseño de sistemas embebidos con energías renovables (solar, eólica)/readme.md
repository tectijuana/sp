# Diseño de sistemas embebidos con energías renovables (solar, eólica)

**Nombre:** Oscar Paul Martinez Herrera - 22211609  
**Materia:** Sistemas Programables  
**Fecha:** 17 de septiembre de 2025 

Los sistemas embebidos son tecnologías invisibles, pero esenciales que impulsan muchos de nuestros dispositivos cotidianos. En su esencia, estos sistemas son microprocesadores integrados que operan dentro de estos dispositivos, encargándose de procesar información, supervisar y controlar funciones específicas.

A diferencia de las computadoras personales, estos sistemas integrados están diseñados para realizar tareas especializadas y, en la mayoría de los casos, no son reprogramables. Son componentes inseparables de los dispositivos en los que se integran, lo que garantiza su funcionamiento eficiente y autónomo. Además, son notables por su capacidad de funcionar sin interacción humana y resistir eventos adversos, reiniciándose por sí mismos cuando sea necesario.

Los sistemas embebidos también son conocidos como sistemas embarcados, sistemas empotrados o sistemas integrados.

<img width="551" height="238" alt="imagen" src="https://upload.wikimedia.org/wikipedia/commons/2/2c/ADSL_modem_router_internals_labeled.jpg">

---

## Diseño de sistemas embebidos en las energías renovables solares y eolicas

Los sistemas embebidos sirven para controlar, regular y optimizar la generación y uso de la energía.

<img width="551" height="238" alt="imagen" src="https://media.licdn.com/dms/image/v2/D4D12AQGcvOsLUq_9Ig/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1727119081531?e=2147483647&v=beta&t=jv8Qm_ua3rALS5AKVGTmX0mdlSawpDIh0UPUtm4k7W4">

Su diseño suele dividirse en estas etapas:

- **1. Captura de datos (sensores)**

  - Solar: sensores de radiación solar, voltaje y corriente de los paneles, temperatura de las celdas.

  - Eólica: sensores de velocidad y dirección del viento, voltaje y corriente generada por el aerogenerador.
- **2. Procesamiento (microcontrolador)**

  - Aquí entra el “cerebro” del sistema, que puede ser un microcontrolador (Arduino, ESP32, STM32) o un procesador más potente (Raspberry Pi, BeagleBone).

  - Procesa la información de los sensores.

  - Decide cuándo cargar baterías, cuándo desconectar paneles o turbinas, y cómo distribuir la energía.

- **3. Actuación (control)**

  - El sistema embebido manda señales a:

  - Controladores de carga (para proteger las baterías de sobrecarga o descarga profunda).

  - Inversores (para convertir la energía de DC a AC y poder usarla en casas).

  - Sistemas de frenado en turbinas eólicas cuando el viento es demasiado fuerte.

- **4. Comunicación**

  - Muchos diseños modernos incluyen comunicación:

  - Local: pantallas LCD o LEDs que muestran estado de energía.

  - Remota: Wi-Fi, Bluetooth, Zigbee o LoRa para enviar datos a una app o a la nube.

- **5. Optimización energética**

  - Dado que el sistema mismo consume energía, debe ser muy eficiente:

  - Bajo consumo en el microcontrolador.

  - Modos de ahorro de energía cuando no hay sol o viento.

# Referencias
  - InnovaciónDigital, R. (2025, 12 junio). Sistemas embebidos: qué son y para qué se utilizan.
    InnovaciónDigital360. https://www.innovaciondigital360.com/iot/sistemas-embebidos-que-son-y-para-que-se-utilizan/
