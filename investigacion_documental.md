# Investigacion documental
# By Ochoa Moran Victor Alejandro


# 
🔹 ¿Qué es la gestión de consola por puerto serial?
Es una forma de controlar y administrar una SBC a través de una conexión serial, permitiendo acceso a la terminal del sistema operativo directamente desde otra computadora. Esto es útil cuando:

No tienes acceso físico a un monitor.
Quieres depurar el sistema operativo o el bootloader.
Necesitas configurar el sistema de manera remota o en entornos embebidos.
🔹 ¿Cómo funciona en Raspberry Pi?
La Raspberry Pi tiene un puerto UART en los pines GPIO (General Purpose Input/Output):

TX (Transmit, GPIO 14 - Pin 8)
RX (Receive, GPIO 15 - Pin 10)

🔹 Pasos para habilitar la consola serial en Raspberry Pi
1️⃣ Habilitar el puerto serial

Edita el archivo de configuración con:
bash
Copiar
Editar
sudo raspi-config
Ve a Interfacing Options > Serial Port
Deshabilita la consola en el puerto de hardware (para evitar conflictos).
Habilita el puerto serial como periférico.
2️⃣ Conectar el adaptador USB a Serial

Conecta los pines TX y RX entre la Raspberry Pi y el adaptador.
Asegura que GND de ambos dispositivos estén conectados.
3️⃣ Usar un software de terminal en la PC

En Windows: Usar PuTTY o Tera Term.
En Linux/Mac: Usar screen o minicom.
Ejemplo en Linux para conectar:
bash
Copiar
Editar
sudo screen /dev/ttyUSB0 115200
Si todo está bien, verás la consola de la Raspberry Pi en tu PC.
🔹 Casos de uso
✔️ Configuración remota de sistemas embebidos.
✔️ Depuración del bootloader y kernel.
✔️ Acceso a la Raspberry Pi sin monitor.
Si necesitas más detalles o quieres un ejemplo práctico, dime y te guío paso a paso. 🚀

#
