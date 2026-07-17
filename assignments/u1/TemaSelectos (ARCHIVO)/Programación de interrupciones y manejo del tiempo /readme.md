# Programación de Interrupciones y Manejo del Tiempo
**Nombre: Brandon Orozco Hernandez**
**Brandon1216**
## Introducción
La programación de interrupciones y el manejo del tiempo son aspectos esenciales en los sistemas embebidos y en la programación a nivel de hardware. Se utilizan para gestionar eventos externos o internos de manera eficiente sin la intervención constante del procesador.

## 1. Interrupciones
Las **interrupciones** son señales que indican a la CPU que debe detener la ejecución normal del programa para atender un evento específico. Pueden clasificarse en:

- **Interrupciones externas**: Generadas por dispositivos externos, como teclados, sensores o botones.
- **Interrupciones internas**: Provienen de eventos dentro del microcontrolador, como temporizadores o errores del sistema.
- **Interrupciones por software**: Se generan mediante instrucciones de software para cambiar el flujo del programa.

### 1.1 Manejo de Interrupciones
El manejo de interrupciones involucra:
1. **Registro del vector de interrupción**: Asociación de una interrupción con una rutina de servicio (ISR).
2. **Atención de la interrupción**: Ejecución de la ISR cuando se dispara la interrupción.
3. **Restauración del estado**: Retorno al estado previo después de atender la interrupción.

## 2. Timers
Los **timers** son contadores de hardware que permiten medir el tiempo y generar eventos periódicos sin intervención del procesador. Son fundamentales para el control de tareas en sistemas en tiempo real.

### 2.1 Tipos de Timers
- **Timers de propósito general**: Se usan para medir intervalos de tiempo o contar eventos.
- **Timers de comparación**: Comparan el valor del contador con un umbral y generan una interrupción al alcanzarlo.
- **Timers PWM (Modulación por Ancho de Pulso)**: Se usan para generar señales PWM utilizadas en el control de motores y LEDs.

### 2.2 Aplicaciones de Timers
- Control de tiempos en sistemas embebidos.
- Generación de retardos precisos.
- Implementación de multitareas en sistemas en tiempo real (RTOS).

## 3. Watchdogs
El **Watchdog Timer** (WDT) es un temporizador especial diseñado para detectar y recuperar el sistema de fallas de software, evitando bloqueos o bucles infinitos.

### 3.1 Funcionamiento del Watchdog
1. Se configura el WDT con un tiempo límite.
2. El software debe resetear el WDT periódicamente.
3. Si el software no lo resetea a tiempo (por un fallo), el WDT genera un reinicio del sistema.

### 3.2 Usos del Watchdog
- Prevención de bloqueos en sistemas embebidos.
- Reinicio automático en caso de fallo.
- Supervisión de software crítico en aplicaciones de seguridad.

## 4. Eventos Asíncronos
Los **eventos asíncronos** son eventos que ocurren en cualquier momento y pueden interrumpir el flujo normal del programa. Son comunes en sistemas que interactúan con hardware externo.

### 4.1 Ejemplos de Eventos Asíncronos
- Recepción de datos en una comunicación serie (UART, I2C, SPI).
- Presión de un botón en una interfaz de usuario.
- Señales de sensores en sistemas embebidos.

### 4.2 Manejo de Eventos Asíncronos
El manejo eficiente de eventos asíncronos se logra mediante:
- Uso de **interrupciones** para capturar eventos sin bloqueo.
- Implementación de **buffers y colas** para procesar datos recibidos de manera ordenada.
- Utilización de **máquinas de estados** para gestionar múltiples eventos.

## Conclusión
La programación de interrupciones, el uso de timers, watchdogs y el manejo de eventos asíncronos son esenciales para el desarrollo de sistemas eficientes y confiables. Estos conceptos permiten optimizar el uso del procesador, mejorar la capacidad de respuesta del sistema y garantizar su estabilidad ante fallos.
