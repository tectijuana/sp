# **Lección 6: Automatización de Procesos en EdgeX Foundry con Inteligencia Artificial y Machine Learning** 🤖🔥  

---

## **1. Objetivo de la Lección**  
Al finalizar esta lección, el estudiante comprenderá cómo integrar **EdgeX Foundry con modelos de Machine Learning (ML) e Inteligencia Artificial (IA)** para la **automatización de procesos en entornos IoT**. Se explorarán herramientas como **TensorFlow, OpenVINO y AutoML**, y se implementará un flujo de trabajo que **detecta anomalías y toma decisiones automáticas en EdgeX**.  

---

## **2. Introducción**  
### **2.1 ¿Por qué usar Machine Learning en Edge Computing?**  
Los modelos de ML permiten:  
✅ **Automatizar decisiones** sin intervención humana.  
✅ **Optimizar el rendimiento** de dispositivos industriales.  
✅ **Detectar anomalías en sensores en tiempo real**.  
✅ **Reducir costos** al procesar datos en el edge en lugar de la nube.  

### **2.2 Aplicaciones en la Industria**  
- **Mantenimiento predictivo** en maquinaria industrial.  
- **Optimización de energía** en edificios inteligentes.  
- **Detección de fraudes** en dispositivos financieros IoT.  
- **Visión artificial en manufactura** para control de calidad.  

---

## **3. Flujo de Trabajo de Machine Learning en EdgeX Foundry**  
1️⃣ **Captura de Datos**: Sensores envían datos a EdgeX (Ejemplo: temperatura, vibración, imágenes).  
2️⃣ **Preprocesamiento**: Filtrado y transformación de datos en los Application Services.  
3️⃣ **Inferencia de Machine Learning**: Uso de modelos de ML en dispositivos Edge o en la nube.  
4️⃣ **Automatización**: EdgeX toma decisiones basadas en las predicciones del modelo.  

---

## **4. Implementación de un Sistema de Detección de Anomalías con Machine Learning en EdgeX**  
### **4.1 Configuración del Entorno**  
Instalar dependencias necesarias en el servidor EdgeX:  
```bash
sudo apt update && sudo apt install -y python3-pip
pip3 install tensorflow numpy paho-mqtt
```

### **4.2 Entrenamiento de un Modelo de Detección de Anomalías**  
Usaremos **TensorFlow** para entrenar un modelo de detección de anomalías en temperatura.  

#### **Paso 1: Crear un script de entrenamiento** (`train_anomaly_model.py`)  
```python
import tensorflow as tf
import numpy as np
import joblib

# Generar datos de temperatura normales (20-30 grados)
normal_data = np.random.normal(loc=25, scale=2, size=(1000, 1))

# Generar datos de anomalía (fuera del rango normal)
anomaly_data = np.random.normal(loc=40, scale=5, size=(100, 1))

# Datos etiquetados (0 = normal, 1 = anomalía)
X_train = np.vstack([normal_data, anomaly_data])
y_train = np.array([0] * 1000 + [1] * 100)

# Crear modelo de detección de anomalías
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Salida 0 o 1
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, batch_size=16)

# Guardar modelo
joblib.dump(model, 'anomaly_detector.pkl')
print("Modelo guardado correctamente.")
```
Ejecutar el script:  
```bash
python3 train_anomaly_model.py
```

---

### **4.3 Integración del Modelo de ML en EdgeX**  
#### **Paso 1: Crear un Servicio de Aplicación que Detecte Anomalías**  
Este servicio leerá datos de temperatura desde EdgeX y aplicará el modelo de ML para detectar anomalías.  

```python
import joblib
import paho.mqtt.client as mqtt
import json

# Cargar el modelo entrenado
model = joblib.load("anomaly_detector.pkl")

# Configuración MQTT para recibir datos de EdgeX
MQTT_BROKER = "localhost"
MQTT_TOPIC = "edgex/temperature"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temperature = float(data["temperature"])
    
    # Predicción de anomalía (0 = normal, 1 = anomalía)
    prediction = model.predict([[temperature]])[0]
    
    if prediction >= 0.5:
        print(f"⚠️ Anomalía detectada: Temperatura {temperature}°C")
        # Publicar alerta en otro topic MQTT
        client.publish("edgex/alerts", json.dumps({"alert": "Anomalía en temperatura", "value": temperature}))

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message

print("Servicio de detección de anomalías ejecutándose...")
client.loop_forever()
```
Ejecutar el servicio:  
```bash
python3 detect_anomalies.py
```

---

## **5. Despliegue del Modelo en Edge con OpenVINO**  
Para ejecutar modelos de IA en **dispositivos con Intel** como cámaras o procesadores de borde, podemos usar **OpenVINO**.  

### **5.1 Instalar OpenVINO**  
```bash
sudo apt install -y intel-openvino-runtime
```
### **5.2 Convertir el Modelo TensorFlow a OpenVINO**  
```bash
mo --input_model anomaly_detector.pb --output_dir ./openvino_model
```
### **5.3 Inferencia con OpenVINO en EdgeX**  
```python
from openvino.runtime import Core
import numpy as np

# Cargar modelo
ie = Core()
model = ie.read_model(model="./openvino_model/anomaly_detector.xml")
compiled_model = ie.compile_model(model, "CPU")

def predict_temperature(temp):
    input_data = np.array([[temp]], dtype=np.float32)
    result = compiled_model(input_data)
    return result[0] >= 0.5

# Prueba de inferencia
temp_test = 45.0
print(f"Anomalía detectada: {predict_temperature(temp_test)}")
```

---

## **6. Automatización de Respuestas a Anomalías en EdgeX**  
Una vez que **EdgeX detecta una anomalía**, podemos automatizar respuestas como:  
✅ **Enviar alertas por MQTT o email**.  
✅ **Activar sistemas de seguridad** (Ejemplo: apagar una máquina si detecta sobrecalentamiento).  
✅ **Registrar eventos en bases de datos**.  

### **Ejemplo: Publicar Alertas Automáticas en EdgeX**  
```python
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def send_alert(temperature):
    alert_msg = {"alert": "Temperatura fuera de rango", "value": temperature}
    client.publish("edgex/alerts", json.dumps(alert_msg))
    print("⚠️ Alerta enviada a EdgeX")

send_alert(42.5)
```

---

## **7. Evaluación**  
### **7.1 Preguntas de Revisión**  
1. ¿Por qué es importante usar Machine Learning en Edge Computing?  
2. ¿Cómo se entrena un modelo de detección de anomalías en Python?  
3. ¿Qué ventajas tiene usar OpenVINO en dispositivos Edge?  

### **7.2 Práctica**  
1. Entrenar un modelo para detectar anomalías en datos de vibración de una máquina.  
2. Implementar un servicio en EdgeX que active una alarma cuando se detecte una anomalía.  
3. Optimizar el modelo con OpenVINO y probar la inferencia en un dispositivo Edge.  

---

## **8. Conclusión**  
Integrar **Machine Learning en EdgeX Foundry** permite que los sistemas IoT sean más **inteligentes y autónomos**. Con herramientas como **TensorFlow, OpenVINO y MQTT**, es posible detectar anomalías en tiempo real y tomar decisiones automáticas sin depender de la nube.  

---

### **Próxima Lección**  
**"Implementación de EdgeX Foundry en Ambientes Industriales (Industria 4.0)"** 🏭🚀
