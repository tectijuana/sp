# Manejo de Memoria en Sistemas Embebidos

## Introducción

El manejo de memoria en sistemas embebidos es esencial para lograr sistemas eficientes, confiables y duraderos. Dado que estos dispositivos operan con recursos limitados, cada tipo de memoria (RAM, ROM, Flash, EEPROM) debe utilizarse de forma estratégica.

![Texto alternativo](https://datascientest.com/es/files/2024/07/sistemas-embebidos-datascientest-1024x585.jpg)

---

## Tipos de Memoria

### 1. RAM (Random Access Memory)

- Volátil.
- Rápido acceso de lectura/escritura.
- Usada para variables temporales, buffers, stack, heap, etc.

**Impacto en el rendimiento:**
- Mayor RAM → mejor rendimiento.
- Poca RAM → desbordamientos, bloqueos, reinicios.

**Tipos:**
- **SRAM** (estática): rápida, costosa, sin refresco.
- **DRAM** (dinámica): más lenta, necesita refresco, más densa.

---

### 2. ROM (Read-Only Memory)

- No volátil.
- Solo lectura.
- Contiene código permanente, como bootloaders.

**Impacto:**
- Bajo consumo.
- Ideal para datos que nunca cambian.

---

### 3. Flash

- No volátil.
- Lectura rápida, escritura lenta y por bloques.
- Reescribible (con límites de ciclos de escritura).

**Usos:**
- Almacenamiento del firmware.
- Sistemas de archivos embebidos: SPIFFS, LittleFS.

**Impacto:**
- Escritura lenta puede afectar tiempos.
- Desgaste con escrituras frecuentes → usar wear leveling.

---

### 4. EEPROM

- No volátil.
- Escritura lenta pero precisa (byte a byte).
- Almacenamiento de configuraciones, calibraciones, etc.

**Impacto:**
- Escritura lenta y con límite de ciclos.
- Ideal para datos ocasionales, no para uso frecuente.

---

## Comparativa Rápida

| Memoria   | Volátil | Velocidad  | Escritura     | Capacidad típica | Uso principal                     |
|-----------|---------|------------|----------------|------------------|-----------------------------------|
| **RAM**   | Sí      | Muy alta   | Rápida         | Baja-Media       | Variables y datos en ejecución    |
| **ROM**   | No      | Alta       | No              | Muy baja         | Bootloaders, constantes           |
| **Flash** | No      | Media-Alta | Lenta (bloques) | Media-Alta       | Código, firmware, almacenamiento  |
| **EEPROM**| No      | Lenta      | Lenta (bytes)   | Muy baja         | Configuraciones persistentes      |

---

## Organización de Memoria

### Segmentos comunes:

- `.text`: Código (en Flash).
- `.data`: Variables inicializadas (copiadas a RAM).
- `.bss`: Variables no inicializadas (RAM).
- `.stack`: Pila (RAM).
- `.heap`: Memoria dinámica.

### Herramientas de control:

- **Linker scripts** (.ld).
- **RTOS traceadores** (FreeRTOS, Zephyr).
- **Analizadores estáticos** (valgrind, pero limitado en embebidos).

---

## Tiempo Real y Determinismo

- **Evitar malloc/new en tiempo real.**
- **Ejecutar código crítico desde RAM.**
- **Usar acceso directo a RAM para menor latencia.**

---

## DMA (Direct Memory Access)

Permite mover datos sin usar la CPU. Beneficios:

- Reduce carga del procesador.
- Mejora velocidad y eficiencia.

Usos comunes: ADC, UART, SPI, I2C, SDIO.

---

## Sistemas de Archivos Embebidos

- **SPIFFS**: Ligero, sin jerarquía, para Flash.
- **LittleFS**: Robusto, con wear leveling.
- **FAT**: Para SD, menos eficiente en micros.

---

## Seguridad y Protección

### MPU y MMU:

- **MPU** (Memory Protection Unit): Define permisos.
- **MMU** (Memory Management Unit): Usado en sistemas con Linux, soporta virtualización.

---

## Problemas Comunes

- **Fragmentación**: Uso ineficiente del heap.
- **Desbordamiento de stack**: Puede corromper datos.
- **Corrupción de memoria**: Punteros mal usados.

---

## Buenas Prácticas

| Buenas Prácticas                        | Justificación                             |
|----------------------------------------|-------------------------------------------|
| Evitar `malloc()` en tiempo real       | Impredecible y propenso a fragmentación   |
| Usar buffers de tamaño fijo            | Previene fragmentación                    |
| Monitorear uso de stack y heap         | Evita desbordamientos                     |
| Evitar escrituras frecuentes en Flash  | Prolonga la vida útil del dispositivo     |
| Usar sistemas de archivos robustos     | Evita corrupción ante apagones            |

---

## Referencias (edicion 7ma APA)

## 📚 Referencias (Formato APA 7ª edición)

1. Barr Group. (s.f.). *Types of memory in embedded systems*. Barr Group. Recuperado el 22 de mayo de 2025, de [https://barrgroup.com/blog/types-memory-embedded-systems](https://barrgroup.com/blog/types-memory-embedded-systems)
2. Tahiru, A. M. (s.f.). *Memory in embedded systems*. Ayuba Monnie Tahiru. Recuperado el 22 de mayo de 2025, de [https://www.ayubamonnietahiru.com/memory.html](https://www.ayubamonnietahiru.com/memory.html)

3. Wikipedia contributors. (2024, enero 15). *EEPROM*. Wikipedia. Recuperado de [https://en.wikipedia.org/wiki/EEPROM](https://en.wikipedia.org/wiki/EEPROM)

4. Air Supply Lab. (s.f.). *Memory technologies in embedded systems*. Air Supply Lab. Recuperado el 22 de mayo de 2025, de [https://www.airsupplylab.com/embedded-info/emb_hardware-information/emb-hwinfo_memory-technologies.html](https://www.airsupplylab.com/embedded-info/emb_hardware-information/emb-hwinfo_memory-technologies.html)

5. Harvie, L. (2021, septiembre 3). *Embedded systems memory types: Flash vs SRAM vs EEPROM*. Medium. Recuperado de [https://medium.com/@lanceharvieruntime/embedded-systems-memory-types-flash-vs-sram-vs-eeprom-93d0eed09086](https://medium.com/@lanceharvieruntime/embedded-systems-memory-types-flash-vs-sram-vs-eeprom-93d0eed09086)

6. Electronic Design. (2012, abril 18). *Selecting the correct memory type for embedded applications*. Electronic Design. Recuperado de [https://www.electronicdesign.com/technologies/embedded/digital-ics/memory/article/21787261/selecting-the-correct-memory-type-for-embedded-applications](https://www.electronicdesign.com/technologies/embedded/digital-ics/memory/article/21787261/selecting-the-correct-memory-type-for-embedded-applications)


---
