# Instituto Tecnológico de Tijuana  

**Nombre:** Pozos Flores Norberto  
**Matrícula:** 22210336  
**Escuela:** Instituto Tecnológico de Tijuana  
**Docente:** Rene Reyes  
**Materia:** Sistemas Programables  
**Tema:** Uso de MQTT con RISC-V: Integración en Hardware Libre  

---

#  Uso de MQTT con RISC-V: Integración en Hardware Libre

## 🔹 Introducción
En el ámbito del **Internet de las Cosas (IoT)**, la comunicación eficiente entre dispositivos es esencial.  
El protocolo **MQTT (Message Queuing Telemetry Transport)** se ha convertido en un estándar para transmitir datos en entornos con recursos limitados, gracias a su **ligereza y bajo consumo de ancho de banda**.  

Por otra parte, la arquitectura **RISC-V** representa un estándar abierto y libre de licencias para el diseño de procesadores, lo que permite a fabricantes, investigadores y comunidades desarrollar soluciones de **hardware libre y personalizable**.  

La integración de **MQTT sobre procesadores RISC-V** en plataformas de hardware libre abre la puerta a sistemas IoT **económicos, escalables y flexibles**.

---

## 🔹 Antecedentes

### MQTT
- Creado en 1999 por IBM para sistemas SCADA y telemetría industrial.  
- Basado en arquitectura **publish/subscribe** (publicador/suscriptor) con un **broker** que centraliza los mensajes.  
- Usado en aplicaciones de domótica, industria 4.0, sensores remotos y redes de bajo consumo energético.  

### RISC-V
- Iniciado en 2010 en la Universidad de California, Berkeley.  
- Arquitectura **RISC (Reduced Instruction Set Computer)** de código abierto.  
- Permite implementar procesadores **personalizados sin restricciones de patentes**.  
- Utilizado en microcontroladores, SoCs (System on Chip), e incluso sistemas de alto rendimiento.  

---

## 🔹 Integración de MQTT con RISC-V
El uso de **MQTT sobre plataformas RISC-V** permite implementar nodos IoT que cumplan con los principios de **hardware libre**.  
La integración se realiza principalmente de dos maneras:

1. **En microcontroladores RISC-V**  
   - Se portan librerías de MQTT ligeras (ejemplo: **Eclipse Paho MQTT C**, **MQTT-C lightweight client**, o implementaciones en **FreeRTOS**).  
   - Los microcontroladores RISC-V pueden ejecutar firmware que conecte sensores y publique datos hacia un **broker MQTT**.  

2. **En SoCs RISC-V con Linux**  
   - Sistemas RISC-V más completos (como **HiFive Unmatched** o placas similares) pueden ejecutar un **broker MQTT** (ej. **Mosquitto**).  
   - Estos dispositivos actúan como servidores IoT, gestionando múltiples nodos sensores.  

---

## 🔹 Ejemplo de Flujo de Comunicación
1. Un sensor de temperatura basado en un **microcontrolador RISC-V** mide datos y los envía con **MQTT Publish** al tópico `sensor/temperatura`.  
2. El **broker MQTT** (que puede ejecutarse en otro RISC-V, Raspberry Pi, o servidor en la nube) recibe el mensaje.  
3. Otro nodo IoT o aplicación suscrita al tópico (`MQTT Subscribe`) obtiene los datos en tiempo real.  

---

## 🔹 Beneficios de la integración
- **Hardware libre**: RISC-V elimina las dependencias de licencias propietarias.  
- **Eficiencia energética**: tanto RISC-V como MQTT están optimizados para entornos de bajo consumo.  
- **Escalabilidad**: permite construir redes de sensores IoT de manera modular.  
- **Flexibilidad**: posibilidad de adaptar procesadores RISC-V al caso de uso específico (sensores, gateways, servidores IoT).  
- **Comunidad abierta**: tanto RISC-V como MQTT tienen un ecosistema abierto y respaldado por comunidades globales.  

---

## 🔹 Desafíos
- **Madurez del ecosistema RISC-V** frente a ARM o x86.  
- **Compatibilidad de librerías MQTT**: no todas están optimizadas para RISC-V.  
- **Herramientas de desarrollo** aún en evolución.  

---

## 🔹 Aplicaciones
- Redes de sensores ambientales con microcontroladores RISC-V.  
- Sistemas de domótica con hardware libre.  
- Dispositivos médicos IoT de bajo costo.  
- Monitoreo industrial con nodos distribuidos basados en RISC-V.  
- Gateways IoT libres (ejecutando Mosquitto o HiveMQ en SoCs RISC-V).  

---

##  Conclusiones
La combinación de **MQTT y RISC-V** potencia el desarrollo de soluciones IoT bajo el paradigma de **hardware libre**,  
ofreciendo una alternativa abierta, económica y eficiente frente a plataformas propietarias.  

A medida que el ecosistema RISC-V crece, se espera que surjan más librerías y soporte para protocolos IoT,  
impulsando la adopción de **infraestructuras libres y modulares** en proyectos de domótica, industria y ciudades inteligentes.

---
