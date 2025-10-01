# 🧠 Optimización de Código en Sistemas Embebidos  
## 📦 Gestión de Memoria, 🔋 Eficiencia Energética y ⏱️ Reducción de Latencia

Alumno: Ivan Gustavo Mendoza Suárez

No. de Control: 22210910

Fecha de Elaboración: 17 de septiembre del 2025

---

## 📑 Índice

1. [Introducción](#introducción)
2. [🧠 Gestión de Memoria](#gestión-de-memoria)
   - [Uso de Memoria Estática vs Dinámica](#uso-de-memoria-estática-vs-dinámica)
   - [Fragmentación y Punteros](#fragmentación-y-punteros)
   - [Herramientas y Estrategias de Optimización](#herramientas-y-estrategias-de-optimización)
3. [🔋 Eficiencia Energética](#eficiencia-energética)
   - [Técnicas para Reducir el Consumo de Energía](#técnicas-para-reducir-el-consumo-de-energía)
   - [Monitoreo y Perfilado Energético](#monitoreo-y-perfilado-energético)
4. [⏱️ Reducción de Latencia](#reducción-de-latencia)
   - [Manejo de Interrupciones](#manejo-de-interrupciones)
   - [Optimización de Algoritmos en Tiempo Real](#optimización-de-algoritmos-en-tiempo-real)
   - [Estrategias Avanzadas para Minimizar la Latencia](#estrategias-avanzadas-para-minimizar-la-latencia)
5. [🎯 Conclusión](#conclusión)
6. [📚 Bibliografía](#bibliografía)

---

## 🧠 Introducción

Los sistemas embebidos son dispositivos diseñados para ejecutar tareas específicas de manera eficiente, utilizando recursos limitados de memoria, procesamiento y energía. Estos sistemas están presentes en aplicaciones críticas, como dispositivos médicos, automóviles inteligentes y equipos de telecomunicaciones. Por ello, la optimización del código es un factor determinante para garantizar tanto la confiabilidad como la eficiencia operativa. Este documento se centra en tres aspectos fundamentales: la **gestión de memoria**, la **eficiencia energética** y la **reducción de latencia**, explicando estrategias y herramientas modernas para mejorar el desempeño de los sistemas embebidos, apoyadas en literatura actual y fuentes confiables.

---

## 🧠 Gestión de Memoria

La memoria es uno de los recursos más limitados en sistemas embebidos, por lo que su correcta administración es crítica. Una mala gestión puede derivar en errores, fugas de memoria y fallos de rendimiento, afectando la estabilidad del sistema.

### 💾 Uso de Memoria Estática vs Dinámica

La memoria estática se asigna en tiempo de compilación y permite predecir exactamente cuánta memoria se utilizará durante la ejecución. Esto reduce riesgos de fragmentación y mejora la confiabilidad, especialmente en sistemas críticos donde cada byte cuenta. Por otro lado, la memoria dinámica se asigna en tiempo de ejecución, proporcionando flexibilidad para tareas que requieren almacenamiento temporal o variable. Sin embargo, su uso indebido puede provocar fragmentación y fugas de memoria, lo que complica la gestión a largo plazo. Por ello, los desarrolladores deben balancear cuidadosamente entre memoria estática y dinámica según la aplicación.

- Ventaja principal de la memoria estática: predictibilidad y seguridad.  
- Ventaja principal de la memoria dinámica: flexibilidad y adaptabilidad.

### 🔗 Fragmentación y Punteros

La fragmentación de memoria es un problema común en sistemas embebidos que utilizan memoria dinámica extensivamente. Cuando la memoria libre se encuentra dispersa en pequeños bloques, se dificulta la asignación de grandes estructuras de datos. Además, el manejo de punteros incorrecto puede generar punteros colgantes, accesos inválidos y fugas de memoria, afectando la estabilidad y seguridad del sistema. Por ello, es recomendable minimizar el uso de punteros complejos y asegurarse de liberar correctamente cualquier memoria asignada dinámicamente.

### 🛠️ Herramientas y Estrategias de Optimización

Para mejorar la gestión de memoria, los ingenieros utilizan análisis de mapas de memoria y herramientas de perfilado que permiten identificar funciones o estructuras que consumen más recursos. También se recomienda el uso de estructuras de datos compactas y buffers preasignados que reducen la fragmentación. Otra estrategia efectiva es el uso de memoria estática siempre que sea posible, para garantizar un comportamiento predecible y estable del sistema.

---

## 🔋 Eficiencia Energética

En sistemas embebidos, el consumo energético es un factor crítico, especialmente en dispositivos portátiles o IoT, donde la duración de la batería determina la operatividad. La eficiencia energética no solo prolonga la vida útil del dispositivo, sino que también mejora la confiabilidad y reduce costos operativos.

### ⚡ Técnicas para Reducir el Consumo de Energía

Entre las técnicas más efectivas se encuentran los modos de bajo consumo, como *sleep* o *deep sleep*, que permiten que el procesador y periféricos se apaguen parcialmente cuando no se utilizan. Otra estrategia importante es el escalado dinámico de voltaje y frecuencia (DVFS), que ajusta automáticamente el voltaje y la velocidad del procesador según la carga de trabajo, optimizando la energía sin afectar el rendimiento. Finalmente, la optimización de algoritmos también influye directamente en la eficiencia energética, ya que algoritmos más rápidos y ligeros consumen menos recursos.

### 📊 Monitoreo y Perfilado Energético

El monitoreo del consumo energético permite identificar rutinas o procesos que consumen más energía de lo necesario. Herramientas como EnergyTrace y STM32CubeMonitor-Power proporcionan métricas detalladas que ayudan a ajustar el comportamiento del sistema y tomar decisiones de optimización más informadas. Este perfilado es especialmente útil en dispositivos IoT donde cada miliamperio cuenta.

---

## ⏱️ Reducción de Latencia

La latencia, definida como el tiempo de respuesta entre un evento y la reacción del sistema, es crucial en sistemas embebidos de tiempo real. Una latencia elevada puede comprometer la seguridad y efectividad de la aplicación.

### 🚦 Manejo de Interrupciones

La correcta priorización de interrupciones garantiza que los eventos críticos se procesen primero. Además, minimizar las interrupciones anidadas y gestionar adecuadamente los buffers circulares reduce la sobrecarga del procesador y mejora la predictibilidad del sistema.

### 📈 Optimización de Algoritmos en Tiempo Real

La selección de algoritmos de baja complejidad y su adaptación al hardware disponible son estrategias clave para reducir la latencia. Aprovechar características del procesador, como pipelines o instrucciones SIMD, puede mejorar significativamente la eficiencia.

### 🏎️ Estrategias Avanzadas para Minimizar la Latencia

El uso de un sistema operativo en tiempo real (RTOS) permite planificar tareas de manera eficiente y garantizar que los procesos críticos se ejecuten dentro de los límites de tiempo establecidos. Además, técnicas como prefetching de instrucciones y datos ayudan a mantener el flujo de ejecución rápido y constante.

---

## 🖼️ Diagrama: Arquitectura de un Sistema Embebido

![Diagrama de arquitectura de un sistema embebido](https://tse1.mm.bing.net/th/id/OIP.uwrcdnB2bmxCs-wgzZRHogHaFj?r=0&pid=Api)

*Fuente: Sistemas Embebidos – Semestre Enero–Junio, Bing Images*

---

## 🎯 Conclusión

La optimización de código en sistemas embebidos es un proceso integral que abarca la gestión de memoria, la eficiencia energética y la reducción de latencia. La correcta implementación de estas estrategias mejora la confiabilidad, el rendimiento y la duración de los dispositivos, haciendo que los sistemas embebidos sean más eficientes y robustos en entornos críticos.

---

## 📚 Bibliografía

- Ganssle, J. (2016). *The Art of Designing Embedded Systems* (2nd ed.). Elsevier.  
- Yiu, J. (2013). *The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors* (3rd ed.). Newnes.  
- Szpiech, M. (2024). *Part 2: Memory Optimization in Embedded Systems in the C Language*. Comarch. Recuperado de [link](https://www.comarch.com/sw-and-hw-services/blog/part-2-memory-optimization-in-embedded-systems-in-the-c-language-ram/)  
- Harvie, L. (2024). *Addressing Latency and Jitter in Time-Critical Firmware Applications*. Medium. Recuperado de [link](https://medium.com/@lanceharvieruntime/addressing-latency-and-jitter-in-time-critical-firmware-applications-b1a03172981a)  
