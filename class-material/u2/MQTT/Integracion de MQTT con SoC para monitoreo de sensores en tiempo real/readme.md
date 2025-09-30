# Integración de MQTT con SoC para Monitoreo de Sensores en Tiempo Real  
**Autor:** Alonso Villela Iker Saúl – 22211517  

**INSTITUTO TECNOLÓGICO DE TIJUANA**  
**Materia:** Sistemas Programables  
**Fecha:** 2025-09-30  

---

## Introducción  

La comunicación en **tiempo real** es un requisito clave en aplicaciones embebidas modernas, especialmente en el **Internet de las Cosas (IoT)** y en sistemas que requieren **monitoreo continuo de sensores**. En este contexto, la integración de **Sistemas en Chip (SoC)** con protocolos de mensajería ligera como **MQTT (Message Queuing Telemetry Transport)** permite construir soluciones eficientes, confiables y escalables.  

MQTT es un protocolo de comunicación **publicación-suscripción**, diseñado para **entornos con recursos limitados** y redes poco confiables, lo que lo convierte en un aliado natural para sistemas embebidos con SoC.  

Esta investigación aborda:  

1. **Fundamentos de MQTT y su integración con SoC**  
2. **Arquitectura de un sistema de monitoreo con sensores en tiempo real**  
3. **Comparación de SoC compatibles con MQTT**  
4. **Técnicas de optimización y seguridad**  
5. **Tendencias futuras en el uso de MQTT y SoC en IoT**  

---

## Fundamentos de MQTT y SoC  

### MQTT en sistemas embebidos  
- Protocolo ligero (usa **TCP/IP**)  
- Modelo **publicador-suscriptor**  
- Componentes principales:  
  - **Broker MQTT**: servidor central que distribuye mensajes  
  - **Publisher**: dispositivo que envía datos (sensor en SoC)  
  - **Subscriber**: cliente que recibe datos (aplicación, dashboard, otro dispositivo)  

### Rol del SoC en el sistema  
Los **SoC** proporcionan la capacidad de:  
- Procesar datos del sensor localmente  
- Conectarse al broker MQTT mediante Wi-Fi, Ethernet o LTE  
- Ejecutar algoritmos de optimización y filtrado antes de enviar los datos  
- Asegurar comunicación eficiente con bajo consumo  

---

## Arquitectura de un Sistema de Monitoreo en Tiempo Real  

Un esquema típico de **SoC + MQTT** incluye:  

1. **Sensores físicos** (temperatura, humedad, presión, acelerómetros, etc.)  
2. **SoC embebido** (ej. ESP32, STM32, Jetson Nano) que procesa los datos y actúa como **publisher**  
3. **Broker MQTT** (ej. Mosquitto, HiveMQ) que gestiona la comunicación  
4. **Clientes suscriptores**: aplicaciones móviles, dashboards en la nube, sistemas de control industrial  

---

### Tabla comparativa de SoC con soporte MQTT  

| SoC | Comunicación integrada | Consumo | Capacidad de procesamiento | Aplicaciones típicas |
|-----|------------------------|---------|---------------------------|----------------------|
| ESP32 | Wi-Fi, Bluetooth | Muy bajo | Doble núcleo, eficiente | IoT, sensores, domótica |
| STM32 (con módulo Wi-Fi externo) | UART, SPI, I2C | Bajo | ARM Cortex-M | Sensores industriales |
| Raspberry Pi | Ethernet, Wi-Fi | Medio | CPU ARM Cortex-A | Gateways, edge computing |
| NVIDIA Jetson Nano | Ethernet, USB | Alto | GPU para IA | Robótica, análisis avanzado |

💡 Observación: Para sensores simples en IoT, **ESP32** es ideal; para aplicaciones con procesamiento de IA, **Jetson Nano** es preferible.  

---

## Optimización y Seguridad en MQTT + SoC  

Para lograr un monitoreo eficiente en tiempo real:  

- **QoS (Quality of Service) de MQTT**:  
  - QoS 0 → entrega sin confirmación (más rápido, menos confiable)  
  - QoS 1 → entrega garantizada al menos una vez  
  - QoS 2 → entrega garantizada exactamente una vez (más lento, más seguro)  

- **Optimización energética en SoC**:  
  - Uso de **sleep modes** para sensores  
  - Procesamiento local antes de transmitir (edge computing)  
  - Compresión de datos  

- **Seguridad**:  
  - **TLS/SSL** en la conexión MQTT  
  - Autenticación mediante certificados o tokens  
  - Control de acceso en el broker  

---

### Comparación de técnicas de optimización  

| Técnica | Beneficio | Limitación |
|---------|-----------|-----------|
| Sleep mode en SoC | Reduce consumo energético | Latencia al reactivar |
| Edge computing | Menos datos enviados, ahorro de ancho de banda | Mayor complejidad en SoC |
| Compresión de datos | Reduce tamaño de mensajes | Uso extra de CPU |
| TLS/SSL | Seguridad en la comunicación | Aumento de consumo y latencia |

---

## Diagramas Conceptuales  

### Arquitectura típica MQTT + SoC  
```mermaid
flowchart TD
    A[Sensores IoT] --> B[SoC con Cliente MQTT]
    B --> C[Broker MQTT]
    C --> D[Servidor en la Nube]
    D --> E[Dashboard en Tiempo Real]

