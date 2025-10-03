# Sensores MEMS conectados vía MQTT: Diseño e Implementación en Plataformas Embebidas

**Autor:** Galeana Leja Jesus Eduardo (22211565)

**Institución:** Instituto Tecnológico de Tijuana

**Materia:** Sistemas Programables

**Profesor:** Rene Solis Reyes

**Fecha:** 30 de septiembre del 2025

### Introducción
MQTT es la abreviatura de Message Queuing Telemetry Transport, el cual es un protocolo de mensajería que funciona por medio de un sistema publisher-subscriber. Para que estos funcionen se requiere de un sistema broker, el cual funciona como un servidor central que se encarga de gestionar los mensajes transmitidos publicados por el publisher, para repartirlos hacia los suscriptores. Los mensajes pueden contar con distintos niveles de calidad de servicio (QoS).

1. QoS 0: "al menos una vez" (es el más rápido, pero también se corre el riesgo de perder un mensaje, ya que estos no se reenvían).
2. QoS 1: "al menos una vez" (Se asegura de que llegue el mensaje, pero puede llegar a duplicarse).
3. QoS 2: "exactamente una vez" (Es el más lento, pero a su vez el más seguro y es capaz de evitar duplicados).

También cuenta con topics, los cuales sirven como directorios o nombres de canal, como se presenta en el siguiente ejemplo:
sala/casa/temperatura

### Implementación del MQTT en un sensor MPU-6050
El sensor MPU-6050 es un sensor MEMS bastante utilizado (cuenta con un acelerómetro, giroscopio y un sensor de temperatura interno). Se puede integrar con un Raspberry PI usando Python3, y enviando los datos por medio del MQTT.

<img width="350" height="250" alt="image" src="https://github.com/user-attachments/assets/dacb6621-c0d6-45ee-9044-7ba8cfcf35a0" />

**Instalación de Python3 y dependencia MQTT en Raspberry PI**
```
sudo apt-get install python3-smbus i2c-tools
pip install paho-mqtt
```
Para que pueda funcionar el bus I²C del sensor dentro de Raspberry PI, se requiere de los siguientes comandos para activarlo y verificar su funcionamiento
```
sudo raspi-config
# Interfacing Options → I2C → Enable
i2cdetect -y 1
```
Para comprobar que esté funcionando, debe contar con la dirección 0x68

Se puede utilizar algo como Eclipse Mosquitto como broker, que implementa el protocolo MQTT en sus versiones 5.0, 3.1.1 y 3.1., y puede instalarse dentro del Raspberry PI.

En el caso del publisher se solicitan datos como el broker o hostname, el puerto que se va a utilizar, así como factores de autenticación, el QoS, entre otras cosas. Aquí está un ejemplo de cómo se configura:
```python3
broker = "IP del broker o localhost"  
port = 1883
topic = "casa/sala/mpu6050" 

client = mqtt.Client("MPU6050Publisher")
client.connect(broker, port)

print("Enviando datos MPU-6050 por MQTT...")
```
Para el subscriber, se debe incluir el código que se encuentra dentro del archivo "Ejemplo_código_publisher".

Tanto el publisher como el subscriber deben importar la biblioteca paho.mqtt.client para permitir el funcionamiento del MQTT.

### REFERENCIAS
Light, R. (2024, 17 abril). How to use the PAHO MQTT client in Python - MQTT Client Library Encyclopedia. HiveMQ. https://www.hivemq.com/blog/mqtt-client-library-paho-python/
MPU-6000-Datasheet1. (2013, 19 agosto). InvenSense. https://cdn.sparkfun.com/datasheets/Sensors/Accelerometers/RM-MPU-6000A.pdf
MQTT  MQTT 5 Essentials (HiveMQ) (Z-Library).pdf. (s. f.). Google Docs. https://drive.google.com/file/d/1lE-pkBQetk-meXwGcSVaRuKeg2E5zXXv/view?usp=drive_link
Schiffler, A. (2025, 9 julio). How to Use the Paho MQTT Client in Python with Examples. Cedalo. https://cedalo.com/blog/configuring-paho-mqtt-python-client-with-examples/#How_to_install_the_Paho_MQTT_Python_client
