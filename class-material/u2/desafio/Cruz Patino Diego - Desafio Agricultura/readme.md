# Sistema de Riego Automatizado para Finca

Este sistema de riego automatizado está diseñado para una finca de 5 hectáreas en una zona rural con conectividad limitada y energía solar. El objetivo es automatizar el riego para optimizar el uso del agua y mejorar el rendimiento de los cultivos. A continuación, se describe la arquitectura propuesta, que incluye la selección de sensores, dispositivos, protocolos de comunicación, plataformas en la nube y la lógica de riego.

## Requerimientos

- **Sensores**: Medición de humedad del suelo, temperatura ambiente y nivel de agua en el tanque.
- **Conectividad**: 3G (intermitente y de baja estabilidad).
- **Energía**: Paneles solares (consumo eficiente).
- **Plataforma en la nube**: Visualización en tiempo real y gestión de alertas.

---

## Arquitectura Propuesta

### 1. **Sensores**

Para la correcta automatización del riego, seleccionamos tres tipos de sensores que proporcionan la información clave para tomar decisiones de riego:

- **Sensor de Humedad del Suelo (Capacitivo)**
  - **Modelo**: YL-69 (sensor capacitivo de humedad del suelo).
  - **Por qué**: Este sensor mide la humedad del suelo, proporcionando datos cruciales para determinar cuándo debe activarse el sistema de riego.
  - **Ventaja**: Comparado con los sensores resistivos, los capacitivos son más duraderos y menos propensos a la corrosión, lo que es crucial en condiciones exteriores.

- **Sensor de Temperatura y Humedad Ambiente**
  - **Modelo**: DHT22 (temperatura y humedad).
  - **Por qué**: La temperatura y la humedad ambiental son factores importantes para el cálculo de la evaporación y la transpiración de las plantas, lo que impacta directamente en la cantidad de agua que necesita el cultivo.
  
- **Sensor de Nivel de Agua en el Tanque**
  - **Modelo**: Sensor ultrasónico HC-SR04.
  - **Por qué**: Este sensor medirá el nivel de agua en el tanque de almacenamiento. Esto ayudará a evitar que el sistema de riego se active sin suficiente agua, evitando daños en la bomba.

### 2. **Microcontrolador / SBC (Single Board Computer)**

- **Modelo**: **ESP32**
  - **Por qué**: El ESP32 es ideal para este tipo de proyectos debido a su bajo consumo de energía, capacidad de conectividad Wi-Fi y Bluetooth, y su potencia de procesamiento. 
  - **Conectividad**: Aunque la finca tiene conectividad limitada (3G), el ESP32 puede conectarse a un módem 3G o 4G para enviar datos a la nube.
  - **Eficiencia Energética**: El ESP32 tiene modos de bajo consumo (Deep Sleep) que optimizan el uso de la energía solar.

### 3. **Procesamiento de Datos y Envío**

- **Edge Device**: El ESP32 será responsable de la adquisición de los datos de los sensores, el procesamiento básico y la toma de decisiones sobre el riego.
  - **Tareas**:
    - Leer los datos de los sensores (suelo, temperatura, humedad).
    - Evaluar la condición de los cultivos en base a la humedad del suelo y la temperatura ambiente.
    - Controlar la bomba de riego en función de las decisiones de riego.
    - Enviar datos a la nube de forma periódica (cada hora o cuando se detecte un evento relevante, como una baja humedad en el suelo).
  - **Frecuencia de Envío**: Los datos no se enviarán constantemente para ahorrar en costos de transmisión. El ESP32 enviará los datos a la nube cada 30 minutos o en eventos específicos, como si el nivel de humedad del suelo es bajo o si la bomba de riego no está funcionando correctamente.
  - **Estrategia de Energía**: El ESP32 entrará en modo de bajo consumo (Deep Sleep) entre los períodos de transmisión.

### 4. **Protocolos de Comunicación**

- **MQTT sobre 3G**:
  - **Por qué**: MQTT es un protocolo ligero y eficiente para enviar datos con bajo ancho de banda. Es ideal para aplicaciones con conectividad limitada como en este caso, donde la conexión es intermitente.
  - **Configuración**: El ESP32 enviará datos al broker MQTT cada vez que haya una actualización significativa en las condiciones del suelo o del sistema de riego.
  - **Cliente MQTT**: El ESP32 actuará como cliente, publicando los datos de los sensores a un servidor MQTT en la nube.

### 5. **Plataforma en la Nube**

- **Plataforma**: **Flespi MQTT + Grafana**
  - **Flespi MQTT**: Es una plataforma de gestión de datos IoT que soporta MQTT y permite la integración con diversos servicios de visualización y almacenamiento de datos. Flespi es adecuado para gestionar la comunicación con dispositivos IoT de forma eficiente, soportando baja conectividad y sincronización.
  - **Grafana**: Es una herramienta poderosa para la visualización de datos. Se utilizará para crear un dashboard interactivo que muestre en tiempo real los datos de humedad del suelo, temperatura, nivel de agua y el estado del sistema de riego.
  - **Alertas**: A través de Grafana, se pueden configurar alertas (por ejemplo, si la humedad del suelo es demasiado baja o si hay fallos en la bomba de riego), enviando notificaciones por correo electrónico o incluso SMS.

### 6. **Lógica de Riego Automático**

La lógica de riego se basará en las condiciones del suelo y el clima, además del nivel de agua en el tanque. Se implementará de la siguiente manera:

- **Condiciones del Suelo**: Si la humedad del suelo es inferior al umbral predefinido (por ejemplo, 30%), el sistema de riego se activará.
- **Condiciones Climáticas**: Si la temperatura ambiente es alta y la humedad es baja, el riego será más intensivo. Si las condiciones son frescas y la humedad alta, el sistema puede no activarse.
- **Nivel de Agua**: Si el nivel de agua en el tanque es inferior a un umbral crítico, el sistema de riego no se activará para evitar que la bomba funcione sin suficiente agua.

### 7. **Sostenibilidad Energética**

- El sistema de riego se alimentará principalmente a través de energía solar, lo que requiere un diseño eficiente en términos de consumo de energía.
- El ESP32, al utilizar el modo de bajo consumo, y los sensores (que solo activan lecturas cuando es necesario) optimizarán el uso de la energía disponible.
- La bomba de riego se controlará a través de un relé, permitiendo que se active únicamente cuando sea necesario, y apagándose de inmediato una vez que se logre el nivel de humedad adecuado.

---

## Conclusión

Este sistema de riego automatizado está diseñado para operar de manera eficiente, tanto en términos de consumo energético como de uso de la conectividad limitada. Utilizando sensores adecuados, el ESP32 como microcontrolador, MQTT para la transmisión de datos y Grafana para la visualización y gestión de alertas, se puede lograr un sistema robusto y fiable para la finca, permitiendo un monitoreo en tiempo real y una gestión eficiente del riego.
