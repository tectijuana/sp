


<img width="1200" height="627" alt="image" src="https://github.com/user-attachments/assets/ad5a4388-dd3b-44e6-b875-967efb776624" />



# ¿Qué es MQTT en salud?
MQTT (Message Queuing Telemetry Transport) es un protocolo ligero de mensajería ideal para IoT y telemedicina.

Funciona bajo un esquema publicador/suscriptor, donde:

Sensores biomédicos → publican datos (ej. frecuencia cardíaca, glucosa).

Broker MQTT → gestiona mensajes.

Aplicaciones médicas → se suscriben para recibir la información en tiempo real.

# Tipos de sensores biomédicos usados

Electrocardiograma (ECG) → monitoreo cardíaco remoto.

Oxímetro de pulso (SpO₂) → saturación de oxígeno en pacientes con EPOC, COVID-19, apnea.

Sensor de glucosa → monitoreo continuo en pacientes diabéticos.

Sensor de presión arterial → control en hipertensión.

Sensores de temperatura → monitoreo de fiebre y estados infecciosos.

Acelerómetros y giroscopios → detección de caídas en adultos mayores.

# Aplicaciones médicas con MQTT

elemedicina y monitoreo remoto

Pacientes con enfermedades crónicas (diabetes, hipertensión) pueden enviar sus datos biomédicos desde casa.

Los médicos reciben la información en dashboards en tiempo real.

b) Hospitales inteligentes

Sensores de signos vitales conectados a un sistema central vía MQTT.

Alertas inmediatas cuando un paciente tiene valores críticos.

c) Ambulancias conectadas

ECG, presión arterial y oxigenación transmitidos al hospital mientras llega el paciente.

Facilita la atención anticipada.

d) Wearables de salud

Relojes inteligentes con sensores biomédicos publican datos en un broker MQTT.

Apps móviles o plataformas en la nube muestran gráficos y alertas.

e) Ensayos clínicos e investigación

Recolección masiva de datos fisiológicos de voluntarios usando MQTT para sincronizar múltiples sensores.



# Ventajas de usar MQTT en aplicaciones médicas 

✅ Bajo consumo de energía → ideal para dispositivos portátiles y wearables.

✅ Bajo ancho de banda → funciona incluso con internet inestable.

✅ Mensajería en tiempo real → fundamental para emergencias.

✅ Escalabilidad → múltiples pacientes y sensores conectados.

✅ QoS (Quality of Service) → garantiza que los datos críticos lleguen sin pérdida.

# Ejemplo práctico
Un paciente con insuficiencia cardíaca usa un dispositivo portátil con ECG y oxímetro:

El sensor publica cada 5 segundos → topic: paciente123/ECG y paciente123/SpO2.

El broker MQTT (ej. Mosquitto, HiveMQ) recibe y distribuye.

Una app móvil del médico está suscrita a esos tópicos.

Si el ECG detecta arritmia → se genera alerta inmediata en la app.
