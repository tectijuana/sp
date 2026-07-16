import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

# Tiene que coincidir con la información puesta previamente en el publisher"
broker = "localhost" 
port = 1883
topic = "casa/sala/mpu6050"

client = mqtt.Client("MPU6050Subscriber")
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic)

# Genera un bucle para esperar los datos del sensor
print("Esperando datos del MPU-6050...")
client.loop_forever()
