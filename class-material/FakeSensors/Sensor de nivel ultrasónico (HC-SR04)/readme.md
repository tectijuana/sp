# Resultados de la Práctica de Programación con Sensor Ultrasónico HC-SR04 en Wokwi

## Descripción del Proyecto

En esta práctica de programación, se desarrolló y simuló un proyecto utilizando el sensor ultrasónico **HC-SR04** con el propósito de medir la distancia y visualizar el resultado en un **monitor serial**. El proyecto se implementó en la plataforma **Wokwi**, simulando un circuito con el microcontrolador **ESP32**.

### Objetivo

El objetivo principal de esta práctica fue aprender a utilizar el sensor ultrasónico **HC-SR04** para medir la distancia en un entorno simulado en **Wokwi**. Los resultados de la medición se envían al monitor serial para observar la distancia en centímetros.

## Requisitos

- Cuenta en Wokwi.
- Conocimientos básicos de programación en **C/C++** para **ESP32**.
- Conocimientos de cómo funcionan los sensores ultrasónicos HC-SR04.

## Hardware Utilizado

- **Microcontrolador:** Arduino Uno
- **Sensor Ultrasónico:** HC-SR04
  - **VCC** al pin **5V** de Arduino
  - **GND** al pin **GND** de Arduino
  - **Trig** al pin **3** de Arduino
  - **Echo** al pin **4** de Arduino
 
- **Conexiones:** 
  - El sensor **HC-SR04** se conecta a los pines digitales de Arduino para la transmisión de señales de disparo y eco.

## Esquema de Circuito

El circuito se simuló en Wokwi con la siguiente configuración:

- El **pin Trig** del sensor está conectado al pin **5** de ESP32.
- El **pin Echo** del sensor está conectado al pin **7** de ESP32.
- El **VCC** se conecta al pin de **5V** de ESP32.
- El **GND** se conecta al pin de **GND** de ESP32.

- Link de Wokwi para mejor identificacion de los pines:
https://wokwi.com/projects/427202158131296257

## Código Fuente

El código que se implementó para medir la distancia con el sensor ultrasónico **HC-SR04** es el siguiente:

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

// Definir los pines del sensor
#define Trigger 2 // Pin digital 2 para el Trigger del sensor
#define Echo 4  // Pin digital 4 para el Echo del sensor

// Definir las variables
long t; // Tiempo que demora en llegar el eco
long d; // Distancia en centímetros

// Datos de la red Wi-Fi
const char* ssid = "Wokwi-GUEST";        // Reemplaza con tu SSID
const char* password = ""; // Reemplaza con tu contraseña de Wi-Fi

// Datos de Flespi
const char* mqtt_server = "mqtt.flespi.io";  // Servidor MQTT de Flespi
const char* mqtt_token = "l3VDhmTWtzu6Dbu8kh1POdvVqKMOljAn9MLkQ1KxATR3seK8gYyhHUKezHtnNX15"; // Tu token de Flespi
const char* mqtt_topic = "Sensores/HC-SR04"; // Tema MQTT para enviar la distancia

WiFiClient espClient; 
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);  // Iniciar la comunicación serial
  pinMode(Trigger, OUTPUT); // Pin como salida
  pinMode(Echo, INPUT);  // Pin como entrada
  digitalWrite(Trigger, LOW); // Inicializamos el pin con 0

  // Conectar a la red Wi-Fi
  setup_wifi();

  // Configurar el servidor MQTT
  client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
  delay(10);
  Serial.println("📡 Conectando a WiFi...");
  
  // Conexión Wi-Fi
  WiFi.begin(ssid, password);
  int retries = 0;
  
  // Esperar hasta que se conecte o llegue al límite de reintentos
  while (WiFi.status() != WL_CONNECTED && retries < 20) {  // Intentar 20 veces
    delay(500);
    retries++;
  }

  if ((WiFi.status() == WL_CONNECTED)){
    delay(500);
    Serial.println("✅ WiFi conectado!");
  }
  else{
    delay(500);
    Serial.println("🚫 Sin conexion WiFi");
    Serial.println("Estado WiFi: " + String(WiFi.status()));
  }
}

void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("👨‍💻 Conectando a MQTT...");
    if (client.connect("ESP32Client", mqtt_token, "")) {
      Serial.println("✅ Conectado a MQTT!");
      } 
    else {
      Serial.print("❌ Fallo MQTT, rc=");
      Serial.println(client.state());
      switch (client.state()) {
        case -1: Serial.println("Error de conexión, motivo: No hay conexión."); break;
        case -2: Serial.println("Error de conexión, motivo: No se pudo encontrar el broker MQTT."); break;
        case -3: Serial.println("Error de conexión, motivo: Conexión rechazada por broker."); break;
        case -4: Serial.println("Error de conexión, motivo: Credenciales incorrectas."); break;
        default: Serial.println("Error desconocido."); break;
      }
      Serial.println("🔄 Reintentando en 5 segundos... ");
      delay(5000);
    }
  } 
}

void loop() {
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();

  // Enviar un pulso de 10us al Trigger del sensor
  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);          // Enviar un pulso de 10us
  digitalWrite(Trigger, LOW);

  // Recibir el pulso de respuesta del sensor por el pin Echo
  t = pulseIn(Echo, HIGH); // Obtener el ancho del pulso

  // Calcular la distancia
  d = t / 59;  // Escalar el tiempo a una distancia en cm

  // Imprimir la distancia en el monitor serial
  Serial.print("Distancia: ");
  Serial.print(d);  // Enviar serialmente el valor de la distancia
  Serial.print(" cm");
  Serial.println();

  // Enviar la distancia a Flespi a través de MQTT
  char msg[50];
  snprintf(msg, 50, "{\"distance\": %ld}", d); // Formato JSON
  client.publish(mqtt_topic, msg);

  delay(1000); // Hacer una pausa de 1 segundo
}
´´´´

## Video demostracion en Loom del codigo:
https://www.loom.com/share/dea4bcdfa9d24c24bd2977aa33cb42da?sid=a5f5cf3c-c0de-4c44-8808-de383a820ed0
