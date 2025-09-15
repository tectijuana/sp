# Nombre : [Gutierrez Cepeda Andres]
# Usuario: [pitonC]

# Sensores de Gas: MQ-2, MQ-7 y Sensores Electroquímicos

## Introducción
Los sensores de gas son dispositivos utilizados para detectar la presencia de gases en el ambiente. Dependiendo de su tecnología, pueden ser utilizados en aplicaciones industriales, seguridad, monitoreo ambiental, entre otros. En este documento, exploraremos el funcionamiento, aplicaciones, ventajas y desventajas de los sensores MQ-2, MQ-7 y los sensores electroquímicos.

---

## 1. Sensor MQ-2
### **Funcionamiento**
El sensor MQ-2 es un sensor de gas basado en un material semiconductor de óxido de estaño (SnO2), cuya resistencia varía en presencia de gases inflamables como GLP, butano, propano, metano, alcohol, hidrógeno y humo.

![Sensor MQ-2](https://uelectronics.com/wp-content/uploads/AR0096-Sensor-de-Gas-v5.jpg)

### **Aplicaciones**
- Detección de fugas de gas en sistemas de seguridad domésticos.
- Monitoreo de calidad del aire en interiores.
- Detección de humo en alarmas contra incendios.

### **Ventajas y Desventajas**
| Ventajas | Desventajas |
|----------|-------------|
| Sensible a múltiples gases inflamables. | Afectado por la humedad y la temperatura. |
| Bajo costo y fácil integración con microcontroladores. | Requiere calibración para obtener mediciones precisas. |
| Respuesta rápida a cambios en la concentración de gas. | Consumo de energía relativamente alto. |

### **Ejemplo Práctico**
```c
int sensorPin = A0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  int valor = analogRead(sensorPin);
  Serial.println(valor);
  delay(1000);
}
```

---

## 2. Sensor MQ-7
### **Funcionamiento**
El sensor MQ-7 está diseñado para detectar monóxido de carbono (CO). Funciona calentando un elemento sensor de SnO2 en ciclos de calentamiento y enfriamiento para medir la concentración de CO de manera precisa.

![Sensor MQ-7](https://uelectronics.com/wp-content/uploads/2018/01/Detector-de-Monoxido-de-Carbono-Modulo-MQ-7-V4-800x800.jpg)

### **Aplicaciones**
- Detección de CO en automóviles.
- Sistemas de ventilación y calefacción.
- Seguridad en minas y espacios cerrados.

### **Ventajas y Desventajas**
| Ventajas | Desventajas |
|----------|-------------|
| Alta sensibilidad al CO. | Requiere tiempo de precalentamiento. |
| Fácil implementación con microcontroladores. | Puede dar lecturas inexactas sin una calibración adecuada. |
| Costo accesible. | Sensible a interferencias ambientales. |

### **Ejemplo Práctico**
```c
int sensorPin = A0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  int valor = analogRead(sensorPin);
  Serial.println(valor);
  delay(1000);
}
```

---

## 3. Sensor Electroquímico
### **Funcionamiento**
Los sensores electroquímicos utilizan una reacción química para generar una corriente eléctrica proporcional a la concentración del gas detectado. Se componen de un electrodo de trabajo, un electrodo de referencia y un electrolito.

### **Aplicaciones**
- Monitoreo de gases tóxicos como CO, NO2, SO2 en industrias.
- Sensores portátiles de detección de gases.
- Seguridad en plantas de producción química.

### **Ventajas y Desventajas**
| Ventajas | Desventajas |
|----------|-------------|
| Alta precisión en la detección de gases específicos. | Vida útil limitada (~2-3 años). |
| Bajo consumo de energía. | Sensible a condiciones ambientales extremas. |
| Respuesta estable en un amplio rango de concentraciones. | Mayor costo en comparación con sensores de óxido metálico. |

### **Ejemplo Práctico**
```c
#include <Wire.h>
void setup() {
  Serial.begin(9600);
}
void loop() {
  Serial.println("Leyendo sensor electroquímico...");
  delay(2000);
}
```

---

## Conclusión
Cada tipo de sensor de gas tiene ventajas y desventajas dependiendo de la aplicación. Mientras que los sensores MQ son accesibles y versátiles, los sensores electroquímicos ofrecen una mayor precisión. La elección del sensor adecuado depende del tipo de gas a detectar, el entorno de uso y los requisitos de precisión.

---

## Referencias
- **Datasheets oficiales**: [MQ-2](https://www.sparkfun.com/datasheets/Sensors/Biometric/MQ-2.pdf), [MQ-7](https://www.sparkfun.com/datasheets/Sensors/Biometric/MQ-7.pdf)
- **Guías técnicas**: "Introduction to Electrochemical Gas Sensors", Spec Sensors, 2021.
- **Ejemplos de implementación**: Arduino Documentation & GitHub Projects.
