
Bot de Asistencia: https://chatgpt.com/g/g-HZPuMKEa9-edgex-expert

### **Lección: Introducción a EdgeX Foundry para Servidores de IoT**

#### **Objetivo de la Lección**
Al finalizar esta lección, el estudiante comprenderá los fundamentos de **EdgeX Foundry**, su arquitectura, los microservicios principales y su implementación en servidores de IoT. Se abordará el flujo de datos en EdgeX, el rol de los servicios principales y cómo extender la plataforma con servicios personalizados.

---

## **1. Introducción a EdgeX Foundry**
### **1.1 ¿Qué es EdgeX Foundry?**
EdgeX Foundry es una **plataforma de código abierto** diseñada para facilitar la integración de dispositivos IoT con aplicaciones empresariales en entornos de computación perimetral (*edge computing*). Su arquitectura **basada en microservicios** permite una implementación modular y flexible para diferentes escenarios industriales.

### **1.2 ¿Por qué utilizar EdgeX Foundry en un servidor de IoT?**
- **Escalabilidad**: Su diseño modular permite la integración de nuevos dispositivos y servicios sin modificar la estructura central.
- **Interoperabilidad**: Soporta múltiples protocolos de comunicación como **Modbus, MQTT, REST, OPC-UA, BLE**, entre otros.
- **Seguridad**: Integra autenticación, cifrado de datos y control de acceso mediante **Vault y Kong**.
- **Independencia tecnológica**: Compatible con múltiples sistemas operativos y arquitecturas de hardware.

---

## **2. Arquitectura de EdgeX Foundry**
EdgeX se compone de **varios microservicios organizados en cuatro capas principales**:

### **2.1 Capas de EdgeX Foundry**
1. **Servicios de Dispositivo (Device Services)**
   - Interactúan directamente con los sensores y dispositivos IoT.
   - Protocolo específico para cada tipo de dispositivo (Modbus, OPC-UA, BLE, etc.).
   - Envían datos a la capa de Core Services.

2. **Servicios Centrales (Core Services)**
   - **Core Data**: Almacena y gestiona los datos recolectados.
   - **Metadata**: Mantiene información sobre dispositivos y sus perfiles.
   - **Command**: Permite la ejecución de comandos en dispositivos conectados.
   - **Notifications & Logging**: Gestión de registros y alertas.

3. **Servicios de Aplicación (Application Services)**
   - Filtran, procesan y transforman los datos.
   - Envían la información procesada a la nube, bases de datos o sistemas de análisis.
   - Se utilizan **funciones de transformación, filtrado, encriptación y exportación**.

4. **Servicios de Apoyo (Supporting Services)**
   - Seguridad (**Vault y Kong**).
   - Programación de tareas (**Scheduler**).
   - Control y gestión de reglas (**Rules Engine**).

---

## **3. Instalación y Configuración de EdgeX Foundry en un Servidor IoT**
### **3.1 Requisitos Previos**
- Sistema operativo: **Ubuntu 22.04 LTS** o similar.
- Docker y Docker Compose instalados.
- Conexión a internet para descargar contenedores.

### **3.2 Instalación con Docker**
```bash
git clone https://github.com/edgexfoundry/edgex-compose.git
cd edgex-compose
git checkout v3.1.0
make run
```
Este comando descarga e inicia los servicios de EdgeX Foundry en contenedores Docker.

### **3.3 Verificación del Estado de los Servicios**
Para verificar los servicios en ejecución:
```bash
docker ps
```
Para probar si Core Data está funcionando:
```bash
curl http://localhost:59880/api/v3/ping
```
Si todo funciona correctamente, debería devolver:
```json
{"apiVersion":"v3","timestamp":"<fecha/hora>","serviceName":"core-data"}
```

---

## **4. Creación de un Servicio de Dispositivo (Device Service)**
Un **Device Service** se encarga de comunicar EdgeX con sensores físicos o dispositivos IoT.

### **4.1 Instalación del SDK de Device Services en Go**
```bash
git clone https://github.com/edgexfoundry/device-sdk-go.git
cd device-sdk-go
git checkout v3.1.0
```

### **4.2 Implementación de un Servicio Modbus**
Para soportar dispositivos Modbus, se usa el servicio oficial de EdgeX:
```bash
git clone https://github.com/edgexfoundry/device-modbus-go.git
cd device-modbus-go
make build
```
Este servicio permite la comunicación con dispositivos Modbus TCP o RTU.

---

## **5. Procesamiento de Datos con Servicios de Aplicación**
Los **Application Services** permiten transformar y exportar datos recolectados.

### **5.1 Instalación del SDK de Aplicación**
```bash
git clone https://github.com/edgexfoundry/app-functions-sdk-go.git
cd app-functions-sdk-go
git checkout v3.1.0
```

### **5.2 Creación de un Servicio de Aplicación**
Ejemplo de aplicación que filtra datos de temperatura y los envía a la nube:
```go
func main() {
    service, err := appsdk.NewAppService("TemperatureFilter")
    if err != nil {
        log.Fatal("Error al iniciar el servicio de aplicación:", err)
    }

    // Filtrar solo datos de temperatura
    filter := transforms.NewFilter([]string{"Temperature"})

    // Enviar datos a un servidor MQTT
    mqttSender := mqtt.NewMQTTSender("tcp://mqtt-server:1883", "edgex/messages")

    if err := service.SetPipeline(filter, mqttSender); err != nil {
        log.Fatal("Error en la configuración del pipeline:", err)
    }

    service.Run()
}
```

---

## **6. Gestión y Seguridad en EdgeX Foundry**
### **6.1 Autenticación y Control de Acceso**
EdgeX utiliza **Vault** para el almacenamiento seguro de credenciales y **Kong** como API Gateway.

Para obtener una clave de autenticación de Vault:
```bash
docker exec -it edgex-vault sh
vault token create
```

### **6.2 Monitoreo de Servicios**
Para ver registros en ejecución:
```bash
docker logs -f edgex-core-data
```

---

## **7. Caso Práctico: Implementación en un Servidor Industrial**
### **7.1 Escenario**
- Se quiere conectar sensores de temperatura y humedad mediante Modbus a un servidor IoT con EdgeX.
- Los datos deben ser procesados y enviados a la nube para monitoreo en tiempo real.

### **7.2 Implementación**
1. **Instalar EdgeX en el servidor IoT**.
2. **Configurar el servicio Modbus para leer los sensores**.
3. **Implementar un servicio de aplicación que filtre y envíe datos a la nube**.
4. **Usar Vault y Kong para asegurar la transmisión de datos**.

---

## **8. Evaluación**
### **8.1 Preguntas de Revisión**
1. ¿Cuáles son las cuatro capas principales de EdgeX Foundry?
2. ¿Qué servicio se encarga de gestionar metadatos de dispositivos?
3. ¿Cómo se asegura la autenticación en EdgeX Foundry?

### **8.2 Práctica**
1. Instalar EdgeX en un servidor y verificar los servicios en ejecución.
2. Configurar un Device Service para interactuar con un sensor Modbus.
3. Implementar un Application Service que procese y exporte datos MQTT.

---

## **9. Conclusión**
EdgeX Foundry es una solución flexible y potente para la implementación de servidores IoT, permitiendo conectar dispositivos, procesar datos y asegurar su transmisión de forma modular y escalable. Con una arquitectura basada en microservicios, ofrece independencia tecnológica y compatibilidad con múltiples protocolos de comunicación.

---

### **Referencias**
- [Documentación Oficial de EdgeX Foundry](https://docs.edgexfoundry.org/3.1/)
- [Repositorio de EdgeX Foundry en GitHub](https://github.com/edgexfoundry/)

---

### **Próxima Lección**
**"Desarrollo de Servicios Personalizados en EdgeX Foundry"** 🚀
