# Instituto Tecnológico de Tijuana
## Materia: Sistemas Programables 2PM
### Nombre y No. Control: Ernesto Torres Pineda 22211665
### Fecha: 15/09/2025
---

# Compilación y depuración de programas embebidos

# Herramientas y técnicas de debugging para FPGA y controladores

## 1. Introducción

En los sistemas embebidos, la **compilación** y la **depuración** son etapas críticas del ciclo de desarrollo.

* **Compilación**: Traduce el código fuente en un archivo ejecutable o un bitstream (para FPGAs) que puede cargarse en el dispositivo.
* **Depuración (debugging)**: Permite detectar, analizar y corregir errores en hardware y software.

Los entornos embebidos presentan retos únicos: recursos limitados, dependencia del hardware y dificultades para observar el comportamiento interno.



## 2. Compilación en sistemas embebidos

La compilación varía dependiendo del dispositivo (microcontrolador o FPGA).

### 2.1. Para microcontroladores

* Se utiliza un **toolchain cruzado (cross-compiler)**, ya que el código se compila en la PC y se ejecuta en el microcontrolador.
* Componentes principales:

  * **Compilador** (por ejemplo GCC para ARM, herramientas propietarias como Keil o IAR)
  * **Ensamblador**
  * **Linker** (que une las bibliotecas y genera el archivo final *.elf* o *.hex*)
  * **Loader/Flasher** para transferir el binario al dispositivo.

### 2.2. Para FPGAs

* En vez de generar un ejecutable como tal, el flujo incluye generación de **bitstream** mediante síntesis de HDL.
* Fases principales:

  1. Síntesis (HDL → lógica intermedia)
  2. Mapeo y colocación (placing)
  3. Ruteo (routing)
  4. Generación del bitstream

Herramientas típicas incluyen **Xilinx Vivado**, **Intel (Altera) Quartus**, etc.
## Ejemplo de Tarjeta FPGA:
![images](https://github.com/user-attachments/assets/222b765c-7233-454d-876f-a4dc131d7638)


## 3. Técnicas de depuración en sistemas embebidos

### 3.1. Depuración en microcontroladores

* **JTAG / SWD**: Interfaces para inspeccionar registros, memoria, poner breakpoints, etc.
* **UART / Serial Debugging**: Envía mensajes de estado o logging desde el firmware hacia el exterior para diagnóstico.
* **Depuración por LED / GPIO**: Indicadores simples que muestran estados internos críticos.
* **Simuladores / Emuladores**: Permiten probar sin hardware real, o antes de desplegarlo.

### 3.2. Depuración en FPGAs

* **Instrumentación interna (Logic Analyzers integrados)**, como Xilinx ILA o Intel SignalTap, para observar señales internas en tiempo real.
* **Testbenches / Simulación previa**: Probar módulos HDL (VHDL / Verilog) antes de síntesis.
* **Depuración en hardware (“in-circuit debugging”)**, inserción de bloques específicos para monitorizar.
* **Boundary Scan / JTAG Scan** para verificar interconexiones físicas y buses.



## 4. Herramientas de software comunes

* **Entornos integrados (IDEs)**: STM32CubeIDE, Vivado, Quartus, ModelSim, IAR, etc.
* **Depuradores (Debuggers)**: GDB, OpenOCD, herramientas propietarias como los IDEs de Xilinx/Intel, etc.
* **Analizadores externos**: Osciloscopios, analizadores lógicos físicos.



## 5. Retos en la depuración

* Recursos limitados (memoria, CPU) impiden logging exhaustivo.
* Paralelismo, concurrencia y temporización (timing) en FPGAs complican reproducir errores.
* Interacción complejo hardware-software, errores intermitentes.
* Tiempo que toma recompilar, sintetizar, colocar, rutear para hacer cambios o agregar observabilidad.



## 6. Contribuciones académicas recientes y casos de estudio

* Microsemi. *In-Circuit FPGA Debug – Challenges and Solutions* analiza enfoques distintos de depuración incorporada en FPGA, comparando ventajas y desventajas ([ww1.microchip.com](https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ProductDocuments/SupportingCollateral/in_circuit_fpga_debug_challenges_solutions.pdf?utm_source=chatgpt.com)).
* Samarjit, K., et al. (2020). *Debugging FPGA-accelerated Real-time Systems* propone metodologías híbridas de *tracing* ([cs.unc.edu](https://www.cs.unc.edu/~samarjit/papers/rtas2020.pdf?utm_source=chatgpt.com)).
* Fiala, G., Scheipel, T., Neuwirth, W., & Baunach, M. (2020). *FPGA-Based Debugging with Dynamic Signal Selection at Run-Time* presenta depuración flexible sin recompilar todo el flujo ([ceur-ws.org](https://ceur-ws.org/Vol-2581/ase2020paper3.pdf?utm_source=chatgpt.com)).
* Tejeswara Rao, P., et al. (2025). *Low-Latency UART Communication Interface Implemented On FPGA* muestra el rol de UART como interfaz para depuración ([ijcrt.org](https://www.ijcrt.org/papers/IJCRT2504507.pdf?utm_source=chatgpt.com)).



## 7. Conclusión

La compilación y depuración en sistemas embebidos, especialmente con FPGAs, requieren métodos especializados que integren hardware y software. Los avances actuales mejoran la observabilidad y reducen tiempos de diagnóstico, aunque los desafíos de recursos limitados y complejidad en hardware paralelo permanecen.

---

## Referencias

* Fiala, G., Scheipel, T., Neuwirth, W., & Baunach, M. (2020). *FPGA-Based Debugging with Dynamic Signal Selection at Run-Time*. ASE Workshops. CEUR-WS.
* Microsemi. (2014). *In-Circuit FPGA Debug – Challenges and Solutions*. Microchip Technology.
* Samarjit, K., et al. (2020). *Debugging FPGA-accelerated Real-time Systems*. Proceedings of RTAS 2020.
* Tejeswara Rao, P., Karthik, P., Balaji Pallampati, J. C., & Bodapati, R. (2025). *Low-Latency UART Communication Interface Implemented On FPGA*. IJCRT, 13(4).
* Venkata Sai Raghava, V., & Kumar, M. R. (2025). *Digital System Design of FPGA-Based UART Protocol Using Verilog HDL*. IJCESEN, 11(3), 5878-5886.
