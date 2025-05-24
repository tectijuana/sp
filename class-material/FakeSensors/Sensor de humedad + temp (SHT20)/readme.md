## Sensor de humedad + temp (SHT20) SHT20
#### Por: Abner Nahum Ortega Medina #20211819
### ¿Qué es un sensor SHT20?
El **SHT20** es un **sensor digital de temperatura y humedad** fabricado por **Sensirion**. Este sensor mide dos parámetros importantes: **temperatura** y **humedad relativa** en el ambiente, y lo hace con alta precisión.

#### Características principales del sensor SHT20:

- **Medición de temperatura**:
  - Mide la temperatura con una precisión de ±0.3°C en un rango de **-40°C a 125°C**.

- **Medición de humedad**:
  - Mide la humedad relativa con una precisión de ±3% en el rango de **0% a 100% de humedad relativa**.

- **Interfaz de comunicación**:
  - Utiliza una interfaz **I2C** para la comunicación, lo que facilita la conexión a microcontroladores y sistemas como el **Arduino**, **ESP32**, **Raspberry Pi**, etc.

- **Consumo de energía**:
  - Tiene un bajo consumo de energía, lo que lo hace adecuado para dispositivos alimentados por batería.

- **Salida digital**:
  - El sensor proporciona datos digitales, lo que significa que no necesitas un convertidor analógico a digital (ADC), simplificando la integración en sistemas electrónicos.

- **Compensación interna**:
  - El SHT20 tiene compensación interna para asegurarse de que las mediciones sean precisas, independientemente de las variaciones de voltaje o la temperatura.
### Código para leer datos del sensor SHT20 y publicarlos en MQTT

```python
import network
import utime
import ujson
from machine import Pin, I2C
from umqtt.simple import MQTTClient
import random

# --- Configuración WiFi y MQTT ---
WIFI_SSID = "Wokwi-GUEST"  # O el nombre de tu red Wi-Fi
WIFI_PASS = ""  # Deja vacío si estás usando Wokwi-GUEST

MQTT_BROKER = "mqtt.flespi.io"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/humedad_temp"
MQTT_TOKEN = "Voyv9LbypAEAkrQ4Hf4d2omZV7xmVTfjMuQ5XYd27aRRlf40F7qx97MZjvEQ5PSH"

# --- Configurar sensor SHT20 (I2C) ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Asegúrate de que estos pines sean correctos

# --- Conectar a WiFi ---
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    
    print("Intentando conectar al WiFi...")
    
    # Intentar conectarse hasta 10 veces
    attempt = 0
    while not wlan.isconnected() and attempt < 10:
        print(f"Conectando... intento {attempt + 1}/10")
        utime.sleep(1)
        attempt += 1
    
    if wlan.isconnected():
        print("✅ WiFi conectado. IP:", wlan.ifconfig()[0])
    else:
        print("❌ No se pudo conectar al WiFi después de 10 intentos.")

# --- Conectar a MQTT ---
def connect_mqtt():
    client_id = f"sensor_{random.randint(0, 10000)}"
    client = MQTTClient(client_id, MQTT_BROKER, port=MQTT_PORT, user=MQTT_TOKEN, password="")
    try:
        client.connect()
        print("✅ Conectado a MQTT")
    except Exception as e:
        print("❌ Error al conectar a MQTT:", str(e))
        return None
    return client

# --- Función para leer datos del sensor SHT20 ---
def read_sht20():
    SENSOR_ADDR = 0x40  # Dirección I2C del SHT20
    
    try:
        # Comando para leer humedad
        i2c.writeto(SENSOR_ADDR, bytearray([0xF5]))  # Comando para leer humedad
        utime.sleep(0.1)  # Espera para que el sensor procese
        
        humidity_data = i2c.readfrom(SENSOR_ADDR, 2)  # Leer los 2 bytes de la humedad
        humidity = ((humidity_data[0] << 8) | humidity_data[1]) & 0xFFFC
        humidity = -6 + 125 * (humidity / 65536.0)  # Convertir a porcentaje
        
        # Comando para leer temperatura
        i2c.writeto(SENSOR_ADDR, bytearray([0xF3]))  # Comando para leer temperatura
        utime.sleep(0.1)  # Espera para que el sensor procese
        
        temperature_data = i2c.readfrom(SENSOR_ADDR, 2)  # Leer los 2 bytes de la temperatura
        temperature = ((temperature_data[0] << 8) | temperature_data[1]) & 0xFFFC
        temperature = -46.85 + 175.72 * (temperature / 65536.0)  # Convertir a °C
        
        return humidity, temperature
    
    except Exception as e:
        print("❌ Error al leer el sensor SHT20:", str(e))
        return None, None

# --- Función para generar datos simulados ---
def generate_sensor_data(humidity, temperature):
    timestamp_ms = utime.time() * 1000  # Convertir a milisegundos
    
    data = {
        "sensor": "SHT20",
        "temperatura": round(temperature, 2),
        "humedad": round(humidity, 2),
        "timestamp": timestamp_ms,
        "device_id": "ESP32-SENSOR01"
    }
    
    return data

# --- Iniciar conexiones ---
connect_wifi()
mqtt_client = connect_mqtt()

# --- Loop principal ---
while True:
    try:
        # Leer datos del sensor SHT20
        humidity, temperature = read_sht20()
        
        if humidity is not None and temperature is not None:
            print(f"💧 Humedad: {humidity}% | 🌡️ Temperatura: {temperature}°C")
            
            # Generar los datos para MQTT
            data = generate_sensor_data(humidity, temperature)
            json_data = ujson.dumps(data)
            
            # Publicar los datos en el servidor MQTT
            mqtt_client.publish(MQTT_TOPIC, json_data)
            print("📤 Mensaje enviado:", json_data)
        else:
            print("❌ Error al leer los datos del sensor")
        
        # Esperar antes de leer nuevamente
        utime.sleep(5)  # Publicar cada 5 segundos
    except Exception as e:
        print("❌ Error al leer el sensor o publicar el mensaje:", str(e))
        utime.sleep(1)
```


### Explicación del Código

Este código corresponde a un programa para un microcontrolador **ESP32** que está diseñado para leer datos de temperatura y humedad desde un sensor **SHT20**, y luego publicar esos datos a un servidor **MQTT**.

Aquí está la explicación de cómo funcionaría la ejecución:

1. **Configuración inicial**: El código establece la configuración para la conexión **WiFi** y **MQTT**, y configura el bus **I2C** para comunicarse con el sensor **SHT20**.
   
2. **Conexión WiFi**: La función `connect_wifi()` intenta conectar el **ESP32** a una red **WiFi** (en este caso, "Wokwi-GUEST" que parece ser un entorno de simulación).
   
3. **Conexión MQTT**: La función `connect_mqtt()` establece una conexión con el broker **MQTT** en `mqtt.flespi.io` usando un token de autenticación.
   
4. **Lectura del sensor**: La función `read_sht20()` lee los datos de **temperatura** y **humedad** del sensor **SHT20** a través del bus **I2C**.
   
5. **Generación de datos**: La función `generate_sensor_data()` empaqueta los datos del sensor en un formato **JSON** con información adicional como la marca de tiempo y el ID del dispositivo.
   
6. **Bucle principal**: En un ciclo infinito, el código:
   - Lee los datos del sensor
   - Genera un paquete **JSON** con esos datos
   - Publica los datos en el tema **MQTT** "sensor/humedad_temp"
   - Espera 5 segundos antes de repetir el proceso

### Requisitos para el funcionamiento

Para el funcionamiento virtual del sistema (como se muestra en la simulación), necesitarías los siguientes elementos:

#### Entorno de simulación:

- **Wokwi**: Es el simulador que parece estar utilizándose en la imagen. **Wokwi** permite simular el hardware **ESP32** y sus periféricos en un navegador web.

#### Proyecto de simulación que incluya:

- Un **ESP32 virtual**
- Un componente **SHT20 virtual** (o algún simulador de sensores I2C)
- Conexiones virtuales entre los componentes

#### Configuración de la simulación:

- **Archivo de configuración** (`wokwi.toml` o similar) que defina:
  - Los componentes utilizados
  - Las conexiones entre ellos
  - Configuración del simulador

#### Simulación de red:

- **Wokwi** proporciona una **red WiFi simulada** ("Wokwi-GUEST")
- Un **servidor MQTT** simulado o conexión a uno real

#### Bibliotecas y firmware:

- **MicroPython** como firmware virtual en el **ESP32** simulado
- Bibliotecas que ya están incluidas en la imagen de **MicroPython** para **Wokwi**:
  - `network`
  - `machine`
  - `umqtt.simple`
  - `ujson`

#### Para la visualización:

- **Panel de visualización** para los datos de sensores (que podría ser parte de **Wokwi** u otra herramienta conectada al mismo broker **MQTT**)
- **Monitor serial** (incluido en **Wokwi**) para ver los mensajes de depuración y la salida del programa
- Aqui una simulacion de como se veria su ejecucion.
  ![sensor sth20 ejecucion](https://github.com/user-attachments/assets/ed2ba027-c2de-4f59-b0ed-ec0a5a909ad3)
  ![image](https://github.com/user-attachments/assets/df84e390-a678-4d9a-84ca-b8c93ce4b30a)


