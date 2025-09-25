## Gonzalo Cortez Huerta 22210761
## Fuentes de información.

- [Qué son los sistemas embebidos y sus aplicaciones](https://www.bbva.com/es/que-son-los-sistemas-embebidos-y-para-que-sirven/)  
- [Realidad Virtual y Aumentada: Definiciones y aplicaciones](https://www.xataka.com/realidad-virtual-aumentada)  
- [Sistemas embebidos en AR/VR](https://www.researchgate.net/publication/333563729_Embedded_Systems_for_Virtual_Reality_and_Augmented_Reality)  
- [NVIDIA - Sistemas embebidos para realidad virtual](https://developer.nvidia.com/embedded-computing)  
- [Qualcomm XR - Procesadores para realidad extendida](https://www.qualcomm.com/products/features/extended-reality-xr)  

# Sistemas Embebidos para Realidad Aumentada (AR) y Realidad Virtual (VR)

## Descripción de la petición
- **Lo que le pedí a la (IA):** Información sobre *sistemas embebidos aplicados a AR y VR*, en formato Markdown  
- **Lo que modifique:** Añadí al inicio toda la información y la modifique, además agregue un **diagrama en formato Mermaid, también agregué imágenes y links de las fuentes.**.  

---

## Introducción

Un **sistema embebido** en el contexto de AR/VR es un dispositivo especializado que integra hardware y software dedicado para procesar datos de sensores, gráficos y audio en tiempo real. Estos sistemas permiten que gafas, cascos o dispositivos móviles logren experiencias inmersivas con baja latencia, alto rendimiento y bajo consumo energético.

---

## Componentes principales

### Hardware

| Componente | Función | Retos clave |
|------------|---------|-------------|
| **Procesador (CPU/GPU/SoC)** | Ejecutar gráficos, lógica, visión por computadora. | Alto rendimiento con bajo consumo. |
| **Sensores de movimiento (IMU)** | Detectar orientación y posición. | Baja latencia, fusión de sensores. |
| **Cámaras / sensores visuales** | Captura del entorno y SLAM. | Velocidad de cuadros, iluminación variable. |
| **Pantallas / ópticas** | Visualización inmersiva. | Alta densidad, brillo, corrección óptica. |
| **Audio** | Sonido espacial e inmersivo. | Calidad + baja latencia. |
| **Conectividad** | WiFi, Bluetooth, etc. | Ancho de banda y estabilidad. |
| **Energía y disipación** | Autonomía y confort. | Minimizar calor y peso. |

### Software

- RTOS o sistemas operativos embebidos.  
- Middleware de visión por computadora (ej. SLAM).  
- Motores gráficos (Unity, Unreal, motores propios).  
- APIs para integración de sensores y renderizado.  

---

## Desafíos

- Balance entre **rendimiento y consumo energético**.  
- Mantener **latencias < 20 ms** para evitar mareos.  
- **Miniaturización y ergonomía** en gafas/cascos.  
- **Fusión de sensores múltiples** con sincronización.  
- **Privacidad y seguridad** de los datos capturados.  

---

## Ejemplos recientes

- **On-sensor compute distribuido** para reducir latencia.  
  [arXiv - Distributed On-Sensor Compute](https://arxiv.org/abs/2203.07474)  

- **SLAM eficiente en móviles** (~50 fps con bajo consumo).  
  [arXiv - Embedded SLAM](https://arxiv.org/pdf/1702.01295)  

- **Framework OpenUVR** para optimizar latencia en VR inalámbrica.  
  [arXiv - OpenUVR](https://arxiv.org/abs/2101.07327)  

---

## Imágenes

- [Enabling the hardware for the metaverse](https://images.openai.com/thumbnails/url/_6vqDHicu1mSUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7JS8_KSvcyzQnI8MqOCsjIdioKdXLNN8yLNEkOTDQuy8hLyfYJs0jJMgkptzQuTgzV9UnLrqhIrXT2T1crBgA09Sql)  
- [Enhance your next VR/AR design with these parts](https://images.openai.com/thumbnails/url/fEq9B3icu1mSUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7Kcs8sc4yo9CwrjwpxNEtLrcrM9fauivANcfX20A2zcCpIcQ8O8jTKjqp0DzI39XGqLE7xK3TJD_f2LFcrBgAp2yoJ)  
- [Computer Vision for AR in Embedded Designs](https://images.openai.com/thumbnails/url/tQNk33icu1mUUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw4s8ynO9HZxSXUyLQpxCY8sSjLVDcm3DC6JiLKs8HLNNSjJcs-OD3OMiEzMjkiuLDUpTQ-2CAw0tyhUKwYAxqApOA)  
- [Embedded Vision - AR](https://images.openai.com/thumbnails/url/R579DXicu1mSUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw6xSMrJzjNMzDXzM3TLznV3y_XPcTMtDsxPLU83zrL0cyxNTgpzNnKKtLQoSHWLLMz2LvOLcg6rcEzVTVcrBgAWcCm2)  

---

## Diagrama en Mermaid

```mermaid
graph TD
    A[Dispositivo AR/VR] --> B[Hardware]
    A --> C[Software]

    B --> B1[Procesador SoC CPU-GPU]
    B --> B2[Sensores IMU]
    B --> B3[Camaras y Vision]
    B --> B4[Pantallas y Opticas]
    B --> B5[Audio]
    B --> B6[Conectividad]
    B --> B7[Energia y Refrigeracion]

    C --> C1[RTOS o Firmware]
    C --> C2[Middleware Vision SLAM]
    C --> C3[Motor Grafico Unity-Unreal]
    C --> C4[APIs de Sensores]
    C --> C5[Optimizacion de Latencia]

    B3 --> C2
    B2 --> C2
    C3 --> B4
    C5 --> A
