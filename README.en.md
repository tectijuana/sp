# Programmable Systems — EmbeddedSP

Official repository for the **Programmable Systems** course (2027 revision).
**Program:** Computer Systems Engineering — Tecnológico Nacional de México (TECNM), Instituto Tecnológico de Tijuana.

> 🌐 The primary language of this repository is Spanish — see [README.md](./README.md). This file provides an English overview for international visitors and accreditation reviewers.

---

## About the course

Programmable Systems teaches the design, programming, and integration of embedded systems with cloud and IoT architectures. The 2027 revision introduces the **AI-IoT-Stack**: the course's IoT data pipeline extended with an intelligence layer — Edge AI (TinyML) on-device and LLM orchestration in the cloud — so systems reason about sensor data instead of merely charting it. See [`docs/ai-iot-stack.md`](./docs/ai-iot-stack.md) (Spanish).

## Learning outcomes

Upon completion, students are able to:

1. Explain the architecture and operation of common microcontrollers and microprocessors.
2. Program embedded systems in C/C++ and MicroPython, using cloud environments (AWS Academy) and simulators (Wokwi, Proteus, Fritzing).
3. Design and simulate digital circuits integrating sensors and actuators.
4. Implement communication protocols (UART, SPI, I²C, MQTT) and deploy an IoT ingestion stack (MQTT broker, EdgeX Foundry).
5. Persist and visualize sensor data as time series (InfluxDB) through dashboards (Grafana, Prometheus, ThingsBoard).
6. Integrate embedded systems with cloud services, external APIs, and AI models (Edge AI/TinyML and LLMs) applying efficiency and security best practices.
7. Develop a capstone project solving a real problem with a connected programmable system.

## Course structure

| Unit | Topic |
|------|-------|
| U01 | Foundations and the cloud-embedded environment (AWS Academy, EC2, Flask) |
| U02 | Sensors, actuators, and IoT messaging (MQTT, EdgeX Foundry) |
| U03 | Data persistence and visualization (InfluxDB, Grafana, ThingsBoard) |
| U04 | Advanced communications and LLM integration |
| U05 | Edge AI (TinyML), security, and energy efficiency |
| U06 | Capstone project: a complete AI-IoT-Stack |

Full details: [SYLLABUS.md](./SYLLABUS.md) · [SCHEDULE.md](./SCHEDULE.md) · [GRADING.md](./GRADING.md) (Spanish).

## Repository structure

- `class-material/` — lecture material per unit (u1–u6)
- `assignments/` — labs and deliverables per unit, plus team capstone projects (`proyectos/`)
- `resources/` — tutorials, bibliography, reference examples
- `docs/` — course documentation, FAQ, references, AI-IoT-Stack concept

## Academic integrity and AI use

Responsible use of AI tools (LLMs, coding assistants) is permitted and valued; every submission must include an AI assistance disclosure ([ANEXO.md](./ANEXO.md)). Guidelines: [AI_GUIDANCE.md](./AI_GUIDANCE.md). Plagiarism results in a zero grade — see [POLICIES.md](./POLICIES.md).

## Contributing and license

This is an open educational project under the [GPL-3.0 license](./LICENSE). See [CONTRIBUTING.md](./CONTRIBUTING.md) and the [Code of Conduct](./CODE_OF_CONDUCT.md). To cite this repository, use [CITATION.cff](./CITATION.cff).
