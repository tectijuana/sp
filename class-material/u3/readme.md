# U03 — Persistencia y visualización de datos

Esta unidad cubre la capa de **persistencia y visualización** del [AI-IoT-Stack](../../docs/ai-iot-stack.md): las lecturas que en U02 viajaron por MQTT ahora se almacenan como series temporales y se presentan en dashboards para su monitoreo y análisis.

---

## Contenido de la unidad

| Subtema | Material | Tema |
|---|---|---|
| 3.1 | [`3.1/`](./3.1/readme.md) | Bases de datos de series temporales con **InfluxDB** |
| 3.2 | [`3.2/`](./3.2/readme.md) | Dashboards y monitoreo con **Grafana** y **Prometheus** |
| 3.3 | [`3.3/`](./3.3/readme.md) | **ThingsBoard** como plataforma IoT open source todo-en-uno |
| 3.4 | [`3.4/`](./3.4/readme.md) | Práctica: Raspberry Pi Pico W consultando la API de ChatGPT (semilla de la capa de inteligencia — se formaliza en U04) |

## Lectura complementaria

- [El valor económico del software de código abierto](./lectura-valor-economico-oss.md) — por qué el stack del curso (Mosquitto, InfluxDB, Grafana, ThingsBoard) se apoya en OSS.

## Prácticas relacionadas

- [`assignments/u1/4-influxdb`](../../assignments/u1/4-influxdb/readme.md) — instalación y carga de datos en InfluxDB
- [`assignments/u1/5-grafana`](../../assignments/u1/5-grafana/readme.md) — instalación de Grafana en AWS (Ubuntu)
- [`assignments/u1/6-prometeus`](../../assignments/u1/6-prometeus/readme.md) — instalación de Prometheus en AWS (Ubuntu)
- [`assignments/u3/`](../../assignments/u3/readme.md) — prácticas propias de la unidad (micro:bit → IoT Stack, flespi)

## Tipos de dashboards (temario 2027)

Al diseñar la visualización del proyecto, identificar qué tipo de dashboard se está construyendo:

- **Estratégico** — indicadores agregados para decisiones de largo plazo
- **Táctico** — seguimiento de procesos y tendencias por área
- **Operacional** — estado en tiempo (casi) real; el más común en IoT
- **Informativo** — comunicación de datos a audiencias generales
