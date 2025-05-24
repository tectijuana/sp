# Solución IoT para Monitoreo y Gestión de Consumo Energético en un Edificio Corporativo

Este proyecto está diseñado para reducir el consumo de energía y detectar anomalías en el uso de electricidad en un 
edificio corporativo de 5 pisos. La solución utiliza IoT local y Cloud para ofrecer monitoreo en tiempo real, alertas 
automáticas, reportes de eficiencia energética y control remoto de dispositivos.

## Arquitectura

La solución se divide en dos partes principales: **IoT Edge** y **Cloud**. El procesamiento inicial de los datos se realiza 
localmente en dispositivos IoT (Edge), mientras que el almacenamiento y visualización de los datos se maneja en el Cloud.

### IoT Edge (Local)
- **Sensores y Actuadores**: Los sensores y actuadores se conectan a microcontroladores (ESP32 o Raspberry Pi 4) que procesan los datos localmente y envían solo los datos filtrados al Cloud.
- **Protocolo de comunicación**: Los dispositivos de monitoreo (como medidores de corriente y Smart meters) se comunican mediante **Modbus TCP** o **UART**.
- **Almacenamiento local**: Los datos se almacenan temporalmente en la memoria local de los dispositivos antes de ser enviados al Cloud cada 15 minutos.

### Cloud
- **Plataforma en la nube**: Se utiliza un servidor Linux (Ubuntu) o EC2 para almacenar los datos históricos y generar reportes.
- **Visualización y análisis**: Se utilizará un stack open source para la visualización y análisis de los datos.

## Sensores y Protocolos

Para monitorear el consumo energético y controlar dispositivos, se utilizarán los siguientes sensores y protocolos:

- **Smart meters Modbus TCP**: Para obtener información de consumo energético de HVAC e iluminación.
- **Medidores de corriente tipo Clamp Sensor (SCT-013)**: Para medir el consumo de energía en circuitos específicos.
- **Relés de corte remoto**: Para controlar remotamente dispositivos no críticos en horarios no laborables.
- **Microcontroladores ESP32 y Raspberry Pi 4**: Para procesar los datos y gestionar la comunicación entre los sensores, actuadores y el Cloud.

## Lógica Local

La lógica de procesamiento local se implementará en los microcontroladores ESP32 y Raspberry Pi 4 para filtrar datos, 
detectar anomalías y realizar cálculos de consumo energético.

### Cálculo de Consumo Horario/Día
- Los sensores registran el consumo energético en tiempo real.
- La lógica local calcula el consumo acumulado por hora y por día.
- El cálculo se realiza utilizando las lecturas de consumo de los medidores Modbus TCP y los medidores de corriente tipo clamp.
- Los datos calculados (consumo horario y diario) se almacenan localmente y se envían al Cloud cada 15 minutos.

### Detección de Anomalías
- **Sobrecargas**: Si el consumo de energía excede un umbral predefinido, se activa una alerta.
- **Picos de Consumo en HVAC**: Si el consumo de los sistemas HVAC supera el valor promedio por más de un período específico, se genera una alerta.
- **Equipos Encendidos Fuera de Horario**: Si se detecta consumo en un dispositivo no crítico fuera del horario laboral, se genera una alerta y se envía al servidor para su análisis.

### Control Remoto de Dispositivos
- Los dispositivos no críticos se pueden apagar remotamente utilizando los relés de corte remoto.
- El microcontrolador ESP32 o Raspberry Pi 4 gestiona la conexión con el relé y apaga los dispositivos fuera de horarios laborables.

## Stack Tecnológico

### Software Local
- **Node-RED**: Para integrar y gestionar los sensores y actuadores de forma sencilla. Facilita la implementación de lógica de control y procesamiento de datos.
- **Mosquitto (MQTT Broker)**: Para la comunicación entre los dispositivos IoT y el servidor Cloud.
- **Python**: Para el procesamiento de datos y detección de anomalías (en el caso de usar Raspberry Pi 4).
- **Modbus TCP y UART**: Para la comunicación con los Smart meters y medidores de corriente.

### Software Cloud
- **InfluxDB**: Para almacenar los datos históricos de consumo energético.
- **Grafana**: Para la visualización de los datos de consumo energético en tiempo real y la generación de reportes semanales.
- **Node-RED** (en el Cloud): Para el análisis y procesamiento de los datos, así como para la generación de alertas y la visualización.

## Requisitos

- **Hardware**:
  - Smart meters Modbus TCP
  - Medidores de corriente tipo Clamp Sensor (SCT-013)
  - Relés de corte remoto
  - Microcontroladores ESP32 o Raspberry Pi 4
- **Software**:
  - Node-RED
  - Mosquitto (MQTT Broker)
  - InfluxDB
  - Grafana
  - Python (para procesamiento en Raspberry Pi 4)

## Procedimiento de Implementación

### Paso 1: Conectar Sensores y Actuadores
1. Configura los Smart meters Modbus TCP y los medidores de corriente tipo Clamp Sensor en los puntos de consumo de energía relevantes (HVAC, iluminación, etc.).
2. Conecta los relés de corte remoto a los dispositivos no críticos.

### Paso 2: Implementar el Microcontrolador IoT
1. Utiliza un microcontrolador ESP32 o Raspberry Pi 4 para conectar los sensores y relés a través de Modbus TCP o UART.
2. Implementa la lógica local de cálculo de consumo, detección de anomalías y control remoto de dispositivos.

### Paso 3: Configurar la Comunicación con el Cloud
1. Establece una comunicación periódica (cada 15 minutos) entre el microcontrolador y el servidor Cloud utilizando MQTT.
2. Almacena los datos históricos en InfluxDB y configura Grafana para visualizar estos datos.

### Paso 4: Visualización y Reportes
1. Configura dashboards en Grafana para visualizar el consumo energético en tiempo real por planta y por equipo.
2. Configura reportes semanales de eficiencia energética en Grafana para que se envíen automáticamente al personal responsable.

### Paso 5: Alertas y Control Remoto
1. Configura alertas en Node-RED para notificar sobre anomalías de consumo (sobrecargas, picos de consumo, equipos fuera de horario).
2. Implementa la funcionalidad de apagado remoto de dispositivos no críticos en Node-RED.
