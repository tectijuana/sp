# Programación en VHDL y Verilog para publicar sensores FPGA vía MQTT

**Nombre:** Lizeth Roxana Castro Reyes - 22211535  
**Materia:** Sistemas Programables  
**Fecha:** 30 de septiembre de 2025 

## 1. Introducción
Las **FPGAs (Field Programmable Gate Arrays)** son dispositivos reconfigurables que permiten implementar sistemas digitales personalizados.  
Una de sus aplicaciones modernas es la conexión de **sensores físicos** a plataformas de comunicación **IoT**.  
Para esto, se usan lenguajes de descripción de hardware como **VHDL** y **Verilog**, mientras que el protocolo **MQTT** se emplea para la transmisión ligera y eficiente de datos hacia un *broker*.

El objetivo es diseñar un sistema donde un FPGA lea datos de sensores, los procese y los envíe a un servidor MQTT.

---

## 2. Lenguajes de programación para FPGA

### VHDL
- Orientado a la documentación estructurada.  
- Sintaxis extensa y muy descriptiva.  
- Usado ampliamente en entornos académicos y sistemas críticos.  

### Verilog
- Sintaxis similar a C, simple y concisa.  
- Favorece la simulación rápida y prototipado.  
- Muy popular en la industria.  

Ambos permiten describir módulos que capturan datos de sensores y controlan protocolos de comunicación.

---

## 3. Interfaz FPGA – Sensores
El FPGA se conecta a sensores usando protocolos como:  
- **I2C**: común en sensores ambientales.  
- **SPI**: rápido, útil para adquisición precisa.  
- **UART**: sencillo y ampliamente soportado.  

En VHDL o Verilog se programan módulos que:  
1. Generan las señales de reloj y control.  
2. Reciben los datos binarios del sensor.  
3. Guardan los valores en registros internos.  

---

## 4. Publicación en MQTT desde FPGA

El FPGA por sí solo no maneja MQTT, por lo que se requiere integración adicional:

### Opción 1: FPGA + SoC / Microcontrolador embebido
- FPGAs modernos (ej. Xilinx Zynq, Intel SoC) incluyen procesadores ARM.  
- El hardware en VHDL/Verilog captura datos y los pasa al procesador.  
- El procesador ejecuta software en C/Python con librerías MQTT (ej. **Paho MQTT**).  

### Opción 2: FPGA + Módulo externo de comunicación
- FPGA transmite datos a un microcontrolador externo (ej. **ESP32**, **STM32**, Raspberry Pi Pico).  
- El microcontrolador maneja la conexión de red y la publicación en MQTT.  

**Flujo de datos típico:**
Sensor → FPGA (VHDL/Verilog) → MCU/SoC → MQTT Broker → Aplicaciones IoT

---

## 5. Caso práctico
1. Un **módulo SPI en Verilog** lee datos de un sensor de temperatura.  
2. Los datos se almacenan en un registro de 16 bits.  
3. El procesador ARM dentro del SoC FPGA toma el valor.  
4. El procesador envía los datos vía Ethernet o WiFi.  
5. Se publica en el tópico `sensor/temperatura` en el *broker MQTT*.  
6. Aplicaciones como **Node-RED** o **Grafana** visualizan la información.  

---

## 6. Ventajas del enfoque
- **Paralelismo**: procesamiento simultáneo de varios sensores.  
- **Baja latencia**: adquisición inmediata de datos.  
- **Escalabilidad**: múltiples suscriptores MQTT.  
- **Flexibilidad**: personalización de protocolos de sensores.  

---

## 7. Retos principales
- Complejidad de implementar **TCP/IP** directamente en FPGA.  
- Necesidad de experiencia en **diseño digital + software embebido**.  
- Depuración de sistemas mixtos (hardware + software).  

---

## Referencias
1. Cadence PCB Solutions. (2022, marzo 17). Hardware description languages: VHDL vs Verilog, and their functional uses. Cadence.com. https://resources.pcb.cadence.com/blog/2020-hardware-description-languages-vhdl-vs-verilog-and-their-functional-uses
2. Getting Started with VHDL: Syntax, Programming & Modules. (2025). Digilent.com. https://digilent.com/reference/programmable-logic/guides/getting-started-with-vhdl?srsltid=AfmBOorIe_dbpHeLqpVBD1qUmaHeGfPkuzuiMN5lbAKP1wNpayDqHnHx
3. Luis. (2020, marzo 11). Cómo adaptar códigos VHDL o Verilog y prácticas externas al laboratorio LabsLand FPGA. Blog de LabsLand; LabsLand. https://labsland.com/blog/es/2020/03/11/como-adaptar-codigos-vhdl-o-verilog-y-practicas-externas-al-laboratorio-labsland-fpga/

---
