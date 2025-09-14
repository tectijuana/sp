
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.niagaramarketplace.com%2Finfluxdb.html&psig=AOvVaw2jkyr565WqEGlLSUH51ADj&ust=1757971274203000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCODh4ryX2Y8DFQAAAAAdAAAAABAE<img width="265" height="265" alt="image" src="https://github.com/user-attachments/assets/d86c2146-e4dc-418c-9bdd-b595f601e208" />


# 🗃️ Uso de InfluxDB en Sensores, IoT y Nuevas Tecnologías

## 📚 Antecedentes: InfluxDB y su Rol en IoT

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

> Para estudiantes de **Sistemas Programables**, InfluxDB es ideal para aprender a gestionar datos de sensores en tiempo real y construir soluciones completas de IoT.

---

## 2. Instalación de InfluxDB 2 en una instancia EC2 con Ubuntu 20.04

### 2.1 Requisitos previos

- Acceso a **AWS Academy** u otra cuenta de AWS.
- Conocer la **Consola web de AWS** para crear instancias EC2.
- Familiaridad básica con sistemas Linux (Ubuntu 20.04 LTS).

### 2.2 Lanzar una instancia EC2 (Ubuntu)

1. Inicia sesión en [AWS Academy](https://aws.amazon.com/) o en tu consola de AWS.
2. Dirígete a **Servicios > EC2** y selecciona **Launch Instance**.
3. Asigna un nombre descriptivo, por ejemplo `InfluxDB-Ubuntu-Instance`.
4. Selecciona la **AMI** de **Ubuntu Server 20.04 LTS** (64 bits).
5. Elige un tipo de instancia pequeño, como `t2.micro` o `t3.micro` (entra en la capa gratuita).
6. Configura las credenciales de acceso:
   - Crea una **key pair** para conectar vía SSH, o
   - Usa **EC2 Instance Connect** si no quieres descargar claves.
7. En la sección de red, habilita una IP pública y crea un **Security Group** que permita:
   - Tráfico de **SSH** (puerto 22).
   - Tráfico **TCP 8086** si deseas acceder a la interfaz web de InfluxDB.
8. Lanza la instancia con un disco de al menos **10 GB** para pruebas.

### 2.3 Conexión a la instancia

1. En la consola de EC2, selecciona la instancia lanzada y haz clic en **Connect**.
2. Selecciona **EC2 Instance Connect** y presiona **Connect**. Se abrirá una terminal en el navegador con usuario `ubuntu`.

**Nota:** no necesitas configurar SSH en tu máquina local si usas Instance Connect.

### 2.4 Actualizar el sistema operativo

Ejecuta estos comandos para actualizar la lista de paquetes y el sistema (puedes pegar varios comandos con `shift` + `enter` en la terminal web):

```bash
sudo apt update
sudo apt upgrade -y
````

### 2.5 Agregar la clave GPG y el repositorio de InfluxData

Debido a los cambios de firma de InfluxData y a la deprecación de `apt-key`, utiliza el nuevo método de almacenamiento de claves. Ejecuta:

```bash
# Importar la clave de firma y guardarla en el directorio de claves de apt
curl -fsSL https://repos.influxdata.com/influxdata-archive_compat.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/influxdata.gpg

# Agregar el repositorio estable de InfluxData para Debian/Ubuntu
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
```

### 2.6 Instalar InfluxDB 2

Actualiza el índice de paquetes e instala el paquete **influxdb2**:

```bash
sudo apt update
sudo apt install -y influxdb2
```

### 2.7 Iniciar y habilitar el servicio

Para que InfluxDB 2 se ejecute automáticamente al arrancar el sistema, habilita y arranca el servicio:

```bash
sudo systemctl enable --now influxdb

# Verifica el estado del servicio
sudo systemctl status influxdb
```

Deberías ver un estado `active (running)` en la salida.

### 2.8 Configuración inicial con `influx setup`

InfluxDB 2 requiere un proceso de configuración inicial para crear una **organización**, un **usuario administrador**, un **token de autenticación** y un **bucket** para almacenar datos. Ejecuta:

```bash
influx setup
```

El asistente interactivo te solicitará:

* **Nombre de la organización** (por ejemplo, `SistemasProgramables`).
* **Nombre de usuario** y **contraseña**.
* **Nombre del bucket** donde se guardarán las métricas.
* **Periodo de retención** (puede dejarse en blanco para infinito).

Una vez completado, se generará un **token de autenticación**. Guarda este token, ya que será necesario para escribir y leer datos mediante la API.

### 2.9 Verificación de la instalación

Para comprobar que InfluxDB 2 funciona correctamente:

* Ejecuta `influx version` para verificar la versión instalada.
* Usa `sudo systemctl status influxdb` para comprobar el estado del servicio, en caso de pausa solo precione letra "q"
* Abre la interfaz web si habilitaste el puerto 8086: `http://<TU_IP_PUBLICA>:8086`. Desde allí puedes crear buckets, cargar datos y generar tokens.

---

## 3. Habilitar acceso externo al puerto 8086

Si necesitas acceder a la interfaz web desde tu red local o internet, edita las **Inbound Rules** del Security Group asociado a tu instancia:

1. En EC2 → **Security Group** → **Edit inbound rules**.
2. Agrega una regla `Custom TCP` con puerto `8086` y origen tu IP pública o `0.0.0.0/0` si es solo para pruebas (no recomendado en producción).
3. Guarda los cambios.

---

## 4. Recomendaciones finales

* Usa tipos de instancia pequeños (`t2.micro`/`t3.micro`) para pruebas si tienes la capa gratuita de AWS.
* Detén la instancia EC2 cuando no la utilices para evitar costos innecesarios.
* Asegura tus servicios: expón únicamente los puertos necesarios y utiliza autenticación y SSL/TLS cuando sea posible.
* Integra InfluxDB con **Grafana** para crear paneles de visualización en tiempo real.

## 🏁 Conclusión

Esta guía te permite:

- Montar **InfluxDB sobre EC2 con Ubuntu**  
- Usar solo la **Consola Web de AWS (EC2 Instance Connect)**  
- Obtener experiencia práctica con **bases de datos de series de tiempo**  
- Prepararte para proyectos reales de IoT, sensorización y analítica de datos

NOTA: Valide las versiones y/o distribucion de linux, este es un procedimiento genérico y puede hacer faltante alguna mejoras.
