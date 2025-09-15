# DANIEL ROMERO BRAVO

```text
Asistencia de IA: El usuario fue apoyado con la asistencia para acomodar las referencias en APA 
y realizar correcciones ortográficas, ajustes de redacción y obtener unas fuentes de información.
Herramienta: ChatGPT (GPT-5)
Fecha: 15 de septiembre de 2025
Plataforma de hardware utilizada: N/A
```
# Manejo de memoria en sistemas embebidos — RAM, ROM, Flash, EEPROM y su impacto en el rendimiento
---

## Resumen

Los sistemas embebidos combinan distintos tipos de memoria (volátiles y no volátiles) para equilibrar coste, tamaño, velocidad y durabilidad. La elección y el manejo de RAM, ROM, Flash y EEPROM influyen directamente en el rendimiento (latencias, throughput), en la predictibilidad temporal (crítico en sistemas en tiempo real) y en la vida útil del dispositivo (debido a límites de ciclos de escritura en memorias no volátiles). ([Microchip][1])

---

## Tipos de memoria (definiciones y características)

### RAM (Random Access Memory)

* **Volatilidad:** Volátil (pierde datos sin alimentación).
* **Tipos comunes:** SRAM (estática, no necesita refresco), DRAM (dinámica, necesita refresco).
* **Características:** Alta velocidad de acceso y baja latencia para lectura/escritura; SRAM suele usarse como RAM on-chip (pocas decenas de KB–MB en microcontroladores). DRAM ofrece mayor densidad pero requiere control más complejo y energía para refresco. ([Barr Group][2])

### ROM (Read-Only Memory)

* **Volatilidad:** No-volátil.
* **Tipos:** Mask ROM (contenido fijado en fabricación), OTP/EPROM (programable una vez).
* **Uso típico:** Contener código de arranque o datos constantes que no cambian en campo. ([Microchip][3])

### Flash (NOR / NAND)

* **Volatilidad:** No-volátil.
* **Subtipos:** NOR (mejor para lectura aleatoria / ejecución in-place — XIP), NAND (mayor densidad, mejor para almacenamiento secuencial).
* **Características:** Escritura/erase a bloques, latencias de borrado y escritura más altas que lectura. Ciclos de vida limitados (endurance), requiere técnicas de gestión (wear-leveling) en aplicaciones con muchas escrituras. Muy usado para memoria de programa y almacenamiento de datos. ([AnySilicon][4])

### EEPROM (Electrically Erasable Programmable ROM)

* **Volatilidad:** No-volátil.
* **Características:** Permite borrado/programación a nivel de byte o palabra (dependiendo del dispositivo), mayor facilidad para pequeñas actualizaciones comparada con flash; típicamente menor densidad y mayor coste por byte. Endurance limitado (aunque normalmente mayor tolerancia a escrituras pequeñas que ciertas flash). Buena para parámetros de configuración que cambian ocasionalmente. ([DigiKey][5])
<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/d955727a-f02e-4302-911a-71bcfa7d6e97" />

---

## Comparación práctica: latencia, ancho de banda, densidad, coste y endurance

(Resumen orientado a decisiones de diseño)

* **Latencia lectura:** SRAM ≈ SRAM on-chip (microsegundos o menos) < NOR-Flash (lectura relativamente rápida) < NAND-Flash (lectura secuencial alta pero latencia de acceso aleatorio mayor).
* **Latencia escritura / erase:** EEPROM (operaciones pequeñas pero lentas) < Flash (erase por bloque, escritura por página — más costosa en tiempo) — ambos mucho más lentos que RAM. ([DigiKey][5])
* **Endurance (ciclos de escritura):** SRAM/ROM (prácticamente ilimitado para lecturas; RAM no aplica), EEPROM (10⁴–10⁶ según tecnología), Flash NAND (10³–10⁵ típicamente) — varia por fabricante. Gestionar escrituras frecuentes es crítico. ([DigiKey][5])
* **Densidad y coste por byte:** DRAM / NAND-Flash > SRAM / EEPROM. Para microcontroladores integrados, Flash on-chip y SRAM on-chip son comunes (balance coste/velocidad). ([Microchip][1])

---

## Impacto en el rendimiento del sistema embebido

### Tiempo de arranque (boot)

* Si el bootloader y la imagen de firmware residen en Flash y se ejecutan mediante **XIP (execute-in-place)** desde NOR-Flash, el arranque puede evitar copiar toda la imagen a RAM — ahorrando RAM y acelerando ciertos diseños. Sin embargo, la velocidad del bus Flash (o la interfaz SPI externa) condiciona el tiempo de arranque y la latencia de ejecución inicial. ([NXP Semiconductors][6])

### Ejecución de código: XIP vs copiar a RAM

* Ejecutar código directamente desde Flash (XIP) reduce uso de RAM pero depende de la latencia de la Flash. Para códigos con acceso intensivo a instrucciones/constantes, copiar secciones críticas a SRAM puede reducir latencia y jitter, mejorando rendimiento temporal en sistemas críticos. ([AnySilicon][4])

### Acceso a datos y operaciones de escritura/lectura

* **Lecturas frecuentes** pequeñas desde EEPROM son relativamente costosas en tiempo; **escribir** a Flash implica borrar por bloques y reprogramar páginas — si no se planifica, las operaciones de mantenimiento (erase/program) pueden introducir latencias largas (“pausas”) que afectan el comportamiento en tiempo real. Técnicas como buffering, journaling o usar RAM como caché mitigarán estos efectos. ([DigiKey][5])

### Consumo de energía y determinismo temporal

* DRAM y operaciones de erase/escritura en Flash consumen más energía; además las operaciones de Flash pueden bloquear el bus o requerir que el CPU espere, lo que reduce determinismo — problemático en sistemas real-time. Es importante medir y diseñar para evitar bloqueos largos en ISRs o secciones críticas. ([ResearchGate][7])

---

## Consideraciones de diseño y técnicas de optimización

### 1. Ubicación del código y datos

* Coloca rutinas críticas en **SRAM** o en Flash NOR XIP dependiendo de latencia requerida. Segmenta el firmware: código no crítico en Flash, rutinas de tiempo crítico en SRAM. ([AnySilicon][4])

### 2. Caché, buffering y DMA

* Usa DMA para transferir grandes bloques desde Flash/NAND sin cargar CPU. Implementa buffers circulares y caching para lecturas repetitivas. Esto reduce accesos directos a Flash/EEPROM y mejora latencia observada. ([ResearchGate][7])

### 3. Gestión de durabilidad (wear-leveling y journaling)

* Para Flash y EEPROM con límites de escritura: emplea wear-leveling (distribuir escrituras), técnicas de journaling/append-only para evitar escrituras destructivas frecuentes, y usa estructuras como circular logs para parámetros que cambian con frecuencia. En sistemas sencillos, usar una RAM-backed cache con sincronización controlada al e.g. apagar o cada N cambios minimiza escrituras. ([DigiKey][5])

### 4. Uso de memoria externa

* Si necesitas grandes volúmenes (archivos, logs), las memorias externas NAND/eMMC/SD son más económicas por byte que SRAM on-chip; sin embargo, exige controladores, gestión de errores ECC, y planificación de latencias. ([AnySilicon][4])

### 5. Prácticas para código en tiempo real

* Evitar operaciones de borrado/escritura de Flash dentro de rutinas críticas o ISRs. Planificar ventanas de mantenimiento (garbage collection, wear-leveling) en momentos de baja carga. ([ResearchGate][7])

---

## Medición y benchmarking sugerido para proyectos embebidos

Para poder tomar decisiones basadas en datos:

1. **Medir latencias de lectura/escritura:** tiempos de lectura aleatoria y secuencial, tiempo de borrado de bloque en Flash, tiempo de escritura por página en EEPROM.
2. **Medir jitter:** ejecutar tareas periódicas (ej. ISR a 1 kHz) mientras se fuerza una operación de escritura en Flash para cuantificar impacto.
3. **Consumo energético:** registrar corriente durante operaciones de lectura/escritura y en reposo.
4. **Endurance testing:** si aplica, realizar pruebas de ciclo de escritura/erase en áreas de memoria que se usarán intensamente (simular carga real).
5. **Herramientas:** usar osciloscopio lógico o trazas del bus (por ejemplo, SPI sniffing) para ver tiempos reales y bloqueos. ([ResearchGate][7])

---

## Ejemplos típicos en microcontroladores y arquitecturas comunes

* **8/16-bit MCU (AVR, PIC):** Programa en Flash on-chip, datos persistentes pequeños en EEPROM, variables temporales en SRAM. Al actualizar parámetros, usar técnicas para minimizar escrituras a EEPROM. ([Microchip][3])
* **32-bit MCU (ARM Cortex-M):** Flash on-chip para firmware; SRAM para pilas/HEAP y código crítico; periféricos y RAM externo (PSRAM/DRAM) si se requiere alta memoria; external QSPI-NOR o eMMC para grandes archivos. Soporta XIP en NOR con consideraciones de latencia. ([AnySilicon][4])
---

## Referencias (APA)
1. Microchip Technology Inc. (2001). *Getting Started with On-chip Memory* (Application note / S0001A). Microchip Technology.
   (Documento técnico sobre memoria on-chip en microcontroladores; útil para entender separación de memoria de programa y datos en MCUs). ([Microchip][1])

2. Beningo, J. (2019, 16 de octubre). *The Fundamentals of Embedded Memory: EEPROM vs FRAM vs eMMC vs SD Cards*. Digi-Key.
   (Artículo práctico y orientado a ingenieros embebidos sobre las diferencias y usos de memorias no volátiles). ([DigiKey][5])

3. Barr Group. (s. f.). *Types of Memory in Embedded Systems*. Barr Group Embedded Systems.
   (Descripción técnica de RAM (SRAM/DRAM) y su uso en sistemas embebidos). ([Barr Group][2])

4. Klotz, D. H. J. (2001). *AN2183 — Using FLASH as EEPROM on the MC68HC908GP32* (Application Note). NXP / Motorola Semiconductor.
   (Ejemplo clásico de cómo usar Flash on-chip para almacenamiento similar a EEPROM y las implicaciones). ([NXP Semiconductors][6])

5. Oliveira, L. S., et al. (año). *Survey of Memory Optimization Techniques for Embedded Systems*. (Resumen en ResearchGate).
   (Revisión académica de técnicas de optimización de memoria para reducir consumo y mejorar rendimiento en sistemas embebidos). ([ResearchGate][7])

---
[1]: https://ww1.microchip.com/downloads/en/devicedoc/ramrom.pdf?utm_source=chatgpt.com "Getting Started with On-chip Memory"
[2]: https://barrgroup.com/blog/types-memory-embedded-systems?utm_source=chatgpt.com "Types of Memory in Embedded Systems"
[3]: https://ww1.microchip.com/downloads/en/DeviceDoc/doc2464.pdf?utm_source=chatgpt.com "Atmel's Self-Programming Flash Microcontrollers"
[4]: https://anysilicon.com/ultimate-guide-embedded-non-volatile-memory-envm/?utm_source=chatgpt.com "Ultimate Guide: Embedded Non-Volatile Memory (eNVM)"
[5]: https://www.digikey.com/en/articles/the-fundamentals-of-embedded-memory?utm_source=chatgpt.com "EEPROM vs. FRAM vs. eMMC vs. SD Cards"
[6]: https://www.nxp.com/docs/en/application-note/AN2183.pdf?utm_source=chatgpt.com "Using FLASH as EEPROM on the MC68HC908GP32"
[7]: https://www.researchgate.net/publication/258848441_Survey_of_Memory_Optimization_Techniques_for_Embedded_Systems?utm_source=chatgpt.com "Survey of Memory Optimization Techniques for Embedded Systems"


