# **Procesamiento Digital de Señales (DSP) en Sistemas Programables** 📡💻🔊

---

## Autor:
**GitHub:** NicolasLF2706

**Nombre:** López Félix Nicolás

**Matrícula:** C21212706

---

## Resumen ejecutivo ✨

Esta investigación revisa el estado del arte y las prácticas actuales para implementar **DSP en sistemas programables**: microcontroladores con extensiones SIMD (Arm Helium), procesadores DSP dedicados 
(TI C66x), SoC/MPSoC (Zynq/RFSoC), FPGAs/ACAPs (DSP slices, Versal AI Engines), y los ecosistemas de software (CMSIS-DSP, GNU Radio, HLS, MATLAB/HDL Coder, TensorFlow Lite Micro). Se discuten algoritmos 
clave (FIR/IIR, FFT, decimación, filtrado adaptativo), flujos de trabajo (model-based design, HLS, co-diseño HW/SW), técnicas de optimización (vectorización, fixed-point), casos de uso (SDR, radar, audio, 
TinyML), y recomendaciones prácticas para prototipado y producción. ([Nature][1])

<img width="1024" height="683" alt="image" src="https://github.com/user-attachments/assets/edc52748-fe11-4e78-8ee5-78bd6992ae39" />

---

## Índice 📚

1. [Introducción y motivación](#introducción-y-motivación)
2. [Plataformas programables — panorama](#plataformas-programables---panorama)
3. [Algoritmos y kernels DSP fundamentales](#algoritmos-y-kernels-dsp-fundamentales)
4. [Herramientas, bibliotecas y flujos de trabajo](#herramientas-bibliotecas-y-flujos-de-trabajo)
5. [Diseño: metodología, HLS y co-diseño HW/SW](#diseño-metodología-hls-y-co-diseño-hwsw)
6. [Optimización: fixed-point, vectorización, memoria y DSP slices](#optimización-fixed-point-vectorización-memoria-y-dsp-slices)
7. [Casos de uso y estudios prácticos](#casos-de-uso-y-estudios-prácticos)
8. [Buenas prácticas y checklist para proyectos](#buenas-prácticas-y-checklist-para-proyectos)
9. [Proyectos sugeridos para GitHub (ideas con stack)](#proyectos-sugeridos-para-github-ideas-con-stack)
10. [Recursos adicionales y lecturas recomendadas (APA)](#recursos-adicionales-y-lecturas-recomendadas-apa)
11. [Conclusión](#conclusión)

---

## Introducción y motivación 🧭

El DSP transforma señales analógicas en información útil mediante muestreo, filtrado y análisis en dominio tiempo/frecuencia. Implementar DSP en **sistemas programables** permite iteración rápida, 
reconfigurabilidad y despliegue en edge/embebidos (IoT, telecom, radar, audio), pero exige equilibrio entre rendimiento, latencia, consumo y coste. Las plataformas modernas ofrecen desde instrucciones 
vectoriales en MCU hasta motores dedicados en ACAPs/SoC para afrontar cargas en tiempo real. ([Nature][1])

---

## Plataformas programables — panorama 🧩

### 1. Microcontroladores y extensiones vectoriales (MCU + Helium)

Los Cortex-M recientes (M55/M85) incluyen **Helium (M-Profile Vector Extension, MVE)** para acelerar kernels DSP y TinyML en MCU con bajo consumo, aprovechando registros vectoriales y autovectorización. 
Ideal para audio, detección de eventos y modelos TinyML en el extremo. ([arm.com][2])

### 2. DSPs dedicados (ej. TI C66x)

Familias como **TMS320C66x** ofrecen núcleos DSP con ISA con soporte SIMD y unidades MAC de alta densidad, pensadas para procesamiento de señales en telecom y ADAS (radar). Son potentes para pipelines 
de baja latencia y throughput muy alto. ([TI][3])

### 3. FPGAs y bloques DSP (DSP48E1/E2)

Las FPGAs contienen **bloques DSP** (DSP48E1/E2 en Xilinx/AMD) especializados para MAC, multiplicación acumulada y rutas de red en cascada — permiten implementaciones paralelas y pipelinadas de filtros 
y multiplicadores complejos con eficiencia energética. ([docs.amd.com][4])

### 4. SoC/MPSoC, RFSoC y ACAPs (Zynq, RFSoC, Versal)

Sistemas heterogéneos combinan CPU, fabric programable y conversores RF integrados (RFSoC) o **AI/DSP Engines** (Versal) para aplicaciones de RF/5G, SDR, radar e inferecia ML a alta velocidad. Estos 
dispositivos facilitan mover tareas críticas a hardware y mantener control en software. ([AMD][5])

---

## Algoritmos y kernels DSP fundamentales 🔑

* **Filtros (FIR, IIR)** — diseño, implementación en directo (transversal, estructurado), simetrías y ahorro de recursos. (usar DSP slices para MACs). ([docs.amd.com][4])
* **FFT / DFT** — núcleo para análisis espectral, procesamiento multicanal y OFDM; bibliotecas altamente optimizadas (FFTW en servidores, KISSFFT para embebidos). ([fftw.org][6])
* **Interpolación / Decimación (sample-rate conversion)** — poliPhase/half-band filters para ahorro de cómputo.
* **Filtrado adaptativo (LMS, RLS)** — usado en cancelación de eco, equalización; buen candidato a HW acelerado.
* **Convoluciones y correlaciones** — optimizables por FFT (overlap-save/overlap-add) o por hardware streaming en FPGAs. ([arXiv][7])

Para MCU/embebido conviene usar librerías optimizadas (CMSIS-DSP) que implementan estos kernels con rotinas asm/vectorizadas. ([GitHub][8])

---

## Herramientas, bibliotecas y flujos de trabajo 🧰

* **CMSIS-DSP (ARM)** — colección optimizada de funciones DSP para Cortex-M/A (filtrado, FFT, álgebra vectorial). Ideal para MCU/embebidos con Helium/NEON. ([GitHub][8])
* **MATLAB & HDL Coder** — diseño basado en modelos (Simulink), conversión a HDL/IP, y workflow para prototipado en FPGA/SoC. Muy usado en industria para acelerar comprobación y generación de HDL. ([MathWorks][9])
* **Vitis HLS (AMD/Xilinx)** — sintetiza C/C++/HLS hacia RTL, con guías para optimizar kernels DSP y explotar AI Engines/PL. Útil para portado rápido a FPGA/SoC. ([docs.amd.com][10])
* **Intel DSP Builder / HLS / oneAPI** — toolbox para integración con Simulink y flujo HLS para FPGAs Intel, actualizado frecuentemente. ([Intel][11])
* **GNU Radio + gr-iio / RF Frameworks** — ecosistema para SDR, con ejemplos de aceleración en Zynq/RFSoC; excelente para prototipado de cadenas PHY. ([gnuradio.org][12])
* **Bibliotecas FFT**: **FFTW** (desktop/HPC) y **KISSFFT** (embebido). ([fftw.org][6])
* **TinyML / TensorFlow Lite for Microcontrollers** — cuando la tarea DSP incluye ML (clasificación de audio, detección), TFLM permite inferencia muy ligera en MCU. ([GitHub][13])

**Ejemplo rápido — clonando CMSIS-DSP**

```bash
# clona la librería CMSIS (ejemplo)
git clone https://github.com/ARM-software/CMSIS_5.git
# revisa la documentación DSP
# (usa CMSIS_DSP/README y ejemplos para Cortex-M)
```

(Ver CMSIS-DSP). ([GitHub][8])

---

## Diseño: metodología, HLS y co-diseño HW/SW 🔄

* **Model-based design** (Simulink → HDL) acorta ciclos: validar en MATLAB/Simulink y luego generar HDL con HDL Coder / DSP Builder. ([MathWorks][9])
* **HLS**: escribir kernels en C/C++ y aplicar pragmas (pipeline, unroll, dataflow) para controlar latencia/reutilización de recursos; Vitis/Intel HLS guían la inferencia de bloques DSP. ([docs.amd.com][10])
* **HW/SW partitioning (co-diseño)**: identificar hotspots (FFTs, filtros, convoluciones) y moverlos a PL/AI Engines/DSP cores mientras mantiene control y lógica de alto nivel en la CPU. Existen metodologías
* y herramientas para explorar el espacio de diseño y coste/consumo/latencia. ([arXiv][7])

---

## Optimización: fixed-point, vectorización, memoria y DSP slices ⚙️

### Fixed-point y cuantización

Para sistemas embebidos y FPGAs la conversión a **fixed-point (Q-format)** reduce recursos y consumo — requiere análisis de rango, simulación de cuantización y pruebas de regresión. Herramientas como Fixed-Point 
Designer y workflows de MATLAB ayudan a automatizar la conversión. ([MathWorks][14])

### Vectorización / SIMD (Helium / NEON)

Usar extensiones vectoriales (Helium en Cortex-M, NEON en Cortex-A) acelera kernels elementales (FIR, vectores, convolución) y reduce consumo por operación. Las bibliotecas CMSIS y compiladores modernos soportan 
autovectorización. ([arm.com][2])

### DSP slices y mapeo a FPGA

Diseña con conocimiento de la **anchura de multiplicación** de los DSP slices (p.ej. 27×18 en Ultrascale) y de cómo inferirlos desde HDL/HLS para maximizar frecuencia y minimizar LUTs. Hay guías específicas 
sobre cómo escribir código HDL/HLS para forzar el uso de DSP slices y evitar mapeos ineficientes. ([docs.amd.com][4])

### Memoria, DMA y streaming

Para throughput alto (multi-canal RF, OFDM) es crítico optimizar accesos a memoria, usar DMA, buffers en BRAM/URAM y streaming AXI-Stream en SoC para mantener las pipelines alimentadas. ([AMD][5])

---

## Casos de uso y estudios prácticos 🧪

### 1. Radio definida por software (SDR) — Zynq/RFSoC + GNU Radio

Despliegues de SDR usan RFSoC (con ADC/DAC integrados) y aceleran etapas (filtrado, decimación, FFT) en PL para alcanzar cientos de MSPS; comunidades como GNU Radio tienen ejemplos y soportes para Zynq 
y aceleradores. ([AMD][5])

### 2. Radar / ADAS — TI SoCs y aceleradores DSP

SOC con DSP (TI AWR family) y SoC heterogéneos permiten pipelines de detección y tracking en tiempo real; los manuales y TRMs del fabricante documentan el flujo para señalización y calibración. ([TI][15])

### 3. Edge ML (TinyML) + DSP (audio/event detection)

Clasificadores de audio y sensores usan preprocessado DSP (MFCCs, filtros) y modelos quantizados en TFLite Micro o CMSIS-NN para MCU. Ideal cuando se requiere latencia baja y consumo mínimo. ([GitHub][13])

### 4. Aceleración ML/DSP en Versal/AI Engines

Aplicaciones que requieren alto throughput (beamforming, STAP, GEMM) mapean kernels a AI Engines y PL para lograr baja latencia en 5G y radar. ([docs.amd.com][16])

Ejemplo publicado: offload de muestras RF a RFSoC para 100 Gbit/s demostrando cómo la integración PL↔PS permite throughput extremo en sistemas RF modernos. ([University of Strathclyde][17])

---

## Buenas prácticas y checklist para proyectos ✅

* Comienza con **model-based design** (Simulink/Matlab) para validar funcionalidad antes de sintetizar. ([MathWorks][9])
* Usa **profiling**: detecta hotspots y decide H/W acceleration (profilers de CPU, emulación HLS). ([docs.amd.com][10])
* Planifica **word-length & Q-format** desde el inicio; automatiza pruebas de cuantización. ([MathWorks][14])
* Prioriza **streaming + DMA + BRAM/URAM** para throughput; evita accesos aleatorios a memoria externa. ([AMD][5])
* Documenta interfaces (AXI-Stream, AXI-Lite) y crea testbenches HDL + golden vectors (MATLAB↔HDL cosim). ([MathWorks][9])

---

## Proyectos sugeridos para GitHub (roadmap rápido) 🚀

1. **Filtro FIR acelerado por Helium (Cortex-M55)**

   * Stack: CMSIS-DSP, GCC arm, board con Cortex-M55
   * Objetivo: comparar rendimiento float vs Q15 y medir consumo. ([GitHub][8])

2. **Flow SDR: GNU Radio + acelerador FIR en Zynq**

   * Stack: GNU Radio, Vitis HLS, Zynq/ZCU board, gr-iio
   * Objetivo: implementar FIR en PL, medir latencia y throughput. ([gnuradio.org][12])

3. **Pipeline FFT para RFSoC (prototipo)**

   * Stack: Vitis, RFSoC eval board, Vivado, MATLAB (golden vectors)
   * Objetivo: despliegue de FFT streaming y comparación con FFTW en servidor. ([AMD][5])

4. **TinyML audio detector (MCU)**

   * Stack: TensorFlow Lite Micro, CMSIS-DSP (preproc), Arduino/STM32 board.
   * Objetivo: extracción de MFCCs en fixed-point + modelo quantizado. ([GitHub][13])

Cada proyecto debería acompañarse de: README con pasos reproducibles, scripts de build (Make/CMake), test vectors, y resultados (latencia/consumo/uso de recursos).

---

## Recursos adicionales y lecturas recomendadas (APA) 📑

* Arm. (n.d.). *Helium technology (M-Profile Vector Extension)*. Recuperado el 15 de septiembre de 2025, de [https://www.arm.com/technologies/helium](https://www.arm.com/technologies/helium). ([arm.com][2])
* ARM-software. (n.d.). *CMSIS-DSP Software Library (repositorio)*. Recuperado el 15 de septiembre de 2025, de [https://github.com/ARM-software/CMSIS\_5](https://github.com/ARM-software/CMSIS_5). ([GitHub][8])
* MathWorks. (n.d.). *HDL Coder — MATLAB*. Recuperado el 15 de septiembre de 2025, de [https://www.mathworks.com/products/hdl-coder.html](https://www.mathworks.com/products/hdl-coder.html). ([MathWorks][9])
* Xilinx / AMD. (2023). *Vitis High-Level Synthesis User Guide (UG1399) — 2023.2*. Recuperado de [https://docs.amd.com/r/2023.2-English/ug1399-vitis-hls](https://docs.amd.com/r/2023.2-English/ug1399-vitis-hls). ([docs.amd.com][10])
* FFTW Project. (n.d.). *FFTW — Fastest Fourier Transform in the West*. Recuperado el 15 de septiembre de 2025, de [http://www.fftw.org/](http://www.fftw.org/). ([fftw.org][6])
* Borgerding, m. (n.d.). *KISSFFT (GitHub)*. Recuperado el 15 de septiembre de 2025, de [https://github.com/mborgerding/kissfft](https://github.com/mborgerding/kissfft). ([GitHub][18])
* TensorFlow. (n.d.). *TensorFlow Lite for Microcontrollers (GitHub)*. Recuperado el 15 de septiembre de 2025, de [https://github.com/tensorflow/tflite-micro](https://github.com/tensorflow/tflite-micro). ([GitHub][13])
* AMD. (2025). *AI Engine — Versal ACAP Design (UG1273 2025.1)*. Recuperado el 15 de septiembre de 2025, de [https://docs.amd.com/r/en-US/ug1273-versal-acap-design/AI-Engine](https://docs.amd.com/r/en-US/ug1273-versal-acap-design/AI-Engine). ([docs.amd.com][16])
* AMD. (n.d.). *Zynq UltraScale+ RFSoCs — product overview*. Recuperado el 15 de septiembre de 2025, de [https://www.amd.com/en/products/adaptive-socs-and-fpgas/soc/zynq-ultrascale-plus-rfsoc.html](https://www.amd.com/en/products/adaptive-socs-and-fpgas/soc/zynq-ultrascale-plus-rfsoc.html). ([AMD][5])
* Analog Devices. (2024). *AD9361 Data Sheet — RF Agile Transceiver (1 Mar 2024)*. Recuperado de [https://www.analog.com/media/en/technical-documentation/data-sheets/ad9361.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/ad9361.pdf). ([analog.com][19])
* Xilinx (AMD). (2020). *DSP48E2 — UltraScale DSP Slice (UG958 / UG579)*. Recuperado el 15 de septiembre de 2025, de [https://docs.amd.com/r/en-US/ug958-v](https://docs.amd.com/r/en-US/ug958-v) i v a d o-sysgen-ref/DSP48E2. ([docs.amd.com][4])
* Intel. (2024). *DSP Builder for Intel® FPGAs — Pro Edition (v24.2)*. Recuperado el 15 de septiembre de 2025, de [https://www.intel.com/content/www/us/en/software-kit/826866/dsp-builder-for-intel-fpgas-pro-edition-software-version-24-2.html](https://www.intel.com/content/www/us/en/software-kit/826866/dsp-builder-for-intel-fpgas-pro-edition-software-version-24-2.html). ([Intel][11])
* Darvish Rouhani, B., Ghasemzadeh, M., & Koushanfar, F. (2024). *A survey on FPGA-based accelerators for ML models*. arXiv. Recuperado de [https://arxiv.org/abs/2412.15666](https://arxiv.org/abs/2412.15666). ([arXiv][7])
* Sadeghi, S. (2024). *Classifying FPGA Technology in Digital Signal Processing: A review*. *International Journal / Procedia* (ResearchGate). Recuperado de [https://www.researchgate.net/publication/383859834](https://www.researchgate.net/publication/383859834). ([ResearchGate][20])
* (Ejemplo académico técnico) Šiaučiulis, M. et al. (2023). *100 GBit/s RF sample offload for RFSoC* (NEWCAS 2023). Recuperado de [https://pureportal.strath.ac.uk/files/175905824/Siauciulis\_etal\_NEWCAS2023\_100GBit\_s\_RF\_sample\_offload\_for\_RFSoC.pdf](https://pureportal.strath.ac.uk/files/175905824/Siauciulis_etal_NEWCAS2023_100GBit_s_RF_sample_offload_for_RFSoC.pdf). ([University of Strathclyde][17])

---

## Conclusión 👁️‍🗨️

El procesamiento digital de señales en **sistemas programables** es un campo maduro pero en rápida evolución: las plataformas heterogéneas (MCU con Helium, SoC/FPGA/ACAP) y las mejoras en toolchains (HLS, HDL Coder, DSP Builder) han hecho posible mover cargas DSP muy exigentes al edge con latencias bajas y alto throughput. Para proyectos reales, el camino recomendado es: validar en MATLAB/Simulink → perfilar en CPU → migrar kernels críticos a HLS/PL → cuantizar y verificar, y medir en hardware (test vectors, golden checks). Las referencias anteriores contienen material práctico y documentación oficial para empezar. ([MathWorks][9])

---

[1]: https://www.nature.com/research-intelligence/nri-topic-summaries/digital-signal-processing-and-time-to-digital-converters-micro-191029 "Digital Signal Processing and Time-to-Digital Converters"
[2]: https://www.arm.com/technologies/helium "Helium Technology"
[3]: https://www.ti.com/lit/ug/sprugh7/sprugh7.pdf "C66x CPU and Instruction Set Reference Guide"
[4]: https://docs.amd.com/r/en-US/ug958-vivado-sysgen-ref/DSP48E2 "DSP48E2 - 2020.2 English - UG958"
[5]: https://www.amd.com/en/products/adaptive-socs-and-fpgas/soc/zynq-ultrascale-plus-rfsoc.html "Zynq UltraScale+ RFSoCs"
[6]: https://www.fftw.org/ "FFTW Home Page"
[7]: https://arxiv.org/html/2412.15666v1 "A survey on FPGA-based accelerator for ML models This ..."
[8]: https://github.com/ARM-software/CMSIS-DSP "CMSIS-DSP embedded compute library for Cortex-M and ..."
[9]: https://www.mathworks.com/products/hdl-coder.html "HDL Coder - MATLAB"
[10]: https://docs.amd.com/r/2023.2-English/ug1399-vitis-hls "Vitis High-Level Synthesis User Guide (UG1399) - 2023.2 ..."
[11]: https://www.intel.com/content/www/us/en/software-kit/826866/dsp-builder-for-intel-fpgas-pro-edition-software-version-24-2.html "DSP Builder for Intel® FPGAs Pro Edition Software Version ..."
[12]: https://www.gnuradio.org/ "GNU Radio"
[13]: https://github.com/tensorflow/tflite-micro "tensorflow/tflite-micro"
[14]: https://www.mathworks.com/help/dsp/fixed-point-design.html "Fixed-Point Design - MATLAB & Simulink"
[15]: https://www.ti.com/lit/ug/spruiv5b/spruiv5b.pdf "AWR294x and AWR2944LC Technical Reference Manual"
[16]: https://docs.amd.com/r/en-US/ug1273-versal-acap-design/AI-Engine "AI Engine - 2025.1 English - UG1273"
[17]: https://pureportal.strath.ac.uk/files/175905824/Siauciulis_etal_NEWCAS2023_100GBit_s_RF_sample_offload_for_RFSoC.pdf "100GBit/s RF sample offload for RFSoC using GNU Radio ..."
[18]: https://github.com/mborgerding/kissfft "mborgerding/kissfft: a Fast Fourier Transform (FFT) library that tries to ..."
[19]: https://www.analog.com/media/en/technical-documentation/data-sheets/ad9361.pdf "Data Sheet - AD9361"
[20]: https://www.researchgate.net/publication/383859834_Classifying_FPGA_Technology_in_Digital_Signal_Processing_A_review "Classifying FPGA Technology in Digital Signal Processing"
