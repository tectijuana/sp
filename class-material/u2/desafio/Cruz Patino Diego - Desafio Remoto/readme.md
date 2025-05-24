# Estaciones de Monitoreo Ambiental IoT en Reserva Natural

## 🆄 Contexto General
Una ONG ambientalista desea implementar estaciones de monitoreo ambiental en una reserva natural montañosa y de difícil acceso. El sistema debe ser autónomo, confiable y capaz de operar sin infraestructura de comunicación tradicional.

## ⚙️ Sensores Seleccionados

### 1. Temperatura y Humedad Relativa 🌡️💧
- **Sensor:** SHT31-D (Sensirion)
- **Justificación:** Alta precisión (±0.3°C, ±2% HR), bajo consumo (<2 µA en modo standby), interfaz I2C, confiable en ambientes extremos.

### 2. Niveles de CO₂ 🌫️
- **Sensor:** SCD30 (Sensirion)
- **Justificación:** Alta precisión, mediciones de CO₂ hasta 10,000 ppm, también mide temperatura y humedad relativa (sirve como respaldo). Consumo moderado, interfaz I2C.

### 3. Humedad del Suelo 🌱
- **Sensor:** Capacitivo v2.0
- **Justificación:** No se corroe, bajo consumo, interfaz analógica, buen comportamiento en suelos diversos.

## 🧰 Nodo IoT

### Microcontrolador
- **Placa:** Raspberry Pi Pico + Módulo LoRa SX1276 (Ra-02 o similar)
- **Razón:** Bajo consumo, buena documentación, fácil de programar en MicroPython o C++, soporte para almacenamiento local.

### Conexión LoRaWAN
- **Vía:** Módulo SX1276 conectado por SPI.
- **Protocolo:** Utiliza LoRaWAN mediante stack como LMIC o equivalente.
- **Frecuencia:** 915 MHz (para LATAM)

## 🔢 Almacenamiento Local
- Si no hay conexión LoRaWAN:
  - Los datos se guardan localmente en una microSD (FAT32).
  - Cada registro incluye: timestamp, sensores, voltaje de batería.
  - Una rutina reintenta el envío cada 30 min hasta tener éxito.

## 🏠 Estación Base
- **Hardware:** Raspberry Pi 4 + Módulo LoRa concentrador (RAK2245 o equivalente)
- **Software:** ChirpStack para gestionar la red LoRaWAN
- **Conectividad:**
  - Prioridad 1: WiFi satelital (ej: Starlink)
  - Prioridad 2: 4G LTE USB dongle
- **Agrega los datos recibidos y los reenvía a la nube cada 30 min**

## ☁️ Arquitectura Nodo → Estación Base → Nube

```
[Nodo IoT x N] --LoRaWAN--> [Estación Base (ChirpStack)] --LTE/WiFi--> [Servidor EC2 (Nube)]
```

## 📈 Visualización de Datos
- **Servidor Cloud:** Amazon EC2 (Ubuntu)
- **Base de Datos:** InfluxDB (time-series)
- **Visualización:** Grafana
- **Características:**
  - Dashboards por estación
  - Alertas por:
    - CO₂ elevado
    - Sensor desconectado/fallo (datos nulos o fuera de rango)
    - Batería baja (<20%)

## ⚠️ Detección de Fallos
- **Sensores:** Verificación por watchdog interno cada hora
- **Batería:** Medición por divisor resistivo al ADC
- **Logs de error:** Enviados junto con los datos o almacenados localmente

---

## 🚀 Futuras Mejores
- Inclusión de panel solar más grande con MPPT
- Deep Sleep para extender autonomía
- Compresión de datos para ahorrar ancho de banda LoRaWAN
