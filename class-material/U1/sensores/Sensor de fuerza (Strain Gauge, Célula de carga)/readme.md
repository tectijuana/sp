# Sensor de fuerza (Strain Gauge, Célula de carga)
## By Ochoa Moran victor Alejandro


## 🔵 ¿Qué hacen las celdas de carga?
Las **celdas de carga** son sensores que miden **fuerza** o **peso** mediante la deformación de un material elástico. Se utilizan en:
- Básculas electrónicas
- Pruebas de materiales
- Automatización industrial
- Control de fuerza en robots

---

## 🛠 ¿Cómo funcionan?
1. **Principio de Deformación**  
   - Una fuerza aplicada deforma ligeramente la celda.  
   - Un **Strain Gauge** adherido cambia su **resistencia eléctrica** según la deformación.

2. **Puente de Wheatstone**  
   - Se usa para medir con precisión los pequeños cambios de resistencia y convertirlos en un voltaje de salida.

3. **Conversión a Datos Útiles**  
   - El voltaje es amplificado y enviado a un **microcontrolador** o **sistema de adquisición de datos** para mostrar el peso/fuerza.

---

## ⚠ Limitaciones
- **Sensibilidad a la temperatura** → Puede afectar la precisión.  
- **Rango de medición** → Cada celda tiene un límite máximo de carga.  
- **Ruido eléctrico** → Necesita **amplificación y filtrado**.  
- **Fatiga mecánica** → Uso excesivo reduce la precisión con el tiempo.  

---

## 💡 Ejemplo de uso con Arduino y HX711

### 🔹 **Materiales**  
- Arduino  
- Celda de carga (ejemplo: 5 kg)  
- Módulo amplificador **HX711**  

### 🔹 **Código en Arduino**
```cpp
#include "HX711.h"

#define DT 3    // Pin de datos del HX711
#define SCK 2   // Pin de reloj del HX711

HX711 scale;

void setup() {
    Serial.begin(9600);
    scale.begin(DT, SCK);
    scale.set_scale(2280.0);  // Ajusta el factor de calibración
    scale.tare();  // Elimina el peso inicial
}

void loop() {
    Serial.print("Peso: ");
    Serial.print(scale.get_units(), 2);
    Serial.println(" kg");
    delay(500);
}
```
# ⚡ **Aplicaciones de las Celdas de Carga (Strain Gauge)**
Las celdas de carga permiten medir peso, fuerza y presión en una gran variedad de industrias.  

---

## 🎯 **Aplicaciones Comunes (Uso Frecuente)**
💡 Estas aplicaciones son ampliamente utilizadas en la industria, laboratorios y el día a día.

### ⚖️ **1. Básculas Electrónicas y Pesaje Industrial**
📌 Usadas en supermercados, almacenes y fábricas.  
📌 Incluyen básculas de precisión, balanzas comerciales y tolvas de pesaje.

### 🏗 **2. Control de Carga en Grúas y Elevadores**
📌 Monitorean el peso de cargas en grúas para evitar sobrecarga.  
📌 Sistemas de seguridad en montacargas y ascensores industriales.

### 🏭 **3. Pruebas de Materiales y Ensayos de Resistencia**
📌 Se usan en laboratorios de ingeniería para medir la resistencia de metales, plásticos y compuestos.  
📌 Aplicadas en la **industria aeroespacial** y de **construcción**.

### 🚛 **4. Pesaje de Vehículos (Básculas Camioneras)**
📌 Miden el peso de camiones para evitar sobrecarga en carreteras.  
📌 Utilizadas en **aduanas y peajes** para regulación de carga.

### 🤖 **5. Control de Fuerza en Robots y Exoesqueletos**
📌 Se integran en **manipuladores robóticos** para medir presión al sujetar objetos.  
📌 En **exoesqueletos**, permiten medir la fuerza ejercida por los músculos.

---

## 🚀 **Aplicaciones Poco Comunes (Innovadoras o Especializadas)**
💡 Estas aplicaciones son menos convencionales, pero muestran el potencial de las celdas de carga.

### 🏎 **1. Sensores de Carga en Autos de Carreras (F1 y Rally)**
📌 Se usan en **suspensiones y neumáticos** para analizar fuerzas en curvas a alta velocidad.  
📌 En **simuladores de carreras**, replican fuerzas realistas en volantes y pedales.

### 🎸 **2. Instrumentos Musicales (Violines y Guitarras)**
📌 Analizan la tensión de las cuerdas en instrumentos de cuerda.  
📌 Usados en **luthiers** para mejorar la acústica y diseño de instrumentos.

### 🔥 **3. Monitoreo de Presión en Reactores Nucleares**
📌 Se usan para **detectar microdeformaciones** en estructuras de reactores.  
📌 Permiten predecir posibles fallas en tuberías y contenedores de presión.

### 🏥 **4. Prótesis Biomédicas y Monitoreo de Pacientes**
📌 En **prótesis avanzadas**, permiten medir la fuerza ejercida al caminar o sujetar objetos.  
📌 En **hospitales**, ayudan en **rehabilitación de pacientes** midiendo fuerza muscular.

### 🛰 **5. Exploración Espacial y Marte Rovers**
📌 Se utilizan en **rovers de Marte** para medir la presión en ruedas y brazos mecánicos.  
📌 Monitorean la **resistencia estructural** de módulos en el espacio.

---


