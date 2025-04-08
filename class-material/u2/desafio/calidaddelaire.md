
### 🚦 Desafío: *Monitor de calidad del aire en una ciudad con zonas escolares y tráfico denso*

<p align="center">
  <img width="608" alt="Screenshot 2025-04-07 at 2 15 37 p m" src="https://github.com/user-attachments/assets/12257e83-00bc-4076-8c9c-c5a5579552a5" />
</p>


**Situación:**
El municipio quiere implementar sensores de calidad del aire en zonas escolares, ya que se ha detectado un aumento en enfermedades respiratorias en niños. Quieren tener datos de:

- Dióxido de nitrógeno (NO₂)  
- Monóxido de carbono (CO)  
- Material particulado PM2.5  
- Temperatura y humedad (para correlación climática)

Y deben colocarse **cerca del tráfico**, **en postes de luz** y **fuera de las escuelas**. Se requiere una solución que:

- Sea **de bajo mantenimiento**
- Funcione con **energía solar o de farola**
- **Almacene datos localmente** y los **suba cada hora** a la nube
- Permita visualización en **Grafana** y generación de alertas por umbrales

---

### ⚠️ Restricciones:
- Comunicación limitada a **WiFi de la escuela** o **LoRaWAN municipal**.
- Requiere caja resistente IP65.
- Necesita detectar **lecturas anómalas** (picos falsos o valores faltantes).

---

### 🎯 Tus objetivos:
1. **Selecciona los sensores** apropiados para medir esos gases y partículas.
2. Elige un **microcontrolador** (ESP32, Pico W, etc.) y justifica tu elección.
3. Diseña la **arquitectura de comunicación** (LoRa, MQTT, etc.).
4. Establece cómo vas a procesar los datos antes de enviarlos.
5. Propón la visualización y alertado (usa open source si puedes: Grafana + InfluxDB o Prometheus).

---

### ¿Listo para comenzar?
Escríbeme tu propuesta de solución o dime “💡 dame una pista” para ayudarte paso a paso. ¿Cómo enfrentarías este reto de ciudad inteligente? 🏙️🌫️📊
