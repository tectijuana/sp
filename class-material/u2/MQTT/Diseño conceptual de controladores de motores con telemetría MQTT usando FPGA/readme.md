# Diseño Conceptual de Controladores de Motores con Telemetría MQTT usando FPGA

##  Información del Proyecto
- **Alumno:** Hernández Limón Edwin Yair
- **Número de Control:** 22211580
- **Institución:** Instituto Tecnológico de Tijuana
- **Carrera:** Ingeniería en Sistemas Computacionales
- **Materia:** Sistemas Programables
- **Semestre:** 7°
- **Fecha:** 30 Septiembre 2024

##  Introducción

En la era de la Industria 4.0 y el Internet de las Cosas (IoT), la integración de sistemas de control tradicionales con tecnologías de comunicación modernas se ha vuelto fundamental. Las FPGAs (Field-Programmable Gate Arrays) ofrecen un potencial único para implementar sistemas de control de motores de alto rendimiento, mientras que el protocolo MQTT (Message Queuing Telemetry Transport) proporciona un mecanismo eficiente para la comunicación machine-to-machine en entornos IoT.

Este documento presenta el diseño conceptual de un sistema integrado que combina la potencia de procesamiento paralelo de las FPGAs con la flexibilidad de comunicación del protocolo MQTT, permitiendo el monitoreo remoto y control en tiempo real de sistemas motrices con capacidades avanzadas de telemetría.

### Ejemplo de Arquitectura Detallada

La siguiente imagen muestra una arquitectura detallada de un sistema de control con FPGA e integración IoT como referencia visual para el diseño conceptual:

![Arquitectura Detallada del Sistema](http://www.fii.gob.ve/wp-content/uploads/2020/08/Fig.-3.-Arquitectura-Detallada.jpg)


##  Objetivos del Diseño

### Objetivo Principal
Diseñar arquitectura conceptual para sistema de control de motores basado en FPGA con capacidades de telemetría MQTT, orientado a aplicaciones industriales IoT.

### Objetivos Específicos
- Definir arquitectura modular del sistema FPGA-MQTT
- Especificar componentes hardware y software requeridos
- Establecer protocolos de comunicación e interfaces
- Definir esquemas de seguridad y confiabilidad
- Proponer métricas de evaluación de performance

##  Arquitectura del Sistema

### Visión General del Sistema
El sistema propuesto consiste en tres capas principales: 
1. **Capa de Control Local:** Implementada en FPGA para control en tiempo real
2. **Capa de Comunicación:** Protocolos MQTT sobre TCP/IP
3. **Capa de Aplicación:** Interfaces de usuario y sistemas supervisores

##  Componentes del Sistema

###  Hardware

| Componente                  | Función                                         |
|-----------------------------|-------------------------------------------------|
| FPGA (e.g. Cyclone IV)      | Control lógico y procesamiento embebido         |
| Nios II (Softcore)          | Gestión del stack MQTT y configuración          |
| Módulo PWM                  | Generación de señales para el motor             |
| ADC / Interfaces de Sensores| Adquisición de datos físicos                    |
| Controlador Ethernet        | Comunicación con red local/internet             |
| Driver H-Bridge             | Control de potencia del motor                   |
| Sensores (temp, corriente)  | Lectura de parámetros físicos                   |

###  Software

| Software                    | Función                                         |
|-----------------------------|-------------------------------------------------|
| HDL (VHDL/Verilog)          | Control lógico, PWM, lectura de sensores        |
| Código C embebido           | Implementación del cliente MQTT                 |
| Servidor MQTT (Mosquitto)   | Broker de mensajes entre dispositivos           |
| Dashboard Web/App SCADA     | Visualización y control remoto                  |

---

##  Seguridad y Confiabilidad

-  **Cifrado de datos:** Uso de TLS para proteger la comunicación MQTT.
-  **Autenticación:** Uso de usuarios y contraseñas para acceso seguro al broker.
-  **Reintentos y QoS:** Uso de QoS 1 o 2 en MQTT para asegurar entrega de datos.
-  **Watchdog FPGA:** Reinicio del sistema en caso de bloqueos o errores graves.

---

##  Métricas de Evaluación Propuesta

| Métrica                     | Objetivo                                        |
|-----------------------------|-------------------------------------------------|
| Latencia de respuesta       | < 100 ms para telemetría y control              |
| Uptime del sistema          | ≥ 99.5% (alta disponibilidad)                  |
| Precisión de PWM            | ±1% respecto al valor esperado                  |
| Consumo energético          | < 5W (sistema completo en operación)            |

---

##  Aplicaciones Potenciales

- Control de motores en entornos industriales con monitoreo remoto.
- Automatización de procesos en fábricas inteligentes (*Smart Factories*).
- Vehículos autónomos o robots industriales.
- Sistemas embebidos educativos con integración IoT.
- Invernaderos automatizados con monitoreo remoto.

---

##  Conclusión

El diseño conceptual desarrollado en este proyecto demuestra cómo las tecnologías FPGA y MQTT pueden integrarse para crear sistemas de control de motores eficientes, escalables y conectados. Aunque no se aborda la implementación completa, se establecen las bases necesarias para llevar a cabo un desarrollo funcional que aproveche las ventajas de la computación embebida en hardware y la conectividad IoT en aplicaciones industriales o educativas.

---

##  Referencias

1. Ramos Tomas, Rondón Hermes, Speranza Armando, & Arellano Miguel. (s. f.). Desarrollo de un sistema de adquisición de imágenes controlado por FPGA. Fundación Instituto de Ingeniería para Investigación y Desarrollo Tecnológico. Recuperado de https://www.fii.gob.ve/desarrollo-de-un-sistema-de-adquisicion-de-imagenes-controlado-por-fpga/?print=print 
2. Intel (Altera). (2020). Nios II processor reference handbook. https://www.intel.com/content/www/us/en/docs/programmable/683000/21-3/introduction.html
3. OASIS. (2014). MQTT version 3.1.1 specification. https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html
4. Roth, C. H., & John, L. K. (2008). Diseño digital con VHDL (2ª ed.). Cengage Learning.
5. Pellerin, D., & Thibault, S. (2005). Practical FPGA programming in C. Prentice Hall PTR.
6. TechTarget. (2021). IoT protocols comparison: MQTT, CoAP, AMQP and more. https://www.techtarget.com/iotagenda/tip/IoT-protocols-comparison-MQTT-CoAP-AMQP-and-more

### Diagrama de Bloques Conceptual

```mermaid
graph TB
    subgraph FPGA [Sistema en FPGA]
        A[Controlador Motor Principal]
        B[Módulo Generador PWM]
        C[Interface Sensores]
        D[Procesador Nios II]
        E[Controlador Ethernet]
        F[Módulo MQTT Client]
        
        A --> B
        C --> A
        D --> A
        D --> F
        F --> E
        D -->|Configuración| B
    end
    
    subgraph NETWORK [Infraestructura de Red]
        G[Switch Ethernet]
        H[Broker MQTT]
        I[Servidor Cloud]
        
        E --> G
        G --> H
        H --> I
    end
    
    subgraph CLIENTS [Clientes y Aplicaciones]
        J[Dashboard Web]
        K[Aplicación Móvil]
        L[Sistema SCADA]
        M[API REST]
        
        I --> J
        I --> K
        I --> L
        I --> M
    end
    
    subgraph HARDWARE [Hardware de Potencia]
        N[Driver Puente H]
        O[Motor DC/Paso a Paso]
        P[Sensores]
        Q[Alimentación]
        
        B --> N
        N --> O
        P --> C
        Q --> N
        Q --> O
    end
    
    style FPGA fill:#e1f5fe
    style NETWORK fill:#f3e5f5
    style CLIENTS fill:#e8f5e8
    style HARDWARE fill:#fff3e0
