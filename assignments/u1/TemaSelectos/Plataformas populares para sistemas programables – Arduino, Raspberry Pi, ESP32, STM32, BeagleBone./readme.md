# Plataformas populares para sistemas programables **Arduino, Raspberry Pi, ESP32, STM32 y BeagleBone**.

---
## Datos del Alumno

- **Nombre:**  
- **Número de control:**  
- **Fecha:**  
- **Nickname:**  

---

## 1) Arduino — definición, características, tipos y ventajas
<p align="center">
<img width="530" height="518" alt="arduino" src="https://github.com/user-attachments/assets/8639f529-bd6a-4791-afa6-05d2f93c2c40" />
</p>

### Definición y propósito
Arduino es una plataforma de prototipado electrónica open-source compuesta por placas con microcontrolador re-programable y un entorno de desarrollo (IDE). Nació como herramienta educativa para facilitar el acceso a la electrónica y el “learning by doing”.

### Características generales
- **Hardware abierto**: esquemáticos y especificaciones accesibles; amplio ecosistema de clones y placas compatibles.  
- **Software**: Arduino IDE (soporta Windows/Mac/Linux), lenguaje basado en C/C++ con librerías amplias.  
- **Shields y expansión**: existe un gran catálogo de shields (placas que se apilan) para añadir Wi-Fi, motores, pantallas, RTC, etc.  
- **Comunidad y documentación**: gran comunidad de makers; enorme cantidad de ejemplos, librerías y tutoriales.  

### Modelos / tipos (ejemplos y notas)
Arduino no es un solo modelo sino una familia. Entre los más usados están:

- **Arduino Uno (R3 / R4 variantes)** — placa clásica para principiantes.  
  - Especificaciones del Uno R3 típicas: ATmega328P, 16 MHz, 5V, 14 pines digitales (6 PWM), 6 entradas analógicas, 32 KB flash, 2 KB SRAM, 1 KB EEPROM.  
  - Ideal para proyectos con sensores y actuadores básicos.  

- **Otros modelos**:  
  - Mega (más I/O y memoria).  
  - Nano (formato pequeño).  
  - Leonardo.  
  - MKR/Nano 33 (orientados a IoT).  
  - Due (ARM).  
  - R4 (nuevas revisiones).  
  *(Ver guía de modelos para detalles).*  

### Ventajas
- Bajo coste y fácil acceso para principiantes.  
- Gran compatibilidad con sensores/hardware común y alto soporte comunitario.  
- Hardware y software open-source → posibilidad de clonar y modificar.  

### Limitaciones
- No es un ordenador: no ejecuta un sistema operativo completo.  
- Para tareas de alto procesamiento, interfaz gráfica o multimedia, quedará limitado.  

### Código de ejemplo — Arduino UNO (Blink + lectura analógica)

Este ejemplo combina el **parpadeo de un LED** integrado en la placa con la **lectura de un potenciómetro** conectado al pin analógico A0.

---

## Código

```cpp
// Blink + lectura analógica (potenciómetro en A0)
const int LED = 13;      // LED onboard
const int POT = A0;      // pot connected to A0

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(300);
  digitalWrite(LED, LOW);
  delay(300);

  int v = analogRead(POT);         // 0..1023
  float voltage = v * (5.0 / 1023);
  Serial.print("Pot: ");
  Serial.print(v);
  Serial.print(" -> ");
  Serial.print(voltage);
  Serial.println(" V");
  delay(200);
}
```

## Notas de wiring y seguridad

- Usar resistencia de aproximadamente 220 Ω en serie con LEDs para protegerlos.

- Respetar los voltajes máximos: Arduino Uno clásico trabaja a 5V.

- Conectar correctamente el potenciómetro: un terminal a 5V, otro a GND, y el wiper (central) a A0.

---

## 2) Raspberry Pi — definición, características, modelos y usos
<p align="center">
<img width="355" height="200" alt="raspberry pi" src="https://github.com/user-attachments/assets/30baeea5-4a23-4bd1-832d-2b4af16c5a6a" />
</p>

### Definición
Raspberry Pi es un ordenador de placa única (SBC) diseñado originalmente para educación pero usado en muchísimas aplicaciones (media center, servidores pequeños, IoT, robótica). Instala y ejecuta un sistema operativo (por ejemplo Raspberry Pi OS basada en Debian).

### Características principales
- **Sistema operativo completo**: Linux y otras opciones. Permite ejecutar programas complejos, servidores, interfaces gráficas y multimedia.  
- **Capacidad de hardware**: modelos con diferentes cantidades de RAM (ej. 1GB, 2GB, 4GB, 8GB según la versión).  
- Conectividad: Ethernet, Wi-Fi y Bluetooth en modelos modernos.  
- Puertos USB, salida HDMI, microSD como almacenamiento.  
- **Versatilidad**: puede actuar como ordenador de escritorio básico, servidor, controlador domótico, media center, retro-consola, etc.  

### Modelos / variantes (breve)
- **Raspberry Pi Zero**: muy pequeño y barato.  
- **Raspberry Pi 3/4/400**: más potencia.  
- **Raspberry Pi 4**: opciones de 2/4/8 GB RAM (elige según tarea).  
*(Ver documentación del fabricante para comparativas exactas).*  

### Ventajas
- Potencia suficiente para ejecutar apps y servicios (Python, Node-RED, servidores, multimedia).  
- Gran comunidad y abundante documentación y proyectos educativos.  

### Limitaciones
- Consume más energía que un microcontrolador típico (no ideal si buscas ultra-bajo consumo).  
- No es tan determinista para tareas en tiempo real (si necesitas latencias estrictas, mejor microcontrolador/STM32 o soluciones con RTOS).  

### Código de ejemplo — Raspberry Pi (Python / gpiozero)

Este ejemplo muestra cómo controlar un **LED conectado a la Raspberry Pi** utilizando la librería `gpiozero`, incluyendo un **parpadeo básico** y el control mediante un **botón**.

---

## A. Blink con gpiozero (GPIO 17)

```python
# led_blink.py
from gpiozero import LED
from time import sleep

led = LED(17)   # usar numeración BCM
try:
    while True:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
except KeyboardInterrupt:
    led.close()
```
## B. Botón que controla el LED

```python
from gpiozero import LED, Button
from signal import pause

led = LED(17)
btn = Button(27)

btn.when_pressed = led.on
btn.when_released = led.off

pause()
```
## Notas de wiring y seguridad
- Usar resistencia en serie con el LED para protegerlo.

- Comprobar permisos de usuario: ejecutar con el usuario adecuado o sudo si es necesario para acceso a GPIO.

- Conectar correctamente los pines:

  - LED: un terminal a GPIO 17, otro a GND a través de resistencia.

  - Botón: un terminal a GPIO 27, otro a GND.

---

## 3) ESP32 — definición, características, variantes y por qué usarlo
<p align="center">
<img width="459" height="456" alt="esp32" src="https://github.com/user-attachments/assets/28bbbc07-1cad-48b7-aee4-517d8101a9bf" />
</p>

### Definición
ESP32 es una familia de SoC (System on Chip) de Espressif que integra procesador(es) de 32 bits, radio Wi-Fi y Bluetooth, orientada a IoT y aplicaciones embebidas que requieren conectividad inalámbrica.

### Características técnicas destacadas
- **CPU**: típicamente Tensilica Xtensa LX6 (dual-core) hasta 240 MHz (según variante).  
- **Memoria**: bloques integrados de ROM/RAM (por ejemplo referencias a ~448 KB ROM y 520 KB SRAM en modelos documentados) y soporte para flash externa en módulos.  
- **Conectividad**: Wi-Fi (802.11 b/g/n), Bluetooth Classic y BLE integrados; módulos comerciales (WROOM/WROVER, PICO, etc.).  
- **Periféricos**: ADCs, DAC, PWM, I²C, SPI, UART, interrupciones, PWM; múltiples pines GPIO.  
- **Bajo consumo**: modos especiales de ahorro de energía, clock gating y escalado dinámico, diseñado para wearables y sensores.  

### Programación y ecosistema
- **SDK oficial**: ESP-IDF (Espressif).  
- Compatibilidad con Arduino core para ESP32.  
- Runtime como MicroPython.  
- Documentación y dev-kits oficiales abundan.  

### Ventajas
- Ideal para IoT: conectividad Wi-Fi/Bluetooth integrada, buen rendimiento por coste, y eficiencia energética.  

### Limitaciones
- No es un SBC: no ejecuta un sistema operativo tradicional (aunque puede ejecutar pequeños RTOS).  
- Para interfaces gráficas complejas o procesamiento intensivo, usar SBCs sería mejor.  

### Código de ejemplo — ESP32

Este ejemplo muestra cómo controlar un **LED** en ESP32 usando tanto **Arduino Core (C++)** como **MicroPython**, incluyendo conexión Wi-Fi en Arduino Core.

---

## A. ESP32 (Arduino Core): Blink + conexión Wi-Fi

```cpp
#include <WiFi.h>

const char* ssid     = "TU_SSID";
const char* password = "TU_PASSWORD";
const int LED = LED_BUILTIN; // puede variar por placa

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Conectado! IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(300);
  digitalWrite(LED, LOW);
  delay(300);
}
```

## B. ESP32 (MicroPython): Blink

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)  # en muchos devkits, LED = GPIO2
while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
```

## Notas de wiring y seguridad
- Revisar el datasheet del módulo (WROOM/WROVER) para conocer pines disponibles y límites eléctricos.

- Conectar el LED con resistencia adecuada para protegerlo.

- Asegurarse de usar pines GPIO correctos según tu devkit.

---

## 4) STM32 — familia, potencias, periféricos y por qué elegirlos
<p align="center">
<img width="603" height="368" alt="stm32" src="https://github.com/user-attachments/assets/2699bef5-e23f-4854-b8cf-9b0d16505f33" />
</p>

### ¿Qué es STM32?
STM32 es una amplia familia de microcontroladores de STMicroelectronics basados en núcleos ARM Cortex-M (M0/M0+, M3, M4, M7, etc.) que cubre desde dispositivos ultra-bajos en consumo hasta MCU de alto rendimiento con FPU/periféricos avanzados.

### Características clave
- **Variedad de núcleos**:  
  - Cortex-M0 / M0+ (muy bajo consumo).  
  - Cortex-M3 (uso general).  
  - Cortex-M4 (DSP/FPU).  
  - Cortex-M7 (alto rendimiento, hasta ~400 MHz en algunos modelos).  
- **Periféricos ricos**: múltiples UART/SPI/I²C, temporizadores avanzados, ADCs configurables, PWM, Ethernet, USB (host/device/OTG), controladores de memoria externa, aceleradores criptográficos según serie.  
- **Modos de bajo consumo**: sleep/stop/standby con microamperios en standby (dependiendo de la serie).  
- **Seguridad**: aceleradores de cifrado, arranque seguro, MPU, y características orientadas a productos industriales.  

### Herramientas y frameworks
- STM32CubeIDE / CubeMX (configuración y generación de código).  
- HAL/LL libraries.  
- Soporte mbed y ecosistema amplio para desarrollo profesional/industrial.  

### Ventajas
- Excelente para aplicaciones embebidas industriales con requisitos de tiempo real, seguridad y eficiencia energética.  
- Gran abanico para escoger el MCU adecuado.  

### Limitaciones
- Curva de aprendizaje más pronunciada que Arduino.  
- Selección del modelo correcto requiere análisis de periféricos y consumo.  

### Código de ejemplo — STM32 (HAL) — Blink

Este ejemplo muestra cómo hacer parpadear un **LED** usando la librería **HAL** de STM32, asumiendo que la inicialización de GPIO fue generada con CubeMX.

---

## Código (fragmento)

```c
/* main.c (fragmento) */
#include "main.h"

int main(void) {
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();  // generado por CubeMX

  while (1) {
    HAL_GPIO_TogglePin(GPIOB, GPIO_PIN_0);
    HAL_Delay(500);
  }
}
```

## Notas de wiring y seguridad
- Usar CubeMX para generar la configuración de relojes y pines, evitando errores en clocks.

- Para depuración, usar ST-Link u otro depurador compatible.

- Conectar correctamente el LED al pin configurado (ej. GPIOB PIN 0) con resistencia en serie si es necesario.

---

## 5) BeagleBone — características y cuándo usarlo
<p align="center">
<img width="637" height="391" alt="beaglebone" src="https://github.com/user-attachments/assets/042cdee3-f05f-45e4-9f99-2b5ce164f8a2" />
</p>

### Definición
BeagleBone es una familia de ordenadores de placa única (SBC) de código abierto (BeagleBone Black, BeagleBone Green, etc.) pensada para proyectos que requieren Linux con control de I/O y algo más de orientación profesional/industrial que la Pi en ciertos usos.

### Características y variantes
- **BeagleBone Black / Green**: típicamente con procesadores ARM (ej. OMAP en versiones clásicas).  
- Memoria integrada (por ejemplo 512 MB en algunos modelos).  
- Ranura microSD.  
- Soporta Linux/Android.  
- Muchos pines de expansión.  
- La Green añade un hub USB integrado en colaboración con Adafruit.  

### Ventajas
- Buena interfaz de I/O y enfoque en aplicaciones embebidas con Linux.  
- Algunas variantes integran características facilitadoras (hub USB, continuidad con ecosistema industrial).  

### Limitaciones
- Comunidad y recursos algo menores que Raspberry Pi.  
- Ciertas versiones antiguas tienen memoria y I/O limitados comparado con SBC más modernos.  

### Código de ejemplo — BeagleBone (Python + Adafruit_BBIO)

Este ejemplo muestra cómo hacer parpadear un **LED** en BeagleBone usando la librería `Adafruit_BBIO.GPIO`.

---

## Código

```python
# beaglebone_blink.py
import Adafruit_BBIO.GPIO as GPIO
import time

LED = "P8_10"   # ajustar según pinout
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
```
## Notas de wiring y seguridad
- Ejecutar con permisos adecuados o agregar el usuario al grupo gpio.

- Revisar el pinout de la placa antes de conectar el LED.

- Usar resistencia en serie con el LED para protegerlo.
---

## Tabla Comparativa de Plataformas de Desarrollo

| Plataforma      | Tipo                  | CPU típico                                | RAM/Flash (ejemplo)                  | OS                         | Conectividad típica                    | I/O / ADC                                                                 | Ideal para                                                                 |
|-----------------|-----------------------|-------------------------------------------|--------------------------------------|-----------------------------|-----------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Arduino (Uno)** | Microcontrolador      | ATmega328P 8-bit @16MHz                   | 32KB flash, 2KB SRAM                 | No (programa quemado)      | Por shields (no nativo)                | 14 I/O digitales, 6 analógicas (10-bit) — ejemplo Uno                     | Prototipos sencillos, sensores, actuadores, educación. <br/> *Fuente: Arduino.cl* |
| **Raspberry Pi** | SBC (microordenador)  | ARM Cortex-A (varía por modelo)           | 1–8 GB (según modelo)                | Linux (Raspbian/otros)     | Ethernet, Wi-Fi, BT (según modelo)     | Pines GPIO (menos ADC nativo)                                             | Proyectos con OS, multimedia, servidores, visualización. <br/> *Fuente: Codelearn* |
| **ESP32**        | SoC (MCU + radio)     | Tensilica Xtensa LX6 dual @ up to 240MHz  | ~520KB SRAM internos, flash externo  | No full-OS (RTOS posible)  | Wi-Fi + Bluetooth integrados           | ADCs múltiples, muchas GPIOs, PWM, UART, SPI, I2C                          | IoT inalámbrico, nodos sensores con conectividad. <br/> *Fuente: Espressif Systems* |
| **STM32**        | MCU (familia amplia)  | ARM Cortex-M (M0..M7) — hasta ~400MHz M7  | Variable (Flash/RAM según serie)     | No (RTOS/firmware)         | Ethernet/USB (según serie)             | ADCs avanzados, timers, PWM, buses múltiples                              | Sistemas embebidos industriales, RTOS, control motor. <br/> *Fuente: Riverdi* |
| **BeagleBone**   | SBC                   | ARM (varía por modelo)                    | Ej. 512MB en versiones clásicas      | Linux                      | USB, Ethernet (según modelo)           | Amplio soporte I/O y expansión                                            | Control embebido con Linux, aplicaciones industriales ligeras. <br/> *Fuente: Transistores.info* |

---

## Referencias consultadas
- [Arduino.cl. (s. f.). ¿Qué es Arduino? Arduino.cl](https://arduino.cl/que-es-arduino/)

- [Xataka. (2021, 16 marzo). Qué es Arduino, cómo funciona y qué puedes hacer con uno. Xataka](https://www.xataka.com/basics/que-arduino-como-funciona-que-puedes-hacer-uno)

- [Bricogeek. (2014, 1 junio). Guía de modelos Arduino y sus características: Arduino Uno. Lab.Bricogeek.com](https://lab.bricogeek.com/tutorial/guia-de-modelos-arduino-y-sus-caracteristicas/arduino-uno)

- [Codelearn. (2023, 24 febrero). Qué es Raspberry Pi y para qué sirve. Codelearn](https://codelearn.es/blog/que-es-raspberry-pi-y-para-que-sirve/)

- [IMEPI. (s. f.). Raspberry Pi: Todo lo que necesitas saber. IMEPI](https://imepi.com.mx/raspberry-pi-todo-lo-que-necesitas-saber/)

- [GoDaddy. (2023, 20 junio). Qué es Raspberry Pi: Todo lo que debes saber. GoDaddy Resources](https://www.godaddy.com/resources/es/tecnologia/que-es-raspberry-pi)

- [Espressif Systems. (s. f.). ESP32 Series. Espressif](https://www.espressif.com/en/products/socs/esp32)

- [QSM Semiconductores. (2022, 18 noviembre). Qué es el ESP32. QSM Semiconductores](https://qsmsemiconductores.com/que-es-el-esp32/)

- [TodoMaker. (2021, 30 mayo). Conociendo al ESP32. TodoMaker](https://todomaker.com/blog/conociendo-al-esp32/)

- [Riverdi. (2021, 26 octubre). ¿Por qué STM32? Introducción a Riverdi STM32 Embedded Displays. Riverdi](https://riverdi.com/es/blog/por-que-stm32-introduccion-a-riverdi-stm32-embedded-displays)

- [Wonderful PCB. (2022, 14 junio). STM32 explained: features & applications. WonderfulPCB](https://www.wonderfulpcb.com/es/blog/stm32-explained-features-applications/)

- [Rowsum. (2023, 18 abril). Comparación de ventajas únicas de STM32. Rowsum](https://www.rowsum.com/es/comparacion-de-ventajas-unicas-de-stm32/)

- [Descubre Arduino. (2020, 17 agosto). BeagleBone Green. DescubreArduino.com](https://descubrearduino.com/beaglebone-green/)

- [Transistores.info. (2021, 10 noviembre). Qué es el BeagleBone: Guía para principiantes de la BeagleBoard. Transistores.info](https://transistores.info/que-es-el-beaglebone-guia-para-principiantes-de-la-beagleboard/)

