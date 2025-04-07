

# 🔌 Desafío: *Sistema de monitoreo y optimización de consumo eléctrico en edificio de oficinas*

<p align="center">
<img width="716" alt="Screenshot 2025-04-07 at 2 18 19 p m" src="https://github.com/user-attachments/assets/758ae9b3-13bc-42f3-aa64-4947c5770453" />
/p>

**Situación:**
Un edificio corporativo de 5 pisos busca reducir su factura eléctrica y detectar anomalías en el consumo (equipos encendidos fuera de horario, sobrecargas, picos de consumo en HVAC, etc). Ya cuentan con una red interna (LAN y WiFi), y quieren implementar una solución **IoT local + cloud** que les permita:

- Ver el consumo de energía en **tiempo real** por planta y por equipo (al menos HVAC e iluminación)
- Generar **alertas automáticas**
- Crear **reportes semanales de eficiencia energética**
- Apagar remotamente dispositivos no críticos en horarios no laborables

---

### 📦 Equipamiento disponible:
- Smart meters Modbus TCP
- Relés de corte remoto
- Medidores de corriente tipo clamp sensor (sensor de efecto Hall o SCT-013)
- Microcontroladores ESP32 y Raspberry Pi 4
- Acceso a servidores Linux (Ubuntu) o cloud EC2

---

### ⚠️ Restricciones:
- No se permite subir datos continuamente al cloud (solo cada 15 min).
- El procesamiento local debe filtrar datos y detectar anomalías.
- Debes usar **software open source** para la visualización.
- Múltiples equipos pueden conectarse por **Modbus TCP o UART**.

---

### 🎯 Tu reto:
1. Diseña la arquitectura completa (IoT Edge + Cloud).
2. ¿Qué sensores y protocolos usarías para cada zona?
3. ¿Qué lógica local implementarías para:
   - calcular consumo horario/día
   - detectar anormalidades?
4. ¿Qué stack usarías para visualizar (ej: Node-RED, InfluxDB, Grafana)?

---

¿Listo para proponer la solución?  
