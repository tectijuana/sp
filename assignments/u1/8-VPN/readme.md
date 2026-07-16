# 🔐 Subtema 8: VPN — Seguridad empresarial aplicada a IoT

> ⚠️ **Estatus: práctica experimental.** La ruta institucional con F5 BIG-IP requiere validar el flujo de autenticación (`openconnect --protocol=f5`) antes de impartirse, y la demo en AWS Academy aún no ha sido probada de punta a punta. Ver el paso C para el plan de validación con agente.

## Propósito del subtema

El estudiante comprenderá el papel de una **VPN como control de seguridad empresarial**, la aplicará para proteger una arquitectura IoT (broker MQTT no expuesto a Internet) y la combinará con un modelo de **inteligencia artificial** para detección de anomalías en telemetría de sensores.

## Ruta de trabajo en 3 pasos

| Paso | Documento | Contenido | Entregable | Duración |
|------|-----------|-----------|------------|---------:|
| **A** | [a-teoria-vpn.md](a-teoria-vpn.md) | Teoría: VPN como seguridad empresarial, SSL-VPN vs IPsec, appliances (F5 BIG-IP, Cisco, Fortinet), licenciamiento, defensa en capas | Resumen + autoevaluación | 1 h |
| **B** | [b-practica-f5-iot.md](b-practica-f5-iot.md) | Práctica completa: monitoreo remoto IoT + detección de anomalías con MQTT, IA (Isolation Forest) y VPN F5 BIG-IP institucional | Reporte con evidencias (rúbrica de 100 pts) | 3 h lab |
| **C** | [c-demo-aws-academy.md](c-demo-aws-academy.md) | Demo experimental: cada equipo monta **su propio servidor VPN (ocserv)** en AWS Academy y opera sus clientes | Evidencias de la demo + checkpoints PASS/FAIL | 3 h lab |

## Arquitectura general

```text
        Computadora del estudiante
        (openconnect + simulador.py + analizador.py)
                        │
                        │  túnel VPN cifrado
                        ▼
        ┌──────────────────────────────────┐
        │  Gateway VPN                     │
        │  Paso B: F5 BIG-IP APM (Tec)     │
        │  Paso C: ocserv en EC2 Ubuntu    │
        └──────────────┬───────────────────┘
                        │  red privada (no expuesta a Internet)
                        ▼
        ┌──────────────────────────────────┐
        │  🦟 Mosquitto MQTT (TLS 8883)    │
        │     ├── telemetría IoT           │
        │     └── resultados de IA         │
        │  🔴 Node-RED (1880)              │
        │     └── dashboard / alertas      │
        └──────────────────────────────────┘
```

La idea central en ambos escenarios es la misma: **el broker MQTT y Node-RED solo son alcanzables a través de la VPN**. El cliente `openconnect` también es el mismo; únicamente cambia el protocolo (`--protocol=f5` con el equipo institucional, `--protocol=anyconnect` con ocserv en la demo).

## ¿Por qué dos escenarios (B y C)?

- **F5 BIG-IP es un producto comercial con licencia** — no existe licencia gratuita para estudiantes y sus AMIs de Marketplace están bloqueadas en AWS Academy Learner Lab (detalles y fuentes en el [paso A](a-teoria-vpn.md)).
- Con **ocserv** (open source) cada equipo puede ser responsable de **su servidor VPN y de sus clientes**, que es justo la competencia a evaluar; el conocimiento del lado cliente se transfiere íntegro al escenario institucional F5.
