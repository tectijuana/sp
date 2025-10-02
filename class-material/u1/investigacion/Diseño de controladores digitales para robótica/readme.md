# Diseño de Controladores Digitales para Robótica

**Autor:** Belen Perez Villa  
**Número de control:** 21212579  
**Fecha:** 17/09/2025

---

## 📌 Introducción

El diseño de **controladores digitales en robótica** combina teoría de control, modelado del sistema y consideraciones prácticas (muestreo, cuantización, tiempo real). Esta área es la base para lograr estabilidad, precisión y robustez en robots móviles, manipuladores y vehículos autónomos (Åström & Murray, 2008).  

<img width="640" height="405" alt="image" src="https://github.com/user-attachments/assets/8f76e8ee-886f-4fe0-bccf-8cf298d80125" />

*Figura 1: Ejemplo de control de un brazo robotico.*

---

## ⚙️ Principios del Diseño de Controladores Digitales

1. **Modelado del sistema** — representación matemática (ecuaciones dinámicas o espacio de estados) para diseñar controladores (Åström & Murray, 2008).  
2. **Digitalización / muestreo** — elección del periodo de muestreo y discretización de controladores continuos (por ejemplo, transformada bilineal/Tustin).  
3. **Algoritmos de control** — desde PID discretos hasta LQR/MPC y filtros de estimación (Kalman), según requisitos de desempeño y recursos.  
4. **Implementación en hardware** — MCU/SoC con/ sin FPU, prioridades en RTOS/ISR y gestión de actuadores/sensores.

<img width="1330" height="447" alt="image" src="https://github.com/user-attachments/assets/3b86500d-e9e4-47e4-8e7d-20ff5b774b7f" />

*Figura 2: Diagrama de bucle de control digital (PID).*

---

## 🧰 Tipos de Controladores y cuándo usarlos

- **PID digital**: simple, eficiente y ampliamente usado; aplicar anti-windup y filtrado derivativo cuando hay ruido o saturación (Åström & Hägglund, 1995).  
- **Control en espacio de estados (LQR, state-feedback)**: para sistemas multivariables con modelo matemático.  
- **Observadores / Filtros de Kalman**: estimación óptima de estados ruidosos o no medidos (Welch & Bishop, 2001).  
- **MPC (Model Predictive Control)**: ideal cuando hay restricciones en entradas/estados y se necesita optimización recursiva (Rawlings, Mayne & Diehl, 2017).

---

## 🛠️ Buenas prácticas y consideraciones prácticas

- **Sintonía**: Ziegler–Nichols o simulación/HIL; preferir sintonía automática si se dispone de herramientas.  
- **Anti-windup y saturación**: imprescindible en PID con límites de actuador.  
- **Discretización**: Tustin (bilinear) para preservar respuesta en frecuencia.  
- **Estimación**: usar Kalman cuando las medidas son ruidosas y se dispone de modelo/ruido estadístico.  
- **Jerarquía de control**: planificador alto (MPC/LQR) + bucles bajos (PID/LQR).

![Jerarquía de control](https://upload.wikimedia.org/wikipedia/commons/7/73/MPC_hierarchical_control.png)
*Figura 3: Jerarquía típica de control en robots (MPC + PID/LQR).*

---

## 📊 Tabla comparativa (resumen)

| Técnica | Costo computacional | Determinismo | Manejo restricciones |
|---|---:|---:|---|
| PID digital | Muy bajo | Alto | No nativo |
| LQR / state-feedback | Medio | Medio | Limitado sin extensión |
| MPC | Alto | Variable | Excelente (trata restricciones) |
| Kalman / Observador | Medio | Alto (si RT) | N/A (estimación) |

---

## ✅ Checklist rápido para diseñar un controlador robótico

1. Definir objetivo (posición, velocidad, fuerza).  
2. Modelar o identificar la planta.  
3. Elegir estructura controladora (PID / LQR / MPC / híbrido).  
4. Seleccionar periodo de muestreo y discretización (Tustin si aplica).  
5. Añadir anti-windup, filtros y lógica de saturación.  
6. Simular con ruido y saturaciones; HIL si es posible.  
7. Implementar en hardware con vigilancia (watchdog, E-stop, límites).

---

## 🧾 Referencias (formato APA)

- Åström, K. J., & Murray, R. M. (2008). *Feedback systems: An introduction for scientists and engineers*. Princeton University Press. [PDF](https://www.cds.caltech.edu/~murray/books/AM08/pdf/am08-complete_22Feb09.pdf)  
- Rawlings, J. B., Mayne, D. Q., & Diehl, M. (2017). *Model predictive control: Theory, computation and design* (2nd ed.). Nob Hill Publishing. [PDF](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)  
- Welch, G., & Bishop, G. (2001). *An introduction to the Kalman filter* (University of North Carolina at Chapel Hill, TR 95-041). [PDF](https://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf)  
- Åström, K. J., & Hägglund, T. (1995). *PID controllers: Theory, design, and tuning* (2nd ed.). [PDF](https://aiecp.files.wordpress.com/2012/07/1-0-1-k-j-astrom-pid-controllers-theory-design-and-tuning-2ed.pdf)  
- The MathWorks, Inc. (s. f.). *Continuous-Discrete conversion methods* (Tustin / bilinear). [MathWorks](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)  

---
