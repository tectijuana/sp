# 3.1 — Bases de datos de series temporales: InfluxDB

Los datos de sensores son **series temporales**: cada lectura es un valor con marca de tiempo (`temperatura=23.4 @ 2027-02-10T14:03:00Z`). Una base relacional puede almacenarlos, pero una **TSDB** (_Time Series Database_) como **InfluxDB** está optimizada exactamente para este patrón: escrituras masivas ordenadas por tiempo, consultas por rango y ventana, y políticas de retención que descartan datos viejos automáticamente.

## Conceptos clave

| Concepto | En InfluxDB | Ejemplo |
|---|---|---|
| Base de datos | _bucket_ | `sensores_aula` |
| Tabla | _measurement_ | `ambiente` |
| Metadatos indexados | _tags_ | `sala=lab3, dispositivo=picow-01` |
| Valores medidos | _fields_ | `temp=23.4, hum=61` |
| Marca de tiempo | _timestamp_ | nanosegundos Unix |

## Line protocol

El formato de ingesta de InfluxDB es una línea de texto por punto — el mismo que producen los generadores de FakeSensors:

```
ambiente,sala=lab3,dispositivo=picow-01 temp=23.4,hum=61 1739196180000000000
```

## Flujo en el curso

```
Pico W / FakeSensors → MQTT (Mosquitto) → Telegraf/bridge → InfluxDB → Grafana (3.2)
```

## Práctica

- [`assignments/u1/4-influxdb`](../../../assignments/u1/4-influxdb/readme.md) — instalación en AWS Academy y carga de datos.

## Referencias

- [Documentación oficial de InfluxDB](https://docs.influxdata.com/)
- [Line protocol reference](https://docs.influxdata.com/influxdb/latest/reference/syntax/line-protocol/)
