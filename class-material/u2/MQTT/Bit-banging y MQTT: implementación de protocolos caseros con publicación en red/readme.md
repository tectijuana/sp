# Investigación extendida: **Bit-banging y MQTT**
> Implementación de protocolos caseros con publicación en red  
> Documento técnico robusto con fuentes y referencias

---

## 1. Introducción

En el contexto del **IoT (Internet of Things)** y la **automatización industrial**, existen situaciones donde los dispositivos deben comunicarse usando protocolos muy específicos, no soportados por los periféricos estándar (UART, SPI, I²C). En esos casos puede emplearse **bit-banging**, técnica que permite **generar o leer protocolos digitales mediante software**, controlando directamente los GPIOs.

Una vez decodificada la información, ésta puede integrarse a redes modernas a través de **MQTT**, un protocolo de mensajería ligero y basado en el modelo **publish/subscribe**, ampliamente adoptado en IoT e IIoT.

---

## 2. Bit-banging: fundamentos teóricos

### 2.1 Definición
Bit-banging es una técnica de control software que permite a un microcontrolador **emular protocolos de comunicación** transmitiendo y recibiendo bits directamente a través de GPIOs, en vez de usar controladores hardware dedicados (UART, SPI, I²C, CAN).

### 2.2 Características
- Se implementa en el **firmware** del microcontrolador.  
- Controla directamente el estado lógico de los pines de entrada/salida.  
- Requiere precisión en **temporización** (delays en µs).  
- Puede trabajar con **cualquier tipo de protocolo serial síncrono o asíncrono**.

### 2.3 Ventajas
- Flexibilidad para protocolos propietarios.  
- Útil cuando el hardware no ofrece suficientes periféricos.  
- Permite prototipado rápido y validación de ideas.  

### 2.4 Desventajas
- **Ineficiencia en CPU**: consume muchos ciclos.  
- **Limitación de velocidad**: difícil superar los 115,200 bps en MCUs pequeños.  
- **Susceptible a jitter** (interrupciones, multitarea).  
- Menor fiabilidad frente a periféricos dedicados.  

### 2.5 Casos de uso reales
- Conectar sensores antiguos sin interfaz estándar.  
- Emulación de buses simples (ej. **1-Wire** o protocolos IR).  
- Bootloaders minimalistas sin hardware UART.  
- Implementación de **prototipos rápidos**.

**Fuente:**  
- Barr Group – *Bit-Banging vs Hardware Communication*  
- Microchip – *AVR UART Emulation with Software*  

---

## 3. Diseño de protocolos caseros

### 3.1 Elementos básicos de una trama
Un protocolo casero necesita:
1. **Preamble/SYNC** → secuencia conocida para sincronizar (ej. `0xAA 0x55`).  
2. **Header** → versión, longitud, tipo de mensaje.  
3. **Payload** → datos del sensor/dispositivo.  
4. **Checksum o CRC** → para verificar integridad.  
5. **End delimiter** (opcional).  

### 3.2 Ejemplo de trama robusta

### 3.3 Métodos de integridad
- **Checksum simple**: suma de bytes mod 256.  
- **CRC-8/16/32**: más robusto, detecta ráfagas de errores.  
- **Hamming code**: útil para detección y corrección en medios muy ruidosos.  

### 3.4 Estrategias de retransmisión
- **ACK/NACK** con número de secuencia.  
- **Backoff exponencial** para evitar congestión.  

**Fuente:**  
- Tanenbaum, *Redes de Computadoras*, Capítulo 2 (protocolos de enlace).  

---

## 4. MQTT: fundamentos

### 4.1 ¿Qué es MQTT?
- Protocolo **publish/subscribe** ligero, sobre TCP/IP.  
- Diseñado en 1999 por IBM para **telemetría en sistemas SCADA**.  
- Optimizado para redes con **ancho de banda limitado y alta latencia**.  

### 4.2 Ventajas
- Bajo consumo de ancho de banda.  
- Semántica pub/sub facilita **desacoplar productores y consumidores**.  
- Soporta **QoS (0,1,2)**.  
- Incluye **retained messages** y **LWT (Last Will Testament)**.  

### 4.3 Limitaciones
- Depende de un broker.  
- Seguridad depende de configuración (usar TLS).  
- QoS alto incrementa latencia y consumo.  

**Fuente:**  
- HiveMQ, *MQTT Essentials eBook*  
- OASIS, *MQTT v3.1.1 Specification*  

---

## 5. Integración Bit-banging + MQTT

### 5.1 Arquitectura típica

- El dispositivo envía datos por protocolo casero (bit-banging).  
- El **gateway** (Arduino+ESP32 o Raspberry Pi) decodifica, valida y publica vía MQTT.  
- El **broker** centraliza la comunicación.  
- Los **clientes** (apps, dashboards, SCADA) se suscriben.  

### 5.2 Ejemplo de flujo
1. Arduino recibe datos vía bit-banging.  
2. Valida CRC y genera JSON.  
3. Publica en topic MQTT `org/site/device/telemetry`.  
4. Cliente Node-RED grafica datos en tiempo real.  

**Fuente:**  
- Sparkplug Essentials, *Integration with MQTT in IIoT*.  

---

## 6. Ejemplos prácticos

### 6.1 Arduino TX bit-banging
```cpp
const int TX = 8;
const int BIT_US = 104; // 9600 bps

void setup(){ pinMode(TX, OUTPUT); digitalWrite(TX,HIGH); }

void sendByte(uint8_t b){
  digitalWrite(TX, LOW); delayMicroseconds(BIT_US); // Start
  for(int i=0;i<8;i++){ digitalWrite(TX, (b&1)?HIGH:LOW); b>>=1; delayMicroseconds(BIT_US); }
  digitalWrite(TX, HIGH); delayMicroseconds(BIT_US); // Stop
}

void loop(){ sendByte(0x55); delay(1000); }
--------------------
import serial, paho.mqtt.client as mqtt, json

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
client = mqtt.Client("pi-gateway")
client.connect("broker.local", 1883, 60)
client.loop_start()

while True:
    line = ser.readline().decode().strip()
    if line:
        payload = {"device":"sensor01","data":line}
        client.publish("factory/sensor01/telemetry", json.dumps(payload), qos=1)
------------------------------------------------------------------------------------------## 7. Seguridad

- **Usar TLS** (puerto `8883`) en MQTT para cifrar el transporte y evitar espionaje o manipulación en tránsito.  
- **Autenticación**: emplear usuario/contraseña fuertes *o*, preferible en entornos sensibles, **certificados X.509 (mutual TLS)** para autenticación de cliente/servidor.  
- **Control de acceso (ACLs)**: implementar reglas en el broker (por ejemplo, Mosquitto, EMQX, HiveMQ) para restringir quién puede publicar o suscribirse a cada topic.  
- **Protección en la capa de enlace**: si las tramas bit-banged atraviesan entornos hostiles, considerar:
  - **HMAC** (firma de mensaje) para autoría e integridad del payload.
  - **Cifrado AES** (por ejemplo AES-GCM) aplicado al payload antes de insertar en la trama (si el MCU lo permite).
- **Buenas prácticas**:
  - Rotación periódica de credenciales y certificados.  
  - Validar la hora del dispositivo (NTP) si se usan certificados X.509.  
  - Limitar puertos y accesos en el firewall; separar el broker en una red protegida o DMZ según necesidad.

## 8. Rendimiento y limitaciones

- **Arduino UNO (digitalWrite)**: confiable típicamente hasta **9.600 bps** en implementaciones por software sin optimización.  
- **Manipulación directa de puertos (direct port I/O)**: permite mayor velocidad — **~38.400 bps** o más, dependiendo del MCU y la optimización.  
- **ESP32 (RMT / periféricos)**: puede manejar tiempos en microsegundos y **bauds mucho más altos** (varios Mbps en función del protocolo y configuración) con baja carga de CPU.  
- **Observación práctica**: el *gargalo* real en sistemas integrados suele ser la **latencia o la disponibilidad de red/broker MQTT**, no necesariamente el bit-banging en sí — especialmente cuando hay un gateway que hace buffering y TLS.
- **Consejos**:
  - Medir siempre en tu plataforma concreta (osciloscopio/analizador lógico).  
  - Si necesitas alta fiabilidad/throughput, usar periféricos hardware (UART/RMT/DMA) en lugar de bit-banging.

**Fuente:** Espressif, *ESP32 Technical Reference Manual*.

## 9. Pruebas y validación

- **Instrumentación física**:
  - Analizador lógico (Saleae, Sigrok) para verificar timing, jitter y estructura de bits.  
  - Osciloscopio para chequear niveles de señal y transitorios.  
- **Validación de red y mensajes**:
  - Wireshark / tcpdump para capturar y analizar tráfico MQTT (asegúrate de poder descifrar TLS si lo necesitas y tienes las claves).  
- **Pruebas funcionales**:
  - Pruebas de estrés: generar miles de tramas con patrones conocidos y validar CRC/ACK.  
  - Inyección de errores controlada para verificar mecanismo de reintento y tolerancia a fallos.  
- **KPIs recomendados**:
  - **BER** (Bit Error Rate).  
  - **PLR** (Packet Loss Rate).  
  - **Latencia end-to-end** (sensor → gateway → broker → suscriptor).  
  - **CPU load** en el MCU/gateway durante operación normal y bajo carga.  
  - **Tasa de reconexión / éxito de reenvío** tras fallos de red.  

## 10. Conclusiones

- **Aplicabilidad**: Bit-banging es una solución válida para **prototipos**, dispositivos legacy o cuando no hay periféricos disponibles.  
- **Producción**: en entornos productivos se recomienda migrar a **periféricos hardware** (UART, SPI, I²C, RMT/DMA) para mayor fiabilidad y menor carga CPU.  
- **Integración con MQTT**: MQTT es una opción adecuada para publicar los datos decodificados (modelo pub/sub, QoS, LWT, retained).  
- **Recomendaciones clave** para un despliegue robusto:
  - Implementar **CRC/Checksum** en la capa bit-banged.  
  - Usar **QoS = 1** en MQTT para equilibrio entre fiabilidad y coste (deduplicar con `seq` si es necesario).  
  - Asegurar el broker (TLS, ACLs, LWT) y disponer de un **gateway** que haga buffering/reintentos si los MCU son limitados.

## 11. Fuentes y referencias

1. Barr Group — *Bit-Banging vs Hardware Communication*  
   <https://barrgroup.com/embedded-systems/how-to/bit-banging>

2. Microchip — *AVR UART Emulation Application Note (AVR305)*  
   <https://ww1.microchip.com/downloads/en/AppNotes/AVR305.pdf>

3. Tanenbaum, A. — *Computer Networks*, 5ª ed. (Cap. 2)

4. HiveMQ — *MQTT Essentials eBook*  
   <https://www.hivemq.com/mqtt-essentials/>

5. OASIS — *MQTT v3.1.1 Specification*  
   <https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/>

6. Cirrus Link — *Sparkplug Essentials for IIoT*  
   <https://cirrus-link.com/sparkplug/>

7. Espressif — *ESP32 Technical Reference Manual*  
   <https://www.espressif.com/en/support/download/documents>
