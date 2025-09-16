# Tipos de Programación en FPGA

**Nombre:** Lizeth Roxana Castro Reyes - 22211535  
**Materia:** Sistemas Programables  
**Fecha:** 15 de septiembre de 2025  

La programación en FPGA (Field Programmable Gate Array) consiste en configurar una matriz de bloques lógicos y conexiones internas para que ejecuten una función digital específica. A diferencia de un microprocesador, que sigue instrucciones secuenciales, una FPGA trabaja en paralelo, permitiendo gran velocidad y flexibilidad para tareas como procesamiento de señales, visión artificial, telecomunicaciones o sistemas embebidos.

---

## 1. Programación en HDL (Hardware Description Language)

Los lenguajes de descripción de hardware (HDL) permiten definir el comportamiento del circuito digital a nivel de compuertas lógicas y registros.  
Los más utilizados son **VHDL** y **Verilog**.  

<img width="551" height="238" alt="imagen" src="https://github.com/user-attachments/assets/041835a9-ceb0-4bd4-b823-1121fdd731fd" />


- **Características:**
  - Bajo nivel, control detallado del hardware.
  - Alta optimización en recursos y rendimiento.
  - Curva de aprendizaje pronunciada.

- **Ejemplo en plataformas:**
  - **Xilinx (Vivado Design Suite):** Implementación de un controlador UART en VHDL o Verilog.
  - **Intel/Altera (Quartus Prime):** Desarrollo de un contador binario en Verilog.

---

## 2. Programación basada en HLS (High Level Synthesis)

El **HLS (Síntesis de Alto Nivel)** permite programar FPGAs usando lenguajes de alto nivel como **C, C++ o SystemC**, que posteriormente se convierten en hardware mediante herramientas de síntesis.

<img width="557" height="272" alt="imagen" src="https://github.com/user-attachments/assets/7fff117f-b069-4c7a-b476-2ad2f10643e5" />


- **Características:**
  - Nivel de abstracción más alto.
  - Desarrollo más rápido y fácil de mantener.
  - Menor optimización comparado con HDL, pero balanceado en productividad.

- **Ejemplo en plataformas:**
  - **Xilinx (Vitis HLS):** Implementación de un algoritmo de procesamiento de imágenes en C++ que se traduce a hardware.
  - **Intel/Altera (Intel HLS Compiler):** Desarrollo de un filtro FIR en C++ optimizado para DSPs dentro del FPGA.

---

## 3. Programación mediante IP Cores y Block Design

Consiste en utilizar bloques predefinidos de hardware (**IP cores**) que se integran gráficamente mediante entornos de desarrollo.

<img width="2048" height="965" alt="EAVB-IP-Core-Block-Diagram-01-01" src="https://github.com/user-attachments/assets/dff02b2c-ea0c-466c-88ac-6367c7195645" />

- **Características:**
  - Uso visual e intuitivo.
  - Ideal para integración rápida de sistemas complejos (procesadores, memorias, periféricos).
  - Dependencia de bibliotecas del fabricante.

- **Ejemplo en plataformas:**
  - **Xilinx (Vivado IP Integrator):** Construcción de un sistema basado en MicroBlaze (soft-core).
  - **Intel/Altera (Platform Designer - antes Qsys):** Diseño de un sistema con Nios II (soft-core) y periféricos conectados por buses.

---

## 4. Programación con OpenCL

OpenCL permite programar FPGAs desde la perspectiva del cómputo heterogéneo, orientado a **aceleración de aplicaciones de alto rendimiento (HPC)**.

<img width="897" height="323" alt="imagen" src="https://github.com/user-attachments/assets/57e31824-86f2-434b-98ba-f140534b6268" />


- **Características:**
  - Uso de kernels en OpenCL.
  - Adecuado para procesamiento paralelo intensivo.
  - Facilita la integración con CPUs y GPUs.

- **Ejemplo en plataformas:**
  - **Xilinx (SDAccel / Vitis):** Aceleración de cálculos matemáticos en paralelo.
  - **Intel (Intel FPGA SDK for OpenCL):** Implementación de un algoritmo de Machine Learning para clasificación de datos.

---

# Conclusión

La programación en FPGA representa una de las alternativas más potentes para el diseño de sistemas digitales, ya que combina la flexibilidad del software con el rendimiento del hardware dedicado. Dependiendo de las necesidades del proyecto, se puede optar por lenguajes de bajo nivel (HDL) para un control detallado, herramientas de alto nivel (HLS) para acelerar el desarrollo de algoritmos complejos, o entornos de diseño por bloques para simplificar la implementación en áreas como control y procesamiento de señales.

Las plataformas más demandadas, **Xilinx (Vivado/Vitis)** e **Intel/Altera (Quartus/Intel HLS)**, ofrecen soporte a todas estas metodologías, permitiendo al desarrollador elegir la que mejor equilibre **rendimiento, complejidad y productividad**.

---

# Referencias

- Data Center Knowledge. (2023, agosto 17). What is an FPGA? Definition, Types, Programming, and More. Datacenterknowledge.com; DataCenterKnowledge. https://www.datacenterknowledge.com/data-center-hardware/what-is-an-fpga-definition-types-programming-and-more

- Kamunya, T. (2023, enero 31). ¿Cómo funciona la programación FPGA? Geekflare Spain. https://geekflare.com/es/fpga-programming/

- Romero, J. (2021, diciembre 21). ¿Qué es un FPGA y para qué sirve? GEEKNETIC. https://www.geeknetic.es/FPGA/que-es-y-para-que-sirve
