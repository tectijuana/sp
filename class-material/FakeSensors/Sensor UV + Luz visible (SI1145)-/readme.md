🚀 Proyecto IoT: Monitoreo Ambiental con MQTT y Flespi
Nombre: Serna Segura Noel Alberto
Número de Control: 22210354

🌟 Descripción del Proyecto
Sistema de monitoreo ambiental que utiliza sensores UV (SI1145) y de dióxido de nitrógeno (MICS-2714) para enviar datos a través de MQTT a Flespi, con versiones para Visual Studio Code y Wokwi.

visual code 
# visual-code/main.py
import time
import json
import random
from datetime import datetime
import paho.mqtt.client as mqtt

class EnvironmentalMonitor:
    """Sistema de monitoreo ambiental con sensores UV y NO2"""
    
    def __init__(self):
        self.setup_sensors()
        self.setup_mqtt()
        
    def setup_sensors(self):
        """Configuración inicial de sensores"""
        try:
            import board
            import busio
            import adafruit_si1145
            import analogio
            
            i2c = busio.I2C(board.SCL, board.SDA)
            self.sensor_uv = adafruit_si1145.SI1145(i2c)
            self.no2_sensor = analogio.AnalogIn(board.A0)
            self.HAS_REAL_SENSORS = True
        except:
            print("⚠ Usando sensores simulados")
            self.HAS_REAL_SENSORS = False
    
    def setup_mqtt(self):
        """Configuración de conexión MQTT"""
        self.MQTT_BROKER = "mqtt.flespi.io"
        self.MQTT_PORT = 1883
        self.MQTT_TOPIC = "sensors/uv_no2"
        self.MQTT_TOKEN = "TU_TOKEN_FLESPI"
        
        self.client = mqtt.Client()
        self.client.username_pw_set(self.MQTT_TOKEN, "")
        self.client.on_connect = self.on_connect
        
    def on_connect(self, client, userdata, flags, rc):
        """Callback de conexión MQTT"""
        if rc == 0:
            print("✅ Conexión MQTT establecida!")
        else:
            print(f"❌ Error de conexión: {rc}")

    def read_sensors(self):
        """Lectura de datos de sensores"""
        if self.HAS_REAL_SENSORS:
            return self.read_real_sensors()
        return self.simulate_sensors()
    
    def read_real_sensors(self):
        """Lectura de sensores físicos"""
        return {
            "uv_index": self.sensor_uv.uv_index,
            "visible_light": self.sensor_uv.visible,
            "no2_ppb": self.no2_sensor.value * 100 / 65535,
            "temperature": 25.0,  # Reemplazar con sensor real
            "humidity": 45.0      # Reemplazar con sensor real
        }
    
    def simulate_sensors(self):
        """Simulación de datos de sensores"""
        return {
            "uv_index": round(random.uniform(0, 12), 2),
            "visible_light": round(random.uniform(100, 1000), 2),
            "no2_ppb": round(random.uniform(0, 100), 2),
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(30, 70), 2)
        }
    
    def run(self):
        """Ejecución principal del sistema"""
        self.client.connect(self.MQTT_BROKER, self.MQTT_PORT)
        self.client.loop_start()
        
        try:
            while True:
                data = self.read_sensors()
                data["timestamp"] = datetime.now().isoformat()
                
                payload = json.dumps(data)
                result = self.client.publish(self.MQTT_TOPIC, payload)
                
                if result[0] == mqtt.MQTT_ERR_SUCCESS:
                    print(f"📊 Datos enviados: {payload}")
                else:
                    print(f"⚠ Error al publicar: {result[0]}")
                
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo el sistema...")
        finally:
            self.client.disconnect()
            self.client.loop_stop()

if __name__ == "__main__":
    monitor = EnvironmentalMonitor()
    monitor.run()
    ![image](https://gist.github.com/user-attachments/assets/794cd0bb-4892-42e1-a970-5519041905db)
 
 -Código para Wokwi
 import time
import random
import network
from umqtt.simple import MQTTClient

# Configuración WiFi (necesaria en Wokwi)
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""

# Config MQTT Flespi
SERVER = "mqtt.flespi.io"
CLIENT_ID = "wokwi-esp32-" + str(random.getrandbits(24))
TOPIC = b"sensors/uv_no2"
TOKEN = "2GMLQr2HLjMV1gi5g8ehAmJUCu7PsZ70AyAT0DqzGmdblLv8HUY6ceiLpeVQ5Ij5"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(WIFI_SSID, WIFI_PASS)
    while not sta_if.isconnected():
        print("Conectando a WiFi...")
        time.sleep(0.5)
    print("✅ WiFi conectado! IP:", sta_if.ifconfig()[0])

def read_sensors():
    return {
        "uv_index": random.uniform(0, 12),
        "visible_light": random.uniform(100, 1000),
        "no2_ppb": random.uniform(0, 100),
        "temp": random.uniform(20, 30),
        "humidity": random.uniform(30, 70),
        "timestamp": time.time()
    }

def main():
    connect_wifi()  # Primero conecta WiFi
    
    try:
        client = MQTTClient(CLIENT_ID, SERVER, user=TOKEN, password="", keepalive=30)
        client.connect()
        print("✅ Conectado a MQTT!")
        
        while True:
            data = read_sensors()
            payload = str(data).encode()
            
            try:
                client.publish(TOPIC, payload)
                print("📤 Publicado:", data)
            except Exception as e:
                print("❌ Error al publicar:", e)
                client.connect()  # Reintenta conexión
            
            time.sleep(5)
            
    except Exception as e:
        print("🔥 Error crítico:", e)
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
    ![image](https://github.com/user-attachments/assets/39c44a51-629a-47ef-9f80-1dac59e71e11)
![image](https://github.com/user-attachments/assets/0b7a72f7-8524-40d3-9ea4-6fa6c72ab844)
![image](https://github.com/user-attachments/assets/3f073bd2-4643-4563-8fc8-bb7edf2bfbc8)
![image](https://github.com/user-attachments/assets/65623c93-e4ac-44de-b5f9-f463da9c62a7)





