# Periféricos y Buses de Comunicación en Sistemas Embebidos

## Datos del Alumno
- **Nombre**: Cruz Hernández Edgar Eduardo
- **Matrícula**: 22210296
- **Fecha**: 15/09/2025
- **Usuario**: Eduardoch12v

---

## Introducción

Los sistemas embebidos requieren diversos protocolos de comunicación para interactuar con periféricos, sensores, actuadores y otros dispositivos. La selección del protocolo adecuado depende de factores como velocidad, distancia, número de dispositivos, consumo de energía y complejidad del sistema.

## 1. UART (Universal Asynchronous Receiver-Transmitter)

### Características Principales
- **Comunicación serie asíncrona** punto a punto
- **Velocidades típicas**: 9600, 19200, 38400, 115200 bps (hasta varios Mbps)
- **Líneas de señal**: TX (transmisión), RX (recepción), opcionalmente RTS/CTS para control de flujo
- **Sin reloj compartido**: cada extremo debe configurarse a la misma velocidad

### Ventajas
- Simplicidad de implementación
- Bajo consumo de energía
- Amplia compatibilidad
- Comunicación full-duplex

### Desventajas
- Solo comunicación punto a punto
- Susceptible a errores por diferencias de velocidad
- Sin mecanismo de direccionamiento

### Aplicaciones Típicas
- Comunicación con módulos GPS, Bluetooth, WiFi
- Debug y programación de microcontroladores
- Interfaz con sensores simples
- Comunicación entre microcontroladores

## 2. SPI (Serial Peripheral Interface)

### Características Principales
- **Comunicación serie síncrona** maestro-esclavo
- **Líneas de señal**: MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), CS/SS (Chip Select)
- **Velocidades**: Hasta decenas de MHz
- **Comunicación full-duplex**

### Ventajas
- Alta velocidad de transmisión
- Comunicación simultánea bidireccional
- Protocolo simple sin overhead
- Múltiples esclavos con líneas CS separadas

### Desventajas
- Requiere más pines (4 mínimo + CS adicionales)
- Solo comunicación de corta distancia
- Sin confirmación de recepción incorporada

### Aplicaciones Típicas
- Memorias flash y EEPROM
- Sensores de alta velocidad (acelerómetros, giroscopios)
- Pantallas LCD/OLED
- Convertidores ADC/DAC externos

## 3. I2C (Inter-Integrated Circuit)

### Características Principales
- **Comunicación serie síncrona** multi-maestro
- **Líneas de señal**: SDA (Serial Data), SCL (Serial Clock)
- **Direccionamiento**: 7 bits (128 direcciones) o 10 bits
- **Velocidades estándar**: 100 kHz (Standard), 400 kHz (Fast), 1 MHz (Fast+), 3.4 MHz (High-speed)

### Ventajas
- Solo 2 líneas para múltiples dispositivos
- Direccionamiento incorporado
- Confirmación de recepción (ACK/NACK)
- Detección de colisiones en modo multi-maestro

### Desventajas
- Menor velocidad que SPI
- Resistencias pull-up requeridas
- Complejidad mayor del protocolo
- Capacitancia limitada del bus

### Aplicaciones Típicas
- Sensores de temperatura, presión, humedad
- Memorias EEPROM
- Relojes de tiempo real (RTC)
- Expansores de puertos GPIO
- Pantallas OLED pequeñas

## 4. CAN (Controller Area Network)

### Características Principales
- **Bus diferencial robusto** para aplicaciones automotrices e industriales
- **Velocidades**: Hasta 1 Mbps (CAN clásico), hasta 8 Mbps en fase de datos (CAN FD)
- **Topología**: Bus lineal con terminaciones de 120Ω
- **Arbitraje**: Por identificador de mensaje sin pérdida de datos

### Ventajas
- Altamente robusto contra interferencias
- Comunicación multi-maestro sin colisiones
- Detección y corrección de errores avanzada
- Priorización automática de mensajes

### Desventajas
- Complejidad de implementación
- Requiere transceptores especializados
- Limitado a 1 Mbps en modo clásico
- Necesita terminaciones adecuadas

### Aplicaciones Típicas
- Sistemas automotrices (ECUs, sensores, actuadores)
- Automatización industrial
- Sistemas de control de procesos
- Redes de sensores en entornos hostiles

## 5. USB (Universal Serial Bus) en Sistemas Embebidos

### Características Principales
- **Comunicación serie diferencial** con alimentación
- **Versiones**: USB 1.1 (12 Mbps), USB 2.0 (480 Mbps), USB 3.0+ (5+ Gbps)
- **Topología**: Árbol con hub raíz
- **Roles**: Host, Device, OTG (On-The-Go)

### Ventajas
- Plug-and-play con enumeración automática
- Alimentación a través del bus (hasta 500mA/900mA)
- Amplia compatibilidad con PCs y dispositivos
- Múltiples clases de dispositivos estándar

### Desventajas
- Complejidad del stack de software
- Consumo de energía relativamente alto
- Requiere cristal preciso (±500 ppm)
- Longitud de cable limitada sin repetidores

### Aplicaciones Típicas
- Interfaces de programación y debug
- Almacenamiento masivo (USB Mass Storage)
- Dispositivos HID (teclados, ratones)
- Comunicación con PC (CDC, dispositivos virtuales)

## Comparación de Protocolos

| Protocolo | Líneas | Velocidad Max | Distancia | Dispositivos | Complejidad |
|-----------|--------|---------------|-----------|--------------|-------------|
| UART      | 2-4    | ~10 Mbps      | Corta     | 2            | Baja        |
| SPI       | 4+     | ~100 Mbps     | Muy corta | Limitado     | Baja        |
| I2C       | 2      | 3.4 MHz       | Corta     | 128          | Media       |
| CAN       | 2+     | 8 Mbps        | Larga     | Muchos       | Alta        |
| USB       | 4      | 10+ Gbps      | Media     | 127          | Muy alta    |

## Criterios de Selección

### Velocidad Requerida
- **Baja velocidad** (<100 kbps): UART, I2C estándar
- **Velocidad media** (100 kbps - 10 Mbps): I2C rápido, SPI, CAN
- **Alta velocidad** (>10 Mbps): USB, SPI de alta velocidad

### Número de Dispositivos
- **Punto a punto**: UART, SPI
- **Pocos dispositivos** (2-10): I2C, SPI con múltiples CS
- **Muchos dispositivos**: CAN, USB, I2C con multiplexores

### Distancia de Comunicación
- **Muy corta** (<10 cm): SPI
- **Corta** (<1 m): UART, I2C
- **Media** (1-5 m): USB
- **Larga** (>5 m): CAN, UART con drivers RS-485

### Robustez Requerida
- **Baja**: SPI, I2C básico
- **Media**: UART, I2C con repetidores
- **Alta**: CAN, USB con aislamiento

### Consumo de Energía
- **Muy bajo**: I2C, UART a baja velocidad
- **Bajo**: SPI a baja velocidad
- **Medio**: CAN en modo sleep
- **Alto**: USB activo

## Tendencias y Evolución

### Nuevos Estándares
- **CAN FD**: Mayor ancho de banda y flexibilidad
- **USB4**: Unificación con Thunderbolt
- **I3C**: Sucesor de I2C con mayor velocidad

### Integración en SoCs
- Controladores USB integrados en la mayoría de microcontroladores modernos
- Múltiples periféricos UART/SPI/I2C en un solo chip
- Soporte de hardware para protocolos de red industrial

### Aplicaciones Emergentes
- **IoT**: Protocolos de bajo consumo como I2C y UART
- **Automotive**: Transición de CAN a CAN FD y Ethernet automotive
- **Industrial 4.0**: Integración de USB y Ethernet en sistemas embebidos

## Consideraciones de Implementación

### Hardware
- **Niveles de voltaje**: 3.3V vs 5V, conversores de nivel
- **Velocidades de slew rate** para reducir EMI
- **Filtrado y protección** contra descargas electrostáticas
- **Layout de PCB** optimizado para integridad de señal

### Software
- **Drivers de dispositivo** y middleware
- **Gestión de errores** y recuperación
- **Buffering** y gestión de memoria
- **Sincronización** y tiempo real

### Debugging
- **Analizadores lógicos** para protocolos digitales
- **Osciloscopios** para análisis de forma de onda
- **Herramientas de protocolo** específicas (CANalyzer, I2C debuggers)

## Conclusión

La selección del protocolo de comunicación apropiado es crucial para el éxito de un sistema embebido. Cada protocolo tiene sus fortalezas y limitaciones específicas, y la elección debe basarse en los requisitos específicos de la aplicación incluyendo velocidad, distancia, número de dispositivos, robustez y restricciones de energía y costo.

La tendencia actual apunta hacia la integración de múltiples protocolos en sistemas híbridos, donde diferentes subsistemas pueden usar el protocolo más apropiado para sus necesidades específicas, conectándose a través de gateways o procesadores centrales que manejan la conversión entre protocolos.
