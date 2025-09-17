# Procesamiento Paralelo en FPGA para Visión por Computadora  

**Autor:** Gómez Aguilar Jared Emmanuel  
**Número de Control:** 22210309  
**GitHub:** JaredEmmanuelGomezAguilar  

---

## 📋 Resumen  

Este proyecto investiga el **procesamiento paralelo en FPGAs** (Field-Programmable Gate Arrays) aplicado a la **visión por computadora**. Las FPGAs permiten implementar **pipelines** de hardware altamente paralelos, ideales para procesar imágenes y vídeo en tiempo real con baja latencia y alto rendimiento energético.  

Con el uso de **paralelismo espacial** y **arquitecturas en flujo (streaming)**, las FPGAs se han convertido en un componente clave en sistemas embebidos y de alto rendimiento que requieren análisis visual rápido, como vehículos autónomos, drones y robots industriales.  

![Imagen FPGA](https://raw.githubusercontent.com/github/explore/main/topics/fpga/fpga.png)  
*Diagrama conceptual de una FPGA con bloques configurables.*  

---

## 🎯 Objetivo del Proyecto  

- Comprender cómo las FPGAs aprovechan el **paralelismo espacial** para acelerar algoritmos de visión por computadora.  
- Explorar las técnicas de **streaming de datos**, **buffers de línea** y **ventanas deslizantes** para filtros 2D.  
- Analizar su aplicación tanto en **visión clásica** (Sobel, Gauss, Morfología) como en **redes neuronales convolucionales (CNNs)**.  
- Identificar casos de uso donde las FPGAs superan a CPU y GPU en rendimiento y eficiencia energética.  

![Imagen de procesamiento paralelo](https://raw.githubusercontent.com/github/explore/main/topics/parallel-computing/parallel-computing.png)  
*Ejemplo de procesamiento paralelo aplicado a datos en hardware.*  

---

## 🔍 Antecedentes  

En CPU y GPU, el paralelismo se logra con **hilos y SIMD**. En FPGA, se construyen **módulos paralelos en hardware** que operan simultáneamente. Esta arquitectura permite:  

- **Latencia constante y predecible.**  
- **Procesamiento pixel-a-pixel en tiempo real.**  
- **Optimización energética para dispositivos embebidos.**  

Las FPGAs también facilitan **co-diseño hardware/software**, donde se combina el control de alto nivel con aceleradores personalizados para cada algoritmo.  

![Imagen visión por computadora](https://raw.githubusercontent.com/github/explore/main/topics/computer-vision/computer-vision.png)  
*Relación entre visión por computadora y aceleración en hardware.*  

---

## ⚙️ Fundamentos del Procesamiento Paralelo  

### Pipelining y Dataflow  
- **PIPELINE:** procesa un dato nuevo cada ciclo.  
- **DATAFLOW:** permite que varias funciones se ejecuten en paralelo usando canales FIFO internos.  

### Buffers de Línea y Ventanas  
- Almacenan `N-1` líneas para construir una ventana `N×N` cada ciclo.  
- Evitan accesos constantes a memoria externa y permiten **II=1** (initiation interval de un ciclo).  

### Comunicación entre Módulos  
- Se usan protocolos como **AXI4-Stream** para encadenar IPs de vídeo.  
- En OpenCL (Intel), se implementan **pipes/channels** para flujos entre kernels.  

---

## 🖼️ Aplicaciones Prácticas  

- **Filtros 2D:** Sobel, Gauss, Laplaciano, morfología.  
- **Conversión de espacio de color y normalización.**  
- **Histogramas y ecualización en hardware.**  
- **Aceleración de CNNs:** uso de arreglos sistólicos, cuantización y tiling.  
- **Visión por eventos:** procesamiento de datos asíncronos provenientes de sensores neuromórficos.  

![Aplicaciones FPGA](https://raw.githubusercontent.com/github/explore/main/topics/machine-learning/machine-learning.png)  
*Ejemplo de aplicaciones de hardware para visión y ML.*  

---

## 🔧 Ventajas del Uso de FPGA en Visión  

- **Determinismo:** los tiempos de procesamiento son predecibles, esencial para sistemas críticos.  
- **Personalización:** los recursos lógicos se ajustan al algoritmo específico.  
- **Baja latencia:** ideal para cámaras de alta velocidad y sistemas de seguridad.  
- **Escalabilidad:** se pueden replicar módulos para procesar múltiples flujos de vídeo simultáneamente.  

---

## 🛠️ Herramientas y Ecosistema  

- **AMD/Xilinx:** Vivado, Vitis HLS, Vitis Vision (IP para visión listas para usar).  
- **Intel:** Quartus, SDK for OpenCL, uso de pipes/channels.  
- **Placas recomendadas:** Zynq, Versal, Arria, Stratix.  
- **Frameworks:** OpenCL, HLS C++, Python con PYNQ para prototipado rápido.  

![Imagen herramientas FPGA](https://raw.githubusercontent.com/github/explore/main/topics/python/python.png)  
*Entorno de desarrollo y prototipado con Python y PYNQ.*  

---

## 📝 Buenas Prácticas  

- Diseñar **streaming end-to-end** evitando memorias externas.  
- Mantener **II=1** y aplicar **DATAFLOW** entre funciones críticas.  
- Usar formatos **fixed-point** y **cuantización** para CNNs.  
- Verificar protocolos AXI4-Stream y señales SOF/EOL para vídeo.  
- Planificar el uso de recursos lógicos (LUTs, BRAM, DSP) para no saturar la FPGA.  

---

## 📊 Arquitectura Típica de un Pipeline de Visión  

```text
Cámara o Fuente de Video 
        │
        ▼
   DMA / Captura
        │
        ▼
   Preprocesamiento (filtros, normalización)
        │
        ▼
   Acelerador CNN / Algoritmo específico
        │
        ▼
  Postprocesamiento (umbralización, detección)
        │
        ▼
   Salida (HDMI, almacenamiento, transmisión)

```
---

## 🚀 Conclusión  

El **procesamiento paralelo en FPGA** ofrece un camino sólido para implementar **sistemas de visión por computadora en tiempo real**. Gracias a su arquitectura configurable, pipelines deterministas y eficiencia energética, las FPGAs son la plataforma ideal para aplicaciones embebidas y de alto rendimiento.  

---

## 📚 Referencias  

1. AMD/Xilinx. [AXI4-Stream Video IP and System Design Guide](https://docs.xilinx.com/)  
2. AMD. [Window2D: Line and Window Buffers – Vitis Tutorials](https://github.com/Xilinx/Vitis-Tutorials)  
3. AMD. [Sobel (Vitis Vision)](https://www.xilinx.com/)  
4. Intel. [FPGA SDK for OpenCL – Best Practices](https://www.intel.com/content/www/us/en/software/programmable/sdk-for-opencl.html)  
5. Jiang et al. “FPGA-based Acceleration for CNNs” (2025)  
6. *A survey on FPGA-based accelerator for ML models* (2024)  
7. *Event-based vision on FPGAs – a survey* (2024) 
   Salida (HDMI, almacenamiento, transmisión)

