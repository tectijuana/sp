# Implementación de sistemas embebidos con Linux embebido (Yocto, Buildroot)

**Autor:** Maya Pino Juan Carlos 

**No. de Control:** 22211611

**Fecha:** 16 de septiembre de 2025

## ¿Qué es un Sistema Embebido?  

Un sistema embebido es un conjunto de hardware y software informático basados en un microcontrolador o microprocesador, controlados por un sistema operativo en tiempo real o RTOS, memoria limitada, y que puede variar tanto en tamaño como complejidad. 

![enter image description here](https://trbl-services.eu/wp-content/uploads/2021/06/embebido1.jpg)

###  Caracteristicas de un sistema Embebido

> - **Operación prolongada:** diseñados para funcionar de manera continua sin interrupciones.  
> - **Inicio rápido:** capaces de arrancar en poco tiempo, lo que permite respuestas inmediatas.  
> - **Eficiencia energética:** optimizados para consumir la menor energía posible, ideal para dispositivos con baterías.  
> - **Alta confiabilidad:** deben funcionar sin fallos, incluso en entornos críticos como salud o seguridad.  
> - **Recursos limitados:** cuentan con restricciones en memoria, procesamiento y almacenamiento

### Componentes de un sistema embebido

> - **Microprocesador:** núcleo del sistema, encargado de ejecutar instrucciones, controlar operaciones y gestionar recursos.  
> - **Memoria:**  
>   - **RAM:** almacena datos temporales y variables de trabajo.  
>   - **Flash:** guarda programas y datos permanentes, como software y configuraciones.  
> - **Periféricos:** permiten la interacción con el entorno. Incluyen sensores, actuadores y dispositivos de entrada/salida.  
> - **Software:** conjunto de programas y algoritmos que definen el comportamiento y funciones del sistema.  
> - **Fuente de poder:** suministra la energía necesaria, ya sea batería, adaptador de corriente u otra fuente.  
> - **Circuito de reloj:** sincroniza las operaciones, marca la velocidad de ejecución y coordina los componentes.

## Linux Embebido (Embedded Linux)

Linux embebido es una versión del kernel Linux diseñada para funcionar en dispositivos o sistemas empotrados. A diferencia de Linux estándar, ocupa menos espacio, requiere menos potencia de procesamiento, tiene funciones básicas y solo ejecuta aplicaciones específicas del dispositivo. Es flexible, económico y de código abierto, permite modificar y redistribuir el código, cuenta con soporte de múltiples proveedores y facilita la creación de sistemas personalizados mediante módulos.

<p align="center">
  <img src="https://nixfaq.org/wp-content/uploads/2024/08/1.jpg" alt="Linux embebido" width="400"/>
</p>

### Características de Linux embebido

> - **Tamaño reducido:** consume menos memoria y potencia de procesamiento.  
> - **Aplicaciones específicas:** solo ejecuta software diseñado para el dispositivo.  
> - **Código abierto y económico:** permite modificaciones y redistribución del código.  
> - **Flexibilidad y modularidad:** facilita la creación de sistemas personalizados.  
> - **Soporte múltiple:** cuenta con proveedores y comunidades que ofrecen desarrollo y soporte.

### Herramientas destacadas

> - **Yocto Project:** proyecto de código abierto que permite crear distribuciones Linux embebidas personalizadas para cualquier arquitectura de hardware.

## Implementación de sistemas embebidos

La implementación de sistemas embebidos requiere herramientas que permitan construir sistemas Linux personalizados adaptados a las necesidades del hardware. Dos de las soluciones más utilizadas son **Yocto** y **Buildroot**.

### Yocto Project
Yocto es un proyecto de código abierto que facilita la creación de distribuciones Linux embebidas personalizadas. Sus principales ventajas son:

<p align="center">
  <img src="https://blog.conan.io/assets/post_images/2019-07-26/conan-yocto.png" alt="Yocto proyect" width="400"/>
</p>

> - **Flexibilidad:** permite construir sistemas a medida según la arquitectura y necesidades del hardware.  
> - **Modularidad:** utiliza recetas y capas para gestionar paquetes y configuraciones de manera organizada.  
> - **Actualización continua:** facilita mantener el sistema actualizado y seguro.  
> - **Soporte comunitario:** amplio respaldo de desarrolladores y documentación detallada.

### Buildroot

Buildroot es una herramienta que genera sistemas Linux embebidos de manera rápida y sencilla, ideal para proyectos pequeños o medianos. Sus características principales incluyen:

<p align="center">
  <img src="https://www.acmesystems.it/www/buildroot_2015_11/buildroot.jpg" alt="Buildroot" width="400"/>
</p>

> - **Simplicidad:** construcción rápida de root filesystem, kernel y herramientas necesarias.  
> - **Ligereza:** produce sistemas compactos optimizados para dispositivos con recursos limitados.  
> - **Configuración controlada:** permite seleccionar únicamente los paquetes necesarios para el sistema.  
> - **Automatización:** facilita la generación de imágenes listas para el hardware objetivo.

Ambas herramientas son ampliamente utilizadas en la industria para **desarrollar sistemas embebidos confiables, eficientes y personalizados** según las necesidades de cada proyecto.


## Referencias 

 1. Ceupe. (2023b, septiembre 15). _Sistema embebido: Qué es, características y componentes_. https://www.ceupe.com/blog/sistema-embebido.html 
 2. Barriuso, R. (2024, 25 enero). _LINUX Embebido | Qué es, cómo funciona y para qué se usa_. TRBL Services. https://trbl-services.eu/blog-linux-embebido-que-es/
 3. González, G. M. (2025, 4 junio). Yocto: Creando tu próxima distro Linux. Adictos Al Trabajo. https://adictosaltrabajo.com/2025/06/04/yocto-creando-tu-proxima-distro-linux/#que-es-y-que-no-es-yocto
 4. Ziv. (2024, 6 septiembre). Yocto or Buildroot? Which to Use when Building your Custom Embedded Systems. Incredibuild. https://www.incredibuild.com/blog/yocto-or-buildroot-which-to-use-when-building-your-custom-embedded-systems
