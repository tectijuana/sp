## Datos del Alumno
#### Nombre: Emmanuel Isai Chavez Hernandez
#### No. Control: 23211005
#### Materia: Sistemas Programables
#### Fecha: 15/09/2025

---

## Índice
1. [Introducción](#introducción)  
2. [Entorno de Desarrollo Integrado (IDE)](#entorno-de-desarrollo-integrado-ide)  
3. [Cadenas de herramientas (Toochains)](#cadenas-de-herramientas-toolchains)  
4. [IDEs y cadenas de herramientas específicas](#ides-y-cadenas-de-herramientas-específicas)
5. [Conclusión sobre IDEs y Toolchains](#conclusión-sobre-ides-y-toolchains)
6. [Referencias](#referencias)

---

# Entornos de desarrollo integrados (IDE) y toolchains – MPLAB, Keil, PlatformIO, Vivado, Quartus

## **Introducción**

Este documento ofrece una descripción general de los Entornos de Desarrollo Integrados (IDE) y sus cadenas de herramientas, centrándose en MPLAB, Keil, PlatformIO, Vivado y Quartus, ampliamente utilizados en el desarrollo de software y sistemas embebidos.

---

## **Entorno de Desarrollo Integrado (IDE)**
Un IDE es un conjunto de software que integra herramientas como un editor de código, un compilador, un depurador y herramientas de automatización en una única interfaz para optimizar el desarrollo.

**Características de un IDE**:
- **Editor de Código**: Para escribir y editar código fuente.
- **Completado de Código**: Sugiere componentes de código para acelerar el desarrollo.
- **Compilador**: Traduce el código a lenguaje máquina.
- **Depurador**: Identifica y corrige errores durante las pruebas.
- **Herramientas de Automatización**: Automatiza tareas como la compilación y las pruebas de código.
- **Compatibilidad con Idiomas**: Algunos IDE son específicos de un lenguaje, mientras que otros admiten varios.
- **Control de versiones**: Rastrea los cambios de código y se integra con repositorios.
- **Exploradores de clases/objetos**: Visualiza estructuras de código orientadas a objetos.
- **Diagramas de jerarquía de clases**: Muestra la estructura y las relaciones del sistema.

---

**Tabla de los IDEs mas utilizados para JAVA**

![IDESs Populares](https://profile.es/wp-content/media/Comparativa-IDEs-en-Java-01-1024x592.png.webp)

> Fuente: profile.es

---

**Tipos de IDE**:
- **IDE multilenguaje**: Admite múltiples lenguajes de programación.
- **IDE de desarrollo móvil**: Diseñados para aplicaciones móviles (p. ej., Android Studio).
- **IDE específicos para lenguaje**: Diseñados para lenguajes específicos como Java o Python.
- **IDE basados en la nube**: Permiten la codificación remota mediante navegadores.
- **IDE HTML**: Para desarrollo web (p. ej., Notepad++, Atom).
- **IDE locales**: Se ejecutan en hardware local con bibliotecas adicionales.
- **IDE específicos para bases de datos**: Incluyen herramientas para el desarrollo de bases de datos.

---

**Beneficios de los IDEs**:
1. **Mayor productividad**: Las herramientas unificadas reducen los cambios de contexto.
2. **Mejor calidad del código**: El resaltado de sintaxis mejora la legibilidad.
3. **Incorporación más rápida**: Las plantillas y guías simplifican el aprendizaje.
4. **Mejor colaboración**: Se integra con el control de versiones para el trabajo en equipo.

--- 

**Diferencias entre IDEs y Editores**

![IDESs Editores](https://static.wixstatic.com/media/2ad0f4_f2643f328055471bad5a27750ae0aef1~mv2.jpg/v1/fill/w_1819,h_1614,al_c,q_90/2ad0f4_f2643f328055471bad5a27750ae0aef1~mv2.webp)

> Fuente: wixsite.com

---

## **Cadenas de herramientas (Toolchains)**
Una cadena de herramientas es un conjunto de herramientas vinculadas que automatizan los procesos de desarrollo de software, mejorando la eficiencia y reduciendo los errores. Los componentes varían según el caso de uso, pero pueden incluir:
- **Gestión del código fuente (SCM)**: Gestiona el código en repositorios.
- **Servidor de compilación**: Componente central para la compilación de código.
- **Repositorio de artefactos**: Almacena resultados binarios.
- **Seguimiento de incidencias/Gestión de proyectos**: Gestiona tareas e incidencias.
- **Gestión del conocimiento**: Almacena información (p. ej., wikis).
- **Automatización de pruebas**: Ejecuta pruebas automatizadas.
- **Configuración/Monitoreo del servidor**: Implementa y monitorea aplicaciones.

---

**Ventajas y desventrajas de un IDE**

- **Ventajas**: Reducción de errores manuales y mayor eficiencia.

- **Desventajas**: La configuración, que requiere mucho tiempo, requiere priorización.

---

**Introducción a la cadena de herramientas FPGA de Intel**

![Intel FPGA](https://static.wixstatic.com/media/ad48ed_f2a8cd73faf44bf4bdaa74e4b521ff97~mv2.png)

> Fuente: wixsite.com

---

## **IDES y cadenas de herramientas específicas**

### 1. **MPLAB (Microchip)**

MPLAB es un editor IDE gratuito, destinado a productos de la marca Microchip. Este editor es modular, permite seleccionar los distintos microcontroladores soportados, además de permitir la grabación de estos circuitos integrados directamente al programador. Es un programa que corre bajo Windows, Mac OS y Linux. El ambiente MPLAB® posee editor de texto, compilador y simulación (no en tiempo real). Puntos clave de MPLAB:

- Un IDE gratuito para microcontroladores Microchip, compatible con Windows, Mac y Linux.

- Características: Editor de código, compilador, depurador y simulación (en tiempo no real).

- Herramientas clave: Vista de E/S para monitoreo de registros, acceso a la hoja de datos con un solo clic, compilación/programación/depuración con un solo botón, gráfico de llamadas para navegación por el código y múltiples configuraciones de proyecto.

- Flujo de trabajo: Crear un archivo .ASM, configurar un proyecto, seleccionar un microcontrolador, escribir código, compilar y programar el dispositivo.

---

**Captura de pantalla de MPLAB X IDE v 1.85**

![IDE MPLAB](https://embedjournal.com/assets/posts/microchip-pic/2013-07-13-8-reasons-why-you-should-switch-to-mplab-x-ide/mplab-x-ide.png)

> Fuente: adiuvoengineering.com

---

### 2. **Keil MDK (Arm)**

Arm Keil MDK es una colección de herramientas de software para el desarrollo de aplicaciones embebidas basadas en procesadores Arm Cortex-M y Arm Ethos-U. Keil MDK facilita y hace más productiva la ingeniería de software al ofrecer la flexibilidad de trabajar con una CLI o un IDE (basado en escritorio o navegador), o al implementar las herramientas en un flujo de trabajo de integración continua. Puntos clave de Keil:

- Un conjunto de herramientas para procesadores Arm Cortex-M y Ethos-U, compatible con flujos de trabajo CLI e IDE.
- Características: Admite más de 10 000 microcontroladores a través de CMSIS, se integra con el IDE de Keil Studio, ofrece simulación de hardware virtual, compiladores con certificación de seguridad, compatibilidad con redes IoT/ML y análisis de consumo de energía y rendimiento.
- Beneficios: Desarrollo más rápido, reducción de costes de hardware y flujos de trabajo compatibles con la nube.

---

**Captura de pantalla de Keil MDK (Arm)**

![IDE Keil](https://www.mathworks.com/products/connections/product_detail/mdk-arm-link/_jcr_content/descriptionImageParsys/image.adapt.full.medium.png/1469940863690.png)

> Fuente: mathworks.com

---

### 3. **PlatformIO**

PlatformIO es una herramienta profesional multiplataforma, multi arquitectura y de múltiples marcos para ingenieros de sistemas integrados y para desarrolladores de software que escriben aplicaciones para productos integrados. Puntos clave de PlatformIO:

- Un IDE multiplataforma para sistemas embebidos y desarrollo de software.
- Características: Editor de código ligero, autocompletado de código inteligente, flujos de trabajo multiproyecto, depurador integrado, pruebas unitarias, análisis de código estático y soporte para desarrollo remoto.
- Beneficios: Simplifica el desarrollo de productos embebidos con una amplia compatibilidad con plataformas.

---

**Captura de pantalla de PlatformIO**

![IDE PlatformIO](https://platformio.org/images/platformio-ide-laptop.93fc8e69.png)

> Fuente: platformio-org

---

### 4. **Vivado (AMD)**

AMD Vivado™ es el software de diseño para SoC y FPGA adaptables de AMD. Incluye las siguientes funciones: Herramientas de entrada de diseño, síntesis, ubicación y ruta, verificación y simulación. Descubre cómo las funciones avanzadas del software de diseño Vivado ayudan a los diseñadores de hardware a reducir los tiempos de compilación y las iteraciones de diseño, como también a calcular con mayor precisión la potencia para los SoC adaptables y las FPGA de AMD. Puntos clave de Vivado:

- Una suite de diseño para SoCs y FPGAs AMD, lanzada en 2012.
- Características: Herramientas para la entrada de diseño, síntesis, colocación, enrutamiento, verificación y simulación. Compatible con C/C++/SystemC para síntesis de alto nivel, kernels OpenCL e integración de IP.
- Componentes: Vivado HLS, Simulador Vivado, Integrador de IP y Tcl Store para scripting.
- Beneficios: Reduce los tiempos de compilación y las iteraciones de diseño, con una edición WebPACK gratuita.

---

**Captura de pantalla  IDE Vivado (AMD) v 2023.2**

![IDE Vivado](https://dojofive.com/wp-content/uploads/2024/06/conclusion-1024x552.png)

> Fuente: dojofive.com

---

### 5. **Quartus (Intel)**

Quartus es un software de Intel (antes Altera) que proporciona un entorno de diseño multiplataforma para la creación y programación de dispositivos lógicos programables como FPGAs, CPLDs y SoCs. Ofrece herramientas para todas las fases del diseño, desde la descripción y síntesis de hardware utilizando lenguajes como VHDL y Verilog, hasta la optimización, simulación y configuración final del dispositivo. Puntos clave de Quartus:

- Una suite de diseño para FPGAs, CPLDs y SoCs Intel.
- Características: Admite diseño de hardware mediante VHDL/Verilog, síntesis lógica, simulación, ajuste y programación de dispositivos.
- Herramientas clave: Diseñador de plataformas para la integración de sistemas, diseño basado en bloques para reutilización y reconfiguración parcial para actualizaciones dinámicas de FPGAs.

---

**Captura de pantalla  IDE Quartus (Intel) Pro Edition**

![IDE Quartus](https://www.intel.com/content/dam/docs/us/en/683498/17-1/guc1507676482989.png)

> Fuente: intel.com

---

## Conclusión sobre IDEs y Toolchains

Los Entornos de Desarrollo Integrados (IDE) y las Toolchains son componentes fundamentales en el desarrollo de software moderno. Mientras que los IDEs ofrecen una interfaz unificada que integra herramientas como editores de código, depuradores y compiladores para facilitar el trabajo del desarrollador, las toolchains representan el conjunto de herramientas necesarias para compilar, ensamblar y enlazar el código fuente, permitiendo su ejecución en un sistema destino.

El uso conjunto de IDEs y toolchains mejora significativamente la productividad, reduce errores y acelera el proceso de desarrollo. Además, proporcionan soporte para múltiples lenguajes, plataformas y arquitecturas, adaptándose a las necesidades específicas de cada proyecto. Comprender y saber utilizar adecuadamente estas herramientas es esencial para cualquier desarrollador que busque eficiencia, calidad y escalabilidad en sus soluciones de software.

---

## Referencias

- Boada, D., & Boada, D. (2025, 11 febrero). ¿Qué es un entorno de desarrollo y en qué se diferencia de un entorno de desarrollo integrado (IDE)? Tutoriales Hostinger. https://www.hostinger.com/mx/tutoriales/que-es-un-entorno-de-desarrollo\

- Schneider, J., & Smalley, I. (2025, 3 septiembre). Entorno de desarrollo integrado (IDE). www.ibm.com. https://www.ibm.com/mx-es/think/topics/integrated-development-environment

- What is a “Toolchain”? – Find out more | Cloudogu. (s. f.). Cloudogu. https://about.cloudogu.com/en/glossary/toolchain/

- MPLAB® X IDE. (s. f.). Microchip Technology. https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide

- Arm Ltd. (s. f.). Arm Keil MDK: Flexible MCU Software development Tools. Arm | The Architecture For The Digital World. https://www-arm-com.translate.goog/products/development-tools/embedded-and-software/keil-mdk?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

- PlatformIO. (s. f.). PlatformIO: Your Gateway to Embedded Software Development Excellence. PlatformIO. https://platformio.org/

- AMD VivadoTM Design Suite. (s. f.). AMD. https://www.amd.com/es/products/software/adaptive-socs-and-fpgas/vivado.html

- Quartus® Prime Design Software | Altera® FPGA. (s. f.). https://www.altera.com/products/development-tools/quartus
