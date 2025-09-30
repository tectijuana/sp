# Implementación de protocolos de comunicación inalámbrica en sistemas embebidos (BLE, Zigbee, LoRa)

**Nombre:** Oscar Sebastian Sandoval Marquez

**No.Control:** 22211660


## 1. Introducción
Los sistemas embebidos conectados requieren elegir el protocolo inalámbrico correcto según requisitos de **alcance, consumo energético, ancho de banda, latencia y topología**.  
- **BLE** → corto alcance, baja energía, ideal para wearables y móviles.  
- **Zigbee** → redes en malla, usado en domótica e industria.  
- **LoRa/LoRaWAN** → largo alcance, baja tasa de datos, aplicaciones IoT y LPWAN.

---

## 2. Bluetooth Low Energy (BLE)
- Opera en 2.4 GHz, orientado a bajo consumo.  
- Usa perfiles GATT/GAP para comunicación con móviles.  
- **Hardware común:** nRF52, TI CC26xx, EFR32.  
- **Implementación:** definir servicios GATT, configurar conexión/advertising, optimizar consumo.  
- **Características:** alcance corto (10–50 m), throughput hasta cientos de kb/s, seguridad con AES-CCM.  

---

## 3. Zigbee
- Basado en **IEEE 802.15.4**, soporta topologías en **malla**.  
- Usa **Zigbee Cluster Library (ZCL)** para definir funciones (ej. On/Off, Level Control).  
- **Hardware común:** EFR32 (Silicon Labs), NXP JN516x, Microchip PIC32CX-BZ.  
- **Implementación:** elegir rol (coordinador, router, end device), configurar clusters, unir dispositivo a red.  
- **Características:** bajo consumo, alcance medio (10–100 m), throughput bajo (~250 kb/s).  

---

## 4. LoRa / LoRaWAN
- Tecnología **LPWAN** → largo alcance (km), baja tasa de datos.  
- **LoRa:** modulación física.  
- **LoRaWAN:** protocolo de red que define seguridad, gateways y servidores.  
- **Hardware común:** SX127x, SX126x, módulos Murata, STM32WL.  
- **Implementación:** configurar transceptor, definir parámetros (frecuencia, SF, BW), usar stack LoRaWAN para redes públicas/privadas.  
- **Características:** muy bajo consumo, ideal para sensores remotos, throughput muy bajo (~0.3–50 kb/s).  

---

## 5. Comparativa rápida

| Protocolo | Alcance      | Consumo     | Throughput       | Topología      | Aplicaciones típicas       |
|-----------|-------------|-------------|------------------|----------------|----------------------------|
| **BLE**   | 10–50 m     | Muy bajo    | ~125–1000 kb/s   | P2P, estrella  | Wearables, móviles, IoT    |
| **Zigbee**| 10–100 m    | Bajo        | ~250 kb/s        | Malla          | Domótica, sensores, luces  |
| **LoRa**  | Km (rural)  | Muy bajo    | 0.3–50 kb/s      | Estrella (LoRaWAN) | Smart Cities, monitoreo remoto |

---
