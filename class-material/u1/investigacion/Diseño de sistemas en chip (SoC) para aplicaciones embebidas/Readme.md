# Diseño de Sistemas en Chip (SoC) para Aplicaciones Embebidas  
**Autor:** Alonso Villela Iker Saúl – 22211517  

**INSTITUTO TECNOLÓGICO DE TIJUANA**  
**Materia:** Sistemas Programables  
**Fecha:** 2025-09-15  

---

## Introducción  
Los **Sistemas en Chip (SoC)** integran múltiples componentes electrónicos, como procesadores, memoria, periféricos y módulos de comunicación, en un único chip. Esta integración permite reducir **consumo energético, tamaño y costo**, manteniendo un alto rendimiento y confiabilidad.  

Los SoC son fundamentales en aplicaciones embebidas, donde la **eficiencia energética, el tiempo de respuesta y la confiabilidad** son críticos. Su uso se extiende en sectores como:  

- Automotriz (vehículos autónomos, sistemas ADAS)  
- Electrónica de consumo (smartphones, wearables, tablets)  
- Internet de las Cosas (IoT, sensores inteligentes)  
- Robótica industrial y drones  
- Dispositivos médicos embebidos  

En esta investigación se exploran:  

1. **Arquitectura y componentes de un SoC**  
2. **Optimización de consumo y rendimiento**  
3. **Comparación y selección de SoC según aplicación**  
4. **Tendencias futuras en diseño de SoC embebidos**  

---

## Arquitectura y Componentes de un SoC  

Un SoC combina múltiples módulos en un solo chip, lo que permite **eficiencia en espacio y consumo**:  

- **CPU**: Procesador central (ARM Cortex, RISC-V, x86 embebido)  
- **GPU / Aceleradores**: Para procesamiento gráfico o de IA  
- **Memoria**: RAM, ROM, cache y memoria no volátil  
- **Periféricos**: UART, SPI, I2C, ADC/DAC, timers, PWM  
- **Módulos de comunicación**: Wi-Fi, Bluetooth, Zigbee, Ethernet  
- **Controladores de energía**: Reguladores y circuitos para eficiencia energética  

### Comparación de arquitecturas SoC
| SoC | CPU | Periféricos integrados | Consumo | Aplicaciones típicas |
|-----|-----|----------------------|---------|-------------------|
| ARM Cortex-M | Cortex-M0/M4 | UART, SPI, I2C, ADC | Muy bajo | IoT, sensores, wearables |
| RISC-V | RV32IMC | GPIO, UART, SPI | Muy bajo | Prototipos, educación, IoT |
| Qualcomm Snapdragon | Kryo CPU + GPU | Wi-Fi, LTE, Bluetooth, GPU | Medio/Alto | Smartphones, tablets |
| NVIDIA Jetson | ARM CPU + GPU | Ethernet, I/O digital | Alto | Robótica, visión artificial, IA |

💡 Observación: La elección de un SoC depende de **balance entre consumo, costo y capacidad de procesamiento**.  

---

## Optimización para Consumo y Rendimiento  

Para aplicaciones embebidas, optimizar **energía y rendimiento** es esencial:  

- **Clock gating** → Apaga circuitos inactivos  
- **Power domains** → Bloques de energía independientes  
- **Dynamic Voltage and Frequency Scaling (DVFS)** → Ajusta voltaje y frecuencia según la carga  
- **Pipeline y caches eficientes** → Mejoran desempeño sin aumentar consumo  

### Comparación de técnicas de optimización
| Técnica | Beneficio | Limitación |
|---------|-----------|-----------|
| Clock gating | Reduce consumo | Complejidad de diseño |
| Power domains | Eficiencia energética | Mayor tamaño de chip |
| DVFS | Balance consumo/rendimiento | Control dinámico requerido |
| Pipeline / caches | Mejor rendimiento | Uso adicional de silicio y energía |

---

## Comparación de SoC según Aplicaciones  

| Aplicación | SoC recomendado | Justificación | Ventajas | Limitaciones |
|------------|----------------|---------------|----------|-------------|
| IoT de sensores | ARM Cortex-M | Bajo consumo y periféricos integrados | Eficiencia energética | Capacidad limitada de procesamiento |
| Wearables | RISC-V | Optimización energética y flexibilidad | Personalizable y de bajo costo | Ecosistema software más reducido |
| Smartphones | Snapdragon | Alto rendimiento, multimedia y conectividad | Potencia, soporte y ecosistema | Consumo elevado y costo |
| Robótica / visión artificial | NVIDIA Jetson | GPU potente para IA y procesamiento paralelo | Procesamiento gráfico e IA eficiente | Alto consumo y precio |

---

## Ventajas de SoC en Aplicaciones Embebidas  

1. **Reducción de espacio y costo**: Todo en un solo chip  
2. **Eficiencia energética**: Crucial para dispositivos portátiles  
3. **Mayor velocidad de comunicación interna**: Entre CPU, memoria y periféricos  
4. **Flexibilidad de diseño**: Se pueden integrar módulos según la aplicación  
5. **Compatibilidad con estándares modernos**: IoT, protocolos de comunicación y sensores  

---

## Tendencias Futuras  

- **Integración de inteligencia artificial** en SoC para procesamiento local (edge computing)  
- **SoC heterogéneos**: combinan CPU, GPU y aceleradores especializados  
- **Tecnologías de bajo consumo extremo**: ideal para IoT de larga duración  
- **Seguridad embebida**: inclusión de módulos criptográficos y control de acceso hardware  
- **Diseño basado en RISC-V**: creciente adopción por flexibilidad y licencias abiertas  

---

## Diagramas Conceptuales  

### Arquitectura típica de un SoC embebido
![Arquitectura SoC](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/ADSL_modem_router_internals_labeled.jpg/800px-ADSL_modem_router_internals_labeled.jpg)  
_Figura 1. Arquitectura conceptual de un SoC embebido._  

### Flujo de optimización de energía y rendimiento
![Optimización SoC](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2024/09/270-Preview-min.jpg?w=800&ssl=1)  
_Figura 2. Técnicas de optimización energética en SoC._  

---

## Conclusiones  

1. Los **SoC** permiten integrar múltiples funciones en un único chip, optimizando espacio, costo y consumo energético.  
2. La arquitectura y elección de CPU, memoria y periféricos impacta directamente en el rendimiento del sistema embebido.  
3. La implementación de técnicas de **optimización de energía y rendimiento** es crucial para dispositivos portátiles y IoT.  
4. Comparar SoC según **aplicación, consumo y capacidad de procesamiento** facilita decisiones de diseño eficientes.  
5. La evolución de SoC, incluyendo **IA integrada, SoC heterogéneos y seguridad embebida**, permite aplicaciones más complejas y confiables.  

---

## Referencias (Formato APA)

- Wolf, W. (2022). *Computers as Components: Principles of Embedded Computing System Design*. Elsevier.  
- ARM Ltd. (2023). *Cortex-M Processor Technical Reference Manual*. ARM. https://developer.arm.com/  
- RISC-V Foundation. (2023). *RISC-V Specifications*. https://riscv.org/  
- Qualcomm. (2023). *Snapdragon Mobile Platform*. Qualcomm. https://www.qualcomm.com/  
- NVIDIA. (2023). *Jetson Developer Guide*. NVIDIA. https://developer.nvidia.com/embedded/jetson  
- Lee, E. A., & Seshia, S. A. (2020). *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. MIT Press.  
- Sysgo. (2022). *Embedded Systems Design and Optimization*. Sysgo. https://www.sysgo.com/


