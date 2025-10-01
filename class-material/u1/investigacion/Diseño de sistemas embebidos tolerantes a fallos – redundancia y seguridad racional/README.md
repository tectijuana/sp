## Datos del alumno

 **Quintero Angulo Roberto Carlos 
---
**22210784
 ---

## Diseño de sistemas embebidos tolerantes a fallos – redundancia y seguridad funcional



---

##  Diseño de Sistemas Embebidos Tolerantes a Fallos

###  Que es 
La tolerancia a fallos es un aspecto crítico del diseño del sistema que garantiza la confiabilidad y disponibilidad del sistema, incluso ante fallas. Se trata de anticipar lo inesperado, planificar contingencias y diseñar sistemas que puedan manejar y recuperarse de las fallas con elegancia. Este concepto no se trata sólo de crear componentes individuales robustos, sino también de crear una arquitectura resistente donde los componentes trabajen juntos para mantener la funcionalidad general del sistema.  

---

##  Redundancia: Pilar de la Tolerancia a Fallos

La redundancia consiste en incorporar componentes o funciones adicionales para que el sistema pueda continuar operando si alguno falla.

### Tipos de redundancia:
- **Redundancia de hardware**: duplicación de componentes físicos (por ejemplo, procesadores, sensores).
- **Redundancia de software**: ejecución de múltiples versiones del mismo software para detectar divergencias.
- **Redundancia temporal**: repetición de operaciones en distintos momentos para verificar consistencia.

### Ejemplos:
- Sistemas RAID en almacenamiento.
- Arquitecturas N-Modular Redundancy (NMR), como Triple Modular Redundancy (TMR), donde tres módulos ejecutan la misma tarea y se vota el resultado.

---

##  Seguridad Funcional
La seguridad funcional se refiere a la capacidad de un sistema para operar sin causar riesgos, incluso ante fallos. Está regulada por estándares como:

- **IEC 61508: Norma base para seguridad funcional en sistemas E/E/PE. Define el ciclo de vida de seguridad, los Niveles de Integridad de Seguridad (SIL), y los requisitos para hardware y software.

- **ISO 26262: Derivada de IEC 61508, específica para automoción. Introduce los niveles ASIL (Automotive Safety Integrity Level) y cubre desde el diseño hasta la validación de sistemas electrónicos en vehículos.

- ** EN 50129: Aplicada en sistemas ferroviarios. Establece requisitos para la aceptación de sistemas de señalización y control, incluyendo análisis de fallos, pruebas y documentación

### Estrategias clave:
- **Diagnóstico de fallos**: monitoreo continuo para detectar errores.
- **Conmutación por error (failover)**: cambio automático a un componente de respaldo.
- **Pruebas de estrés y validación**: simulación de fallos para verificar la respuesta del sistema.

---

##  Aplicación en Sistemas Programables

Los **sistemas programables** como FPGAs y microcontroladores permiten implementar tolerancia a fallos de forma flexible:

### En FPGAs:
- Implementación de lógica redundante.
- Reconfiguración dinámica ante fallos.
- Uso de bloques de recuperación y verificación de errores.

### En microcontroladores:
- Supervisión de watchdogs.
- Detección de errores mediante CRC y ECC.
- Programación con múltiples versiones (N-version programming).

---

##  Referencias

FasterCapital. (s.f.). Tolerancia a fallos: diseño de sistemas tolerantes a fallos para un éxito escalable. Recuperado de https://fastercapital.com/es/contenido/Tolerancia-a-fallos--diseno-de-sistemas-tolerantes-a-fallos-para-un-exito-escalable.html

Universidad de Sevilla. (s.f.). Fiabilidad y tolerancia de fallos. Recuperado de http://icaro.eii.us.es/descargas/Tema%206.3%20Fiabilidad%20y%20tolerancia.pdf
