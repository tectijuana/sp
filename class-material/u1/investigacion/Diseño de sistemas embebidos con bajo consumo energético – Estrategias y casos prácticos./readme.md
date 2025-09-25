# Jorge Luis Castro Alvarado 22211533 
# Diseño de Sistemas Embebidos de Bajo Consumo – Estrategias y Casos Prácticos

Este repositorio contiene una investigación sobre las metodologías y técnicas para el diseño de sistemas embebidos de bajo consumo energético.
## Resumen de la Investigación (Por gemini 2.5) 
---
# PROMPT UTILIZADO:
  
* "A partir del documento de investigación proporcionado, necesito que generes lo siguiente en formato Markdown:

1.  Un resumen conciso del informe, optimizado para ser incluido en el archivo `README.md` de un repositorio de GitHub. Debe capturar los puntos clave, las estrategias principales y las conclusiones más importantes de la investigación.
2.  Al final, escribe la lista de las fuentes de información que fueron consultadas para elaborar el documento, de forma ordenada y en formato markdown."

El diseño de bajo consumo es un enfoque holístico que requiere la optimización conjunta de hardware y software para minimizar el consumo de energía, extender la autonomía de la batería, mejorar la gestión térmica y aumentar la fiabilidad del sistema.
--- 
### 1. Fundamentos del Consumo Energético

El consumo en circuitos CMOS se divide en dos categorías principales:

*   **Potencia Dinámica ($P_{dyn}$):** Energía consumida durante la conmutación de los transistores (estado activo). Es proporcional a la capacitancia ($C$), al cuadrado del voltaje de alimentación ($V_{DD}$) y a la frecuencia de reloj ($f$).
    $$P_{dyn} \propto C \cdot V_{DD}^2 \cdot f$$
*   **Potencia Estática ($P_{static}$):** Energía consumida por las corrientes de fuga cuando el dispositivo está inactivo. Su importancia ha crecido exponencialmente con la miniaturización de los transistores.

### 2. Estrategias de Optimización a Nivel de Hardware

La base de un sistema eficiente se establece en el hardware.

*   **Selección de Componentes de Ultra-Bajo Consumo (ULP):** Elegir microcontroladores (MCUs), sensores y módulos de comunicación con modos de sueño profundos (consumo en nA o µA), bajo voltaje de operación y periféricos autónomos (como DMA) que operen sin despertar a la CPU.
*   **Diseño Eficiente de la Fuente de Alimentación:** Utilizar reguladores de conmutación (DC-DC) por su alta eficiencia (>90%) en lugar de LDOs. Implementar **dominios de potencia** para apagar completamente secciones del hardware que no se están utilizando.
*   **Técnicas a Nivel de Chip (SoC/ASIC):**
    *   **Escalado Dinámico de Voltaje y Frecuencia (DVFS):** Ajustar dinámicamente el voltaje y la frecuencia del procesador según la carga de trabajo para un ahorro energético cuadrático.
    *   ***Clock Gating* (Compuerta de Reloj):** Desactivar la señal de reloj en los módulos lógicos inactivos para eliminar el consumo de potencia dinámica innecesario.
    *   ***Power Gating* (Compuerta de Potencia):** Desconectar completamente la alimentación de bloques enteros del chip para eliminar la potencia de fuga (estática) durante largos períodos de inactividad.

### 3. Estrategias de Optimización a Nivel de Software

El software determina cuán eficientemente se utiliza el hardware.

*   **Gestión de Modos de Bajo Consumo:** El firmware debe maximizar el tiempo que el sistema pasa en el modo de reposo más profundo posible (ej. Stop, Standby, Shutdown), despertando solo cuando sea estrictamente necesario.
*   **Arquitectura Dirigida por Eventos:** Reemplazar los bucles de sondeo (*polling*) por un modelo basado en interrupciones. El sistema permanece en modo de bajo consumo (`WFI` - Wait For Interrupt) hasta que un evento (temporizador, dato de sensor, etc.) lo despierta. Este es el principio de la **"carrera hacia el reposo" (*race-to-idle*)**.
*   **Firmware Consciente de la Energía:**
    *   **Algoritmos Eficientes:** Reducir la complejidad computacional para terminar las tareas más rápido y volver al estado de reposo.
    *   **Optimización del Compilador:** Usar banderas de optimización para tamaño de código (`-Os`) para reducir accesos a memoria.
    *   **Gestión de Periféricos:** Habilitar los relojes de los periféricos solo cuando se usan y deshabilitarlos inmediatamente después.

### 4. Validación y Metodología

El diseño de bajo consumo es un proceso iterativo y empírico.

1.  **Crear un Presupuesto de Potencia (*Power Budget*):** Estimar el consumo promedio del dispositivo antes de comenzar el diseño.
2.  **Medir, No Adivinar:** Utilizar herramientas de perfilado de potencia (ej. Nordic PPK2, Joulescope) para medir el consumo real y correlacionarlo con la ejecución del código.
3.  **Optimizar:** Identificar "vampiros energéticos" en el hardware o software y aplicar las estrategias de optimización correspondientes.

### 5. Conclusión

El diseño exitoso de sistemas embebidos de bajo consumo no se logra con una única solución, sino a través de un **co-diseño hardware-software** riguroso y un ciclo continuo de **planificación, medición y optimización**. Adoptar un enfoque basado en estados, maximizar el tiempo de inactividad y validar cada decisión con mediciones empíricas son las claves para crear dispositivos eficientes, autónomos y fiables.

Por supuesto. Aquí tienes una lista con las principales fuentes de información utilizadas para la elaboración de la investigación, organizadas por temas y en formato Markdown.

### Fuentes Principales de la Investigación

#### Fundamentos y Conceptos Generales
*  ([https://www.innovaciondigital360.com/iot/sistemas-embebidos-que-son-y-para-que-se-utilizan/](https://www.innovaciondigital360.com/iot/sistemas-embebidos-que-son-y-para-que-se-utilizan/)) - InnovaciónDigital360
*  ([http://untref.edu.ar/wpcontent/uploads/2013/02/Sistemas-Embebidos-Plan-2013.pdf](http://untref.edu.ar/wpcontent/uploads/2013/02/Sistemas-Embebidos-Plan-2013.pdf)) - Universidad Nacional de Tres de Febrero

#### Estrategias de Optimización a Nivel de Hardware
*  ([https://anysilicon.com/power-gating/](https://anysilicon.com/power-gating/)) - AnySilicon
*  ([https://anysilicon.com/the-ultimate-guide-to-clock-gating/](https://anysilicon.com/the-ultimate-guide-to-clock-gating/)) - AnySilicon
*   [¿Cómo elegir el microcontrolador adecuado para su proyecto?](https://www.tme.eu/es/news/library-articles/page/58382/como-elegir-el-microcontrolador-adecuado-para-su-proyecto/) - TME.eu

#### Estrategias de Optimización a Nivel de Software y Arquitectura
*   [Arm Cortex-M low-power mode fundamentals](https://www.embedded.com/arm-cortex-m-low-power-mode-fundamentals/) - Embedded.com
*  ([https://aws.amazon.com/es/what-is/eda/](https://aws.amazon.com/es/what-is/eda/)) - Amazon Web Services (AWS)

#### Casos de Estudio y Aplicaciones Prácticas
*  ([https://pmc.ncbi.nlm.nih.gov/articles/PMC5124429/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5124429/)) - PMC (PubMed Central) 
*  ([https://www.researchgate.net/publication/391107128_Design_and_Deployment_of_Low-Power_IoT_Sensor_Networks_for_Sustainable_Energy_Monitoring_in_Industrial_Automation](https://www.researchgate.net/publication/391107128_Design_and_Deployment_of_Low-Power_IoT_Sensor_Networks_for_Sustainable_Energy_Monitoring_in_Industrial_Automation)) - ResearchGate

#### Herramientas y Metodologías de Validación
*   [Power Profiler Kit II](https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2) - Nordic Semiconductor 
*   [Energy Profiler](https://www.silabs.com/software-and-tools/simplicity-studio/energy-profiler) - Silicon Labs 

#### Horizontes Futuros y Desafíos Emergentes
*  ([https://www.embedur.ai/reducing-energy-demand-of-ai-with-edge-computing/](https://www.embedur.ai/reducing-energy-demand-of-ai-with-edge-computing/)) - embedUR 
*  ([https://onomondo.com/blog/iot-security-issues-and-solutions-low-power-devices/](https://onomondo.com/blog/iot-security-issues-and-solutions-low-power-devices/)) - Onomondo 
