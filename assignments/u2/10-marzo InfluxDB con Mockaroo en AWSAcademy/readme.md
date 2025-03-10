<img width="1124" alt="Screenshot 2025-03-10 at 2 01 54 p m" src="https://github.com/user-attachments/assets/bb9cd28f-a469-40d8-986a-ca4cf0c25edf" />





**Ejercicio Práctico para Ingeniería: Implementación y análisis de datos de sensores usando InfluxDB en AWS Academy**

## 🎯 Objetivo
Los estudiantes aprenderán a valorar el potencial de **InfluxDB** como base de datos de series temporales para almacenar, consultar y analizar datos provenientes de sensores, aplicando un caso práctico utilizando infraestructura en AWS Academy.

---

### 🚀 Contexto del Caso

Una empresa ficticia, **EcoGrow**, especializada en agricultura vertical inteligente, desea implementar una solución tecnológica que capture datos de sensores ambientales (temperatura, humedad, luminosidad y pH) desde distintos puntos de cultivo vertical, almacenando estos datos para análisis en tiempo real y predicción futura.

Tu equipo ha sido contratado para desarrollar una solución robusta y escalable basada en InfluxDB, implementándola sobre AWS.

---

### 📝 Requisitos Técnicos

- Utilizar una instancia **Amazon EC2** (Ubuntu Server 22.04) en AWS Academy.
- Instalar y configurar **InfluxDB**.
- Simular datos generados por sensores con **Mockaroo.com**.
- Utilizar scripts en **Python** para insertar datos automáticamente en la base de datos.
- Consultar y visualizar los datos recolectados usando comandos específicos (InfluxQL).

---

### 🔖 Procedimiento Paso a Paso

#### 🟢 Paso 1: Preparación del servidor en AWS
- Accede a AWS Academy y crea una instancia EC2 con Ubuntu Server 22.04.
- Actualiza el servidor:
```bash
sudo apt update && sudo apt upgrade -y
```

#### 🟢 Paso 2: Instalación de InfluxDB
- Instala InfluxDB en la instancia Ubuntu:
```bash
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.6-amd64.deb
sudo dpkg -i influxdb2*.deb
sudo systemctl start influxdb
sudo systemctl enable influxdb
```

- Configura inicialmente InfluxDB (crear usuario, contraseña y organización).

#### 🟢 Paso 2: Creación de datos de sensores usando Mockaroo
- Utiliza [mockaroo.com](https://www.mockaroo.com/) con el siguiente prompt del bot generador:

> 🔸 **Prompt para Mockaroo:**  
> Crea un dataset llamado "sensores_ecogrow" con campos:  
> - `sensor_id` (UUID)  
- `sensor_type` (ej. temperatura, humedad, luminosidad, humedad_suelo)
- `value` (número decimal, según el tipo de sensor)
- `timestamp` (tipo fecha y hora, intervalo cada minuto durante 24 horas)

- Exporta el archivo generado en formato CSV.

#### 🟢 Paso 3: Importación automática en InfluxDB
- Copia el archivo CSV al servidor AWS.
- Usa el cliente CLI de InfluxDB para importar los datos:
```bash
influx write -b ecogrow_data -f sensores.csv --header "sensor_data,sensor_type=value,value=value timestamp"
```

#### 🟢 Paso 4: Análisis básico de los datos
- Realiza consultas desde la interfaz de InfluxDB para obtener:
  - Promedio, mínimo y máximo de temperatura por hora.
  - Intervalos de humedad del suelo críticos.

#### Ejemplo consulta:
```sql
from(bucket:"eco_grow")
  |> range(start: -24h)
  |> filter(fn: (r) => r["sensor_type"] == "temperatura")
  |> aggregateWindow(every: 1h, fn: mean)
```

#### 🟢 Paso 5: Visualización
- Usa el dashboard integrado de InfluxDB para crear gráficos interactivos que muestren tendencias y comportamientos de los sensores.

---

### 🤖 Prompt para Bot asistente (Mockaroom.com)

Copia el siguiente prompt en **mockaroom.com** para generar automáticamente datos realistas del caso:

> " Crea un conjunto de datos realista simulando la captura de múltiples sensores agrícolas durante un día entero. Incluye sensores de temperatura (entre 10 y 30 ºC), humedad ambiental (entre 40% y 90%), luminosidad (0 a 1000 lux), y humedad del suelo (20% a 80%). El intervalo debe ser de 1 minuto para representar datos continuos. Entrega el resultado en CSV para fácil importación a InfluxDB."

---

### 🎯 Objetivos de aprendizaje del ejercicio
- Identificar ventajas de InfluxDB para datos de series temporales.
- Desarrollar habilidades para manejar herramientas de simulación (Mockaroo).
- Practicar configuraciones en entornos de nube AWS.
- Aplicar análisis y visualización básica de datos en contexto ingenieril.

---

### 🧑‍💻 Entrega del ejercicio

Cada estudiante entregará:
- Captura del dashboard con gráficos generados.
- Documento corto explicando resultados de consultas hechas.
- Breve reflexión sobre las ventajas observadas en el uso de InfluxDB para datos de sensores.

---
NOTA: Recuerde que AWS el Security Groups para exponer el puerto TCP 8080s
✨ ¡Éxito en tu actividad! 🌱📈

