# Plataformas populares para sistemas programables
**Nombre:** Carlos Alberto Iñiguez Gallego<br>
**Número de Control:** 19211660<br>
**GitHub:** [CarlosAlberto193](https://github.com/CarlosAlberto193)


# 💻Plataformas Populares para Sistemas Programables💻
**¿Que son los Sistemas Programables?:** Son sistemas de control informático industrial que supervisa continuamente el estado de los dispositivos de entrada y toma decisiones basadas en un programa personalizado para controlar el estado de los dispositivos de salida.<br><br>
Estos controladores pueden automatizar un proceso específico, una función de la máquina o incluso toda una línea de producción.

**¿Quines lo usan?:** 
-  Ingenieros y Desarrolladores de Hardware
-  Hobbyistas
-  Empresas de Tecnología e Industria
-  Investigadores y Científicos

## 1️⃣Arduino
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Arduino_Logo.svg" width="200">
</p>

**Descripcion:**  Es una plataforma de desarrollo basada en una placa electrónica de hardware libre que incorpora un microcontrolador re-programable y una serie de pines hembra. Estos permiten establecer conexiones entre el microcontrolador y los diferentes sensores y actuadores de una manera muy sencilla (principalmente con cables dupont).

**¿Quienes son los dueños/encargados de este sistema?:** Consta de dos instituciones italianas, la primera siendo la compañia Arduino LLC y Arduino SSL

**¿Cual es el precio sugerido por unidad?:** Varía según el modelo, desde $10 USD (Arduino Nano) hasta $50 USD (Arduino Mega).

**Caracteristicas**
- Basado en microcontroladores AVR y ARM.
- Lenguaje de programación basado en C/C++.
- Compatible con múltiples sensores y módulos.

## 2️⃣Raspberry Pi
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/c/cb/Raspberry_Pi_Logo.svg" width="200">
</p>

**Descripcion:** Es una computadora de bajo costo y con un tamaño compacto, del porte de una tarjeta de crédito, puede ser conectada a un monitor de computador o un TV, y usarse con un mouse y teclado estándar. Es un pequeño computador que correo un sistema operativo linux

**¿Quienes son los dueños/encargados de este sistema?:** Son una fundacion localizada en Inglaterra, la llamada "Raspberry Pi Fundation"

**¿Cual es el precio sugerido por unidad?:** 15$ a 75$ USD, depende el modelo y la cantidad de Ram con la que se desea.

**Caracteristicas**
- Basado en procesadores ARM.
- Soporta sistemas operativos como Raspberry Pi OS, Ubuntu y más.
- Posee GPIO para interacción con hardware externo.
- Uso en aplicaciones de IoT, servidores, educación y automatización.

## 3️⃣ESP32
<p align="center">
  <img src="https://www.electronicwings.com/storage/PlatformSection/TopicContent/424/icon/ESP32%20GPIO%20Banner%20Image.jpg" width="200">
</p>

**Descripcion:** Es la denominación de una familia de chips SoC (System on a chip / Sistema en un Chip)  de bajo costo y consumo de energía, con tecnología WiFi y Bluetooth. El ESP32 fue creado y desarrollado por Espressif Systems y es el sucesor de la la familia ESP8266.

**¿Quienes son los dueños/encargados de este sistema?:** La empresa china Espressif Systems

**¿Cual es el precio sugerido por unidad?** 5$ a 15$ USD

**Caracteristicas**
- Procesador dual-core Xtensa LX6.
- Soporta Wi-Fi y Bluetooth.
- Programable con Arduino IDE, MicroPython y Espressif IDF.
- Bajo consumo energético.

## 4️⃣STM32
<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbJ9kvb91Qv9CrKUAzNU5yGJhEJKLiWjCe5A&s" width="200">
</p>

**Descripcion:** Es una empresa de larga trayectoria en el mercado que fabrica una gran variedad de componentes electrónicos, entre los que destacan distintas líneas de microcontroladores, sensores, dispositivos para RF y electrónica de potencia entre otros.

**¿Quienes son los dueños/encargados de este sistema?:** Es una empresa multinacional europea llamada STMicroelectronics

**¿Cual es el precio sugerido por unidad?:** 2$ a 50$ USD segun el modelo.

**Caracteristicas**
- Alto rendimiento y bajo consumo.
- Programable en C/C++ y con herramientas como STM32CubeIDE y Arduino IDE.
- Soporte para aplicaciones industriales y embebidas.

## 5️⃣BeagleBone
<p align="center">
  <img src="https://www.beagleboard.org/app/uploads/2023/07/DSC00505-400x345.webp" width="200">
</p>

**Descripcion:** Es una placa de desarrollo basada en el procesador AM335x Arm Cortex-A8. Esta placa BeagleBone es un ordenador de una sola placa (SBC) que se puede utilizar como ordenador autónomo o integrado en un sistema.

**¿Quienes son los dueños/encargados de este sistema?:** Son producidos por Texas Instruments, sin embargo son OpenSource por BeagleBoard.org

**¿Cual es el precio sugerido por unidad?:** 50$ a 150$ USD segun el modelo.

**Caracteristicas**
- Procesador ARM Cortex-A8.
- Variantes como BeagleBone Black y BeagleBone AI.
- Soporta Debian Linux y otras distribuciones.

# 📓Notas del Estudiante
De manera independiente he trabajado con ya varios de estos dispositivos, no solamente contando con usted profesor al tener que trabajar con el Pico W, si no que por interes (meramente de Hobby) he llegado a contar con:
- ESP32: En la escena del homebrew del PS4, un exploit que se llego a encontrar en la version 9.00 de firmware vio una debilidad para correr codigo sin firmar al utilizar el navegador predeterminado de Playstation. al momento de sobrecargar los recursos este fuerza un kernel panic el cual permite cargar el mismo exploit desde un USB, el ESP32 tiene la de crear un WebHost local y de esta manera no tener que contar con paginas de terceros.
- LuckFox Pico: En este caso llegue a querer usar el Pico W, sin embargo este requiere de una entrada/salida Ethernet, me decidi por vender mi PS4 Slim por una PS4 Pro, encontre una en version 11.00 la cual tiene otro tipo de exploit; en este caso no lo entiendo del todo, sin embargo se encontro un punto de entrada con la entrada de Ethernet, al modificar las DNS.
- Libre Computer "AML-S905X-CC" Le Potato: Esta fue/es por una etapa de Hobbysta que tuve, en la cual queria hacer una pequeña maquina de emulacion; no lo he terminado, instalarle Batocera fue lo mas sencillo, sin embargo quiero que esta despliegue imagen en una TV CRT por su puerto AV, pero esto implica conocimiento que todavia no tengo (y no he tenido el tiempo de aprender), tal vez en esta materia lo consiga.

# 🔖Referencias
- Cursos Aula 21. (s.f.). ¿Qué es un PLC? Recuperado el 5 de febrero de 2025, de https://www.cursosaula21.com/que-es-un-plc/
- Tutorial Markdown. (s.f.). Emojis en Markdown. Recuperado el 5 de febrero de 2025, de https://tutorialmarkdown.com/emojis
- Raspberry Pi Chile. (s.f.). ¿Qué es Raspberry Pi? Recuperado el 5 de febrero de 2025, de https://raspberrypi.cl/que-es-raspberry/
- Arduino Chile. (s.f.). ¿Qué es Arduino? Recuperado el 5 de febrero de 2025, de https://arduino.cl/que-es-arduino/?srsltid=AfmBOopKmxhwllDATec5_r37eR7MGjCDkZWuPl4loqUr-MVmGwEBdSqW
- TodoMaker. (s.f.). Conociendo al ESP32. Recuperado el 5 de febrero de 2025, de https://todomaker.com/blog/conociendo-al-esp32/
- Profetolocka. (2021, 29 de marzo). La familia de microcontroladores STM32. Recuperado el 5 de febrero de 2025, de https://www.profetolocka.com.ar/2021/03/29/la-familia-de-microcontroladores-stm32/#google_vignette
- RS Online. (s.f.). Kit de desarrollo de microcontroladores. Recuperado el 5 de febrero de 2025, de https://es.rs-online.com/web/p/kits-de-desarrollo-de-microcontroladores/1252411
