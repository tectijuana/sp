# TECNOLÓGICO NACIONAL DE MÉXICO INSTITUTO TECNOLÓGICO DE TIJUANA
## Subdirección académica departamento de sistemas y computación

**Semestre:** Enero - Junio

**Carrera:** Sistemas computacionales

**Grupo:** SC7B

**Materia:** Lenguajes de interfaz SCC-1014

**Titulo:** Herramientas de simulación y modelado en el diseño de sistemas programables
 
**Unidad:** 1

**Alumno:** 
 - Roldan Castro Luis Alberto

**Docente:**
  Rene Solis Reyes

## **El Papel Crucial de la Simulación y el Modelado en el Diseño de Sistemas Programables**
En el ámbito del diseño de sistemas programables, como los FPGAs (Field-Programmable Gate Arrays) y los sistemas embebidos, la simulación y el modelado no son simplemente un paso más, sino la base para lograr sistemas confiables, eficientes y sólidos. Estas herramientas ayudan a prever cómo se comportará un diseño, a detectar errores antes de llevarlo al hardware —lo cual puede ser muy costoso— y a reducir significativamente el tiempo de desarrollo. Por eso, su uso resulta esencial para impulsar la innovación en áreas como telecomunicaciones, automoción, inteligencia artificial y computación de alto rendimiento.

![FPGAs](https://digitalsystemdesign.in/wp-content/uploads/2019/05/test_ckt.png)

## Modelado: La Abstracción del Comportamiento del Hardware
El modelado se entiende como el proceso de crear una representación abstracta de un sistema o de uno de sus componentes. En el caso de los sistemas programables, este proceso se lleva a cabo principalmente mediante Lenguajes de Descripción de Hardware (HDLs). Los más utilizados son:
- VHDL (Very High-Speed Integrated Circuit Hardware Description Language): Es un lenguaje fuertemente tipado, desarrollado originalmente por el Departamento de Defensa de los Estados Unidos. Su sintaxis es estricta y bastante extensa, lo que permite reducir la probabilidad de errores en el diseño (Ashenden, 2008).
![VHDL](https://www.fpgakey.com/uploads/images/original/20200619/015014vhdl.jpg)
- Verilog: Presenta una sintaxis más parecida al lenguaje de programación C, lo que lo hace más accesible para personas con experiencia en software. Es uno de los más empleados en la industria, sobre todo en Norteamérica, y es muy común en el diseño de ASICs (Application-Specific Integrated Circuits) (Palnitkar, 2003).
![Verilog](https://numato.com/help/wp-content/uploads/2016/04/mimasv2leds.png)
El propósito del modelado es describir cómo funciona un circuito, ya sea detallando su estructura a nivel de compuertas lógicas o utilizando un nivel de abstracción más alto, como el modelo de comportamiento (Behavioral Model). Este último permite enfocarse en la lógica y funcionalidad del sistema sin tener que preocuparse, en un inicio, por los detalles físicos de su implementación.

### Simulación: La Verificación Funcional del Diseño
La simulación es el proceso de utilizar un modelo para imitar el comportamiento del sistema real a lo largo del tiempo. Un software de simulación, o simulador, interpreta el código HDL y calcula las señales de salida en respuesta a un conjunto de entradas de estímulo definidas en un banco de pruebas o testbench.

El propósito fundamental de la simulación es la verificación funcional, es asegurar que el diseño se comporta tal y como se especifica en los requisitos. "La verificación consume ahora hasta el 70% del esfuerzo total de diseño de un sistema en chip (SoC) complejo" (Foster, 2013). Esto subraya la importancia crítica de la simulación para detectar errores en las primeras etapas, cuando su corrección es órdenes de magnitud más barata y rápida que después de la fabricación del chip.

### Herramientas Clave en la Industria
El ecosistema de herramientas de diseño electrónico ofrece varias opciones para trabajar con modelado y simulación. Algunas de las más importantes son:
- ModelSim/Questa (Siemens EDA): Durante mucho tiempo ha sido el estándar en simulación de HDL, con soporte para VHDL, Verilog y SystemVerilog, destacando por su rendimiento y depuración.
- Xilinx Vivado Design Suite: Plataforma de Xilinx (ahora AMD) que integra simulación, síntesis, implementación y depuración en un solo entorno.
- Intel Quartus Prime: Herramienta de Intel (antes Altera) con simulador propio y funciones como SignalTap para depuración en hardware.
- MATLAB/Simulink (MathWorks): Muy usado en Diseño Basado en Modelos (Model-Based Design). Permite diseñar con diagramas de bloques y generar automáticamente código HDL (MathWorks, s.f.).

### Beneficios del Uso de Simulación y Modelado
La adopción de estas herramientas ofrece ventajas transformadoras en el ciclo de diseño:
1.	Detección Temprana de Errores: Permite identificar fallos lógicos o de comportamiento antes de la costosa implementación en el hardware físico.
2.	Reducción de Costos y Tiempo: Al minimizar el número de iteraciones de hardware, se reduce drásticamente el tiempo de llegada al mercado y los costos asociados a prototipos fallidos.
3.	Verificación Exhaustiva: Los bancos de pruebas automatizados pueden simular millones de ciclos de reloj y probar el diseño en una multitud de escenarios, incluyendo casos extremos que serían difíciles o imposibles de replicar en un laboratorio físico.
4.	Exploración del Espacio de Diseño: Los diseñadores pueden experimentar rápidamente con diferentes arquitecturas y algoritmos a nivel de modelo para encontrar la solución óptima en términos de rendimiento, área y consumo de energía antes de escribir una sola línea de código HDL detallado.

### Referencias Citadas
- Ashenden, P. J. (2008). The Designer's Guide to VHDL (3rd ed.). Morgan Kaufmann.
- Foster, H. (2013). The 2013 Wilson Research Group Functional Verification Study. Mentor Graphics.
- MathWorks. (s.f.). HDL Coder. Recuperado de https://www.mathworks.com/products/hdl-coder.html
- Palnitkar, S. (2003). Verilog HDL: A Guide to Digital Design and Synthesis (2nd ed.). Prentice Hall.
