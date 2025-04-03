# Sensor de Nivel de Agua (Analógico)

## Descripción  
El **sensor de nivel de agua analógico** es un dispositivo que permite detectar la presencia o ausencia de agua en un depósito o superficie, proporcionando una salida de voltaje proporcional al nivel del líquido detectado.

## Principio de Funcionamiento  
Este sensor consta de varias pistas conductoras en su superficie. Cuando el agua entra en contacto con ellas, se genera un cambio en la resistencia eléctrica, lo que permite obtener un voltaje variable en su salida analógica. Este voltaje se puede leer mediante un **convertidor analógico-digital (ADC)** en un microcontrolador o placa de desarrollo como **Arduino**.

## Características Generales  
- **Tipo de salida:** Analógica  
- **Tensión de operación:** Generalmente de **3.3V a 5V**  
- **Corriente de operación:** Alrededor de **20 mA**  
- **Rango de detección:** Dependiendo del modelo, puede detectar niveles de agua de **0 a 40 mm** o más  
- **Interfaz:** Se conecta mediante pines **VCC, GND y A0 (salida analógica)**  
- **Material:** Placa PCB con recubrimiento anticorrosivo  

### Código
El siguiente código lee los valores del sensor y los muestra en el **Monitor Serie** de Arduino:

```codigo visual code
import paho.mqtt.client as mqtt
import time

# Configuración de Wokwi
WOKWI_BROKER = "test.mosquitto.org"
WOKWI_PORT = 1883
WOKWI_TOPIC = "wokwi/agua"

# Configuración de Flespi
FLESPI_BROKER = "mqtt.flespi.io"
FLESPI_PORT = 1883
FLESPI_TOPIC = "wokwi/agua"  # Puedes cambiarlo según tus necesidades
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
        print(f"📥 : {payload}")
        
        # Verificar si es un mensaje de Sensor de Nivel de Agua
        if payload.startswith('SensorNivelAgua'):
            parts = payload.split(',')
            
            # Validar que haya suficientes partes y que cada parte tenga el formato esperado
            if len(parts) >= 3 and ':' in parts[0] and ':' in parts[1] and ':' in parts[2]:
                sensor_data = {
                    'type': 'SensorNivelAgua',
                    'nivel': parts[0].split(':')[1],  # Extraer el valor de nivel
                    'estado': parts[1].split(':')[1],  # Extraer el estado (OK/ERROR)
                    'timestamp': parts[2].split(':')[1],  # Extraer el timestamp
                    'raw': payload
                }

                # Convertir a JSON para enviar a Flespi
                json_payload = str(sensor_data).replace("'", '"')
                
                # Enviar a Flespi
                flespi_client.publish(FLESPI_TOPIC, json_payload)
                print(f"Procesando...")
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
![image](https://github.com/user-attachments/assets/8fba0e6c-d729-4dee-bec3-c5578ad2a153)
![image](https://github.com/user-attachments/assets/2b322b48-95a9-45f4-bd94-e01765917000)

