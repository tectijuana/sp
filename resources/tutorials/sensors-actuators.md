

# 📘 Sensores y Actuadores en Sistemas Embebidos e Inteligencia Artificial

> 🧑‍🏫 **Objetivo de aprendizaje**: El estudiante identificará y aplicará sensores y actuadores adecuados en proyectos embebidos e inteligentes, comprendiendo su funcionamiento, clasificación, integración y control a través de microcontroladores.

---

## 1. 🧠 Fundamentos

### ¿Qué es un sensor?
Un **sensor** es un dispositivo que detecta una variable física o química del entorno (temperatura, luz, presión, humedad, etc.) y la convierte en una señal eléctrica interpretable por un sistema.

### ¿Qué es un actuador?
Un **actuador** transforma una señal de control en una **acción física**, como mover un motor, encender una luz o abrir una válvula.

---

## 2. 🔍 Clasificación de sensores

| Tipo           | Variable medida       | Ejemplo                          |
|----------------|------------------------|----------------------------------|
| Ambientales    | Temperatura, humedad   | DHT11, BME280                    |
| Mecánicos      | Movimiento, presión    | PIR, MPU6050 (IMU), FSR          |
| Ópticos        | Luz, color, distancia  | LDR, TCS34725, VL53L0X           |
| Acústicos      | Sonido, ultrasonido    | Micrófono, HC-SR04               |
| Químicos       | Gases, calidad del aire| MQ-135, CO2 NDIR                 |
| Biológicos     | Señales bioeléctricas  | ECG, PPG, EEG                    |

---

## 3. ⚙️ Clasificación de actuadores

| Tipo            | Acción                  | Ejemplo                          |
|------------------|--------------------------|----------------------------------|
| Electromecánicos | Movimiento/posición     | Servomotor, motor DC, relé       |
| Ópticos          | Iluminación             | LED, pantalla OLED               |
| Térmicos         | Calor                   | Calentadores, peltier            |
| Hidráulicos/neumáticos | Presión/flujo     | Válvulas controladas             |
| Acústicos        | Sonido                  | Zumbadores, parlantes            |

---

## 4. 🧪 Práctica: Integración de sensores y actuadores con microcontroladores

### Ejemplo 1: Sensor de temperatura con actuador
**Descripción**: Encender un ventilador si la temperatura supera 30 °C.

**Materiales**:  
- Sensor **DHT22**  
- Actuador: **Relé + Ventilador 5V**  
- **ESP32 / Raspberry Pi Pico W**

**Código base (MicroPython)**:
```python
import dht
from machine import Pin
import time

sensor = dht.DHT22(Pin(15))
rele = Pin(5, Pin.OUT)

while True:
    sensor.measure()
    temp = sensor.temperature()
    if temp > 30:
        rele.value(1)  # activa el ventilador
    else:
        rele.value(0)
    time.sleep(2)
```

---

## 5. 🌐 Sensores y actuadores en proyectos de Edge AI

### Caso: Clasificación de gestos con IMU + servomotor
- Sensor **MPU6050** detecta la inclinación del brazo.  
- Microcontrolador analiza patrones con modelo IA preentrenado.  
- Si se detecta gesto “saludo”, el servomotor mueve una bandera.

> 💡 Esto es posible gracias a librerías como **TensorFlow Lite for Microcontrollers** y plataformas como **Edge Impulse**.

---

## 6. ⚠️ Consideraciones técnicas

- **Interfaz de comunicación**:
  - Digital: GPIO, I2C, SPI, UART
  - Analógica: ADC (entrada analógica)
- **Voltaje compatible**: Evitar dañar sensores por incompatibilidad (3.3V vs 5V)
- **Calibración**: Sensores como gas o presión deben calibrarse
- **Control de potencia**: Los actuadores (motores, relés) pueden necesitar transistores o drivers

---

## 7. 📊 Actividad práctica sugerida (laboratorio o simulador)

> Diseña un sistema embebido que:
- Lea **temperatura y humedad** (DHT22)
- Detecte si el valor está fuera de rango ideal (IA o lógica)
- Active un **ventilador** o **alarma sonora** si es necesario
- Visualice los datos en pantalla OLED o envíe por MQTT

Opcional: **Simula en Wokwi** o implementa físicamente en ESP32/Raspberry Pi.

---

## 8. ✅ Evaluación rápida

> **1. ¿Qué diferencia hay entre un sensor analógico y uno digital?**  
> **2. ¿Cuál es el actuador más adecuado para controlar una válvula de riego?**  
> **3. Menciona dos sensores compatibles con I2C.**  
> **4. ¿Qué técnicas ayudan a ejecutar modelos IA en microcontroladores de bajos recursos?**

---

## 9. 📚 Recursos complementarios

- [Wokwi](https://wokwi.com) – Simulador de microcontroladores
- [Edge Impulse](https://www.edgeimpulse.com) – Entrenamiento de modelos TinyML
- [Datasheets de sensores](https://components101.com/) – Información técnica
- Libro: *Mastering Python for IoT Development*   
- Libro: *TinyML for Edge Intelligence in IoT* 

