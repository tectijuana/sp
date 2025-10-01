# Análisis comparativo de buses de comunicación de alta velocidad: PCIe y AXI

## Datos

Nombre: Alexis Sebastian Sanchez Ruano

Número de control: 22211659

Fecha: 15 de Septiembre del 2025

Nickname: SanchezRuano22211659

## Introducción

La creciente demanda de ancho de banda y la reducción de latencia en sistemas computacionales modernos, desde centros de datos hasta dispositivos embebidos de edge computing, han posicionado a los buses de interconexión como elementos críticos del diseño. La arquitectura de un sistema se define no solo por su unidad de procesamiento, sino también por la eficiencia con la que sus componentes pueden comunicarse. En este ámbito, dos protocolos destacan por su predominio en sus respectivos dominios: **PCI Express**, abreviado como PCIe y **Advanced eXtensible Interface**, conocido como AXI. PCIe se ha establecido como el estándar indiscutible para comunicación **off-chip** de alta velocidad, conectando componentes a nivel de placa base. Por otro lado, AXI, parte de la familia AMBA de ARM, es el protocolo **on-chip** por excelencia para conectar núcleos de procesamiento, memorias y periféricos dentro de un System-on-Chip o FPGA.

---

## Bases

### PCI Express
PCIe surgió como sucesor de los buses paralelos PCI y PCI-X, que enfrentaban limitaciones de escalabilidad de frecuencia y integridad de señal debido a su naturaleza paralela. Introducido por el PCI-SIG en 2003, PCIe 1.0 adoptó una arquitectura serie punto-a-punto, solucionando estos cuellos de botella. Cada generación posterior (2.0, 3.0, 4.0, 5.0 y la reciente 6.0, la cual no ha recibido dispositivos compatibles hasta el momento) ha duplicado aproximadamente la tasa de transferencia, manteniendo una estricta compatibilidad hacia atrás, un factor clave para su adopción masiva y longevidad.

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.stack.imgur.com%2F3l92b.png&f=1&nofb=1&ipt=12b3c3848399f770808169b9a92d2a0661c7aa3a940955b84d0e8d4720149348)

### AXI (AMBA)

El protocolo AXI se introdujo con la versión 3 de la especificación Advanced Microcontroller Bus Architecture con la abreviatura AMBA de ARM en 2003. Fue diseñado para abordar las limitaciones de rendimiento de sus predecesores, el Advanced High-performance Bus o AHB y el Advanced System Bus, conocido como ASB. AXI ofrece una mayor frecuencia de operación, un mayor paralelismo y un manejo más eficiente de las transacciones. Su éxito lo consolidó como el pilar de la versión AMBA 4 y continúa evolucionando en AMBA 5, often integrado con otros protocolos como CHI para coherencia en sistemas multinúcleo complejos.

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F2.bp.blogspot.com%2F-SNWjTKXOU-s%2FUcMaedzK3qI%2FAAAAAAAAAyg%2F_auTCzKDwa8%2Fs400%2F%25E8%259E%25A2%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7%2B2013-06-20%2B%25E4%25B8%258B%25E5%258D%258811.05.44.png&f=1&nofb=1&ipt=d5c8058e7ca087631113966a909147bebe1a9305c52c415a444ff3fb3d86159a)

---

## Arquitectura y características técnicas

### PCI Express (PCIe)
- **Filosofía de Diseño**
	- Estándar de bus de expansión serie **off-chip**. Su arquitectura es radicalmente diferente de los buses paralelos, utilizando enlaces seriales full-duplex escalables llamados *lanes*.
- **Arquitectura en Capas**
	- Emula el modelo OSI para garantizar modularidad
	    - **Capa de Transacción**
		    - Genera paquetes de lectura/escritura (TLPs) con mecanismos de crédito para control de flujo.
	    - **Capa de Enlace de Datos**
		    - Gestiona la integridad de los datos mediante secuencias de números y acknowledgments (ACK/NAK), y control de flujo.
	    - **Capa Física**
		    - Implementa la señalización diferencial de bajo voltaje, codificación (128b/130b en PCIe 3.0+), y el interface eléctrico real (SerDes).
- **Escalabilidad**
	- Se agregan múltiples lanes (×1, ×4, ×8, ×16, ×32) para multiplicar el ancho de banda aggregate.
- **Características Avanzadas**
	- Soporte para virtualización (Single Root I/O Virtualization - SR-IOV), funciones alternativas (Alternative Routing-ID Interpretation - ARI), y gestión avanzada de energía (Active State Power Management - ASPM) (PCI-SIG, 2019).

### AXI (Advanced eXtensible Interface)
- **Filosofía de Diseño**
	- Protocolo de bus **on-chip** síncrono y paralelo, optimizado para alta frecuencia, bajo consumo y modularidad. Su esencia es la separación de concerns mediante canales independientes.
- **Arquitectura de Canales**
	- Utiliza cinco canales independientes y desacoplados para cada interfaz maestro-esclavo
	    1.  **Write Address Channel (AW)**
	    2.  **Write Data Channel (W)**
	    3.  **Write Response Channel (B)**
	    4.  **Read Address Channel (AR)**
	    5.  **Read Data Channel (R)**
- **Transferencias en Ráfaga (Burst)**
	- Soporta transacciones burst de longitud fija, incremental y envolvente, con beats de hasta 256 datos en AXI4.
- **Operaciones Out-of-Order**
	- Utiliza identificadores de transacción (AWID, ARID) para permitir que las respuestas sean completadas en un orden diferente al de las solicitudes, mejorando la eficiencia en sistemas con múltiples maestros y slaves con diferentes latencias.
- **Variantes**
    - **AXI4**
	    - Para dispositivos de alto rendimiento que requieren acceso en ráfaga.
    - **AXI4-Lite**
	    - Subconjunto simplificado para registros de control de periféricos simples, sin soporte para ráfagas.
    - **AXI4-Stream**
	    - Para flujos de datos unidireccionales de gran volumen sin direcciones (ideal para video, DSP).

---

## Rendimiento

### PCI Express (PCIe)
- **Ancho de Banda**
	- La métrica clave es la tasa de transferencia por lane (GT/s - GigaTransfers per second). Debido a la sobrecarga de codificación, el ancho de banda útil es aproximadamente el 98% del *raw* para 128b/130b encoding.
	    - PCIe 4.0: 16 GT/s → ~1.97 GB/s por lane útil.
	    - PCIe 5.0: 32 GT/s → ~3.94 GB/s por lane útil.
	    - PCIe 6.0: 64 GT/s (PAM4 encoding) → ~7.88 GB/s por lane útil.
	    - Un enlace ×16 PCIe 5.0 ofrece ~63 GB/s de ancho de banda aggregate bidireccional.
- **Latencia** 
	- Relativamente alta comparada con buses del tipo on-chip. Incluye overhead de encapsulado de paquetes, el paso por la de la jerarquía (root complex, switches) y latencia de propagación física. Los valores típicos rondan los **200-500 ns** para transacciones simples.

### AXI (AMBA)
- **Ancho de Banda**
	- Determinado por el ancho de bus (e.g., 128, 256, 512 bits) y la frecuencia de operación del reloj (e.g., 500 MHz, 1 GHz).
	- En la práctica, la eficiencia se ve afectada por la contención en el interconnect, la preparación de las ráfagas y la latencia de los slaves.
- **Latencia**
	- Extremadamente baja, medida en **ciclos de reloj**. Una transacción de lectura puede tener una latencia de ida y vuelta de **10-20 ciclos**. A 500 MHz, esto equivale a **20-40ns**. Esta baja latencia es su principal ventaja para la comunicación entre cores cercanos.

---

## Escalabilidad y compatibilidad

### PCIe
- **Escalabilidad Física** 
	- Escalable horizontalmente (número de lanes) y verticalmente (generaciones). Un dispositivo PCIe 3.0 ×4 funcionará en un slot PCIe 4.0 ×4, operando a la velocidad del Gen3.
- **Escalabilidad Topológica**
	- Utiliza switches para permitir que un único host (Root Complex) se comunique con docenas de endpoints, fundamental en sistemas de almacenamiento y networking.

### AXI
- **Escalabilidad Estructural** 
	- Escalable en ancho de bus, frecuencia y número de puertos. Los *AXI Interconnect* IP cores (e.g., de Xilinx/AMD o ARM) pueden conectar dinámicamente docenas de maestros y docenas de esclavos en topologías como crossbar, matrix, o N-to-1.
- **Escalabilidad Funcional** 
	- Las variantes (AXI4, Lite, Stream) permiten adaptar la complejidad del protocolo a las necesidades de cada componente del SoC, optimizando área y potencia.

---

## Facilidad de implementación y diseño

### PCIe
- **Complejidad** 
	- Alta. La implementación de un controlador PCIe desde cero es una tarea monumental que involucra diseño analógico de alta velocidad (SerDes PHY) y lógica digital compleja para las capas de enlace y transacción.
- **Flujo de Diseño Típico**
	- Los diseñadores utilizan IP cores certificados por el PCI-SIG, proporcionados por los fabricantes de FPGA (Xilinx/AMD, Intel), ASIC foundries o proveedores de IP third-party (e.g., Synopsys). En FPGAs, estos cores se conectan often mediante interfaces AXI, creando un "bridge" entre el mundo off-chip y on-chip.

### AXI
- **Complejidad**
	- Moderada. La especificación del protocolo es robusta pero bien definida, haciendo factible de implementar maestros y esclavos personalizados el HDL (VHDL/Verilog).
- **Flujo de Diseño Típico**
	- Totalmente integrado en los ecosistemas de diseño de SoC y FPGA. Herramientas como Vivado (Xilinx/AMD) o Quartus (Intel) proporcionan generadores gráficos para configurar interconnects, manejar arbitraje, y convertir entre diferentes estándares de bus (e.g., AXI to AHB). Esta integración acelera el tiempo de desarrollo.

---

## Aplicaciones típicas

### PCIe
- **Aceleración de Cómputo**
	- GPUs, FPGAs como aceleradores, y Tensor Processing Units (TPUs) se conectan al CPU host via PCIe.
- **Almacenamiento de Ultra Baja Latencia**
	- Unidades NVMe SSDs, que aprovechan el paralelismo de los múltiples lanes de PCIe para superar por completo los límites de interfaces SATA/SAS.
- **Networking**
	- Tarjetas de interfaz de red (NICs) de 100G, 200G, y 400G Ethernet e InfiniBand.
- **Interconexión de Sistemas**
	- Cables para extender PCIe entre chasis (e.g., Thunderbolt 3/4, que encapsula PCIe).

### AXI
- **Núcleo de SoCs y FPGAs**
	- Interconecta los cores de un procesador ARM Cortex con memorias (DDR controller), periféricos de alta velocidad (USB, Ethernet), y otros aceleradores integrados.
- **Diseños Personalizados en FPGAs**
	- Casi todos los IP cores modernos para FPGAs (Xilinx/AMD, Intel) utilizan AXI como interfaz estándar, facilitando la integración plug-and-play de bloques de DSP, procesamiento de video, interfaces, etc.
- **Bridges**
	- Muy often se implementan bridges para conectar el dominio AXI on-chip con el mundo exterior PCIe, permitiendo, por ejemplo, que un IP core en una FPGA se vea como un dispositivo PCIe para el sistema host.

---

## Ventajas y limitaciones

### PCIe
- **Ventajas**
    - Rendimiento externo extremadamente alto y escalable.
    - Estandarizado a nivel de industria, garantizando interoperabilidad.
    - Rico conjunto de características empresariales (virtualización, QoS, gestión de errores).
    - Compatibilidad reversa protege las inversiones.
- **Limitaciones**
    - Alta latencia comparativa para comunicación entre chips.
    - Implementación compleja y costosa; requiere PHYs analógicos especializados.
    - Consumo de potencia y área significativos.
    - Overhead de protocolo para paquetes pequeños.

### AXI
- **Ventajas**
    - Latencia ultrabaja, crucial para el rendimiento on-chip.
    - Arquitectura desacoplada que permite alto paralelismo y rendimiento.
    - Flexibilidad y modularidad extremas gracias a sus variantes.
    - Ampliamente soportado y fácil de integrar en flujos de diseño EDA modernos.
- **Limitaciones**
    - Estrictamente para comunicación on-chip. No puede ser usado fuera de un chip/FPGA.
    - La complejidad del arbitraje y el routing puede crecer exponencialmente con el número de maestros/esclavos.
    - El rendimiento máximo está limitado por las restricciones de timing y ruteo física dentro del chip.

---

## Tabla comparativa

| Característica              | PCI Express (PCIe)                                                                                           | AXI (AMBA)                                                                                                           |
|-----------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Alcance**                 | Off-chip (placa, chasis, cable)                                                                              | On-chip (interno al SoC/FPGA)                                                                                       |
| **Topología**               | Punto-a-punto, con switches                                                                                  | Punto-a-punto, Crossbar, Matrix (mediante Interconnect)                                                              |
| **Modo de Señalización**    | Serie diferencial (SerDes)                                                                                   | Paralelo síncrono                                                                                                    |
| **Capas/Canales**           | Tres capas (Transacción, Enlace, Física)                                                                     | Cinco canales independientes (AW, W, B, AR, R)                                                                      |
| **Escalabilidad**           | Carriles (×1 a ×32) y generaciones (Gen1-6)                                                                  | Ancho de bus (32–1024+ bits), frecuencia, variantes (AXI4, Lite, Stream)                                             |
| **Ancho de banda máximo**   | PCIe 6.0 ×16: ~126 GB/s (bidireccional)                                                                      | Teórico: Ej. 512b @ 1GHz = 64 GB/s (por puerto). Práctico: Limitado por el interconnect.                             |
| **Latencia típica**         | Alta (200-500 ns). Overhead de protocolo y traversing.                                                       | Muy baja (10-50 ns). Pocos ciclos de reloj entre componentes.                                                        |
| **Gestión de Errores**      | CRC robusto en capa de enlace, con retransmisión.                                                            | Sin mecanismo de retransmisión inherente. Errores often manejados a nivel de sistema.                                |
| **Aplicaciones típicas**    | GPUs, SSDs NVMe, NICs, extensión de chasis                                                                   | Conexión CPU-DDR, DSPs, IP cores en FPGAs, periféricos de alta velocidad en SoCs                                    |
| **Ventajas principales**    | Alto BW externo, estándar universal, características enterprise (SR-IOV), compatibilidad.                    | Baja latencia, paralelismo, flexibilidad, integración simplificada en flujos EDA.                                    |
| **Limitaciones principales**| Alta latencia, complejidad de implementación (PHY analógico), consumo de potencia.                           | Alcance limitado on-chip, complejidad de arbitraje en diseños grandes, dependiente de la ruta física (timing closure).|

---

## Conclusión

PCIe y AXI son protocolos fundamentales que operan en dominios complementarios pero a menudo interconectados entre sí. PCIe es el rey indiscutible de la comunicación **off-chip**, proporcionando el ancho de banda y la estandarización necesarios para conectar componentes heterogéneos entre la placa base y demás componentes.

Por otro lado, AXI es el tejido conectivo esencial **on-chip**, optimizado para la máxima eficiencia, baja latencia y modularidad dentro de un SoC o FPGA. Su evolución está ligada a las crecientes demandas de coherencia y eficiencia en sistemas multinúcleo, con protocolos como ACE y CHI extendiendo sus conceptos.

La sinergia entre ambos es la base de las arquitecturas modernas. Un SoC típico utilizará AXI para su comunicación interna e integrará uno o más controladores PCIe como puertas de enlace de ultra alta velocidad hacia el mundo exterior (e.g., una GPU externa o un SSD NVMe). El futuro verá una integración aún más estrecha, con tecnologías como CXL (Compute Express Link) construida sobre la infraestructura física de PCIe pero con protocolos semánticos más avanzados para coherencia de memoria, haciendo la línea entre la comunicación on-chip y off-chip más borrosa. 

---

## Referencias

ARM Holdings. (2011). *AMBA 4 AXI4-Stream Protocol Specification*. ARM IHI 0051A. Recuperado de https://developer.arm.com/documentation/ihi0051/a/?lang=en

Dolphin Interconnect Solutions. (s.f.). *Benefits of using PCI Express with VxWorks*. Dolphin ICS White Paper. Recuperado de https://www.dolphinics.com/whitepapers.html

Intel Corporation. (s.f.). *PCI Express 5.0 Architecture*. Intel Technology Journal. Recuperado de https://download.intel.com/newsroom/2021/manufacturing/12th-Gen-Intel-Core-PCIe.pdf

LSoft Technologies. (s.f.). Comparing pcie data transfer. LSoft Blog. Recuperado de https://www.lsoft.net/posts/comparing-pcle-data-transfer/

PCI-SIG. (2019). *PCI Express Base Specification Revision 5.0 Version 1.0*. Recuperado de https://picture.iczhiku.com/resource/eetop/SYkDTqhOLhpUTnMx.pdf

St. Michael, S. (2019, octubre 17). *Introduction to the Advanced Extensible Interface (AXI)*. All About Circuits. Recuperado de https://www.allaboutcircuits.com/technical-articles/introduction-to-the-advanced-extensible-interface-axi/

Synopsys, Inc. (s.f.). *Building a Bridge from PCI Express to AMBA 3 AXI On-Chip Bus*. Synopsys Technical Bulletin. Recuperado de https://www.synopsys.com/dw/dwtb.php?a=pcie_tb_axi

Verma, A., & Dahiya, P. K. (2017). *PCIe BUS: A State-of-the-Art-Review*. IOSR Journal of VLSI and Signal Processing, 7(4), 24–28. Recuperado de https://www.researchgate.net/publication/318360748_PCIe_BUS_A_State-of-the-Art-Review

Xilinx, Inc. (2021). *AXI Reference Guide* (UG1037). AMD. Recuperado de https://docs.amd.com/v/u/en-US/ug1037-vivado-axi-reference-guide
