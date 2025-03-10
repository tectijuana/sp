# **Lección 2: Desarrollo de Servicios Personalizados en EdgeX Foundry**  

---

## **1. Objetivo de la Lección**  
Al finalizar esta lección, el estudiante será capaz de desarrollar y desplegar **servicios personalizados** en EdgeX Foundry. Se explorará la **creación de Device Services y Application Services**, su configuración y prueba en un entorno EdgeX.  

---

## **2. Introducción**  
### **2.1 ¿Por qué crear servicios personalizados en EdgeX Foundry?**  
EdgeX Foundry proporciona microservicios prediseñados para la mayoría de los casos de uso en IoT. Sin embargo, en escenarios específicos puede ser necesario crear servicios personalizados para:  
- Soportar **protocolos de comunicación propietarios**.  
- Implementar **lógica de negocio** en el procesamiento de datos.  
- Integrarse con **sistemas externos** como bases de datos o plataformas en la nube.  

### **2.2 Tipos de Servicios Personalizados**  
- **Device Services**: Permiten la comunicación entre EdgeX y dispositivos físicos.  
- **Application Services**: Procesan y exportan datos a otros sistemas.  

---

## **3. Creación de un Device Service Personalizado**  

### **3.1 Instalación del SDK para Device Services**  
El SDK de Device Services en Go facilita la creación de servicios personalizados para conectar EdgeX con dispositivos IoT.  

#### **Pasos de instalación**  
```bash
git clone https://github.com/edgexfoundry/device-sdk-go.git
cd device-sdk-go
git checkout v3.1.0
```
Este SDK proporciona una base para desarrollar nuevos servicios de dispositivo.  

---

### **3.2 Estructura de un Device Service**  
Un Device Service en EdgeX tiene la siguiente estructura:  
```plaintext
/device-service
├── cmd/main.go  # Punto de entrada del servicio
├── internal/
│   ├── driver.go  # Lógica de comunicación con el dispositivo
│   ├── config.yaml  # Configuración del servicio
├── go.mod  # Dependencias del proyecto
└── Dockerfile  # Archivo para la creación del contenedor
```

### **3.3 Implementación de un Servicio para Sensores de Temperatura**  
Vamos a crear un Device Service que lea datos de temperatura desde un sensor virtual.  

#### **Paso 1: Crear un nuevo servicio**  
```bash
mkdir device-temperature
cd device-temperature
go mod init device-temperature
go get github.com/edgexfoundry/device-sdk-go/v3
```

#### **Paso 2: Implementar la lógica de conexión con el sensor**  
Editar `internal/driver.go`:  
```go
package driver

import (
    "errors"
    "math/rand"
    "time"

    "github.com/edgexfoundry/device-sdk-go/v3/pkg/models"
    "github.com/edgexfoundry/go-mod-core-contracts/v3/models"
)

type TemperatureDriver struct{}

func (d *TemperatureDriver) Initialize() error {
    return nil
}

func (d *TemperatureDriver) HandleReadCommands(deviceName string, protocols map[string]models.ProtocolProperties,
    reqs []models.CommandRequest) ([]*models.CommandValue, error) {

    var responses []*models.CommandValue
    for _, req := range reqs {
        if req.DeviceResourceName == "Temperature" {
            temp := float64(rand.Intn(30) + 10) // Simulación de temperatura
            cmdVal, _ := models.NewCommandValue(req.DeviceResourceName, time.Now().UnixNano(), temp)
            responses = append(responses, cmdVal)
        } else {
            return nil, errors.New("Recurso desconocido")
        }
    }
    return responses, nil
}
```

#### **Paso 3: Configurar el servicio**  
Editar `res/configuration.yaml`:  
```yaml
Service:
  Host: localhost
  Port: 49992
DeviceList:
  - Name: VirtualTemperatureSensor
    Profile: temperature-profile.yaml
    AutoEvents:
      - Frequency: 10s
        OnChange: false
        SourceName: Temperature
```

#### **Paso 4: Definir el perfil del dispositivo**  
Crear `res/temperature-profile.yaml`:  
```yaml
deviceResources:
  - name: Temperature
    properties:
      valueType: Float64
      readWrite: R
      defaultValue: 25.0
```

#### **Paso 5: Construir y ejecutar el servicio**  
```bash
go build -o device-temperature
./device-temperature
```

---

## **4. Creación de un Application Service Personalizado**  

### **4.1 Instalación del SDK para Application Services**  
```bash
git clone https://github.com/edgexfoundry/app-functions-sdk-go.git
cd app-functions-sdk-go
git checkout v3.1.0
```

### **4.2 Implementación de un servicio para filtrar y enviar datos**  
Vamos a crear un Application Service que filtre los datos de temperatura y los envíe a un servidor MQTT.

#### **Paso 1: Crear un nuevo servicio de aplicación**  
```bash
mkdir app-temperature
cd app-temperature
go mod init app-temperature
go get github.com/edgexfoundry/app-functions-sdk-go/v3
```

#### **Paso 2: Implementar la lógica de filtrado y envío**  
Editar `main.go`:  
```go
package main

import (
    "log"

    "github.com/edgexfoundry/app-functions-sdk-go/v3/pkg/appsdk"
    "github.com/edgexfoundry/app-functions-sdk-go/v3/pkg/transforms"
    "github.com/edgexfoundry/go-mod-messaging/v3/pkg/messaging/mqtt"
)

func main() {
    service, err := appsdk.NewAppService("TemperatureProcessor")
    if err != nil {
        log.Fatal("Error al iniciar el servicio de aplicación:", err)
    }

    // Filtrar solo datos de temperatura
    filter := transforms.NewFilter([]string{"Temperature"})

    // Enviar datos a un servidor MQTT
    mqttSender := mqtt.NewMQTTSender("tcp://mqtt-server:1883", "edgex/temperature")

    if err := service.SetPipeline(filter, mqttSender); err != nil {
        log.Fatal("Error en la configuración del pipeline:", err)
    }

    service.Run()
}
```

#### **Paso 3: Construir y ejecutar el servicio**  
```bash
go build -o app-temperature
./app-temperature
```

---

## **5. Integración y Despliegue en EdgeX**  
Para integrar estos servicios personalizados en un entorno EdgeX, se deben incluir en el archivo `docker-compose.yml`.  

### **5.1 Añadir el Device Service**  
```yaml
device-temperature:
  image: device-temperature
  container_name: edgex-device-temperature
  ports:
    - "49992:49992"
  networks:
    - edgex-network
```

### **5.2 Añadir el Application Service**  
```yaml
app-temperature:
  image: app-temperature
  container_name: edgex-app-temperature
  networks:
    - edgex-network
```

Para desplegar ambos servicios, ejecutar:  
```bash
docker-compose up -d device-temperature app-temperature
```

---

## **6. Evaluación**  
### **6.1 Preguntas de Revisión**  
1. ¿Cuál es la función de un Device Service en EdgeX?  
2. ¿Cómo se define un perfil de dispositivo en EdgeX?  
3. ¿Cuál es el propósito de un Application Service?  

### **6.2 Práctica**  
1. Crear un Device Service para leer datos de humedad.  
2. Crear un Application Service que filtre y almacene los datos en una base de datos.  

---

## **7. Conclusión**  
En esta lección, aprendimos a desarrollar **servicios personalizados en EdgeX Foundry** para conectar dispositivos y procesar datos. Estos servicios permiten adaptar la plataforma a necesidades específicas de IoT.  

---

### **Próxima Lección**  
**"Seguridad y Autenticación en EdgeX Foundry"** 🔒
