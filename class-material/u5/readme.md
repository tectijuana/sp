# U05 — Edge AI, seguridad y eficiencia

Esta unidad cubre la **otra ruta de la capa de inteligencia** del [AI-IoT-Stack](../../docs/ai-iot-stack.md): mientras U04 llevó el razonamiento a la nube (LLM vía API), aquí la inferencia ocurre **dentro del microcontrolador**, sin depender de conectividad.

---

## 5.1 ¿Por qué inteligencia en el borde?

La ruta LLM de U04 tiene tres costos que a veces son inaceptables:

| Costo | Ejemplo donde falla la nube |
|---|---|
| **Latencia** (cientos de ms a segundos) | Detectar una vibración anómala en un motor antes de que se dañe |
| **Conectividad** | Estación agrícola remota con LoRaWAN que transmite unas cuantas veces por hora |
| **Privacidad/costo** | Sensor biométrico que no debe enviar datos crudos a terceros; miles de llamadas API al día |

**Edge AI / TinyML** resuelve los tres: un modelo de ML comprimido (KBs, no GBs) corre en el propio chip y solo se comunica cuando hay algo que reportar. El dato crudo muere en el borde; lo que viaja por MQTT es la *conclusión* ("anomalía detectada", "clase: persona"), no la señal completa.

**Regla de diseño del curso:** decisión rápida y repetitiva → borde (TinyML). Razonamiento contextual y lenguaje natural → nube (LLM, U04). Los buenos proyectos usan ambas.

---

## 5.2 Flujo de trabajo TinyML

```
1. Capturar datos     → el propio sensor del proyecto (acelerómetro, micrófono, temp)
2. Entrenar modelo    → en PC o nube (Edge Impulse, TensorFlow)
3. Comprimir          → cuantización a int8, poda (el modelo pasa de MB a KB)
4. Desplegar al chip  → TensorFlow Lite Micro (C++) o firmware generado por Edge Impulse
5. Inferir localmente → el microcontrolador clasifica en tiempo real
6. Publicar resultado → solo la conclusión sale por MQTT al resto del stack
```

**Herramientas del curso:**

- [Edge Impulse](https://edgeimpulse.com/) — pipeline completo en el navegador (captura, entrenamiento, despliegue); tiene plan gratuito para estudiantes y exporta firmware para ESP32 y RP Pico. Es la vía recomendada para las prácticas.
- [TensorFlow Lite Micro](https://www.tensorflow.org/lite/microcontrollers) — la librería de inferencia subyacente, para quien quiera ver qué hay debajo.

**Casos típicos alcanzables en un semestre:**

- Detección de anomalías en vibración (acelerómetro MEMS — conecta con `class-material/u2/sensores`)
- Reconocimiento de palabras clave por voz ("enciende", "apaga")
- Clasificación de gestos con IMU
- Detección de presencia/conteo con sensor de bajo costo

---

## 5.3 Seguridad en el AI-IoT-Stack

Al agregar capas de inteligencia, la superficie de ataque crece. Mínimos del curso:

- **Transporte:** MQTT sobre TLS; nunca broker abierto sin autenticación en un despliegue real (ver material de seguridad MQTT en `class-material/u2/MQTT`).
- **Secretos:** API keys y credenciales fuera del repositorio — `secrets.py` en `.gitignore` o variables de entorno. Una key filtrada en un repo público se explota en minutos.
- **El LLM no toca el control crítico:** los umbrales de seguridad (sobretemperatura, sobrecorriente) se resuelven con lógica local determinista. La IA recomienda; el `if` protege.
- **Datos personales:** si el sensor captura voz, imagen o biometría, la inferencia en el borde es también una decisión de privacidad — es preferible publicar la clase inferida y no el dato crudo.

---

## 5.4 Eficiencia energética

- La inferencia local consume energía de cómputo pero **ahorra energía de radio** — transmitir es típicamente más caro que computar. Medirlo es parte de la práctica.
- Ciclos de sueño profundo (deep sleep) entre inferencias; el modelo despierta al chip solo ante eventos.
- LoRaWAN + TinyML es la combinación natural para nodos remotos: meses de batería publicando solo conclusiones.

---

## 5.5 Práctica sugerida

Con Edge Impulse, entrena un clasificador sobre datos de un sensor de tu elección (vibración, sonido o gesto), despliégalo a un ESP32/RP Pico, y publica **solo la clase inferida** por MQTT hacia el dashboard del curso (Grafana/ThingsBoard). Documenta: tamaño del modelo, latencia de inferencia, y comparación de tráfico de red contra enviar el dato crudo.

Ver rúbrica general de prácticas en [GRADING.md](../../GRADING.md).
