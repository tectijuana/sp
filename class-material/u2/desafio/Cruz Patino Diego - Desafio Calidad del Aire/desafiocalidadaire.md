# Estación de Monitoreo de Calidad del Aire en Zonas Escolares

Este proyecto tiene como objetivo implementar una solución de monitoreo de calidad del aire para detectar y mitigar el impacto de la contaminación en la salud. Se han seleccionado sensores para medir los niveles de dióxido de nitrógeno (NO₂), monóxido de carbono (CO), material particulado (PM2.5), temperatura y humedad. Los datos se almacenarán localmente y se enviarán a la nube para su análisis y visualización.

## Objetivos del Proyecto

1. Medir la calidad del aire en zonas cercanas a las escuelas.
2. Detectar posibles picos de contaminación que puedan afectar la salud de los niños.
3. Visualizar los datos en tiempo real mediante **Grafana** y **InfluxDB**.
4. Generar alertas automáticas cuando los niveles de contaminación superen umbrales predefinidos.
5. Implementar una solución de bajo mantenimiento, que funcione con energía solar o de farola.

## Sensores Utilizados

### 1. **Dióxido de Nitrógeno (NO₂)**
   - **Sensor:** MiCS-5524 o CCS811
   - **Justificación:** Sensores de gases que permiten medir NO₂ con buena precisión para aplicaciones urbanas.

### 2. **Monóxido de Carbono (CO)**
   - **Sensor:** MQ-7 o MiCS-5524
   - **Justificación:** El MQ-7 es ampliamente utilizado para la medición de CO en entornos urbanos.

### 3. **Material Particulado (PM2.5)**
   - **Sensor:** Plantower PMS5003 o Nova Fitness SDS011
   - **Justificación:** Sensores precisos para medir PM2.5 y PM10 en ambientes urbanos.

### 4. **Temperatura y Humedad**
   - **Sensor:** BME280 o DHT22
   - **Justificación:** El BME280 ofrece una mayor precisión y fiabilidad, permitiendo correlacionar los contaminantes con las condiciones climáticas.

## Microcontrolador Seleccionado

### **ESP32**
   - **Razón de elección:**
     - Conectividad **WiFi** integrada.
     - **Bajo consumo de energía** en modo de reposo, ideal para alimentación solar o de farola.
     - Capacidad de procesamiento suficiente para filtrar picos falsos y valores faltantes.
     - **Compatibilidad con LoRaWAN**, lo que lo hace flexible para diferentes métodos de comunicación.

## Arquitectura de Comunicación

La arquitectura de comunicación depende de la disponibilidad de red en la zona:

### 1. **WiFi (preferible en las cercanías de las escuelas)**
   - El **ESP32** se conectará a la red WiFi de la escuela.
   - Los datos se enviarán a la nube cada hora utilizando el protocolo **MQTT**, ideal para integrarse con plataformas como **Grafana** y **InfluxDB**.

### 2. **LoRaWAN (cuando no hay WiFi disponible o la cobertura es insuficiente)**
   - El **ESP32** se conectará a un módulo **LoRa** (como el **SX1278** o **RFM95**) para transmitir los datos a una gateway LoRaWAN.
   - Se utilizará **MQTT** para enviar los datos a la nube, o bien el protocolo específico de LoRaWAN para integrarse a la infraestructura del municipio.

## Procesamiento de Datos

### Filtrado de Anomalías:
- **Filtrado de picos:** Se aplicarán filtros de mediana o filtros de Kalman para eliminar picos atípicos en los datos de los sensores.
- **Validación de datos:** Verificación de que las lecturas estén dentro de rangos válidos esperados. Por ejemplo, si se detecta una humedad de 0% o un valor negativo para PM2.5, se considera como datos erróneos.
- **Promedio de lecturas:** Se puede almacenar la medición de los sensores durante un período (5 minutos) y enviar el promedio cada hora.

## Visualización y Generación de Alertas

### 1. **Almacenamiento de Datos:**
   - **InfluxDB** se utilizará para almacenar los datos de calidad del aire en series temporales.
   - Los datos se almacenarán en intervalos regulares (por ejemplo, cada hora) para su posterior análisis.

### 2. **Visualización de Datos:**
   - **Grafana** se conectará a **InfluxDB** para mostrar los datos de calidad del aire en tiempo real.
   - Se crearán paneles interactivos para visualizar la evolución de contaminantes como NO₂, CO, PM2.5, temperatura y humedad a lo largo del tiempo.

### 3. **Alertas:**
   - Se configurarán **alertas en Grafana** cuando los niveles de contaminantes superen umbrales predefinidos (por ejemplo, PM2.5 > 35 µg/m³ o NO₂ > 100 ppb).
   - Las alertas se enviarán por correo electrónico o a plataformas como **Telegram**.

## Diseño de la Caja y Alimentación

### 1. **Caja Resistente IP65:**
   - La estación de monitoreo estará protegida en una **caja con clasificación IP65**, que asegura resistencia al agua, polvo y otras inclemencias climáticas.

### 2. **Alimentación Solar o de Farola:**
   - El sistema utilizará **paneles solares** para cargar una batería recargable, garantizando una fuente de energía autónoma y sostenible.
   - Si es posible, también se podrá utilizar **energía de los postes de luz cercanos** para alimentar la estación.

## Requisitos de Hardware

- **ESP32**: Microcontrolador con WiFi o LoRa.
- **Sensores**: MiCS-5524, MQ-7, PMS5003, BME280.
- **Módulos adicionales**:
  - **Módulo LoRa**: SX1278 o RFM95.
  - **Panel solar y batería recargable** para la alimentación autónoma.
  - **Caja IP65** para la protección de los sensores y componentes.

## Requisitos de Software

- **InfluxDB**: Base de datos para almacenar las series temporales de los datos de calidad del aire.
- **Grafana**: Herramienta para la visualización de datos y configuración de alertas.
- **MQTT**: Protocolo para la transmisión eficiente de datos entre la estación de monitoreo y la nube.
