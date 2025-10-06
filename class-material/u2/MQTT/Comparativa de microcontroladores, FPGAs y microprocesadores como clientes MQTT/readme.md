# Comparativa: Microcontroladores, FPGAs y Microprocesadores como Clientes MQTT
* America Fernanda Nevarez de la Cruz 
* 22211621
* Sistemas Programables
## 1. Microcontroladores
- **Ejemplos**: ESP32, STM32, Arduino con módulos WiFi/Ethernet.  
- **Ventajas**:
  - Bajo consumo de energía (ideal para IoT y dispositivos portátiles).
  - Coste reducido.
  - Integración sencilla con sensores/actuadores.
  - Muchos tienen librerías MQTT listas para usar (ej. PubSubClient en Arduino, AsyncMQTT en ESP32).
- **Limitaciones**:
  - Memoria y potencia de procesamiento limitadas.
  - Soporte de seguridad TLS puede ser costoso en recursos.
  - No aptos para manejar grandes volúmenes de datos ni conexiones concurrentes.

**Uso típico**: sensores IoT, domótica, wearables, telemetría de bajo consumo.

---
![Arduino y Wifi-Ethernet](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYTb2WcgNNY6RgTH3T5bjf4sIAsZZzsxXTnw&s)
## 2. FPGAs
- **Ejemplos**: Xilinx Zynq, Intel/Altera Cyclone, Lattice.  
- **Ventajas**:
  - Procesamiento en paralelo (latencia muy baja).
  - Muy alta personalización de la lógica.
  - Pueden integrar núcleos “soft” de CPU que ejecuten clientes MQTT.
  - Adecuados para aplicaciones en tiempo real crítico.
- **Limitaciones**:
  - Complejidad de desarrollo (requiere HDL o HLS).
  - Librerías MQTT menos maduras en comparación con microcontroladores y microprocesadores.
  - Mayor costo de hardware.
  - Menor flexibilidad para cambios rápidos (en comparación con software en CPUs).
  
**Uso típico**: aplicaciones industriales críticas, sistemas embebidos de alto rendimiento, procesamiento en tiempo real con comunicación MQTT.

---
![Xilinx](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDsx5x8LNB-MKtjoHsZnE7WERPyuuFYXTerw&s)
## 3. Microprocesadores
- **Ejemplos**: Raspberry Pi, BeagleBone, CPUs ARM Cortex-A, x86.  
- **Ventajas**:
  - Potencia de cálculo alta.
  - Ejecución de sistemas operativos completos (Linux, Windows IoT).
  - Amplio soporte de librerías MQTT (Eclipse Paho, Mosquitto client, etc.).
  - Capacidad de manejar múltiples conexiones, cifrado TLS/SSL y QoS avanzados sin problemas.
- **Limitaciones**:
  - Mayor consumo de energía.
  - Más costosos que microcontroladores.
  - Menos adecuados para sistemas ultra-embebidos de bajo costo o batería.

**Uso típico**: gateways IoT, servidores locales MQTT, sistemas con necesidad de análisis y agregación de datos.

---
![Raspberry PI](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbv2CBasls2zlDOKOOST-Wm-G0Pcirdav8-w&s)

## Tabla Comparativa

| Característica       | Microcontroladores       | FPGAs                        | Microprocesadores           |
|----------------------|--------------------------|------------------------------|-----------------------------|
| **Consumo energético** | Muy bajo                 | Medio-alto                   | Medio-alto                  |
| **Costo**            | Bajo                     | Alto                         | Medio                       |
| **Facilidad de uso** | Alta (muchas librerías)  | Baja (desarrollo complejo)   | Alta (ecosistema Linux)     |
| **Potencia de cálculo** | Limitada              | Muy alta (paralelismo)       | Alta                        |
| **Soporte MQTT**     | Amplio (Arduino, ESP)    | Limitado (requiere CPU soft) | Muy amplio (librerías OS)   |
| **Aplicaciones típicas** | Sensores IoT, domótica | Tiempo real crítico, industria | Gateways, edge computing    |

---
