# 5G para Microcontroladores

## Datos

**Nombre:** Jorge Joshel Leon Cruz

**Número de control:** 22210772

**Fecha:** 15 de Septiembre del 2025

**Nickname:** JOSHELCRUZ28

---

## Introducción

La conectividad inalámbrica se ha convertido en un factor determinante para la evolución de los sistemas embebidos. Desde la domótica hasta la automatización industrial, la capacidad de los microcontroladores (MCUs) de integrarse en redes rápidas y confiables define el alcance de las aplicaciones modernas. En este contexto, la quinta generación de telecomunicaciones móviles, conocida como 5G, emerge como la tecnología que promete revolucionar la interacción de dispositivos IoT, sensores distribuidos y sistemas críticos en tiempo real.

Mientras que estándares previos como Wi-Fi y LTE ofrecieron conectividad básica, 5G plantea un ecosistema optimizado para la masividad de dispositivos conectados y la reducción drástica de la latencia. Este trabajo explora las bases, arquitectura, características técnicas, retos y aplicaciones del 5G aplicado a microcontroladores.

---

## Bases

**Microcontroladores (MCUs)**

Los microcontroladores son circuitos integrados que incluyen CPU, memoria y periféricos en un único chip. Su función es ejecutar tareas específicas con bajo consumo de energía. Tradicionalmente se conectan mediante buses internos y módulos de comunicación inalámbrica como Wi-Fi, Bluetooth o LoRa.

**5G (Quinta Generación)**

El estándar 5G, definido por la 3GPP (Third Generation Partnership Project), se diseñó para superar las limitaciones de 4G LTE. Sus tres pilares son:

1. **eMBB (Enhanced Mobile Broadband)** → velocidades de hasta 10 Gbps.

2. **URLLC (Ultra-Reliable Low Latency Communication)** → latencias menores a 1 ms.

3. **mMTC (Massive Machine-Type Communication)** → soporte para millones de dispositivos/km².

<img width="623" height="461" alt="image" src="https://github.com/user-attachments/assets/4a29e458-2cda-4360-aa21-36048157075e" />


---

## Arquitectura y características técnicas

**Microcontroladores con 5G**

- **Diseño:** los MCUs no incluyen directamente transceptores 5G, sino que se integran con módulos 5G NR (New Radio) mediante interfaces como UART, SPI o USB.

 **Capas de operación:**

- **Capa Física (PHY):** 
maneja la señalización 5G, frecuencias sub-6 GHz y mmWave.

**Capa MAC/Radio:**
gestionada por el módulo 5G, no por el MCU.

**Interfaz MCU-Módulo:** 
el microcontrolador ejecuta la lógica de aplicación y envía/recibe datos.

<img width="1280" height="460" alt="image" src="https://github.com/user-attachments/assets/88d95b4b-861f-433f-855f-0d168141c87a" />

---

## Características clave del 5G aplicadas a MCUs

- **Velocidad:**
hasta 100× más rápido que LTE.

- **Latencia:**
1–10 ms, permitiendo control en tiempo real.

- **Confiabilidad:**
protocolos URLLC garantizan continuidad en aplicaciones críticas.

- **Escalabilidad:**
millones de dispositivos pueden coexistir en un área reducida.

- **Consumo energético:** 
optimizaciones con 5G RedCap (Reduced Capability) para IoT.

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/a213aace-5bcb-4871-9a25-fd6115345408" />

---

## Rendimiento

- **Ancho de banda:**
microcontroladores con módulos 5G pueden manejar desde Mbps (IoT básico) hasta varios Gbps (aplicaciones multimedia).

- **Latencia:**
inferior a 10 ms, frente a los 30–50 ms de LTE.

- **Conexiones simultáneas:**
hasta 1 millón de nodos/km², frente a ~100,000 en 4G.

- **Movilidad:**
soporte hasta 500 km/h (ej. trenes de alta velocidad).

<img width="921" height="390" alt="image" src="https://github.com/user-attachments/assets/0afc90a1-652f-42a0-ad7f-adaaa60346f5" />


---

## Escalabilidad y compatibilidad

- **Escalabilidad:** 
5G permite integrar desde sensores simples (mMTC) hasta controladores industriales complejos (URLLC).

- **Compatibilidad:** 
retrocompatible con 4G LTE mediante dual-mode modules.

- **Topologías posibles:**

1. Redes celulares masivas.

2. Redes privadas 5G para fábricas y hospitales.

<img width="600" height="273" alt="image" src="https://github.com/user-attachments/assets/3277cd34-276e-4d2f-9150-73147a006526" />

---

## Facilidad de implementación y diseño

- **Complejidad:**

- Alta en el módulo 5G (maneja pilas de red, protocolos, PHY).

- Moderada en el microcontrolador (solo gestiona lógica y datos).

- **Flujo de diseño típico:**

- MCU → comunica por UART/SPI → Módulo 5G.

- Módulo 5G → accede a red 5G NR → Operador/Cloud.

- **Ejemplos comerciales:**

- **Quectel RG500Q:** módulo 5G NR para IoT industrial.

- **u-blox 5G modules:** integración para MCUs de bajo consumo.

- **Arduino + Shield 5G** (prototipado académico).

<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/579fdc42-08b9-429b-8315-a58cbdce75b2" />

---

## Aplicaciones típicas

- **IoT masivo:** sensores de agricultura inteligente transmitiendo datos ambientales.

- **Vehículos autónomos:** comunicación V2X (vehicle-to-everything).

- **Telemedicina:** dispositivos médicos portátiles enviando datos vitales en tiempo real.

- **Fábricas inteligentes:** control de robots industriales con URLLC.

- **Ciudades inteligentes:** semáforos, alumbrado y cámaras conectadas.

---

## Ventajas y limitaciones

**Ventajas**

- Baja latencia crítica (<1 ms).

- Soporte para millones de dispositivos.

- Mayor velocidad de transmisión.

- Confiabilidad para entornos industriales y médicos.

**Limitaciones**

- Costo elevado de módulos 5G.

- Consumo energético aún significativo (aunque RedCap lo reduce).

- Dependencia de infraestructura (no todo el mundo tiene cobertura 5G).

- Complejidad de diseño frente a tecnologías más simples como LoRa o Wi-Fi.


---

| Característica           | 4G LTE                  | 5G aplicado a MCUs                |
| ------------------------ | ----------------------- | --------------------------------- |
| **Velocidad**            | ~100 Mbps               | 1–10 Gbps                         |
| **Latencia**             | 30–50 ms                | 1–10 ms                           |
| **Conexiones/km²**       | ~100,000                | ~1,000,000                        |
| **Consumo**              | Moderado                | Optimizado (5G RedCap)            |
| **Fiabilidad**           | Media                   | Alta (URLLC)                      |
| **Aplicaciones típicas** | Smartphones, IoT básico | IoT masivo, tiempo real, robótica |

---

## Conclusión

La integración de 5G en microcontroladores abre un nuevo horizonte para sistemas embebidos y aplicaciones IoT. Su capacidad para ofrecer alta velocidad, baja latencia y masividad de dispositivos conectados permite abordar casos de uso que antes eran imposibles con 4G o Wi-Fi. Sin embargo, la adopción enfrenta retos relacionados con el costo, consumo y la disponibilidad de infraestructura.

A medida que los módulos 5G RedCap y las redes privadas 5G se masifiquen, los microcontroladores podrán convertirse en nodos críticos de ecosistemas interconectados, consolidando la visión de un mundo plenamente digital e inteligente.

---

## Referencias

- 3GPP. (2020). 5G; NR; Overall description; Stage-2 (Release 16).

- Qualcomm. (2021). 5G and IoT: The Next Evolution.

- u-blox. (2022). 5G Modules for Embedded Systems.

- Quectel Wireless Solutions. (2021). 5G Modules Portfolio.

- Ericsson. (2020). 5G for Industries.

- ITU-R. (2017). Minimum requirements related to technical performance for IMT-2020 radio interface(s).

  ---
  
