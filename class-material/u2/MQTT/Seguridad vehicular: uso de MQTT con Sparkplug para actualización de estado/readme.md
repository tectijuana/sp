# Uso de MQTT con Sparkplug en Seguridad Vehicular

## Aplicaciones típicas de MQTT/Sparkplug en automóviles

En automóviles modernos se emplea MQTT (con Sparkplug) para diversos fines de telemetría y control distribuido. Por ejemplo:

- **Telemetría del vehículo:** transmisión de velocidad, nivel de combustible, temperatura del motor, etc. hacia servidores centrales para monitoreo remoto .  
- **Diagnóstico remoto:** envío de datos de fallos y códigos de error a talleres o centros de servicio .  
- **Actualizaciones OTA:** distribución de software en módulos electrónicos .  
- **Info-entretenimiento:** sincronización de música, navegación y servicios con dispositivos del usuario .  
- **Gestión de flotas:** transmisión en tiempo real de ubicación y estado de cada vehículo .  

Sparkplug añade un modelo de datos estandarizado (payload en **ProtoBuf**) y un esquema de tópicos unificado, lo que facilita la interoperabilidad de equipos heterogéneos .  

---

## Contribución a la seguridad vehicular

### 🔒 Ciberseguridad
- Uso de **TLS** y certificados digitales para cifrar y autenticar clientes .  
- Integración con sistemas de identidad (OAuth, PKI).  
- Confidencialidad e integridad garantizadas en tránsito.  

### 📡 Confiabilidad de comunicaciones
- Niveles de QoS 0, 1 y 2 para asegurar entrega de mensajes críticos .  
- Sesiones persistentes y reconexión automática .  
- Estrategia *report-by-exception* para optimizar ancho de banda.  

### ⚙️ Gestión de fallos y estado
- Certificados de **nacimiento (NBIRTH)** al conectarse y **defunción (NDEATH)** al desconectarse .  
- El sistema siempre conoce qué dispositivos están activos.  
- Se evita procesar datos obsoletos y se mejora la **consistencia** .  

---

## Ejemplos de implementaciones

- **Rimac Automobili (autos eléctricos):**  
  Cada coche transmite miles de datos por segundo vía **MQTT/HiveMQ**, permitiendo telemetría en tiempo real, diagnósticos remotos y actualizaciones OTA robustas  .  

- **OEM automotriz global:**  
  Reportó que al migrar de un protocolo propietario a **MQTT**, logró mayor escalabilidad y redujo costos. Hoy, **todos sus modelos nuevos reciben actualizaciones OTA por MQTT** .  

---

## Comparación con otras tecnologías vehiculares

| Tecnología               | Características | Seguridad | Uso típico |
|--------------------------|-----------------|-----------|------------|
| **CAN**                 | 1 Mbps, robusto, muy usado en ECUs  | Sin cifrado, vulnerable a inyecciones | Control interno en tiempo real |
| **LIN**                 | 20 kbps, simple, esclavo | Sin seguridad | Funciones básicas (ventanas, espejos) |
| **Ethernet automotriz** | Multi-Gbps  | Puede usar TLS/IPsec, requiere configuración | ADAS, multimedia, backbone |
| **MQTT + Sparkplug**    | Pub/Sub sobre IP, QoS, payload ProtoBuf  | TLS, certificados, gestión de estado | Conectividad externa, nube, flotas |

👉 MQTT/Sparkplug **no sustituye** a CAN/LIN, sino que los complementa al encapsular sus datos y transmitirlos con seguridad hacia la nube  .  

---

## Conclusión

MQTT con Sparkplug se está convirtiendo en una pieza clave en la **seguridad vehicular conectada**, ya que:
- Garantiza **comunicación confiable y segura** en redes móviles.  
- Proporciona **gestión de estado en tiempo real**, esencial para detectar fallos.  
- Escala desde un solo vehículo hasta **flotas completas**.  

Con estas características, se posiciona como una tecnología esencial para el futuro de los **vehículos inteligentes y conectados**.  
