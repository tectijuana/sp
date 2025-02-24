# Sensor de Temperatura (Termopares, RTD, NTC/PTC)

## Datos del Autor  
**Nombre:** [Arias Verdin Vivian]  
**Fecha:** [23/02/2024]  
**Institución:** [Instituto Tecnologico de Tijuana]  

---

## Introducción  
Los sensores de temperatura son dispositivos diseñados para medir la temperatura de un entorno o un objeto. Se utilizan en una variedad de aplicaciones industriales, científicas y domésticas. Entre los sensores más comunes se encuentran los **termopares, RTD (Resistencias Dependientes de Temperatura), y termistores NTC/PTC**. Cada uno de estos sensores tiene características específicas en términos de funcionamiento, precisión, respuesta y aplicaciones.  

---

## Tipos de Sensores de Temperatura  

### 1. **Termopares**  
Los **termopares** son sensores que generan un voltaje en respuesta a una diferencia de temperatura entre dos puntos. Se basan en el **efecto Seebeck**, que ocurre cuando dos metales distintos están unidos y expuestos a diferentes temperaturas.  

#### **Funcionamiento**  
- Consisten en dos metales distintos unidos en un extremo (unión caliente) y abiertos en el otro extremo (unión fría).  
- Al haber una diferencia de temperatura, se genera un voltaje proporcional a la temperatura medida.  
- Se requiere un circuito de compensación para corregir la lectura.  

#### **Aplicaciones**  
- Industria metalúrgica (hornos, fundiciones).  
- Procesos de manufactura de alta temperatura.  
- Motores de combustión interna.  

#### **Ventajas y Desventajas**  
| Ventajas  | Desventajas  |
|-----------|-------------|
| Amplio rango de temperatura (-200°C a 1750°C)  | Baja precisión en comparación con otros sensores |
| Respuesta rápida | Necesidad de calibración frecuente |
| Resistente a entornos hostiles | Señal débil y susceptible a interferencias |

---

### 2. **RTD (Resistencias Dependientes de Temperatura)**  
Los **RTD** son sensores de temperatura basados en la variación de resistencia de un material (generalmente platino) con la temperatura. Son más precisos que los termopares pero menos resistentes a temperaturas extremas.  

#### **Funcionamiento**  
- A medida que la temperatura aumenta, la resistencia del RTD también aumenta.  
- Se usa una corriente constante para medir el cambio de voltaje, que se convierte en temperatura.  

#### **Aplicaciones**  
- Industria alimentaria y farmacéutica.  
- Laboratorios de calibración y control de calidad.  
- Sistemas HVAC.  

#### **Ventajas y Desventajas**  
| Ventajas  | Desventajas  |
|-----------|-------------|
| Alta precisión y estabilidad | Costo elevado en comparación con termopares |
| Rango de temperatura moderado (-200°C a 850°C) | Tiempo de respuesta más lento |
| Menor susceptibilidad al ruido eléctrico | Sensibles a golpes y vibraciones |

---

### 3. **Termistores NTC/PTC**  
Los **termistores** son resistencias cuya variación de resistencia con la temperatura es mucho mayor que en los RTD. Se dividen en:  
- **NTC (Coeficiente de Temperatura Negativo):** Su resistencia disminuye al aumentar la temperatura.  
- **PTC (Coeficiente de Temperatura Positivo):** Su resistencia aumenta al aumentar la temperatura.  

#### **Funcionamiento**  
- Fabricados con materiales semiconductores que cambian de resistencia en función de la temperatura.  
- La variación de resistencia se convierte en una señal de temperatura con un circuito adecuado.  

#### **Aplicaciones**  
- Electrónica de consumo (sensores de sobrecalentamiento en baterías y circuitos).  
- Control de temperatura en dispositivos médicos.  
- Termostatos digitales y protección de motores.  

#### **Ventajas y Desventajas**  
| Ventajas  | Desventajas  |
|-----------|-------------|
| Alta sensibilidad a pequeños cambios de temperatura | No funcionan bien en temperaturas extremas |
| Bajo costo y tamaño reducido | Respuesta no lineal, requiere calibración |
| Respuesta rápida | Menos duraderos en entornos agresivos |

---

## Ejemplos Prácticos  

### **Ejemplo 1: Monitoreo de Temperatura en un Motor con un Termopar**  
Un termopar tipo K se coloca en el bloque de un motor para monitorear su temperatura. Se usa un amplificador de señal y un microcontrolador para interpretar el voltaje generado y desplegar la temperatura en un panel digital.  

### **Ejemplo 2: Control de Temperatura en un Laboratorio con RTD**  
Un laboratorio de química usa RTDs de platino (PT100) para garantizar que las reacciones químicas se realicen en un rango de temperatura preciso. La señal del RTD se procesa en un controlador PID para mantener la temperatura estable.  

### **Ejemplo 3: Protección de Baterías con un Termistor NTC**  
Un termistor NTC se coloca dentro de una batería de litio para detectar sobrecalentamiento. Si la temperatura supera un umbral, el circuito de carga se desactiva para evitar daños o explosiones.  

---

## Imagen Representativa  
![Sensores-de-temperatura-Logicbus](https://github.com/user-attachments/assets/806eda44-a63e-4666-98cc-350a49beda10)


![Sensores de Temperatura](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Thermocouple.svg/800px-Thermocouple.svg.png)  
*(Fuente: Wikimedia Commons, Ejemplo de termopar, 2012)*  

---

## Referencias  
- Bentley, J. P. (2005). *Principles of Measurement Systems* (4th ed.). Pearson Education.  
- Omega Engineering. (2023). *Introduction to Temperature Sensors: Thermocouples, RTDs, and Thermistors*. Retrieved from [https://www.omega.com](https://www.omega.com)  
- Callendar, H. L. (1887). *On the Practical Measurement of Temperature*. *Proceedings of the Royal Society of London*.  
- Wikimedia Commons. (2012). *Thermocouple Example*. Retrieved from [https://commons.wikimedia.org/wiki/File:Thermocouple.svg](https://commons.wikimedia.org/wiki/File:Thermocouple.svg)  
```  
