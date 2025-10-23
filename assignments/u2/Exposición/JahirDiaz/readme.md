## 🧍‍♀️ Introducción
La **escoliosis** es una desviación anormal de la columna vertebral que puede desarrollarse progresivamente si no se detecta y corrige a tiempo.  
En nuestra vida cotidiana, especialmente con el uso prolongado de dispositivos electrónicos y el trabajo frente a pantallas, es común adoptar **posturas inadecuadas durante largos períodos**.  
Estas malas posturas, sostenidas en el tiempo, pueden generar **dolor lumbar, tensiones musculares** e incluso favorecer el desarrollo de **curvaturas en la columna**.

Actualmente, la detección temprana depende de revisiones médicas o escolares, que suelen ser esporádicas.  
Por eso, surge la necesidad de un sistema que **monitoree la postura de manera continua y automática**, brindando alertas tempranas y datos objetivos para prevenir la aparición o progresión de la escoliosis.

---
## 🚀 Objetivo demostrativo
Este proyecto busca demostrar cómo se pueden integrar **tecnologías de monitoreo industrial (Prometheus + Grafana)** en un **entorno de salud y bienestar**, ofreciendo una visualización clara y cuantificable de los hábitos posturales.

## 💡 Objetivo del proyecto
Diseñar e implementar un **sistema de medición de postura corporal** en tiempo real que permita:
- **Detectar malas posturas** mediante sensores electrónicos o cámaras.  
- **Registrar métricas** sobre la inclinación y el alineamiento corporal.  
- **Alertar al usuario** ante posturas inadecuadas sostenidas.  
- **Visualizar y analizar datos históricos** para seguimiento médico o personal.

El enfoque está orientado a la **prevención**, ofreciendo una herramienta tecnológica accesible y no invasiva para mejorar la salud postural en estudiantes, trabajadores de oficina y deportistas.

---

## ⚙️ Descripción general del sistema
El proyecto combina **hardware de sensorización** (IMU o cámaras) con un **pipeline de software basado en tecnologías IoT y observabilidad**, siguiendo esta arquitectura:

## 🧰 Tecnologías utilizadas
- **MQTT (Mosquitto):** comunicación ligera entre sensores y el servidor.  
- **Prometheus:** recolección y almacenamiento de métricas temporales.  
- **Grafana:** visualización, dashboards y alertas.  
- **Python:** lógica de procesamiento y exportación de métricas.  
- **Docker Compose:** orquestación local de todos los servicios.

# Pantalla: Postura Actual – Monitoreo en tiempo real

## Descripción general
La interfaz representa la vista principal del sistema de **monitoreo de postura**, mostrando en tiempo real los valores de **inclinación frontal (Pitch)** y **lateral (Roll)** del usuario. 
<img width="1504" height="558" alt="pantalla1" src="https://github.com/user-attachments/assets/4be4aef6-ff2a-412b-bb00-f9d5227b0d75" />

# Pantalla: Resumen Diario
La pantalla **“Resumen Diario”** presenta una síntesis visual y cuantitativa de la actividad postural del usuario durante el día.  
Está diseñada con un estilo **oscuro, limpio y de alta legibilidad**, destacando los indicadores clave de desempeño y las franjas horarias con mejor o peor comportamiento postural.
<img width="1521" height="741" alt="panrtlla2" src="https://github.com/user-attachments/assets/f3296f35-b812-44e4-91b3-95c0f5f43db4" />

# Pantalla: Dashboard Clínico
La vista **Dashboard Clínico** está diseñada para ofrecer una **perspectiva técnica y cuantitativa** del comportamiento postural.  
<img width="1509" height="513" alt="image" src="https://github.com/user-attachments/assets/dab311cc-600a-4fb0-a2e0-af5d792361dd" />
<img width="1496" height="794" alt="image" src="https://github.com/user-attachments/assets/c4c540f1-a145-4a58-943f-c3e32abeee52" />

# Pantalla: Configuración
La vista **Configuración** permite ajustar los parámetros operativos del sistema de medición postural.  
Está pensada tanto para el **usuario final** (que puede personalizar la sensibilidad o las alertas) como para un **terapeuta o especialista**, que podría calibrar el sistema según las características de cada persona.
<img width="717" height="750" alt="image" src="https://github.com/user-attachments/assets/5883b308-81a6-49dd-9445-56bd7574fc60" />
<img width="719" height="454" alt="image" src="https://github.com/user-attachments/assets/250af15e-1282-48d3-8280-d84bbb831f9b" />





