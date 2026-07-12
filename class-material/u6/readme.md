# U06 — Proyecto integrador: un AI-IoT-Stack completo

El proyecto final del ciclo 2027 exige demostrar el [AI-IoT-Stack](../../docs/ai-iot-stack.md) de extremo a extremo: no basta con graficar datos — el sistema debe **decidir o razonar** algo con ellos.

---

## Requisitos mínimos del sistema

El proyecto de equipo debe cubrir todas las capas del stack:

1. **Percepción:** al menos 2 sensores reales o simulados (Wokwi / FakeSensors) y 1 actuador.
2. **Conectividad + mensajería:** publicación por MQTT (Mosquitto/EMQX o flespi).
3. **Persistencia:** lecturas almacenadas en InfluxDB (u otra base de series temporales justificada).
4. **Capa de inteligencia — obligatoria, al menos UNA de las dos rutas:**
   - **Ruta borde:** un modelo TinyML corriendo en el microcontrolador (clasificación, detección de anomalías) — ver U05.
   - **Ruta nube:** integración con un LLM vía API que interprete el estado de los sensores y genere una recomendación, alerta o resumen — ver U04.
   - Los proyectos que integren **ambas rutas** con una justificación de diseño coherente puntúan más alto en innovación.
5. **Visualización y acción:** dashboard (Grafana/ThingsBoard) que muestre el dato crudo **y** la salida de la capa de inteligencia, más el actuador respondiendo.

**Regla de seguridad no negociable:** cualquier decisión crítica (apagado por sobretemperatura, límites físicos) se implementa con lógica local determinista. La IA recomienda; el `if` protege. Proyectos que deleguen seguridad al LLM pierden puntos de implementación.

---

## Entregables

- **Repositorio del equipo** con README (arquitectura, diagrama del stack, instrucciones de reproducción), código fuente y esquemas — usar la [plantilla profesional de proyecto](../../assignments/proyectos/PLANTILLA-PROYECTO.md).
- **Declaración de asistencia de IA** ([ANEXO.md](../../ANEXO.md)) — obligatoria; usar IA para desarrollar está permitido y valorado, ocultarlo no.
- **Informe técnico** de 5–8 páginas.
- **Demostración en vivo** en la presentación final: el flujo sensor → inteligencia → acción debe verse funcionando.
- **Métrica de valor de la IA:** una medición que justifique la capa de inteligencia (latencia de inferencia, ahorro de tráfico frente a enviar dato crudo, o comparación de la recomendación LLM contra una regla fija).

Ejemplos de proyectos de ciclos anteriores en [`assignments/proyectos`](../../assignments/proyectos) (drones, monitoreo de plantas, manufactura, transporte) — todos son extensibles con la capa de inteligencia 2027.

Rúbrica detallada en [GRADING.md](../../GRADING.md).
