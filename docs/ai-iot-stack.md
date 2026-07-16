# El AI-IoT-Stack — la innovación del curso 2027

## De dónde venimos

Este curso ha cambiado de fondo en cada ciclo:

1. **Electrónica pura (Arduino):** el foco era el hardware — pines, protocolos, control directo.
2. **IoT-Stack:** el foco se movió a mover datos a escala — MQTT, EdgeX Foundry, InfluxDB, Grafana/Prometheus — con menos énfasis en electrónica y más en el pipeline de datos.
3. **2027 — AI-IoT-Stack:** el mismo pipeline de datos, pero con una capa de inteligencia que decide y razona, no solo que almacena y grafica.

No es una moda: es la misma progresión que está viviendo la industria (edge computing + modelos de lenguaje aplicados a IoT). El curso adopta esa progresión un ciclo antes de que sea "obvia" para que los egresados 2027 lleguen ya con ese criterio.

## Las capas del AI-IoT-Stack

```
┌─────────────────────────────────────────────────────────────┐
│ 6. Visualización y acción                                    │
│    Grafana · Prometheus · ThingsBoard · actuadores            │
├─────────────────────────────────────────────────────────────┤
│ 5. Inteligencia (dos rutas, no excluyentes)                    │
│    ├─ Edge AI / TinyML → inferencia local, sin salir del chip  │
│    └─ Orquestación con LLM → razonamiento, lenguaje natural,    │
│       decisiones contextuales vía API (ChatGPT, Claude, etc.)  │
├─────────────────────────────────────────────────────────────┤
│ 4. Persistencia                                                │
│    InfluxDB (series temporales)                                │
├─────────────────────────────────────────────────────────────┤
│ 3. Mensajería                                                  │
│    MQTT (Mosquitto/EMQX) · EdgeX Foundry                       │
├─────────────────────────────────────────────────────────────┤
│ 2. Conectividad                                                │
│    UART/SPI/I²C · WiFi/BT · LoRaWAN (bajo consumo)             │
├─────────────────────────────────────────────────────────────┤
│ 1. Percepción                                                  │
│    Sensores y actuadores (temperatura, movimiento, MEMS, etc.)  │
└─────────────────────────────────────────────────────────────┘
```

La diferencia clave frente al IoT-Stack "clásico" está en la **capa 5**: en vez de que el dato solo llegue a un dashboard para que una persona lo interprete, el sistema mismo puede:

- Clasificar o detectar anomalías **en el borde** (TinyML), sin depender de la nube ni de conectividad constante.
- Consultar un **LLM** para traducir un estado técnico ("temp=38.4, humedad=22%, tendencia+") en una recomendación en lenguaje natural, o para generar documentación/alertas automáticamente.

## Mapeo a las unidades del curso

| Capa del stack | Unidad | Dónde vive el material |
|---|---|---|
| Percepción, conectividad básica | U01–U02 | `class-material/u1`, `u2` |
| Mensajería | U02 | `class-material/u2` (MQTT, EdgeX) |
| Persistencia y visualización | U03 | `class-material/u3` |
| Conectividad avanzada + orquestación con LLM | U04 | `class-material/u4` |
| Edge AI / TinyML + seguridad | U05 | `class-material/u5` |
| Stack completo integrado | U06 (proyecto final) | `class-material/u6`, `assignments/proyectos` |

## Precedente ya en el repo

La práctica de `class-material/u3/3.4` (Raspberry Pi Pico W consultando la API de ChatGPT vía HTTP en Wokwi) es la primera semilla de esta capa de inteligencia. U04 la retoma y la formaliza como parte central del stack, no como una demo aislada.

## Estado

Esta es la primera versión del concepto (ciclo 2027). Conforme se generen las prácticas de U04/U05, este documento se actualiza para reflejar ejemplos concretos, diagramas de referencia por proyecto y la rúbrica del proyecto integrador que exija demostrar al menos una capa de inteligencia (Edge AI o LLM) funcionando sobre el resto del stack.
