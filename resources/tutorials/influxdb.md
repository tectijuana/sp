
## 1. Antecedentes: Uso de InfluxDB en Sensores, IoT y Nuevas Tecnologías

Las bases de datos de series de tiempo (Time Series Databases, TSDB) son sistemas diseñados específicamente para almacenar, consultar y manejar datos que varían con el tiempo (por ejemplo, mediciones de sensores en intervalos regulares). En escenarios de **Internet de las Cosas (IoT)** o con **dispositivos de sensorización**, estos sistemas permiten:

- **Almacenamiento eficiente** de grandes volúmenes de datos que llegan constantemente.  
- **Consultas y análisis en tiempo real**, facilitando la detección de eventos, anomalías y el monitoreo continuo.  
- **Optimización de espacio y rendimiento** debido a la compresión y a índices temporales especializados.  

**InfluxDB** es una de las bases de datos de series de tiempo más populares. Cuenta con:
- Un lenguaje de consultas (Flux / InfluxQL) orientado a análisis de datos temporales.  
- Integración sencilla con otras herramientas de visualización (ej. Grafana).  
- Facilidad de escalabilidad y configuración inicial rápida.  

Para los estudiantes de **Sistemas y Computación** que cursan materias relacionadas con Sistemas Programables, InfluxDB se convierte en una excelente elección para aprender a manejar datos de sensores y orquestar soluciones de IoT y analítica de datos en tiempo real.

---

## 2. Procedimiento de instalación y configuración de InfluxDB en una instancia EC2 de Ubuntu (vía Consola Web de AWS)

A continuación se describe el paso a paso asumiendo que ya se cuenta con acceso a **AWS Academy** y se desea crear y configurar una instancia EC2 usando **Ubuntu** como sistema operativo.

### 2.1 Crear la instancia EC2 en la consola web AWS ACADEMY

1. Ingrese a la [Consola de AWS Academy](https://www.awsacademy.com/vforcesite/LMS_Loginhttps://aws.amazon.com/).  
2. Seleccione el servicio **EC2**.  
3. En la barra lateral, busque **Instances** (Instancias) y haga clic en **Launch instances** (Lanzar instancias).  
4. Asigne un **Nombre** a la instancia, por ejemplo, `InfluxDB-Ubuntu-Instance`.  
5. En la sección **Application and OS Images (Amazon Machine Image)**, elija la AMI de **Ubuntu Server** (generalmente “Ubuntu Server 20.04 LTS” o la versión más reciente disponible).  
6. En **Instance type**, seleccione un tipo gratuito o económico (por ejemplo, `t2.micro` o `t3.micro`, si aplica).  
7. En **Key pair (login)**, puede:
   - Crear un nuevo key pair, o  
   - Seleccionar “Proceed without a key pair” si planea conectarse solo mediante **EC2 Instance Connect** (opción que veremos más adelante).  

8. En **Network settings (Configuración de red)**:
   - Deje la **VPC** por defecto o seleccione la que corresponda.
   - Asegúrese de que la instancia **tenga asignada una IP pública** para poder conectarse vía la Consola Web (EC2 Instance Connect).  
   - Configure el **Security Group** para permitir al menos:
     - Tráfico de **SSH (puerto 22)** desde su IP o desde cualquier lugar (si planea usar EC2 Instance Connect, también se requiere que el puerto 22 esté abierto, pero EC2 Instance Connect lo maneja internamente).  
     - **Puerto 8086** (TCP) para InfluxDB, si desea acceder a la API de InfluxDB desde fuera de la instancia (esto puede configurarse más tarde).

9. En **Configure Storage** (Almacenamiento), ajuste el tamaño del disco según las necesidades (por ejemplo, 8 o 10 GB es suficiente para pruebas básicas).  
10. Revise la configuración en el resumen y haga clic en **Launch instance**.  
11. Espere a que el estado de la instancia cambie a **Running**.

### 2.2 Conexión a la instancia vía EC2 Instance Connect (Consola Web)

Para evitar el uso de SSH desde una terminal local o PowerShell, usaremos **EC2 Instance Connect**:

1. En la Consola de AWS, vaya a **EC2 > Instances** y seleccione la instancia que acaba de lanzar.  
2. Haga clic en el botón **Connect** (Conectar) en la parte superior.  
3. Elija la pestaña **EC2 Instance Connect** y luego haga clic en **Connect**.  
4. Se abrirá una ventana de terminal en el navegador, con la sesión iniciada como usuario `ubuntu`.

Ahora ya estamos dentro de la instancia **sin usar SSH local** ni PowerShell; todo se hace desde la consola web.

### 2.3 Actualizar el sistema operativo (desde la terminal en el navegador)

Ejecute los siguientes comandos:

```bash
# Nos aseguramos de que el sistema esté actualizado
sudo apt-get update
sudo apt-get upgrade -y
```

### 2.4 Agregar el repositorio oficial de InfluxDB e instalar

1. **Importar la clave GPG** y agregar el repositorio de InfluxData:

```bash
# Instalar herramientas si no están disponibles
sudo apt-get install -y curl gnupg

# Descargar la clave y añadirla
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -

# Añadir el repositorio de InfluxDB (estable) a la lista de sources
echo "deb https://repos.influxdata.com/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

2. **Actualizar repositorios e instalar InfluxDB**:

```bash
sudo apt-get update
sudo apt-get install -y influxdb
```

### 2.5 Iniciar y habilitar el servicio de InfluxDB

```bash
# Iniciar el servicio
sudo systemctl start influxdb

# Habilitar que inicie automáticamente en cada reinicio
sudo systemctl enable influxdb

# Verificar el estado del servicio
sudo systemctl status influxdb
```

Si todo está correcto, deberá ver un mensaje que indique que InfluxDB se está ejecutando (“active (running)”).

### 2.6 Configuración básica de puertos en el Security Group (opcional)

Para poder acceder a la API de InfluxDB o a un panel de visualización externo (por ejemplo, con Grafana) desde Internet, necesitará abrir el puerto **8086** en el **Security Group** de su instancia.

1. En la Consola de AWS, vaya a **EC2 > Instances**, seleccione su instancia y haga clic en el **Security Group** asociado.  
2. En la pestaña **Inbound rules**, haga clic en **Edit inbound rules**.  
3. Agregue una regla con:
   - **Type**: Custom TCP  
   - **Port**: 8086  
   - **Source**: (opcional, puede poner su IP o 0.0.0.0/0 si desea acceso público, aunque se recomienda restringirlo).  
4. Guarde los cambios.

### 2.7 Verificación de la instalación

- Desde la terminal del navegador (EC2 Instance Connect), puede ingresar al CLI de InfluxDB con:

  ```bash
  influx
  ```
  
  Dependiendo de la versión de InfluxDB que haya instalado (2.x o 1.x), verá un prompt o se iniciará la configuración inicial dentro de la CLI/Setup.  

- Para InfluxDB 2.x, puede requerir crear un **usuario**, **organización** y **bucket** inicial. Normalmente se hace así:

  ```bash
  sudo influx setup
  ```
  Le pedirá valores como organización, usuario, contraseña, etc.

- Para InfluxDB 1.x, simplemente se iniciará una interfaz de línea de comando más sencilla.

### 2.8 (Opcional) Acceso vía interfaz web de InfluxDB 2.x

- En la versión 2.x, InfluxDB cuenta con una interfaz web integrada que corre en el **puerto 8086**.  
- Si el Security Group está configurado correctamente y usted conoce la **IP pública** o **DNS público** de la instancia, puede acceder a:
  ```
  http://<IP_PÚBLICA_O_DNS>:8086
  ```
  Desde un navegador local y continuar la configuración por la interfaz gráfica.

---

## 3. Recomendaciones finales

- **Monitorear costos**: Aunque la instancia `t2.micro` o `t3.micro` es apta para el nivel de uso gratuito (Free Tier) en AWS, revisen su **facturación** si ejecutan la instancia por mucho tiempo.  
- **Seguridad**: Si van a exponer InfluxDB a Internet, es crucial:
  - Restringir las IPs que pueden acceder al puerto 8086 (Inbound Rules en el Security Group).  
  - Configurar autenticación y cifrado (HTTPS/SSL) si el proyecto lo requiere en producción.  
- **Herramientas de visualización**: Integrar con **Grafana** para crear dashboards y representar datos de manera más amigable es común en entornos de IoT.

Con esto, los estudiantes de TECNM en la clase de Sistemas Programables tienen un **proceso claro** para montar un **servidor de base de datos de línea de tiempo (InfluxDB)** sobre Ubuntu en un nodo EC2 de **AWS Academy**, **usando únicamente la consola web EC2** (vía “EC2 Instance Connect”). ¡Éxito en su práctica!
