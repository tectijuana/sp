# Sensor UV VEML6075
## Molina Fabela Edgar Fabian

## Descripción  
El **VEML6075** es un sensor de radiación ultravioleta que mide la intensidad de los rayos **UVA y UVB**, proporcionando una estimación del **Índice UV** (UVI). Este sensor se comunica mediante el protocolo **I²C**, lo que permite una fácil integración con microcontroladores como **Arduino, ESP32 y Raspberry Pi**.

## Principio de Funcionamiento  
El **VEML6075** utiliza fotodiodos específicos para detectar longitudes de onda de **UVA (315-400 nm)** y **UVB (280-315 nm)**. Gracias a un algoritmo interno, el sensor compensa la interferencia de luz visible e infrarroja para mejorar la precisión de las lecturas.

## Características Generales  
- **Protocolo de comunicación:** I²C  
- **Rango de tensión de operación:** **1.7V a 3.6V**  
- **Consumo de corriente:** **0.8 mA (modo activo), 0.0001 mA (modo apagado)**  
- **Salidas:** Valores de **UVA**, **UVB** y **UVI** calculado  
- **Longitud de onda de detección:**  
  - **UVA:** **315 - 400 nm**  
  - **UVB:** **280 - 315 nm**  
- **Dirección I²C:** **0x10**  
- **Dimensiones:** Compacto y de bajo consumo, ideal para dispositivos portátiles  


### Código

```Codigo wokwi
import time
import network
from umqtt.simple import MQTTClient

# Configurar WiFi en Wokwi
SSID = "Wokwi-GUEST"
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Conectando a WiFi...")
    time.sleep(1)

print("✅ WiFi Conectado. IP:", wifi.ifconfig()[0])

# Configurar MQTT
BROKER = "test.mosquitto.org"
TOPIC = "wokwi/rayos"
client = MQTTClient("esp32", BROKER)
client.connect()

# Datos Rayos simulados
rayos_data = [
    "Flespi - UVA:2.35,UVB:1.58,Index:1.97",
    "Flespi - UVA:2.79,UVB:0.75,Index:1.77",
    "Flespi - UVA:4.98,UVB:0.45,Index:2.72",
    "Flespi - UVA:1.97,UVB:0.38,Index:1.18",
    "Flespi - UVA:4.7,UVB:3.81,Index:4.25",
    "Flespi - UVA:0.37,UVB:3.05,Index:1.71"
]

# Bucle infinito para enviar datos cada 3 segundos
while True:
    for sentence in rayos_data:
        client.publish(TOPIC, sentence)
        print("📤 Enviado:", sentence)
        time.sleep(3)  # Esperar 3 segundos antes de enviar el siguiente dato

//
codigo visual code
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "wokwi/rayos"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "wokwi/rayos"  # Puedes cambiarlo según tus necesidades
FLESPI_TOKEN = "UZWw15Ebqz5hEbWPdblv1UFWei9qdJmVLU4mivpjcmJBzSHZeR5h8QvBdWDMmec7"  # Reemplaza con tu token de Flespi

# Solución para la advertencia de deprecación
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado correctamente")
    else:
        print(f"❌ Error de conexión: {rc}")

def on_message_wokwi(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Recibido de Wokwi: {payload}")
        
        # Verificar si es un mensaje Flespi y si tiene el formato correcto
        if payload.startswith('Flespi'):
            parts = payload.split(',')
            
            # Validar que haya suficientes partes y que cada parte tenga el formato esperado
            if len(parts) >= 4 and ':' in parts[1] and ':' in parts[2] and ':' in parts[3]:
                nmea_data = {
                    'type': 'Flespi',
                    'UVA': parts[1].split(':')[1],  # Extraer el valor de UVA
                    'UVB': parts[2].split(':')[1],  # Extraer el valor de UVB
                    'Index': parts[3].split(':')[1],  # Extraer el valor de Index
                    'raw': payload
                }

                # Convertir a JSON para enviar a Flespi
                json_payload = str(nmea_data).replace("'", '"')
                
                # Enviar a Flespi
                flespi_client.publish(FLESPI_TOPIC, json_payload)
                print(f"📤 Enviado a Flespi: {json_payload}")
            else:
                print("Procesando...")
        else:
            # Si no es Flespi, enviar tal cual
            flespi_client.publish(FLESPI_TOPIC, payload)
            print(f"📤 Enviado a Flespi (raw): {payload}")
            
    except Exception as e:
        print(f"⚠️ Error al procesar mensaje: {e}")


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
![image](https://github.com/user-attachments/assets/f7726fbe-d1f4-40c8-baaf-ca71e2a73e40)
![image](https://github.com/user-attachments/assets/22ab2634-39ac-4228-94ee-61f66aa5e448)
