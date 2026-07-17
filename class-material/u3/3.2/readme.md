# 3.2 — Dashboards y monitoreo: Grafana y Prometheus

Con las lecturas persistidas en InfluxDB (3.1), el siguiente paso del stack es **verlas**: dashboards que conviertan las series temporales en gráficas, medidores y alertas.

## Grafana

**Grafana** es el visualizador estándar del ecosistema: se conecta a InfluxDB (y a decenas de fuentes más) y permite construir dashboards con paneles de series de tiempo, gauges, tablas y umbrales de alerta.

- Cada panel es una consulta a la fuente de datos + una visualización.
- Las **variables** de dashboard permiten filtrar por dispositivo o sala sin duplicar paneles.
- Las **alertas** notifican (correo, webhook, Telegram) cuando una serie cruza un umbral.

## Prometheus

**Prometheus** invierte el modelo: en lugar de que el dispositivo empuje datos (_push_, como MQTT→InfluxDB), Prometheus **jala** métricas (_pull_) consultando endpoints HTTP `/metrics` en intervalos regulares. Es el estándar para monitorear la **infraestructura** del stack (el broker, la base de datos, el servidor EC2) más que los sensores mismos.

| | InfluxDB + MQTT | Prometheus |
|---|---|---|
| Modelo | push | pull (scrape) |
| Uso típico en el curso | telemetría de sensores | salud de servicios del stack |
| Visualización | Grafana | Grafana (misma instancia) |

## Prácticas

- [`assignments/u1/5-grafana`](../../../assignments/u1/5-grafana/readme.md) — instalación de Grafana en AWS (Ubuntu)
- [`assignments/u1/6-prometeus`](../../../assignments/u1/6-prometeus/readme.md) — instalación de Prometheus en AWS (Ubuntu)

## Referencias

- [Grafana Docs](https://grafana.com/docs/)
- [Prometheus Docs](https://prometheus.io/docs/)
