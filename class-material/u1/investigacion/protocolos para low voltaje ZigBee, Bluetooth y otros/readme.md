************************************************************************
* Reseña: Detiene con un switch slider la enumeracion del display en wokwi
* Fecha: 19/05/2025
* Autor: Oscar Sebastian Sandoval Marquez
************************************************************************
# Implementación de Protocolos de Comunicación Inalámbrica en Sistemas Embebidos  
### *Materia: Sistemas Programables – Ingeniería en Sistemas Computacionales*

---

## Introducción

Los sistemas embebidos modernos requieren conectividad inalámbrica para aplicaciones como IoT, automatización industrial, monitoreo ambiental y domótica. Protocolos como **Bluetooth Low Energy (BLE)**, **Zigbee** y **LoRa** permiten esta comunicación eficiente entre dispositivos, cada uno con características específicas que los hacen adecuados para distintos escenarios.

---

## 🔌 Protocolos Analizados

### 1. **Bluetooth Low Energy (BLE)**a``

- **Estándar:** IEEE 802.15.1  
- **Frecuencia:** 2.4 GHz  
- **Alcance:** ~10-100 metros  
- **Ventajas:**
  - Bajo consumo energético
  - Ideal para dispositivos móviles y wearables
  - Soporte nativo en smartphones y tablets
- **Aplicaciones típicas:**
  - Monitoreo de salud
  - Control de acceso
  - Comunicación entre periféricos

### 2. **Zigbee**

- **Estándar:** IEEE 802.15.4  
- **Frecuencia:** 2.4 GHz (también 868 MHz y 915 MHz)  
- **Alcance:** ~10-100 metros (extensible con red de malla)  
- **Ventajas:**
  - Red de malla robusta
  - Alta escalabilidad
  - Bajo consumo energético
- **Aplicaciones típicas:**
  - Automatización del hogar
  - Redes de sensores
  - Control industrial

### 3. **LoRa (Long Range)**

- **Estándar:** LoRaWAN  
- **Frecuencia:** Sub-GHz (433 MHz, 868 MHz, 915 MHz)  
- **Alcance:** ~2-15 km  
- **Ventajas:**
  - Muy bajo consumo
  - Gran alcance
  - Ideal para zonas rurales o urbanas dispersas
- **Aplicaciones típicas:**
  - Agricultura inteligente
  - Monitoreo ambiental
  - Ciudades inteligentes

---

##  Implementación en Sistemas Embebidos
### Hardware común

- **Microcontroladores:** ESP32, STM32, Arduino, Raspberry Pi  
- **Módulos:**
  - BLE: nRF52, HC-08  
  - Zigbee: XBee, CC2530  
  - LoRa: SX1278, RFM95

### Software y herramientas

- **Lenguajes:** C/C++, Python, MicroPython  
- **Entornos:** Arduino IDE, PlatformIO, VS Code  
- **Protocolos de aplicación:** MQTT, CoAP, HTTP
