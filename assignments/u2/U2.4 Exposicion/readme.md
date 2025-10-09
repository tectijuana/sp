

# 🧠 Desafíos IoT - Proyectos Individuales (Stack: MQTT, InfluxDB, Grafana, Prometheus)

> **Instrucciones**: Cada estudiante debe seleccionar un proyecto y desarrollarlo individualmente usando el stack IoT disponible. Todos los proyectos deben tener:
>
> * Captura de datos con sensores
> * Publicación vía MQTT
> * Persistencia en InfluxDB o Prometheus
> * Visualización con Grafana
> * Documentación en Markdown y código en GitHub

---

## 🏥 Salud

| Proyecto                                       | Stack                     |
| ---------------------------------------------- | ------------------------- |
| Monitor de signos vitales para adultos mayores | MQTT, Grafana, InfluxDB   |
| Detección de caídas en personas mayores        | MQTT, Prometheus, Grafana |
| Sistema de monitoreo de temperatura de vacunas | MQTT, InfluxDB, Grafana   |
| Monitoreo remoto de pacientes COVID-19         | MQTT, InfluxDB, Grafana   |

---

## 🌱 Agrotech

| Proyecto                                              | Stack                   |
| ----------------------------------------------------- | ----------------------- |
| Sistema de riego automatizado por humedad             | MQTT, Grafana, InfluxDB |
| Monitoreo de invernaderos (CO₂, humedad, temperatura) | MQTT, InfluxDB, Grafana |
| Control de plagas con sensores de movimiento          | MQTT, Prometheus        |
| Estación meteorológica local para agricultores        | MQTT, InfluxDB, Grafana |

---

## 🏭 Industria

| Proyecto                                     | Stack                      |
| -------------------------------------------- | -------------------------- |
| Monitoreo de motores eléctricos (vibración)  | MQTT, Grafana, Prometheus  |
| Prevención de fallas en líneas de producción | MQTT, InfluxDB, Prometheus |
| Medición de consumo energético industrial    | MQTT, InfluxDB, Grafana    |
| Control de acceso industrial con RFID        | MQTT, InfluxDB, Grafana    |

---

## 🏠 Hogar Inteligente

| Proyecto                                           | Stack                     |
| -------------------------------------------------- | ------------------------- |
| Sistema antirrobo con sensores de puertas/ventanas | MQTT, InfluxDB, Grafana   |
| Detección de fugas de gas con alertas tempranas    | MQTT, Prometheus, Grafana |
| Automatización de luces con sensores de presencia  | MQTT, Grafana             |
| Medidor de consumo de agua doméstico               | MQTT, InfluxDB            |

---

## 🏙️ Smart City

| Proyecto                                     | Stack                   |
| -------------------------------------------- | ----------------------- |
| Monitoreo de nivel de ruido urbano           | MQTT, InfluxDB, Grafana |
| Gestión inteligente de tráfico en semáforos  | MQTT, Prometheus        |
| Control eficiente de alumbrado público       | MQTT, InfluxDB, Grafana |
| Sensores de basura para rutas de recolección | MQTT, Grafana           |

---

## 🎓 Educación

| Proyecto                                            | Stack                   |
| --------------------------------------------------- | ----------------------- |
| Medidor de CO₂ en aulas escolares                   | MQTT, InfluxDB, Grafana |
| Asistencia automática con RFID                      | MQTT, Grafana           |
| Ambientes de aprendizaje seguros (temp, CO₂, ruido) | MQTT, InfluxDB          |
| Control de ruido en bibliotecas universitarias      | MQTT, Grafana           |

---

## ⚡ Energía

| Proyecto                                    | Stack                   |
| ------------------------------------------- | ----------------------- |
| Monitoreo de paneles solares residenciales  | MQTT, InfluxDB, Grafana |
| Seguimiento de turbinas eólicas caseras     | MQTT, Prometheus        |
| Gestión inteligente de baterías de respaldo | MQTT, Grafana           |
| Contador eléctrico inteligente con alertas  | MQTT, InfluxDB          |

---

## 🚚 Transporte / Logística

| Proyecto                                          | Stack            |
| ------------------------------------------------- | ---------------- |
| Rastreo GPS de flotas en tiempo real              | MQTT, Grafana    |
| Monitoreo de temperatura en camiones refrigerados | MQTT, InfluxDB   |
| Presión de llantas en autobuses urbanos           | MQTT, Prometheus |
| Control de consumo de combustible en vehículos    | MQTT, Grafana    |

---

## 🌎 Medio Ambiente

| Proyecto                                         | Stack                   |
| ------------------------------------------------ | ----------------------- |
| Calidad del aire en zonas urbanas                | MQTT, InfluxDB, Grafana |
| Nivel de agua en ríos para alertas de inundación | MQTT, Prometheus        |
| Sensor UV para alertas de radiación solar        | MQTT, Grafana           |
| Monitoreo de temperatura de lagos o embalses     | MQTT, InfluxDB          |

---

### 🧩 ¿Qué sigue?

* [ ] Cada estudiante debe enviar su propuesta con una justificación técnica.
* [ ] Se validará si el proyecto es viable según los sensores disponibles.
* [ ] Se espera una entrega en GitHub con:

  * Código comentado (libre de lenguaje)
  * Diagrama de arquitectura
  * Dashboards de Grafana
  * Dataset (si aplica)
  * README detallado

---

Perfecto 💡
Aquí tienes una **rúbrica de evaluación en formato Markdown** diseñada para proyectos individuales de IoT con el stack MQTT, InfluxDB, Prometheus y Grafana.

---

# 📊 Rúbrica de Evaluación – Proyecto IoT Individual

> Total: **100 puntos**
> Modalidad: Individual
> Entrega: Repositorio GitHub con README, código, dashboards, y dataset simulado o real

---

## ✅ 1. Documentación Técnica – 20 pts

| Criterio                   | Descripción                                                                                               | Puntos |
| -------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |
| README.md claro y completo | Explica el propósito, arquitectura, uso del stack, instalación y uso del sistema.                         | 10 pts |
| Diagrama de arquitectura   | Uso de herramientas como Mermaid.js, Lucidchart, Draw.io. Incluye sensores, MQTT, base de datos, Grafana. | 10 pts |

---

## 🧠 2. Lógica y Flujo del Sistema – 20 pts

| Criterio                                                           | Descripción                                                                             | Puntos |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ------ |
| Implementación del flujo de datos (sensor → MQTT → DB → Dashboard) | El sistema funciona end-to-end de forma coherente.                                      | 10 pts |
| Control de errores y validaciones                                  | Se filtran valores corruptos o atípicos del sensor, y se gestiona la reconexión a MQTT. | 10 pts |

---

## 📦 3. Stack IoT Utilizado – 25 pts

| Criterio                                          | Descripción                                                         | Puntos |
| ------------------------------------------------- | ------------------------------------------------------------------- | ------ |
| MQTT correctamente implementado                   | Suscripción y publicación de datos con topic estructurado.          | 5 pts  |
| Base de datos (InfluxDB o Prometheus) funcionando | Los datos se guardan con timestamp, correctamente formateados.      | 10 pts |
| Grafana funcional con al menos 2 paneles útiles   | Dashboards visualmente claros, con al menos un gráfico y una tabla. | 10 pts |

---

## 📈 4. Simulación de Datos / Recolección Real – 15 pts

| Criterio                                       | Descripción                                                         | Puntos |
| ---------------------------------------------- | ------------------------------------------------------------------- | ------ |
| Datos simulados realistas o uso de sensor real | Se generan datos creíbles (Mockaroo, script Python, sensor físico). | 10 pts |
| Análisis básico de datos                       | Se describe brevemente comportamiento observado en los datos.       | 5 pts  |

---

## 🎯 5. Originalidad y Resolución de Problema – 10 pts

| Criterio                                      | Descripción                                                       | Puntos |
| --------------------------------------------- | ----------------------------------------------------------------- | ------ |
| Proyecto con aplicación clara y bien definida | Se resuelve un problema real o se adapta a un caso de uso válido. | 10 pts |

---

## 💡 6. Presentación Final – 10 pts

| Criterio                                  | Descripción                                                            | Puntos |
| ----------------------------------------- | ---------------------------------------------------------------------- | ------ |
| Video o demo en vivo funcional (opcional) | Presentación de 3–5 min explicando el proyecto y mostrando dashboards. | 5 pts  |
| Repositorio bien organizado y sin errores | Estructura clara: `/src`, `/data`, `/dashboards`, `README.md`          | 5 pts  |

---

## 🧮 Total de puntos

| Área                       | Puntos      |
| -------------------------- | ----------- |
| Documentación              | 20 pts      |
| Lógica del sistema         | 20 pts      |
| Uso del stack IoT          | 25 pts      |
| Datos generados o reales   | 15 pts      |
| Resolución de problema     | 10 pts      |
| Presentación y repositorio | 10 pts      |
| **TOTAL**                  | **100 pts** |

---

