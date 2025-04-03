

# 🗃️ Uso de InfluxDB en Sensores, IoT y Nuevas Tecnologías

## 1. 📚 Antecedentes: InfluxDB y su Rol en IoT

Las bases de datos de series de tiempo (**TSDB – Time Series Databases**) están diseñadas para almacenar y consultar datos que **cambian con el tiempo**, como lecturas de sensores a intervalos regulares.

En contextos como **IoT**, domótica o monitoreo industrial, estas bases de datos permiten:

- ✅ **Almacenamiento eficiente** de flujos constantes de datos.  
- ⚡ **Consultas en tiempo real** para detectar eventos o anomalías.  
- 📦 **Compresión optimizada** e índices temporales para alto rendimiento.

### 🧩 ¿Por qué InfluxDB?

InfluxDB es una de las TSDB más populares gracias a:

- 📈 Un potente lenguaje de consultas: `InfluxQL` y `Flux`.  
- 🧩 Integración nativa con herramientas como **Grafana**.  
- 🚀 Escalabilidad y despliegue ágil en nubes, edge y entornos locales.

> Para estudiantes de **Sistemas Programables** en Ingeniería, InfluxDB es ideal para aprender a gestionar datos de sensores en tiempo real y construir soluciones completas de IoT.

---

## 2. ☁️ Instalación de InfluxDB en Ubuntu EC2 (AWS)

### 🔧 Requisitos Previos

- Acceso a **AWS Academy**.  
- Cuenta en la **Consola Web de AWS**.  
- Familiaridad básica con instancias EC2.

---

## 2.1 🚀 Lanzamiento de Instancia EC2 (Ubuntu)

1. Ingresa a [AWS Academy](https://aws.amazon.com/).
2. Ve a **Servicios > EC2** y selecciona **Launch Instance**.
3. Asigna nombre: `InfluxDB-Ubuntu-Instance`.
4. Selecciona una AMI de **Ubuntu Server 20.04 LTS**.
5. Tipo de instancia: `t2.micro` o `t3.micro`.
6. Login:
   - Crea una **Key Pair**, o  
   - Usa **EC2 Instance Connect** (sin clave).
7. Red:
   - Asegúrate de **habilitar IP pública**.
   - Configura Security Group para permitir:
     - `SSH` (puerto 22)
     - `TCP 8086` (opcional, para interfaz/API de InfluxDB).
8. Almacenamiento: mínimo 8–10 GB para pruebas.
9. Confirma y **lanza la instancia**.

---

## 2.2 🖥️ Conexión vía EC2 Instance Connect

1. En EC2, selecciona la instancia → **Connect**.
2. Usa la pestaña **EC2 Instance Connect** → clic en **Connect**.
3. Se abrirá una terminal web como usuario `ubuntu`.

> ✅ No necesitas configurar SSH en tu máquina local.

---

## 2.3 🔄 Actualizar el sistema operativo

```bash
sudo apt-get update
sudo apt-get upgrade -y
```

---

## 2.4 📦 Agregar Repositorio e Instalar InfluxDB

### 🔐 Importar clave GPG y configurar repositorio:

```bash
sudo apt-get install -y curl gnupg
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

### 📥 Instalar InfluxDB:

```bash
sudo apt-get update
sudo apt-get install -y influxdb
```

---

## 2.5 ▶️ Iniciar y habilitar el servicio

```bash
sudo systemctl start influxdb
sudo systemctl enable influxdb
sudo systemctl status influxdb
```

> ✅ Deberías ver “active (running)” si todo está correcto.

---

## 2.6 🔓 (Opcional) Habilitar Acceso Externo (Puerto 8086)

1. EC2 → tu instancia → Security Group asociado.  
2. Edita las **Inbound Rules**:
   - Type: `Custom TCP`
   - Port: `8086`
   - Source: tu IP o `0.0.0.0/0` (solo para pruebas).
3. Guarda los cambios.

---

## 2.7 ✅ Verificación de instalación

### ➤ Accede al CLI:

```bash
influx
```

### ➤ Configuración inicial (InfluxDB 2.x):

```bash
sudo influx setup
```

Te pedirá:

- Organización  
- Usuario  
- Contraseña  
- Token  
- Bucket de datos  

---

## 2.8 🌐 (Opcional) Interfaz Web de InfluxDB 2.x

Si abriste el puerto 8086 y conoces tu IP pública o DNS:

```
http://<TU_IP_PUBLICA>:8086
```

Desde ahí puedes crear Buckets, visualizar datos, tokens de API, y más.

---

## 3. 🧠 Recomendaciones Finales

### 💰 Costo
- Usa `t2.micro` o `t3.micro` si estás en **Free Tier**.
- Detén la instancia cuando no la uses.

### 🔐 Seguridad
- No expongas puertos abiertos innecesariamente.
- Usa autenticación y, si puedes, configura SSL/TLS.

### 📊 Visualización
- Integra InfluxDB con **Grafana** para dashboards en tiempo real.

---

## 🏁 Conclusión

Esta guía te permite:

- Montar **InfluxDB sobre EC2 con Ubuntu**  
- Usar solo la **Consola Web de AWS (EC2 Instance Connect)**  
- Obtener experiencia práctica con **bases de datos de series de tiempo**  
- Prepararte para proyectos reales de IoT, sensorización y analítica de datos

NOTA: Valide las versiones y/o distribucion de linux, este es un procedimiento genérico y puede hacer faltante alguna mejora.
