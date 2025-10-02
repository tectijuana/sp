# Configuración y uso de toolchains para proyectos MQTT en dispositivos embebidos

Antes de configurar y usar toolchains en proyectos MQTT en dispositivos embebidos, primero es necesario elegir el toolchain adecuado para el microcontrolador a utilizar (como GCC for ARM para sistemas basados en ARM) y configurarlo con las bibliotecas MQTT necesarias (por ejemplo, Paho MQTT). Luego, en el código, se inicializara el cliente MQTT, para conectarse a un broker, al conectarse existe la opcion de suscribirse o publicar mensajes en tópicos, gestionando la autenticación y la reconexión para asegurar la comunicación eficiente en la red con recursos limitados. 

## 1. Elegir y Configurar el Toolchain
**Seleccionar Toolchain:** Para dispositivos embebidos, el toolchain más común es el GNU Compiler Collection (GCC) para la arquitectura del microcontrolador a utilizar, como ARM Cortex-M. También se puedes usar el SDK del fabricante del chip (por ejemplo, el ESP-IDF para ESP32) que incluye bibliotecas para MQTT y el toolchain necesario. 

**Instalar las Bibliotecas Necesarias:** Descargar e integrar las bibliotecas cliente MQTT en el proyecto. La biblioteca PubSubClient para Arduino, para microcontroladores como el ESP32, o la biblioteca Paho MQTT para Rust son opciones populares. Estas bibliotecas permitirán implementar el protocolo MQTT. 

**Instalación de Bibliotecas MQTT**

```
// Paho MQTT C (para sistemas embebidos)
#include "MQTTClient.h"

// PubSubClient para Arduino
#include <PubSubClient.h>

// AWS IoT Device SDK
#include "aws_iot_mqtt_client.h"
```

## 2. Configurar la Comunicación MQTT
**Configura el Cliente MQTT:** En el código, se crea una instancia del cliente MQTT (como Paho o PubSubClient), especificando la dirección del broker MQTT, el puerto y un ID de cliente único para el dispositivo a utilizar. 

**Conectarse al Broker:** Establecer la conexión TCP/IP entre el dispositivo y el broker MQTT. 

**Gestionar la Autenticación:** Si es necesario, configurar credenciales de usuario y contraseña para que el dispositivo pueda autenticarse en el broker, lo cual es un paso clave para una conexión segura y válida. 

**Configuración del Cliente MQTT**

```
// Ejemplo con Paho MQTT
MQTTClient client;
MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;

// Configuración básica
conn_opts.keepAliveInterval = 60;
conn_opts.cleansession = 1;
conn_opts.username = "usuario";
conn_opts.password = "contraseña";

// Configuración SSL/TLS (para conexiones seguras)
MQTTClient_SSLOptions ssl_opts = MQTTClient_SSLOptions_initializer;
ssl_opts.trustStore = "/cert/ca.crt";
ssl_opts.keyStore = "/cert/client.crt";
ssl_opts.privateKey = "/cert/client.key";
```

**Parámetros de Conexión Críticos**

```
typedef struct {
    char *broker_host;
    int broker_port;
    char *client_id;
    int keepalive_interval;
    int timeout_ms;
    bool clean_session;
    bool enable_ssl;
} mqtt_config_t;
```

## 3. Publicar y Suscribirse a Tópicos
***Crear Tópicos MQTT:** Definir los tópicos para el intercambio de mensajes, que son cadenas de texto que funcionan como canales de comunicación. Por ejemplo, sensor/temperatura o actuador/luz.

**Publicar Mensajes:** Envía datos (cargas útiles) a un tópico específico para que los suscriptores reciban la información.

**Suscribirse a Tópicos:** Suscribe el dispositivo a tópicos para recibir los mensajes publicados por otros clientes. 

```
// Estructura recomendada
// dispositivo/{ID_DISPOSITIVO}/{SENSOR}/{COMANDO}
// ejemplo: dispositivo/ESP32_001/temperatura/lectura

void message_arrived_callback(MQTTClient_message *message) {
    char *topic = message->payload;
    char *payload = (char*)message->payload;
    
    // Procesar mensaje recibido
    process_incoming_message(topic, payload);
    
    MQTTClient_freeMessage(&message);
    MQTTClient_free(topic);
}
```
**Publicación Eficiente**

```
int publish_sensor_data(MQTTClient client, const char* topic, float value) {
    char payload[50];
    snprintf(payload, sizeof(payload), "{\"value\":%.2f,\"timestamp\":%ld}", 
             value, get_timestamp());
    
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    pubmsg.payload = payload;
    pubmsg.payloadlen = strlen(payload);
    pubmsg.qos = QOS;
    pubmsg.retained = 0;
    
    return MQTTClient_publishMessage(client, topic, &pubmsg, NULL);
}
```

## 4. Gestión de Conexiones y Errores
**Habilitar la Reconexión Automática:** Implementar la funcionalidad de reconexión para gestionar la inestabilidad de la conexión a internet y asegurar que el dispositivo se vuelva a conectar si se pierde la conexión con el broker. 

**Manejo de los Errores:** Utilizar métodos de gestión de errores robustos para que la aplicación se mantenga fiable y no falle abruptamente si hay problemas durante la comunicación. 

**Mecanismo de Reconexión Robusto**

```
typedef struct {
    int max_retry_attempts;
    int retry_delay_ms;
    int backoff_multiplier;
    int current_retry_count;
} reconnect_config_t;

bool reconnect_with_backoff(MQTTClient client, reconnect_config_t *config) {
    int delay = config->retry_delay_ms * 
                pow(config->backoff_multiplier, config->current_retry_count);
    
    vTaskDelay(delay / portTICK_PERIOD_MS);
    
    int rc = MQTTClient_connect(client, &conn_opts);
    if (rc == MQTTCLIENT_SUCCESS) {
        config->current_retry_count = 0;
        return true;
    } else {
        config->current_retry_count++;
        return false;
    }
}
```

**Manejo de Errores Completo**

```
typedef enum {
    MQTT_ERROR_NONE = 0,
    MQTT_ERROR_CONNECTION_LOST,
    MQTT_ERROR_SUBSCRIBE_FAILED,
    MQTT_ERROR_PUBLISH_FAILED,
    MQTT_ERROR_TIMEOUT
} mqtt_error_t;

void handle_mqtt_error(mqtt_error_t error, const char* context) {
    switch(error) {
        case MQTT_ERROR_CONNECTION_LOST:
            ESP_LOGE("MQTT", "Conexión perdida en: %s", context);
            initiate_reconnection();
            break;
        case MQTT_ERROR_SUBSCRIBE_FAILED:
            ESP_LOGE("MQTT", "Error en suscripción: %s", context);
            break;
        // ... manejar otros errores
    }
}
```
## 5. Consideraciones Adicionales para Producción

**Seguridad**

- Usar TLS/SSL para todas las comunicaciones

- Implementar autenticación con certificados clientes

- Rotar credenciales periódicamente

**Optimización de Recursos**

- Usar QoS 0 para datos no críticos

- Limitar tamaño de mensajes

- Implementar sleep modes cuando sea posible

**Monitoreo**

- Logging de eventos MQTT

- Métricas de conexión

- Alertas de desconexión prolongada

## Bibliografia
- Trovò, M. (2025, 22 enero). How to Use the Paho MQTT Client Library in a Rust Project. Cedalo. https://cedalo.com/blog/integrating-mqtt-in-rust/#:~:text=Conexi%C3%B3n%20al%20br%C3%B3ker%20Mosquitto%20MQTT&text=Este%20c%C3%B3digo%20inicializa%20el%20cliente,se%20mantenga%20fiable%20y%20mantenible.
- Jecrespom. (2021, 7 noviembre). MQTT. Aprendiendo Arduino. https://aprendiendoarduino.wordpress.com/2018/11/19/mqtt/#:~:text=mqtt%2Dover%2Dwebsockets-,Protocolo%20MQTT,a%20trav%C3%A9s%20de%20la%20red.&text=Una%20sesi%C3%B3n%20MQTT%20se%20divide,una%20identidad%20de%20cliente%20reutilizada.
- Monitoreo, Telemetría, Sensores y Automatización Industrial. (2023, 8 agosto). Microcontroladores IoT. https://www.controltec.cl/microcontroladores-iot
- Garcia, J., & Garcia, J. (2024, 12 junio). Protocolo MQTT: Funcionamiento y creación de tu propio Broker - ATG Analytical. ATG Analytical -. https://atganalytical.com/protocolo-mqtt-funcionamiento-y-creacion-de-tu-propio-broker/#:~:text=Tras%20su%20descarga%20(y%20opcionable%20instalaci%C3%B3n%20para,aparecer%C3%A1%20una%20ventana%20parecida%20a%20la%20siguiente:
- ¿Qué es el MQTT? - Explicación del protocolo MQTT - AWS. (s. f.). Amazon Web Services, Inc. https://aws.amazon.com/es/what-is/mqtt/#:~:text=El%20agente%20MQTT%20es%20el,mensaje%20y%20enviarles%20los%20mensajes.
- Sesión 6: MQTT - HackMD. (s. f.). HackMD. https://hackmd.io/@LF0FqZwDTDWM-MMK06IEWA/BkdxYltPn#:~:text=Cuando%20un%20cliente%20se%20conecta%2C%20podr%C3%ADa%20configurar,que%20ese%20cliente%20ya%20no%20est%C3%A1%20disponible.
