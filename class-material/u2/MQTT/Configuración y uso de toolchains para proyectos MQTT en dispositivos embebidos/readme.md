# Configuración y uso de toolchains para proyectos MQTT en dispositivos embebidos

## 1. Elección y Configuración del Toolchain

### Selección del Toolchain Específico

**Para diferentes arquitecturas:**
- **ARM Cortex-M**: GNU Arm Embedded Toolchain
- **ESP32**: ESP-IDF (incluye toolchain completo)
- **RISC-V**: RISC-V GNU Toolchain
- **AVR**: AVR-GCC

**Consideraciones importantes:**
- **Tamaño del código**: Optar por optimizaciones -Os para minimizar footprint
- **Compatibilidad de librerías**: Verificar que las librerías MQTT sean compatibles
- **Debugging**: Incluir GDB para debugging remoto

### Instalación de Bibliotecas MQTT

**Opciones populares:**
```c
// Paho MQTT C (para sistemas embebidos)
#include "MQTTClient.h"

// PubSubClient para Arduino
#include <PubSubClient.h>

// AWS IoT Device SDK
#include "aws_iot_mqtt_client.h"
```

**Gestión de dependencias:**
- Usar CMake o Make para automatizar la construcción
- Considerar sistemas de paquetes como PlatformIO
- Verificar compatibilidad de versiones

## 2. Configuración Detallada de Comunicación MQTT

### Configuración del Cliente MQTT

```c
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

### Parámetros de Conexión Críticos

```c
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

## 3. Implementación de Publicación y Suscripción

### Gestión de Tópicos

**Estructura recomendada:**
```
dispositivo/{ID_DISPOSITIVO}/{SENSOR}/{COMANDO}
ejemplo: dispositivo/ESP32_001/temperatura/lectura
```

**Implementación de callbacks:**
```c
void message_arrived_callback(MQTTClient_message *message) {
    char *topic = message->payload;
    char *payload = (char*)message->payload;
    
    // Procesar mensaje recibido
    process_incoming_message(topic, payload);
    
    MQTTClient_freeMessage(&message);
    MQTTClient_free(topic);
}
```

### Publicación Eficiente

```c
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

## 4. Gestión Avanzada de Conexiones y Errores

### Mecanismo de Reconexión Robusto

```c
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

### Manejo de Errores Completo

```c
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

## 5. Ejemplo Completo con ESP32 y ESP-IDF

### Configuración del Proyecto

**CMakeLists.txt:**
```cmake
cmake_minimum_required(VERSION 3.5)
set(CMAKE_C_STANDARD 99)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(mqtt_temperature_sensor)

# Componentes requeridos
set(COMPONENTS esp32 mbedtls esp-tls tcp_transport esp_http_client)

# Configuración MQTT
set(MQTT_PROTOCOL_311 true)
set(MQTT_TASK_STACK_SIZE 6144)
```

### Código Principal

```c
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_log.h"
#include "mqtt_client.h"

static const char *TAG = "MQTT_EXAMPLE";

// Callback para eventos MQTT
static void mqtt_event_handler(void *handler_args, esp_event_base_t base, 
                              int32_t event_id, void *event_data) {
    esp_mqtt_event_handle_t event = event_data;
    esp_mqtt_client_handle_t client = event->client;
    
    switch ((esp_mqtt_event_id_t)event_id) {
        case MQTT_EVENT_CONNECTED:
            ESP_LOGI(TAG, "MQTT conectado");
            esp_mqtt_client_subscribe(client, "casa/sala/luz", 0);
            break;
            
        case MQTT_EVENT_DISCONNECTED:
            ESP_LOGI(TAG, "MQTT desconectado");
            break;
            
        case MQTT_EVENT_DATA:
            ESP_LOGI(TAG, "Datos recibidos: %.*s", event->data_len, event->data);
            process_command(event->topic, event->topic_len, event->data, event->data_len);
            break;
            
        case MQTT_EVENT_ERROR:
            ESP_LOGI(TAG, "Error MQTT");
            break;
            
        default:
            break;
    }
}

void app_main(void) {
    // Configuración MQTT
    esp_mqtt_client_config_t mqtt_cfg = {
        .broker.address.uri = "mqtt://broker.emqx.io",
        .credentials.client_id = "esp32_temperature_sensor",
    };
    
    esp_mqtt_client_handle_t client = esp_mqtt_client_init(&mqtt_cfg);
    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, 
                                  mqtt_event_handler, NULL);
    esp_mqtt_client_start(client);
    
    // Publicar datos periódicamente
    while(1) {
        float temperature = read_temperature_sensor();
        char payload[30];
        snprintf(payload, sizeof(payload), "{\"temp\":%.2f}", temperature);
        
        esp_mqtt_client_publish(client, "casa/salon/temperatura", 
                               payload, 0, 1, 0);
        
        vTaskDelay(10000 / portTICK_PERIOD_MS); // 10 segundos
    }
}
```

## 6. Consideraciones Adicionales para Producción

### Seguridad
- Usar TLS/SSL para todas las comunicaciones
- Implementar autenticación con certificados clientes
- Rotar credenciales periódicamente

### Optimización de Recursos
- Usar QoS 0 para datos no críticos
- Limitar tamaño de mensajes
- Implementar sleep modes cuando sea posible

### Monitoreo
- Logging de eventos MQTT
- Métricas de conexión
- Alertas de desconexión prolongada

Esta estructura proporciona una base sólida para implementar MQTT en dispositivos embebidos, considerando tanto el desarrollo como aspectos de producción.
