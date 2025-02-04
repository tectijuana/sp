# Periféricos y buses de comunicación en sistemas embebidos: UART, SPI, I2C, CAN y USB
## Jesus Uriel Luna Gomez - UrieLuna17
## 19211675

En sistemas embebidos, los periféricos y los buses de comunicación juegan un papel crucial en la interacción entre microcontroladores, sensores, memorias y otros dispositivos. A continuación, se describen algunos de los buses de comunicación más utilizados:

### 1. **UART (Universal Asynchronous Receiver-Transmitter)**
   - **Tipo**: Comunicación serie asíncrona.
   - **Características**:
     - Utiliza solo dos líneas: **TX** (transmisión) y **RX** (recepción).
     - No requiere señal de reloj compartida.
     - Usa bits de inicio y parada para sincronización.
     - Velocidades típicas: 9600, 115200 baudios, entre otras.
   - **Aplicaciones**:
     - Comunicación con módulos Bluetooth (HC-05, HC-06).
     - Comunicación con GPS, sensores y computadoras.

### 2. **SPI (Serial Peripheral Interface)**
   - **Tipo**: Comunicación serie síncrona.
   - **Características**:
     - Usa cuatro líneas principales:
       - **SCLK** (Serial Clock).
       - **MOSI** (Master Out Slave In).
       - **MISO** (Master In Slave Out).
       - **SS/CS** (Slave Select/Chip Select).
     - Full-duplex (puede enviar y recibir datos simultáneamente).
     - Rápida (varios MHz de velocidad).
   - **Aplicaciones**:
     - Comunicación con memorias Flash, sensores, pantallas OLED.
     - Conexión de múltiples esclavos a un maestro.

### 3. **I2C (Inter-Integrated Circuit)**
   - **Tipo**: Comunicación serie síncrona multimaster-multiesclavo.
   - **Características**:
     - Usa solo dos líneas: **SDA** (datos) y **SCL** (reloj).
     - Cada dispositivo tiene una dirección única en el bus.
     - Soporta múltiples dispositivos con solo dos cables.
     - Velocidades estándar: 100 kHz (Standard), 400 kHz (Fast Mode), 1 MHz (Fast Mode Plus).
   - **Aplicaciones**:
     - Sensores (IMU, temperatura).
     - Módulos RTC (Reloj en Tiempo Real).
     - Expansores de IO y memorias EEPROM.

### 4. **CAN (Controller Area Network)**
   - **Tipo**: Comunicación serie diferencial orientada a redes.
   - **Características**:
     - Diseñado para entornos industriales y automotrices.
     - Usa dos líneas: **CAN_H** y **CAN_L**.
     - Alta inmunidad al ruido y robustez en largas distancias.
     - Control de errores avanzado mediante CRC.
     - Velocidades comunes: 125 kbps, 500 kbps, 1 Mbps.
   - **Aplicaciones**:
     - Automóviles (ECUs, ABS, airbags).
     - Sistemas industriales y domótica.

### 5. **USB (Universal Serial Bus)**
   - **Tipo**: Comunicación serie universal.
   - **Características**:
     - Proporciona alimentación y datos en el mismo cable.
     - Modos de operación: **Low Speed (1.5 Mbps), Full Speed (12 Mbps), High Speed (480 Mbps), SuperSpeed (5 Gbps)**.
     - Admite diferentes configuraciones: Host, Dispositivo, OTG.
   - **Aplicaciones**:
     - Conexión de microcontroladores con PC.
     - Dispositivos de almacenamiento masivo (USB Flash, discos duros).
     - Periféricos como teclados, ratones y cámaras.

Cada bus tiene sus ventajas y desventajas según el contexto de aplicación. En sistemas embebidos, la elección del bus depende de la velocidad, el número de dispositivos y la distancia de comunicación.
