# Resultados de la Práctica de Programación con Sensor de Corriente ACS712 en Wokwi

## Descripción del Proyecto

En esta práctica de programación, se desarrolló y simuló un proyecto utilizando el sensor de corriente **ACS712** con el propósito de medir la corriente que pasa y visualizar el resultado en un **monitor serial**. El proyecto se implementó en la plataforma **Wokwi**, simulando un circuito con el microcontrolador **ESP32**.

### Objetivo

El objetivo principal de esta práctica fue aprender a utilizar el sensor **ACS712** para medir la distancia en un entorno simulado en **Wokwi**. Los resultados de la medición se envían al monitor serial para observar la corriente que recibe el sensor.

## Requisitos

- Cuenta en Wokwi.
- Conocimientos básicos de programación en **C/C++** para **ESP32**.
- Conocimientos de cómo funcionan los sensor de corriente ACS712.

## Hardware Utilizado

- **Microcontrolador:** ESP32
- **Sensor de Corriente:** ACS712

## Link de Wokwi:
https://wokwi.com/projects/427249570362939393

## Video demostracion en Loom del codigo:
https://www.loom.com/share/234a7e0d41a94cfa9a9d7d28b1059402?sid=7c1ad1e5-d467-4a0e-a9f3-e836190731e0

## Código Fuente

El código que se implementó para medir la distancia con el sensor ultrasónico **HC-SR04** es el siguiente:

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

// Definir el pin para leer el sensor ACS712
#define SensorPin A0  // Pin analógico A0 para leer el voltaje del ACS712

// Datos de la red Wi-Fi
const char* ssid = "Wokwi-GUEST";        // Reemplaza con tu SSID
const char* password = ""; // Reemplaza con tu contraseña de Wi-Fi

// Datos de Flespi
const char* mqtt_server = "mqtt.flespi.io";  // Servidor MQTT de Flespi
const char* mqtt_token = "l3VDhmTWtzu6Dbu8kh1POdvVqKMOljAn9MLkQ1KxATR3seK8gYyhHUKezHtnNX15"; // Tu token de Flespi
const char* mqtt_topic = "Sensores/ACS712"; // Tema MQTT para enviar la corriente

WiFiClient espClient; 
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);  // Iniciar la comunicación serial

  // Configurar el pin del sensor como entrada
  pinMode(SensorPin, INPUT);

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

  // Leer el valor analógico del sensor ACS712
  int sensorValue = analogRead(SensorPin);  // Valor entre 0 y 4095

  // Convertir el valor a voltaje (3.3V de referencia en ESP32)
  float voltage = sensorValue * (3.3 / 4095.0);  // Convertir a voltaje
  
  // Calcular la corriente basada en el voltaje
  // El valor de referencia es 2.5V, y la sensibilidad es 0.185 A/V para el ACS712
  float current = (voltage - 2.5) / 0.185;

  // Imprimir el valor de la corriente en el monitor serial
  Serial.print("Voltaje: ");
  Serial.print(voltage);
  Serial.print(" V, Corriente: ");
  Serial.print(current);
  Serial.println(" A");

  // Enviar la corriente a Flespi a través de MQTT
  char msg[50];
  snprintf(msg, 50, "{\"current\": %.3f}", current); // Formato JSON
  client.publish(mqtt_topic, msg);

  delay(1000); // Hacer una pausa de 1 segundo
}

