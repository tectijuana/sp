## Datos de alumno 
**Nombre y numero de contol** Quintero Angulo Roberto Carlos 22210784

**Fecha** 15 de septiembre 2025

## Tema Diseño de sistemas embebidos tolerantes a fallos – redundancia y seguridad funcional

## Que es el diseño de sistemas embebidos tolerantes a fallos
El diseño de sistemas embebidos tolerantes a fallos es una disciplina clave en el desarrollo de sistemas críticos donde la fiabilidad y la seguridad son esenciales, como en la automoción, la aviación, la medicina o la industria. La tolerancia a fallos se refiere a la capacidad de un sistema para continuar funcionando correctamente, o al menos de manera controlada, incluso cuando se producen fallos en uno o más de sus componentes.

Para los sistemas embebidos, la tolerancia a fallos se implementa comúnmente mediante redundancia y seguridad funcional. A continuación, exploraremos estos conceptos dentro del contexto de sistemas programables, como los que están basados en FPGAs o microcontroladores.

## Redundancia en Sistemas Embebidos

La redundancia se refiere a la duplicación de componentes del sistema para garantizar que si uno falla, otro pueda asumir su rol sin interrumpir la operación general del sistema. La redundancia se puede aplicar a varios niveles:

Redundancia de hardware:

Redundancia de componentes: Consiste en tener componentes duplicados (como procesadores, memoria o sensores) que pueden asumir la carga en caso de fallos de uno de ellos.

Redundancia activa: Los componentes redundantes están trabajando en paralelo de forma continua, compartiendo la carga del sistema.

Redundancia pasiva: Solo se activa la copia redundante cuando el componente original falla.

Redundancia de datos:

Codificación de Hamming o Códigos de Bloques: Se utilizan para detectar y corregir errores en los datos. Esto es especialmente importante cuando el sistema embebido interactúa con redes o tiene que transmitir datos entre componentes.

Técnicas de checksums o CRC (Cyclic Redundancy Check): Para asegurar la integridad de los datos transmitidos o almacenados.

Redundancia a nivel de software:

Software de respaldo o alternativo: Se implementan algoritmos que aseguran que si un módulo del software falla, otro pueda tomar su lugar o el sistema sea capaz de detectar y corregir fallos.

## Seguridad Funcional

La seguridad funcional es un principio fundamental para garantizar que un sistema embebido funcione de manera segura, incluso cuando se produce un fallo. El estándar más reconocido en este ámbito es el IEC 61508 (para la industria general) y el ISO 26262 (para la automoción), que define las prácticas para diseñar sistemas con un alto nivel de seguridad funcional.

Conceptos clave:

ASIL (Automotive Safety Integrity Level): En la industria automotriz, el ASIL clasifica los requisitos de seguridad funcional de acuerdo con la gravedad del riesgo. El nivel más alto (ASIL D) es para fallos más graves.

FMEA (Análisis de Efectos de Fallos y Análisis de Modos): Técnica que se usa para identificar posibles fallos en el sistema y sus consecuencias. Ayuda a priorizar las áreas que necesitan redundancia o medidas de mitigación.

Sistemas de monitoreo y diagnóstico: Los sistemas embebidos deben ser capaces de detectar fallos en tiempo real y, en algunos casos, corregirlos o notificar a un operador.

Principios de seguridad funcional:

Prevención de fallos: Diseñar el sistema para que los fallos sean menos probables. Esto incluye pruebas exhaustivas y el uso de componentes certificados.

Detección de fallos: Detectar fallos de manera temprana y garantizar que el sistema pueda continuar funcionando de manera controlada.

Mitigación de fallos: Cuando un fallo es detectado, el sistema debe ser capaz de aislar la falla y, si es posible, continuar con la operación, minimizando el impacto en la funcionalidad.

## Aplicación de Redundancia y Seguridad Funcional en Sistemas Programables
Uso de FPGAs en sistemas tolerantes a fallos:

Las FPGAs (Field Programmable Gate Arrays) son ideales para sistemas embebidos tolerantes a fallos debido a su flexibilidad y capacidad de redundancia. Algunas técnicas que se pueden aplicar en FPGAs son:

Redundancia espacial: Se duplican los módulos de hardware dentro del FPGA, asegurando que si un bloque de lógica falla, otro puede tomar su lugar sin afectar al sistema.

Redundancia temporal: Se realizan varias ejecuciones de las mismas operaciones en diferentes ciclos de reloj para detectar fallos transitorios.

Redundancia de datos (TMR - Triple Modular Redundancy): Tres copias de una operación se ejecutan y se compara su salida para detectar discrepancias.

Uso de microcontroladores:

En sistemas basados en microcontroladores, la redundancia se puede implementar mediante:

Microcontroladores redundantes: Conmutación de respaldo entre dos o más microcontroladores, asegurando que uno esté siempre activo mientras que el otro está en espera o realizando una operación de monitoreo.

Monitoreo de integridad de software y hardware: El microcontrolador puede implementar un watchdog que reinicia el sistema en caso de un comportamiento anómalo.

## Estándares y Normativas de Seguridad Funcional

Es fundamental que el diseño de sistemas embebidos tolerantes a fallos cumpla con los estándares relevantes para la seguridad funcional. Los principales estándares incluyen:

IEC 61508: Un estándar internacional para la seguridad funcional de sistemas eléctricos, electrónicos y programables.

ISO 26262: Específico para la seguridad funcional en sistemas de control eléctrico y electrónico en vehículos.

DO-254: Estándar específico para sistemas de hardware en la aviación.

## Conclusión

El diseño de sistemas embebidos tolerantes a fallos en entornos programables involucra redundancia de hardware y software, y una estricta adherencia a estándares de seguridad funcional para asegurar su operación continua y segura ante cualquier fallo.
