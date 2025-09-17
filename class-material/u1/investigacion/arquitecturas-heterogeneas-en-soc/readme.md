# Arquitecturas Heterogéneas en System-on-Chip (SoC) – Combinación de CPU, GPU, FPGA y NPU

**Autor:** Oscar Esteban Pacheco Cabrera

## Introducción a la Computación Heterogénea en SoC

### Definición y Evolución del SoC 

Un System-on-a-Chip (SoC) es un circuito integrado que consolida todos o la mayoría de los componentes funcionales de un ordenador u otro sistema electrónico en un único chip. A diferencia de un sistema tradicional basado en una placa base, donde la CPU, la GPU, la memoria y los puertos de E/S son componentes separados, un SoC integra todos estos elementos en un solo sustrato de silicio. Esta consolidación minimiza el tamaño, el peso y el consumo de energía, lo que lo convierte en una solución ideal para dispositivos con restricciones de espacio y batería, como teléfonos inteligentes, tabletas, consolas de videojuegos y sistemas embebidos. Actualmente, la tecnología SoC también se está expandiendo a ordenadores personales, servidores y vehículos, demostrando su versatilidad y eficiencia en una amplia gama de aplicaciones.

El diseño compacto de los SoC mejora la velocidad de comunicación entre los componentes cruciales, lo que resulta en un rendimiento más rápido y una experiencia de usuario más fluida. Además, al reducir la necesidad de transferencias de datos entre chips separados, los SoC minimizan el consumo de energía, extendiendo la duración de la batería, un factor crítico en dispositivos móviles y portátiles.

### La Transición a la Heterogeneidad

El modelo monolítico de procesamiento, centrado en una CPU única, ha demostrado ser un "todoterreno" capaz de manejar una amplia variedad de tareas de propósito general. Sin embargo, esta versatilidad tiene un costo: la falta de especialización. La búsqueda de una mayor eficiencia energética y un rendimiento superior para cargas de trabajo específicas, como gráficos, simulaciones científicas e inteligencia artificial, ha impulsado un cambio fundamental en el diseño de los chips. En lugar de depender de un solo procesador, la arquitectura moderna ha adoptado un enfoque heterogéneo, que integra múltiples procesadores especializados para que cada uno se encargue de la tarea para la que está mejor optimizado.

Esta transición de la arquitectura monolítica a la heterogénea es una respuesta estratégica a las limitaciones de las leyes de la física y a las exigencias del mercado. En un diseño de chip, la optimización para una tarea particular, como las operaciones de matriz masivas para la IA, a menudo compromete la eficiencia para otras cargas de trabajo, como la ejecución de código secuencial o el manejo de bifurcaciones. La integración de aceleradores en el SoC no es simplemente un aumento de la potencia de cálculo, sino una redefinición de cómo se diseñan los sistemas para maximizar el rendimiento por vatio. Esta estrategia permite que la carga de trabajo se distribuya de manera inteligente, asignando cada tarea al procesador más adecuado. Este cambio fundamental en la filosofía de diseño es lo que impulsa las decisiones arquitectónicas de los principales fabricantes de semiconductores.

## Roles y Funciones de los Componentes

### CPU

La Unidad Central de Procesamiento (CPU) es el "cerebro" de un ordenador y es fundamental en cualquier SoC. Su función principal es ejecutar instrucciones, realizar operaciones aritméticas y lógicas, y coordinar todas las operaciones de hardware y software del sistema. En un SoC heterogéneo, la CPU se especializa en cargas de trabajo de propósito general que requieren baja latencia y un procesamiento secuencial rápido, como la ejecución del sistema operativo, la gestión de la memoria y el control de las aplicaciones. A diferencia de la GPU, la CPU se caracteriza por tener un número menor de núcleos, pero de mayor potencia y con cachés muy rápidas para manejar de manera eficiente las dependencias de datos.

### GPU

La Unidad de Procesamiento Gráfico (GPU), inicialmente concebida para el renderizado de gráficos y el procesamiento visual , ha evolucionado para convertirse en un acelerador de propósito general (GPGPU) capaz de manejar una amplia gama de tareas intensivas en cálculo. Su arquitectura única consiste en miles de núcleos de procesamiento más simples que los de la CPU, diseñados para ejecutar simultáneamente operaciones idénticas en grandes conjuntos de datos, lo que se conoce como procesamiento en paralelo. Esta capacidad masiva de paralelismo hace que las GPU sean ideales para aplicaciones como el aprendizaje automático, las simulaciones científicas, la edición de vídeo y el renderizado 3D.

### FPGA
Una Matriz de Puertas Programables en Campo (FPGA) es un tipo de circuito integrado cuya lógica interna no está "cableada" de forma permanente. En su lugar, puede ser programada y reconfigurada por el usuario a través de software, incluso después de la fabricación. Esta flexibilidad es su mayor ventaja, lo que permite a los diseñadores crear hardware personalizado para tareas específicas que requieren un control estricto de la latencia y la eficiencia energética. Las FPGA son especialmente adecuadas para la creación de prototipos, la optimización de algoritmos en tiempo real y aplicaciones donde la lógica de operación física necesita ser modificada continuamente, como en la optimización de algoritmos de inteligencia artificial, sistemas embebidos y la automoción. Al combinar la programabilidad de un procesador con la flexibilidad y el rendimiento de la lógica programable, las FPGA en un SoC ofrecen una plataforma de computación embebida muy potente.

### NPU

La Unidad de Procesamiento Neuronal (NPU) es un chip o núcleo de silicio dedicado exclusivamente a acelerar las cargas de trabajo de inteligencia artificial (IA), como las redes neuronales y el aprendizaje profundo. Su arquitectura está específicamente optimizada para realizar operaciones de matriz y tensor, que son el núcleo de los algoritmos de IA, con una eficiencia energética y una velocidad de inferencia inigualables por una CPU o GPU. El propósito de la NPU es descargar estas tareas de alto consumo de recursos de la CPU y la GPU, permitiendo que estos procesadores se concentren en sus funciones principales.

La aparición de la NPU como un componente dedicado del SoC es una clara validación de que la inteligencia artificial no es una carga de trabajo transitoria que puede ser gestionada por hardware existente. En cambio, es una función fundamental que exige su propio silicio especializado. La demanda de IA omnipresente y de baja latencia en dispositivos móviles, vehículos y el borde de la red ha hecho que las NPU sean un componente esencial. Este desarrollo marca una maduración en la industria de la IA, donde la solución ya no es usar hardware adaptado, sino diseñar hardware desde cero para la IA. La NPU es la respuesta arquitectónica a la necesidad de una IA omnipresente, eficiente y en tiempo real, lo que ha dado lugar a la "era del AI PC".

## Tabla de Comparación

| Unidad de Procesamiento | Funcion Principal | Estilo de Procesamiento | Fortalezas | Debilidades | Ejemplos de Cargas de Trabajo |
| ----------------------- | ----------------- | ----------------------- | ---------- | ----------- | ----------------------------- |
CPU | Procesamiento de proposito general, control del sistema. | Secuencial | Versátil, flexible, excelente en dependencias de datos. | Menos eficiente para tareas especializadas, alto consumo en paralelo. | Sistema operativo, aplicaciones de oficina, bases de datos. |
GPU | Gráficos, aceleración de la computación paralela. | Paralelo masivo (miles de núcleos) | Altamente eficiente para operaciones idénticas en grandes conjuntos de datos. | Poca versatilidad, limitada para tareas secuenciales. | Renderizado 3D, IA (entrenamiento y grandes modelos), simulaciones científicas. |
FPGA | Hardware reconfigurable para tareas específicas. | Paralelo personalizado (lógica reprogramable) | Flexibilidad, baja latencia determinista, eficiencia energética a medida. | Mayor costo y consumo que los ASIC, complejidad de programación. | Prototipos, sistemas de tiempo real, optimización de algoritmos de IA en el borde. |
NPU | Aceleración de tareas de IA. | Aceleración de tareas de IA. | Altamente eficiente para cargas de trabajo de IA con bajo consumo de energía. | Limitado a tareas específicas de redes neuronales, no apto para uso general. | Inferencia de IA en el dispositivo, reconocimiento de voz e imágenes, procesamiento del lenguaje natural.

## Referencias

Avnet Silica. (2021, April 28). FPGA vs. GPU vs. CPU – hardware options for AI applications | Avnet Silica. https://my.avnet.com/silica/resources/article/fpga-vs-gpu-vs-cpu-hardware-options-for-ai-applications/

Bonilla, L. (2025, March 10). Qué es una Unidad central de procesamiento (CPU) y cómo funciona. Guía completa. Data Center Market. https://www.datacentermarket.es/dcm-xl/cpu-unidad-central-de-procesamiento-guia-completa/ 

Drex. (2022, November 8). What is an FPGAs & SOC FPGAs? DRex Electronics. https://www.icdrex.com/what-is-an-fpgas-soc-fpgas/ 

GPU y CPU: diferencia entre unidades de procesamiento. AWS. (n.d.). Amazon Web Services, Inc. https://aws.amazon.com/es/compare/the-difference-between-gpus-cpus/ 

¿Qué es la IA en el borde? Navegando por la inteligencia artificial en el borde | F5. (n.d.). F5, Inc. https://www.f5.com/es_es/glossary/what-is-edge-ai 

¿Qué es un sistema en un chip? | Supermicro. (n.d.). https://www.supermicro.com/es/glossary/soc 

¿Qué es un Sistema en un Chip? (SOC) | Definición. (n.d.). Digi. https://es.digi.com/resources/definitions/soc 

Schneider, J., & Smalley, I. (2025, July 3). Neural Processing Unit. IBM. https://www.ibm.com/think/topics/neural-processing-unit 

Soto, J. A. (2025, February 25). ¿Qué es la NPU y para qué sirve? GEEKNETIC. https://www.geeknetic.es/NPU/que-es-y-para-que-sirve 

System on a Chip (SOC) explained - Revolutionizing Electronics | Lenovo US. (2023, May 28). https://www.lenovo.com/us/en/glossary/system-on-a-chip/ 

TRG Datacenters. (2025, April 14). GPU vs CPU for AI: A Detailed Comparison | TRG Datacenters. https://www.trgdatacenters.com/resource/gpu-vs-cpu-for-ai/ 

What is an NPU? And why is it key to unlocking on-device generative AI? (n.d.). Qualcomm. https://www.qualcomm.com/news/onq/2024/02/what-is-an-npu-and-why-is-it-key-to-unlocking-on-device-generative-ai

## Uso responsable de IA

- Asistencia de IA: Se realizó consulta con el siguiente prompt: "Arquitecturas heterogéneas en SoC"
- Herramienta: Gemini 2.5 flash
- Fecha: 2025-09-16