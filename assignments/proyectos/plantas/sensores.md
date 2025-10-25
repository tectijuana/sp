
## 📋 **Cuestionario: Sensores y Electrónica en el Mundo Real (Aplicado a la Práctica PlantCare Pro)**

---

### 🔌 **Sección 1: Selección de Sensores y Electrónica (20 pts)**

1. **¿Qué principio físico permite a un sensor LDR medir la intensidad de luz?**

   * a) Capacitancia variable
   * b) Conductividad óptica
   * c) Resistencia dependiente de la luz
   * d) Efecto piezoeléctrico

2. El sensor **MQ135** simulado mediante potenciómetro en Wokwi mide:

   * a) Monóxido de carbono
   * b) Humedad relativa
   * c) Temperatura ambiente
   * d) Intensidad de luz

3. ¿Qué tipo de sensor sería más adecuado si se quisiera medir el **nivel real** de agua (no solo binario) con precisión en un tanque vertical?

   * a) Sensor de nivel resistivo con electrodos
   * b) Sensor capacitivo de nivel
   * c) Sensor ultrasónico
   * d) Sensor digital de nivel ON/OFF

4. ¿Cuál de los siguientes sensores requiere **calibración previa al uso** para valores confiables en el mundo real?

   * a) LDR
   * b) DHT22
   * c) MQ135
   * d) Sensor de nivel digital

---

### 📊 **Sección 2: Análisis de Datos Sensoriales (20 pts)**

5. Si se reciben los siguientes datos:

```json
{
  "soil": null,
  "temp": 82,
  "light": 820,
  "air": 710,
  "water": 0
}
```

¿Cuál(es) sería(n) los comportamientos esperados del dashboard?

* a) Marcar temperatura como alerta crítica
* b) Ocultar la tarjeta de humedad del suelo por falta de datos
* c) Activar riego automático
* d) Mostrar mensaje de sensor desconectado en humedad del suelo

6. ¿Qué estrategia puede aplicarse para evitar la publicación excesiva de datos hacia Flespi desde el dispositivo?

* a) Aumentar el sampling rate a 1s
* b) Publicar solo si hay un delta significativo respecto al valor anterior
* c) Publicar todo en JSON con un solo tópico
* d) Usar interrupciones en lugar de polling

---

### 🏗️ **Sección 3: Arquitectura y Comunicación IoT (20 pts)**

7. ¿Qué característica hace que **Flespi** sea útil para este tipo de proyectos?

* a) Es un servidor web embebido
* b) Permite crear reglas y flujos sin código
* c) Ofrece token de autenticación para control seguro de acceso MQTT
* d) Transforma JSON en HTML automáticamente

8. ¿Cuál sería una arquitectura óptima si se quiere escalar el sistema a 100 macetas reales en un jardín con monitoreo externo?

* a) MQTT local con Raspberry Pi como broker
* b) MQTT → Backend Flask → WebSocket a Dashboard
* c) Bluetooth LE directo al navegador
* d) Dashboard que accede a sensores con HTTP polling

---

### ⚙️ **Sección 4: Fallas, Anomalías y Edge Computing (15 pts)**

9. Si el sensor de temperatura muestra esporádicamente **80 °C** sin razón aparente, ¿cómo debería manejar el sistema esta lectura?

* a) Enviarla como está
* b) Descartarla y registrar como fallo
* c) Aplicar media móvil para suavizar
* d) Desconectar MQTT

10. ¿Qué beneficio ofrece usar lógica de publicación condicional en el Pico W (edge computing)?

* a) Menor latencia en la red local
* b) Reducción del consumo energético y ancho de banda
* c) Mejora en el renderizado del dashboard
* d) Aumento de la velocidad de WiFi

---

### 🧠 **Sección 5: Razonamiento y Creatividad (Opcional – 5 pts extra)**

11. Propón una modificación al sistema actual que permita incluir un sensor adicional (por ejemplo, **pH del suelo**) considerando:

* Limitación de pines
* Ancho de banda
* Representación visual en el dashboard

*(Respuesta abierta – se evalúa creatividad + justificación técnica)*
