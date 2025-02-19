# 📖 Investigación Documental

## ✍️ By Ochoa Morán Víctor Alejandro

## 🔌 Puerto Serial

### 📌 ¿Qué es la gestión de consola por puerto serial?

Es una forma de controlar y administrar una SBC (Single Board Computer) a través de una conexión serial, permitiendo acceso a la terminal del sistema operativo directamente desde otra computadora. Esto es útil cuando:

✅ No tienes acceso físico a un monitor.
✅ Quieres depurar el sistema operativo o el bootloader.
✅ Necesitas configurar el sistema de manera remota o en entornos embebidos.

## 🖥️ ¿Cómo funciona en Raspberry Pi?

La Raspberry Pi tiene un puerto UART en los pines GPIO (General Purpose Input/Output):

- **TX (Transmit)** → GPIO 14 (Pin 8)
- **RX (Receive)** → GPIO 15 (Pin 10)

## ⚙️ Pasos para habilitar la consola serial en Raspberry Pi

### 1️⃣ Habilitar el puerto serial

Edita el archivo de configuración con:

```bash
sudo raspi-config
```

Navega a:

```text
Interfacing Options > Serial Port
```

- Deshabilita la consola en el puerto de hardware (para evitar conflictos).
- Habilita el puerto serial como periférico.

### 2️⃣ Conectar el adaptador USB a Serial

🔗 **Conexión de pines:**

- TX de la Raspberry Pi → RX del adaptador
- RX de la Raspberry Pi → TX del adaptador
- GND de ambos dispositivos conectados

### 3️⃣ Usar un software de terminal en la PC

📌 **Opciones de software:**

- **Windows:** PuTTY, Tera Term
- **Linux/Mac:** screen, minicom

Ejemplo de conexión en Linux:

```bash
sudo screen /dev/ttyUSB0 115200
```

Si todo está bien, verás la consola de la Raspberry Pi en tu PC. 🎉

## 🔍 Casos de uso

✔️ Configuración remota de sistemas embebidos.
✔️ Depuración del bootloader y kernel.
✔️ Acceso a la Raspberry Pi sin monitor.

---

## 📡 Sensor GPS

El cable **FTDI** es un adaptador USB a TTL (serial) que permite la comunicación entre una computadora y dispositivos electrónicos como microcontroladores, módulos GPS y sensores. Usa un chip FTDI (de Future Technology Devices International) para convertir señales USB en UART, lo que lo hace útil para:

✅ Depuración
✅ Carga de firmware
✅ Control de dispositivos

## 🛠️ ¿Cómo usar un cable FTDI con PuTTY u otros softwares?

### 🔗 Conectar el cable correctamente

- **Negro (GND)** → Tierra del dispositivo.
- **Rojo (VCC)** → Alimentación (3.3V o 5V según el dispositivo).
- **Blanco (TXD)** → Se conecta al RX del dispositivo.
- **Verde (RXD)** → Se conecta al TX del dispositivo.

📌 Algunos cables tienen más pines como RTS/CTS para control de flujo.

### 📥 Instalar los drivers FTDI

- **Windows, macOS o Linux:** Puede ser necesario instalar los drivers FTDI (disponibles en el sitio oficial de FTDI).

### 🔍 Identificar el puerto COM asignado

- **Windows:** Revisar en el Administrador de Dispositivos (`devmgmt.msc`).
- **Linux:** Usar `ls /dev/ttyUSB*` o `ls /dev/ttyS*`.
- **macOS:** Usar `ls /dev/cu.usbserial*`.

### 🖥️ Abrir PuTTY o cualquier otro terminal serial

1. Seleccionar: **Serial**
2. Especificar el puerto COM detectado.
3. Configurar **baud rate** (Ej: 9600, 115200, según el dispositivo).
4. Ajustar **paridad, bits de datos y bits de parada** según necesidad.
5. Habilitar **flujo de control** si es requerido.

### 🚀 Iniciar la comunicación

Una vez configurado, presiona "Abrir" en PuTTY para ver y enviar comandos al dispositivo.

## 📌 Aplicaciones comunes del cable FTDI

1.✔️ Depuración de dispositivos embebidos (ESP8266, Arduino, Raspberry Pi).
2.✔️ Comunicación con módulos GPS para leer datos NMEA.
3.✔️ Programación de microcontroladores y placas con UART.
4.✔️ Conversión de comunicación serie para dispositivos antiguos.


