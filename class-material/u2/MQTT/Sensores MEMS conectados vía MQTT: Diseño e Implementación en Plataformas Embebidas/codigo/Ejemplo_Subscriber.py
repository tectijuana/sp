# ╔═══════════════════════════════════════════════════════════════╗
# ║  Programa:    Ejemplo_Subscriber.py — Suscriptor MQTT         ║
# ║  Programador: MC. René Solis R.                               ║
# ║  Curso:       Sistemas Programables (EmbeddedSP) TECNM / ITT  ║
# ║  Horario:     [999]                                           ║
# ║  Actividad:   U2 — Sensores MEMS (MPU-6050) vía MQTT          ║
# ║  Asciinema:   [URL de la grabación]                           ║
# ╚═══════════════════════════════════════════════════════════════╝
#
# Objetivo: suscribirse al tópico MQTT donde el publisher publica las
# lecturas del sensor MPU-6050 y mostrarlas en consola conforme llegan.
#
# Recuerde iniciar su asciinema identificándose antes de cualquier comando:
#   $ echo "Programa Ejemplo_Subscriber.py, por MC. René Solis R. de curso Sistemas Programables Horario [999] actividad MQTT-MEMS"

import paho.mqtt.client as mqtt

# Callback: se ejecuta cada vez que llega un mensaje al tópico suscrito
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
