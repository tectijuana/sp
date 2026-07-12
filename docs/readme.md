# Estructura del Repositorio

```bash
sp/
│
├── README.md                # Descripción general del curso
├── README.en.md              # Resumen del curso en inglés (paridad internacional)
├── CITATION.cff               # Metadatos de citación académica del repositorio
├── SYLLABUS.md                 # Temario oficial del curso (revisión 2027)
├── SCHEDULE.md                # Cronograma por semanas (sin fechas fijas)
├── GRADING.md                 # Criterios de evaluación y rúbricas
├── POLICIES.md                 # Políticas del curso
├── CODE_OF_CONDUCT.md           # Código de conducta
├── CONTRIBUTING.md               # Guía de contribución
├── AI_GUIDANCE.md                  # Uso responsable de IA/LLM en el curso
├── ANEXO.md                         # Declaración de asistencia de IA por entrega
├── LICENSE                           # Licencia del repositorio
│
├── docs/                      # Documentación y lineamientos
│   ├── readme.md              # Este archivo
│   ├── schedule.md            # Referencia cruzada al cronograma
│   ├── grading.md             # Referencia cruzada a la evaluación
│   ├── contribution.md        # Guía de contribuciones
│   ├── guidelines.md          # Lineamientos generales y de entrega
│   ├── references.md          # Referencias y enlaces del curso
│   ├── ai-iot-stack.md        # Concepto AI-IoT-Stack (innovación 2027)
│   └── FAQ.md                 # Preguntas frecuentes
│
├── resources/                 # Material de apoyo
│   ├── tutorials/              # Tutoriales: microcontroladores, sensores/actuadores,
│   │                            # comunicación, Embedded Linux, InfluxDB, AWS Academy, flespi
│   ├── bibliography.md          # Catálogo de libros y recursos recomendados
│   ├── images/                   # Imágenes de apoyo
│   └── examples/                  # Código y esquemas de referencia
│
├── class-material/            # Material de clase por unidad
│   ├── u1/                     # U01 — Fundamentos, AWS Academy, EC2, IoT stack, Flask
│   │   └── investigacion/       # Investigaciones de estudiantes (temas U01)
│   ├── u2/                     # U02 — Sensores, MQTT, EdgeX Foundry, desafíos IoT
│   ├── u3/                     # U03 — Persistencia/visualización, ThingsBoard, integración con APIs/IA
│   ├── u4/                     # U04 — Comunicaciones avanzadas e integración con IA (en construcción)
│   ├── u5/                     # U05 — Edge AI, seguridad y eficiencia (en construcción)
│   ├── u6/                     # U06 — Proyecto integrador (en construcción)
│   └── FakeSensors/             # Simuladores de sensores para prácticas sin hardware físico
│
└── assignments/                # Tareas y laboratorios entregables
    ├── u1/                      # Prácticas U01 (AWS, dashboards, InfluxDB, Grafana, Prometheus, MQTT)
    ├── u2/                      # Prácticas U02 (sensores, LLM aplicado, smartphone como sensor)
    ├── u3/                      # Prácticas U03 (microbit → IoT stack, flespi)
    ├── u4/                      # Prácticas U04 (en construcción)
    ├── u5/                      # Prácticas U05 (en construcción)
    ├── u6/                      # Prácticas U06 (en construcción)
    └── proyectos/                # Proyectos integradores de equipos (U06)
```

> Nota: `class-material/u4`–`u6` y `assignments/u4`–`u6` están creadas con temario base (ver [`SYLLABUS.md`](../SYLLABUS.md)) y contenido pendiente de agregarse conforme avance el ciclo 2027.
