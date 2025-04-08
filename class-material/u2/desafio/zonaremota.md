
# 🌍 Desafío: *Estación IoT de Monitoreo Ambiental en Zona Remota*

<p align="center">
  <img width="551" alt="Screenshot 2025-04-07 at 2 20 12 p m" src="https://github.com/user-attachments/assets/6bb7ab15-1199-4869-810a-ccd4fc0c7f37" />
</p>

**Contexto:**
Una ONG ambientalista quiere instalar estaciones de monitoreo en una reserva natural de difícil acceso (bosques montañosos). Las estaciones deben medir:

- Temperatura 🌡️  
- Humedad relativa 💧  
- Niveles de CO₂ 🌫️  
- Humedad del suelo 🌱  

---

### 🎯 Requisitos clave:
- **Totalmente autónomas** (alimentación solar)
- **Conectividad solo por LoRaWAN**
- Los datos deben ser enviados cada 30 min y agregados en una estación base.
- La estación base sube datos a la nube vía **4G LTE o WiFi satelital**.
- El sistema debe detectar fallos de sensores o baja batería.

---

### 🧩 Tu reto:
1. Elige sensores específicos y justifica por qué (bajo consumo, precisión, etc).
2. Diseña el nodo IoT (Pico W o similar) y cómo se conecta a LoRaWAN.
3. Describe cómo se almacenan los datos localmente si no hay señal.
4. Diseña la arquitectura desde nodo → estación base → nube.
5. Propon una forma de visualizar todo (ej: Grafana en EC2 con InfluxDB).

---

¿Te atreves a resolver este reto de naturaleza conectada? 🌿  
