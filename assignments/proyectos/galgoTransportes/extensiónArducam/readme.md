

### 🚀 **Propuesta: “Smart Cargo Guardian — Visión Inteligente para Transporte Seguro”**

#### 🎯 **Objetivo**

Agregar al sistema de Galgo Transportes un módulo de **visión embebida en el camión** que detecte eventos críticos como:

* Robo o manipulación de carga
* Conducción distraída o somnolencia del chofer
* Carga incorrecta o mal asegurada
* Accidentes o caídas de bultos

Todo con **procesamiento en el borde (edge AI)** y sincronización de alertas en tiempo real mediante **Flespi MQTT + Grafana Cloud Dashboard**.

---

### 🧠 **Arquitectura propuesta**

```mermaid
graph TD
A[Arduino ML Camera (Nicla Vision)] -->|MQTT Publish| B[Flespi MQTT Broker]
B --> C[Edge Gateway (ESP32 / Raspberry Pi)]
C -->|Data forwarding| D[Cloud Storage (InfluxDB + Grafana Cloud)]
D --> E[Smart Dashboard + Alerts (Grafana / Telegram Bot)]
```

---

### ⚙️ **Componentes clave**

| Componente                               | Función                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Arduino ML Camera Kit**                | Captura y clasifica imágenes (personas, carga, rostros, movimiento).                        |
| **TinyML model (TensorFlow Lite)**       | Detecta eventos anómalos (intrusos, somnolencia, carga abierta).                            |
| **Flespi MQTT**                          | Broker gratuito para transmitir datos compactos (JSON con etiquetas de evento y timestamp). |
| **Raspberry Pi / ESP32 Gateway**         | Conecta sensores adicionales (GPS, temperatura, vibración).                                 |
| **Grafana Cloud**                        | Visualiza eventos en mapas y gráficos de actividad.                                         |
| **Prometheus + Alertmanager (opcional)** | Genera alertas a WhatsApp o correo.                                                         |

---

### 📡 **Datos transmitidos por MQTT**

```json
{
  "device_id": "truck_07_camA",
  "event": "cargo_open_detected",
  "confidence": 0.87,
  "gps": {"lat": 32.532, "lon": -117.018},
  "timestamp": "2025-11-04T14:32:10Z",
  "image_url": "flespi.io/frames/galgo07/event123.jpg"
}
```

---

### 💡 **Innovación**

1. **TinyML en el borde:** evita enviar video completo → ahorro de ancho de banda.
2. **Fusión de sensores:** combina datos visuales, acelerómetros y GPS.
3. **Uso de Flespi MQTT:** integra con bajo costo y excelente compatibilidad con Grafana, Node-RED o InfluxDB.
4. **Escalabilidad industrial:** puede expandirse a flotas completas.
5. **Sostenible:** procesamiento local reduce consumo energético de red.

---

### 🔐 **Seguridad y mantenimiento**

* Certificados MQTT (TLS) para cámara y gateway.
* Actualizaciones OTA desde Flespi o EC2 host.
* Edge buffering si se pierde conexión.

---

### 🧩 **Posible roadmap**

| Fase | Actividad                                          | Hardware            |
| ---- | -------------------------------------------------- | ------------------- |
| 1    | Prototipo de detección de eventos visuales         | Arduino ML Kit      |
| 2    | Integración MQTT y dashboard Flespi                | ESP32 + Flespi      |
| 3    | Dashboard Grafana + Alertas Telegram               | EC2 o Grafana Cloud |
| 4    | Optimización de modelo TinyML y despliegue a flota | Docker + OTA        |

