# Tipos de Programación en FPGA

**Nombre:** Lizeth Roxana Castro Reyes - 22211535  
**Materia:** Sistemas Programables  
**Fecha:** 15 de septiembre de 2025  

La programación en FPGA (Field Programmable Gate Array) consiste en configurar una matriz de bloques lógicos y conexiones internas para que ejecuten una función digital específica. A diferencia de un microprocesador, que sigue instrucciones secuenciales, una FPGA trabaja en paralelo, permitiendo gran velocidad y flexibilidad para tareas como procesamiento de señales, visión artificial, telecomunicaciones o sistemas embebidos.

---

## 1. Tipos

Los lenguajes de descripción de hardware (HDL) permiten definir el comportamiento del circuito digital a nivel de compuertas lógicas y registros.  
Los más utilizados son **VHDL** y **Verilog**.  

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

- **Características:**
  - Uso de kernels en OpenCL.
  - Adecuado para procesamiento paralelo intensivo.
  - Facilita la integración con CPUs y GPUs.

- **Ejemplo en plataformas:**
  - **Xilinx (SDAccel / Vitis):** Aceleración de cálculos matemáticos en paralelo.
  - **Intel (Intel FPGA SDK for OpenCL):** Implementación de un algoritmo de Machine Learning para clasificación de datos.

---

# Conclusión

En resumen, los principales **tipos de programación en FPGA** abarcan desde lenguajes de bajo nivel como **VHDL/Verilog**, hasta enfoques de alto nivel como **HLS y OpenCL**, pasando por la integración visual de **IP cores**.  

Las plataformas más demandadas, **Xilinx (Vivado/Vitis)** e **Intel/Altera (Quartus/Intel HLS)**, ofrecen soporte a todas estas metodologías, permitiendo al desarrollador elegir la que mejor equilibre **rendimiento, complejidad y productividad**.

