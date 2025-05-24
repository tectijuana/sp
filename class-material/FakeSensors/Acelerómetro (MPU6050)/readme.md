# Proyecto de Integración de Acelerómetro MPU6050 con ESP32, Python, MQTT y Flespi

**Alumno**: Lennyn Alejandro Castillejo Robles  
**Materia**: Sistemas Programables

## Introducción

Este proyecto tiene como objetivo integrar un **acelerómetro MPU6050** con un **ESP32**, procesar los datos en **Python** y luego enviar esos datos a **Flespi** mediante el protocolo **MQTT**. El sistema está diseñado para permitir la visualización de los datos de acelerómetro a través de un **dashboard** de Flespi, utilizando widgets para representar los valores en tiempo real.

## Componentes Utilizados

- **ESP32**: Tarjeta de desarrollo basada en un microcontrolador de 32 bits.
- **MPU6050**: Acelerómetro y giroscopio con interfaz I2C.
- **Python**: Lenguaje de programación utilizado para procesar y enviar los datos a través de MQTT.
- **Flespi**: Plataforma IoT para la gestión de datos en tiempo real y visualización mediante MQTT.
- **MQTT**: Protocolo de comunicación utilizado para enviar datos desde el ESP32 a Flespi y otros sistemas.
  
## Configuración del Hardware

1. **Conexión del Acelerómetro al ESP32**:
   - **MPU6050** se conecta al **ESP32** utilizando la interfaz **I2C**:
     - **VCC** del MPU6050 al **3.3V** del ESP32.
     - **GND** del MPU6050 al **GND** del ESP32.
     - **SDA** del MPU6050 al **GPIO21** del ESP32.
     - **SCL** del MPU6050 al **GPIO22** del ESP32.

## Configuración del ESP32

### Código en el ESP32 (para leer los datos del MPU6050 y enviarlos por MQTT)

```cpp
    import time
    import network
    from umqtt.simple import MQTTClient
    from random import randint  

    # Configuración del Wi-Fi
    SSID = "Wokwi-GUEST"
    PASSWORD = ""

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    while not wifi.isconnected():
      print("Conectando a WiFi...")
      time.sleep(1)

    print("✅ WiFi Conectado. IP:", wifi.ifconfig()[0])

    # Configuración MQTT
    BROKER = "test.mosquitto.org"
    TOPIC = "geps/sensor"
    client = MQTTClient("esp32", BROKER)
    client.connect()

    # Función para generar datos  del sensor MPU6050
    def generate_sensor_data():
      # Generar valores aleatorios para acelerómetro (x, y, z)
      accel_x = randint(-16000, 16000)
      accel_y = randint(-16000, 16000)
      accel_z = randint(-16000, 16000)

      # Generar valores aleatorios para giroscopio (x, y, z)
      gyro_x = randint(-2000, 2000)
      gyro_y = randint(-2000, 2000)
      gyro_z = randint(-2000, 2000)

      # Devolver los valores como un diccionario
      return {
          "accel_x": accel_x,
          "accel_y": accel_y,
          "accel_z": accel_z,
          "gyro_x": gyro_x,
          "gyro_y": gyro_y,
          "gyro_z": gyro_z
      }

    # Bucle infinito para  el sensor y enviar datos cada 3 segundos
    while True:
      # Obtener los datos simulados del sensor
      sensor_data = generate_sensor_data()

      # Crear el mensaje para MQTT
      payload = "Acelerómetro -> x: {0}, y: {1}, z: {2}; Giroscopio -> x: {3}, y: {4}, z: {5}".format(
          sensor_data["accel_x"], sensor_data["accel_y"], sensor_data["accel_z"],
          sensor_data["gyro_x"], sensor_data["gyro_y"], sensor_data["gyro_z"]
      )

      # Publicar los datos a MQTT
      client.publish(TOPIC, payload)  # Enviar los datos simulados al topic
      print("📤 Enviado:", payload)   # Imprimir los datos enviados en la consola

      time.sleep(3)  # Esperar 3 segundos antes de enviar los siguientes datos
     
```
![image](https://github.com/user-attachments/assets/5574cfeb-d7fd-45de-838b-9c74b011f4a6)


## Código de visual code en python 
```
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "geps/sensor"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "geps/sensor"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "EgSoZ4aHSwmmMTHJHkNl1oy7rynU87drVAJMt3HnkzdzDIyAlzEDaYKnC6s6QBFG"  # Reemplaza con tu token de Flespi

# Función para conectar con el broker y verificar la conexión
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado correctamente")
    else:
        print(f"❌ Error de conexión: {rc}")

# Función para procesar los mensajes recibidos desde Wokwi
def on_message_wokwi(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Recibido de Wokwi: {payload}")
        
        # Verificar si el mensaje contiene datos del acelerómetro
        if 'accelerometer' in payload:
            # Procesar los datos del acelerómetro (suponiendo que están en formato JSON o similar)
            data = eval(payload)  # Convertir la cadena de texto a un diccionario (esto es solo un ejemplo, usa json.loads en lugar de eval)
            
            accelerometer_data = data.get("accelerometer", {})
            if accelerometer_data:
                # Crear un payload para Flespi con solo los datos del acelerómetro
                json_payload = {
                    'accelerometer': accelerometer_data
                }
                
                # Enviar los datos a Flespi
                flespi_client.publish(FLESPI_TOPIC, str(json_payload).replace("'", '"'))
                print(f"📤 Enviado a Flespi: {json_payload}")
        
        # Enviar siempre el mensaje recibido (aunque no sea acelerómetro)
        else:
            flespi_client.publish(FLESPI_TOPIC, payload)
            print(f"📤 Enviado a Flespi (raw): {payload}")
            
    except Exception as e:
        print(f"⚠ Error al procesar mensaje: {e}")

# Configurar cliente Wokwi (versión actualizada para evitar warning)
wokwi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
wokwi_client.on_message = on_message_wokwi
wokwi_client.on_connect = on_connect

# Configurar cliente Flespi
flespi_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
flespi_client.username_pw_set(FLESPI_TOKEN)
flespi_client.on_connect = on_connect

try:
    # Conectar a Flespi
    flespi_client.connect(FLESPI_BROKER, FLESPI_PORT)
    flespi_client.loop_start()
    
    # Conectar a Wokwi
    wokwi_client.connect(WOKWI_BROKER, WOKWI_PORT)
    wokwi_client.subscribe(WOKWI_TOPIC)
    print("📡 Esperando datos de Wokwi...")
    
    # Mantener el script corriendo
    wokwi_client.loop_forever()
    
except KeyboardInterrupt:
    print("\n🔌 Desconectando...")
    wokwi_client.disconnect()
    flespi_client.disconnect()
except Exception as e:
    print(f"❌ Error crítico: {e}")
```

![image](https://github.com/user-attachments/assets/ba5023b2-2ee1-4a6e-add0-5ada721fbb99)

## Board en MQTT


![image](https://github.com/user-attachments/assets/4ea3d777-56e2-411d-b9fa-0f461bad4b7c)


     
