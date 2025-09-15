# Sensor de Voltaje: Divisor Resistivo y Transformador de Voltaje

---

## **Funcionamiento**

Un **sensor de voltaje** puede implementarse mediante dos métodos principales: el **divisor resistivo** y el **transformador de voltaje**.

### **Divisor Resistivo**
Consiste en dos resistencias conectadas en serie. El voltaje de salida (\(V_{out}\)) es una fracción del voltaje de entrada (\(V_{in}\)), determinado por la relación entre las resistencias \(R_1\) y \(R_2\):

\[
V_{out} = V_{in} \times \frac{R_2}{R_1 + R_2}
\]

Este método es ideal para circuitos de corriente continua (DC) y aplicaciones de bajo costo.


![Divisor-de-voltaje---1 0](https://github.com/user-attachments/assets/ac7a3743-51c2-479d-b345-9d5e807c1f4a)



### **Transformador de Voltaje**
Utiliza dos bobinas (primaria y secundaria) acopladas magnéticamente para modificar el voltaje en circuitos de corriente alterna (AC). La relación entre el voltaje de entrada (\(V_p\)) y salida (\(V_s\)) depende del número de vueltas en las bobinas (\(N_p\) y \(N_s\)):

\[
\frac{V_p}{V_s} = \frac{N_p}{N_s}
\]

Este método es común en sistemas de distribución eléctrica y aplicaciones de alta potencia.

![Transformer filament agr](https://github.com/user-attachments/assets/b005b1a8-07f0-4d05-ad5b-df0a2ca9f8e2)


---

## **Aplicaciones**

### **Divisor Resistivo**
- Medición de voltaje en baterías y sensores.
- Acondicionamiento de señales para microcontroladores o ADCs.
- Regulación de voltaje en circuitos electrónicos.

### **Transformador de Voltaje**
- Reducción o elevación de voltaje en redes eléctricas.
- Aislamiento eléctrico en fuentes de alimentación.
- Convertidores de potencia en electrónica industrial.

---

## **Ventajas y Desventajas**

| **Método**            | **Ventajas**                                                                 | **Desventajas**                                                                 |
|-----------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Divisor Resistivo** | - Simple y económico. <br> - Precisión con resistencias de alta calidad.    | - Pérdida de energía en forma de calor. <br> - No apto para alta corriente.     |
| **Transformador**     | - Eficiente en transferencia de energía. <br> - Aislamiento eléctrico.      | - Voluminoso y pesado. <br> - Solo funciona con AC. <br> - Costo elevado.       |

---

## **Ejemplos Prácticos**

### **Divisor Resistivo**
- En un sistema de monitoreo de baterías, se usa para reducir el voltaje de una batería de 12V a 5V, compatible con un microcontrolador.
- En sensores de nivel de líquidos, convierte la resistencia variable en un voltaje medible.

### **Transformador de Voltaje**
- En una subestación eléctrica, reduce el voltaje de 110 kV a 220 V para distribución residencial.
- En una fuente de alimentación de computadora, transforma 120 V AC a 12 V AC para su posterior rectificación.

---

- **Referencias:**
  - [Divisor de Voltaje - Wikipedia](https://es.wikipedia.org/wiki/Divisor_de_tensi%C3%B3n)
  - [Transformador de Voltaje - Wikipedia](https://es.wikipedia.org/wiki/Transformador)

---
