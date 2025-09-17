# Anexo – Diseño de Sistemas en Chip (SoC) para Aplicaciones Embebidas  
**Autor:** Alonso Villela Iker Saúl – 22211517  

## Asistencia de IA  

Para la investigación sobre diseño de **SoC para aplicaciones embebidas**, utilicé **ChatGPT (GPT-5)** como apoyo únicamente para:  

- Identificar **fuentes confiables** en la web sobre arquitecturas y SoC modernos.  
- Recibir recomendaciones de **diagramas y tablas** que muestran comparaciones de SoC y optimización de consumo.  
- Estructurar el documento en **formato Markdown** siguiendo buenas prácticas para GitHub.  
- Resumir información compleja sobre **arquitecturas, rendimiento y consumo** en tablas comparativas.  

El contenido final fue redactado, organizado y revisado de manera manual por el autor.  

---

## Herramientas Utilizadas  
- **ChatGPT (GPT-5, modo investiga a fondo).**  
- **Fecha de asistencia:** 2025-09-15.  
- **Plataforma:** Recomendaciones sobre diseño de SoC y optimización embebida.  
- **Otras herramientas:**  
  - VS Code para edición de Markdown.  
  - Navegadores web para consulta de documentación oficial y papers académicos.  

---

## Prompts Utilizados (ejemplos)  
1. *“Necesito investigar sobre diseño de SoC para aplicaciones embebidas, incluyendo arquitectura, consumo y rendimiento.”*  
2. *“Por favor, agrega referencias en formato APA para incluirlas en mi investigación.”*  
3. *“Recomiéndame diagramas y tablas comparativas de SoC para ilustrar mi README.md.”*  
4. *“Explícame cómo insertar imágenes en Markdown con ajuste de tamaño y posición.”*  
5. *“Genera una tabla comparativa de arquitecturas SoC (ARM, RISC-V, Snapdragon, Jetson) con ventajas, limitaciones y aplicaciones.”*  
6. *“Haz un cuadro comparativo de técnicas de optimización energética en SoC, indicando beneficios y limitaciones.”*  

---

## Ejemplos de Información Integrada  

### Comparación de Arquitecturas SoC
| SoC | CPU | Periféricos integrados | Consumo | Aplicaciones típicas |
|-----|-----|----------------------|---------|-------------------|
| ARM Cortex-M | Cortex-M0/M4 | UART, SPI, I2C, ADC | Muy bajo | IoT, sensores, wearables |
| RISC-V | RV32IMC | GPIO, UART, SPI | Muy bajo | Prototipos, educación, IoT |
| Qualcomm Snapdragon | Kryo CPU + GPU | Wi-Fi, LTE, Bluetooth, GPU | Medio/Alto | Smartphones, tablets |
| NVIDIA Jetson | ARM CPU + GPU | Ethernet, I/O digital | Alto | Robótica, visión artificial, IA |

### Comparación de Técnicas de Optimización de Consumo
| Técnica | Beneficio | Limitación |
|---------|-----------|-----------|
| Clock gating | Reduce consumo | Complejidad de diseño |
| Power domains | Eficiencia energética | Mayor tamaño de chip |
| DVFS | Balance consumo/rendimiento | Control dinámico requerido |
| Pipeline / caches | Mejor rendimiento | Uso extra de silicio y energía |

### Comparación de SoC según Aplicaciones  
| Aplicación | SoC recomendado | Justificación | Ventajas | Limitaciones |
|------------|----------------|---------------|----------|-------------|
| IoT de sensores | ARM Cortex-M | Bajo consumo y periféricos integrados | Eficiencia energética | Capacidad limitada de procesamiento |
| Wearables | RISC-V | Optimización energética y flexibilidad | Personalizable y de bajo costo | Ecosistema software reducido |
| Smartphones | Snapdragon | Alto rendimiento, multimedia y conectividad | Potencia, soporte y ecosistema | Consumo elevado y costo |
| Robótica / visión artificial | NVIDIA Jetson | GPU potente para IA y procesamiento paralelo | Procesamiento gráfico e IA eficiente | Alto consumo y precio |

---

## Referencias Consultadas  
Además de las referencias listadas en el README, se consultaron:  

- Wolf, W. (2022). *Computers as Components: Principles of Embedded Computing System Design*. Elsevier.  
- ARM Ltd. (2023). *Cortex-M Processor Technical Reference Manual*. ARM. https://developer.arm.com/  
- RISC-V Foundation. (2023). *RISC-V Specifications*. https://riscv.org/  
- Qualcomm. (2023). *Snapdragon Mobile Platform*. Qualcomm. https://www.qualcomm.com/  
- NVIDIA. (2023). *Jetson Developer Guide*. NVIDIA. https://developer.nvidia.com/embedded/jetson  
- Sysgo. (2022). *Embedded Systems Design and Optimization*. Sysgo. https://www.sysgo.com/  

---

## Observaciones Adicionales  

- La asistencia de IA fue **solo orientativa**, para organizar información, generar ejemplos visuales y sugerir comparaciones de SoC.  
- Todas las decisiones de contenido, redacción y selección de referencias fueron tomadas por el autor para asegurar **coherencia académica y profesional**.  
- Se incluyeron **tablas comparativas y diagramas conceptuales** para facilitar la comprensión de arquitecturas, técnicas de optimización y aplicaciones de SoC.  
- Este anexo complementa el README, ofreciendo **información práctica y profesional** sobre diseño de sistemas embebidos basados en SoC.  
