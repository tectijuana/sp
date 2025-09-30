# Microcontroladores y su Arquitectura Interna- Angel Lopez 22211596


Los **microcontroladores** son circuitos integrados que combinan en un solo chip los elementos esenciales de un sistema de cómputo: procesador, memoria y periféricos. Están diseñados para controlar dispositivos electrónicos de manera autónoma y eficiente, siendo ampliamente utilizados en sistemas embebidos, electrodomésticos, automóviles e IoT.

---

## Componentes de la Arquitectura Interna

### 1. Registros
- Son pequeñas memorias internas de acceso ultrarrápido.
- Almacenan datos temporales, instrucciones o direcciones de memoria.
- Tipos comunes:  
  - **Registros de propósito general**: usados en operaciones de la ALU.  
  - **Registros especiales**: contador de programa (PC), acumulador (ACC), puntero de pila (SP).  

### 2. ALU (Unidad Aritmético-Lógica)
- Ejecuta operaciones matemáticas básicas (suma, resta, multiplicación simple).
- Realiza operaciones lógicas y de comparación (AND, OR, XOR, NOT).
- Trabaja directamente con los registros y la memoria.

### 3. Memoria
- **ROM/Flash**: almacena el programa (firmware).  
- **RAM**: guarda variables y datos temporales.  
- **EEPROM**: usada para datos que deben mantenerse tras reinicios.  

### 4. GPIOs (General Purpose Input/Output)
- Pines configurables como entrada o salida.  
- Permiten la interacción con el entorno: leer sensores, activar actuadores, controlar pantallas, etc.  

### 5. Periféricos Internos
- **Temporizadores y contadores**: generan retardos, PWM o mediciones de tiempo.  
- **Convertidores ADC/DAC**: convierten señales analógicas ↔ digitales.  
- **Interfaces de comunicación**: UART, SPI, I2C, CAN, USB.  
- **Módulos de interrupciones**: permiten respuestas rápidas a eventos externos.  

---

## Conclusión
Los microcontroladores son el “cerebro” de los sistemas embebidos. Su arquitectura interna integra procesador, memoria, registros, GPIOs y periféricos en un solo chip, lo que los hace compactos, eficientes y versátiles para múltiples aplicaciones tecnológicas.

---

## Referencias
- Mazidi, M. A., Naimi, S., & Naimi, S. (2018). *The 8051 Microcontroller and Embedded Systems*. Pearson.  
- Patterson, D. A., & Hennessy, J. L. (2017). *Computer Organization and Design*. Morgan Kaufmann.  
