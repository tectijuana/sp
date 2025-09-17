# Sensores biométricos (frecuencia cardiaca, huella, EEG, EMG) y sus aplicaciones en sistemas embebidos.

##
**Nombre:** Diego Huerta Espinoza  
**Numero de control:** 20212411  
**Fecha:** 17 de Septiembre del 2025  

<img width="400" height="350" alt="image" src="https://github.com/user-attachments/assets/9f9a59d8-74b6-4b2f-9821-d2f39032d01c" />

## 1. Introducción
Los sensores biométricos permiten capturar señales fisiológicas únicas que identifican o monitorean a una persona. En sistemas embebidos se utilizan en aplicaciones médicas, de seguridad y de interacción hombre-máquina. Sus principales retos son el consumo energético, el ruido de señal y la privacidad de datos.
## Principales sensores biométricos


| Sensor                | Variable medida             | Aplicación principal                     |
|-----------------------|-----------------------------|------------------------------------------|
| **Frecuencia cardiaca** | Ritmo cardíaco (BPM)        | Monitoreo médico, wearables de fitness   |
| **Huella dactilar**   | Patrones de huella          | Seguridad y autenticación de usuarios    |
| **EEG** (Electroencefalograma) | Actividad eléctrica cerebral | Neurociencia, control por pensamiento   |
| **EMG** (Electromiograma) | Actividad muscular        | Rehabilitación, prótesis biónicas        |

## 2. Sensor de Frecuencia Cardíaca (PPG / ECG)

### Principio de funcionamiento
- **PPG (Fotopletismografía):** usa LED y fotodetector para medir variaciones en el flujo sanguíneo.  
- **ECG (Electrocardiograma):** mide la actividad eléctrica del corazón mediante electrodos en la piel.

### Señal
- PPG: baja frecuencia (0.5–4 Hz), sensible a movimiento.  
- ECG: incluye ondas P, QRS y T; amplitud en mV.

### Integración embebida
- Front-ends: MAX86140, AD8232, ADS129x.  
- MCU con ADC de 12–24 bits.  
- Muestreo: 100–1000 Hz.

### Procesamiento
- Filtrado pasa-banda y notch.  
- Algoritmos de detección de picos (Pan-Tompkins).  
- Cálculo de frecuencia cardíaca y variabilidad (HRV).

### Aplicaciones
- Smartwatches y pulseras fitness.  
- Monitores médicos portátiles.  
- Alarmas de arritmias y telemetría clínica.

---

## 3. Sensor de Huella Dactilar

### Principio de funcionamiento
- **Óptico:** obtiene imagen iluminada de la huella.  
- **Capacitivo:** mide diferencias de capacitancia entre crestas y valles.  
- **Ultrasónico:** usa ondas para mapear microestructuras de la piel.

### Datos generados
- Imagen o plantilla biométrica (minucias).  
- Tamaño: pocos kilobytes.

### Integración embebida
- Interfaces: UART, SPI, I²C.  
- Sensores comunes: R305, GT-521F.  
- Procesamiento local o en coprocesador.

### Aplicaciones
- Control de acceso (cerraduras inteligentes).  
- Terminales de pago y kioscos.  
- Autenticación en IoT.

---

## 4. Sensor EEG (Electroencefalograma)

### Principio de funcionamiento
Mide señales eléctricas del cerebro mediante electrodos en el cuero cabelludo.

### Señal
- Amplitud en µV.  
- Bandas: delta, theta, alfa, beta, gamma.  
- Muy sensible a ruido y artefactos.

### Integración embebida
- Front-end: ADS1299.  
- ADC de 16–24 bits.  
- Muestreo: 128–1024 Hz.

### Procesamiento
- Filtrado, eliminación de artefactos (ICA, PCA).  
- Extracción de características (PSD, wavelets).  
- Clasificación mediante ML ligero (SVM, LDA, CNN).

### Aplicaciones
- Interfaces cerebro-computadora (BCI).  
- Monitoreo de sueño y epilepsia.  
- Juegos y neurofeedback.

---

## 5. Sensor EMG (Electromiograma)

### Principio de funcionamiento
Registra la actividad eléctrica muscular mediante electrodos en la piel.

### Señal
- Rango: 20–500 Hz.  
- Amplitud en mV.  
- Afectado por ruido y movimiento.

### Integración embebida
- Amplificador diferencial + filtros.  
- ADC de 12–16 bits.  
- Módulos listos como MyoWare.

### Procesamiento
- Filtrado y rectificación.  
- Cálculo de RMS, MAV, ZC, SSC.  
- Reconocimiento de gestos.

### Aplicaciones
- Control de prótesis mioeléctricas.  
- Biofeedback y rehabilitación.  
- Wearables para deportes y fatiga muscular.

---

## 6. Consideraciones generales

- **Hardware común:** MCU ARM Cortex-M, ESP32, nRF52, Raspberry Pi.  
- **Software:** filtrado en tiempo real, CMSIS-DSP, ML ligero en el edge.  
- **Energía:** optimización de muestreo y modos sleep.  
- **Seguridad:** cifrado de plantillas biométricas y comunicación TLS/DTLS.

---

## 7. Desafíos principales

- Ruido y artefactos.  
- Consumo energético en dispositivos portátiles.  
- Miniaturización y confort de uso.  
- Seguridad y privacidad de datos biométricos.  
- Certificaciones clínicas en aplicaciones médicas.

---

## 8. Conclusión

Los sensores biométricos como PPG/ECG, huella dactilar, EEG y EMG son fundamentales en la integración de sistemas embebidos modernos. Permiten desarrollar aplicaciones médicas, de seguridad y de interacción avanzada, siempre considerando el reto del procesamiento en tiempo real, la eficiencia energética y la protección de datos sensibles.


---

## 9. Referencias

1. Ja-Bots.com. (n.d.). Sensores Biométricos – Precisión en Salud y Seguridad. Todo Lo Que Necesites En Robótica De Competencia. https://ja-bots.com/categoria-producto/sensores/biometricos/?srsltid=AfmBOoqRKYWrKiiz8tTMmTqBwsGTg2UGeUGsgDX0LzS7Zj7nRPv9X8WS
2. Sensores biomédicos: tipos de sensores y cómo funcionan – Hacedores.com | Maker Community. (n.d.). https://hacedores.com/sensores-biomedicos/
3. Pereira, T. M. C., Conceição, R. C., Sencadas, V., & Sebastião, R. (2023). Biometric Recognition: A Systematic Review on Electrocardiogram Data Acquisition Methods. Sensors (Basel, Switzerland), 23(3), 1507. https://doi.org/10.3390/s23031507
   
