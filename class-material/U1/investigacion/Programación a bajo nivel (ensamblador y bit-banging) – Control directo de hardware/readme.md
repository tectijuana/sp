 # Programación a Bajo Nivel  
### (Ensamblador y Bit-Banging – Control Directo de Hardware)

---

## Introducción
La **programación a bajo nivel** se refiere al desarrollo de software que interactúa de forma directa con el hardware, gestionando instrucciones del procesador y controlando dispositivos sin capas intermedias.  

Mientras que los lenguajes de **alto nivel** (como Python o Java) priorizan la productividad y portabilidad, los lenguajes de bajo nivel permiten **máxima eficiencia, rapidez y control**, aunque requieren mayor conocimiento técnico.

Su aplicación es crucial en:
- **Sistemas operativos** y controladores.  
- **Firmware** de dispositivos electrónicos.  
- **Sistemas embebidos** en automóviles, electrodomésticos o IoT.  
- Áreas críticas como **ciberseguridad** y **optimización de hardware**.  

![Esquema alto nivel vs bajo nivel](https://upload.wikimedia.org/wikipedia/commons/9/9e/Programming_languages_abstraction_layers.svg)  
*Figura 1. Lenguajes de alto nivel vs. bajo nivel (Fuente: Wikimedia Commons).*

---

## Ensamblador

El **lenguaje ensamblador** es un lenguaje de programación que traduce de forma casi directa a **código máquina**. Se caracteriza por usar **mnemónicos** que representan instrucciones del procesador (ejemplo: `MOV`, `ADD`, `JMP`).  

### Características principales
- **Dependiente de la arquitectura** (x86, ARM, RISC-V, etc.).  
- Acceso a **registros, memoria y periféricos** del procesador.  
- **Alta eficiencia** en el uso de CPU y memoria.  
- Dificultad de aprendizaje y **código poco portable**.  

![Código ensamblador](https://upload.wikimedia.org/wikipedia/commons/9/9e/X86assembly.jpg)  
*Figura 2. Código ensamblador en arquitectura x86 (Fuente: Wikimedia Commons).*

### Aplicaciones del ensamblador
- **Optimización extrema** en videojuegos y motores gráficos.  
- Desarrollo de **BIOS y firmware**.  
- Rutinas críticas en **sistemas embebidos**.  
- **Reversing e ingeniería inversa** en ciberseguridad.  

---

## Bit-Banging

El **bit-banging** es una técnica de software para manipular manualmente pines de **entrada/salida (I/O)** en un microcontrolador, simulando protocolos de comunicación (como I2C, SPI o UART) sin usar periféricos especializados.  

### Características
- **Control total** de las señales digitales.  
- Ideal para **microcontroladores simples** sin hardware especializado.  
- Alto **consumo de CPU** y dependencia del **timing preciso**.  
- Mayor riesgo de errores en **aplicaciones de tiempo real**.  

![Bit-banging en comunicación serie](https://upload.wikimedia.org/wikipedia/commons/8/87/Serial_bit-banging.png)  
*Figura 3. Representación de la técnica de bit-banging en comunicación serie (Fuente: Wikimedia Commons).*

### Ejemplos de uso
- Implementación casera de **protocolos de comunicación**.  
- Prototipado de hardware cuando no hay periféricos dedicados.  
- **Sistemas educativos**, para enseñar fundamentos de electrónica digital.  
- IoT y proyectos con **Arduino, ESP32 o Raspberry Pi**.  

---

## Comparación: Ensamblador vs Bit-Banging

| Aspecto               | Ensamblador                          | Bit-Banging                          |
|-----------------------|---------------------------------------|---------------------------------------|
| Nivel de control      | CPU y registros internos              | Pines de E/S directamente             |
| Dependencia           | Arquitectura del procesador           | Temporización del hardware            |
| Ventajas              | Máxima eficiencia, velocidad          | Flexibilidad, implementación propia   |
| Desventajas           | Difícil de mantener, poco portable    | Consume CPU, timing crítico           |
| Aplicaciones típicas  | Sistemas operativos, firmware, seguridad | Comunicaciones serie, prototipado    |

---

## Importancia en la Actualidad
A pesar del dominio de los lenguajes de alto nivel, la programación a bajo nivel sigue siendo **esencial** en la industria tecnológica:  

1. **Sistemas embebidos**  
   - Automóviles modernos, dispositivos médicos y electrodomésticos requieren **control preciso**.  
2. **Internet de las Cosas (IoT)**  
   - Dispositivos de bajo consumo necesitan rutinas eficientes en ensamblador y control de pines mediante bit-banging.  
3. **Ciberseguridad y malware**  
   - Análisis de exploits, rootkits y virus requiere entender ensamblador.  
4. **Optimización extrema**  
   - Motores de videojuegos retro y emuladores usan ensamblador por velocidad.  

---

## Conclusión
La programación a bajo nivel, a través del **ensamblador** y del **bit-banging**, representa la base del control directo de hardware. Aunque demanda más conocimientos técnicos y presenta mayores retos de mantenimiento, ofrece ventajas que ningún lenguaje de alto nivel puede igualar: **precisión, eficiencia y control absoluto del sistema**.  

Sin estas técnicas, sería imposible desarrollar sistemas confiables en áreas críticas como la **aeroespacial, automotriz, médica e IoT**. En pocas palabras: la programación a bajo nivel es la **columna vertebral del software que controla directamente la tecnología moderna**.  

---

## Referencias
- Stallings, W. (2017). *Computer Organization and Architecture*. Pearson.  
- Patterson, D. A., & Hennessy, J. L. (2021). *Computer Organization and Design RISC-V Edition*. Morgan Kaufmann.  
- Barr, M. (2006). *Programming Embedded Systems in C and C++*. O’Reilly Media.  
- Wikipedia contributors. (2025). **Assembly language**. En *Wikipedia*. Disponible en: [https://es.wikipedia.org/wiki/Lenguaje_ensamblador](https://es.wikipedia.org/wiki/Lenguaje_ensamblador)  
- Wikipedia contributors. (2025). **Bit banging**. En *Wikipedia*. Disponible en: [https://en.wikipedia.org/wiki/Bit_banging](https://en.wikipedia.org/wiki/Bit_banging)  

---

## Link de la Actividad
👉 [Pega aquí el link cuando lo tengas listo]  

---

## Datos del Alumno
**Nombre:** Francisco Javier Villegas Suárez  
**Número de control:** 22210364  
