
<img width="1124" alt="Screenshot 2025-03-10 at 2 01 54 p m" src="https://github.com/user-attachments/assets/bb9cd28f-a469-40d8-986a-ca4cf0c25edf" />

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/7b9f47eb-b0d1-4f6e-9469-b78c67b4c299" />

# Práctica: Uso actualizado de InfluxDB en Sensores, IoT y Nuevas Tecnologías

## Objetivo
El estudiante será capaz de instalar y configurar **InfluxDB 2** en una instancia **AWS EC2 con Ubuntu 20.04**, crear la organización inicial, buckets y tokens, y comprender su rol en proyectos de **IoT** para almacenar datos de sensores en tiempo real.

---

## 1. Contexto y rol de InfluxDB en IoT

Las bases de datos de series de tiempo (**TSDB**) están diseñadas para almacenar y consultar datos que cambian con el tiempo, como lecturas de sensores o métricas de sistemas.  
En entornos de **Internet de las Cosas (IoT)**, domótica o monitorización industrial, estas bases de datos permiten:

- **Almacenamiento eficiente** de flujos constantes de datos.
- **Consultas en tiempo real** para detectar eventos o anomalías.
- **Compresión optimizada** e índices temporales para alto rendimiento.

### ¿Por qué InfluxDB?
- Lenguajes de consulta: `InfluxQL` y `Flux`.
- Integración nativa con **Grafana**.
- Escalabilidad en nubes públicas, edge o servidores locales.

---

## 2. Instalación de InfluxDB 2 en Ubuntu 20.04 (EC2)

### 2.1 Requisitos previos
- Cuenta en **AWS Academy** (o AWS).
- Familiaridad básica con Linux.

### 2.2 Crear la instancia EC2
1. Inicia sesión en AWS.
2. Lanza una **Ubuntu Server 20.04 LTS (64 bits)**.
3. Tipo de instancia: `t2.micro` o `t3.micro`.
4. Security Group:
   - Puerto **22** (SSH).
   - Puerto **8086** (InfluxDB, opcional).

### 2.3 Conexión y actualización del sistema
```bash
sudo apt update
sudo apt upgrade -y
```

### 2.4 Agregar repositorio oficial
```bash
curl -fsSL https://repos.influxdata.com/influxdata-archive_compat.key | \
  sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/influxdata.gpg

echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata.gpg] https://repos.influxdata.com/debian stable main' \
  | sudo tee /etc/apt/sources.list.d/influxdata.list
```

### 2.5 Instalar InfluxDB 2
```bash
sudo apt update
sudo apt install -y influxdb2
```

### 2.6 Habilitar servicio
```bash
sudo systemctl enable --now influxdb
sudo systemctl status influxdb
```

### 2.7 Configuración inicial
Ejecuta:
```bash
influx setup
```

Configura:
- Organización: `SistemasProgramables`. (puede cambiarla)
- Usuario y contraseña. (no la olvide)
- Bucket inicial.
- Retención (infinita o personalizada).
- Se genera un **token de autenticación** (guardar y no perder use Google KEEP).

### 2.8 Verificación
- `influx version`
- `systemctl status influxdb`
- Navegador: `http://<TU_IP_PUBLICA>:8086`

---

## 3. (Opcional) Acceso externo
En el **Security Group** agrega regla TCP 8086 con tu IP pública a todo el mundo IP 0.0.0.0 o el de su routeador.

---

## 4. Actividad práctica

1. Documenta en un archivo Markdown los pasos realizados con **capturas de pantalla** (consola AWS, estado del servicio, interfaz web).  
2. Inserta al menos **una consulta simple** desde CLI o interfaz web (ejemplo: listar buckets).  
3. Incluye el **token generado** en el reporte (en texto tachado o bloqueado).  
4. Sube tu archivo final un GIST.github.com, bien estructurado por favor.

---

## 5. Recomendaciones
- Detén la instancia EC2 cuando no la uses.
- Usa autenticación y TLS en producción.
- Integra con **Grafana** para visualización.
- Usar http://mockaroo.com para datos simulador (o ChatGPT tambien)

---

## 7. Rúbrica de evaluación

| Criterio                               | Excelente (100%)                              | Satisfactorio (80%)            | Insuficiente (50%)         | Nulo (0%)        |
|----------------------------------------|-----------------------------------------------|--------------------------------|-----------------------------|------------------|
| **Instancia EC2**                      | Instancia creada y funcionando con Ubuntu 20.04 | Instancia con errores menores | Instancia con errores graves | No entregado     |
| **Instalación InfluxDB 2**             | Instalada y corriendo correctamente            | Instalación con errores leves  | Servicio no corre correctamente | No entregado |
| **Configuración inicial (`setup`)**    | Organización, bucket y token creados           | Configuración incompleta       | Configuración incorrecta    | No entregado     |
| **Documentación y evidencia**          | Markdown completo con capturas y consultas, asciinemas, etc.     | Markdown con capturas parciales | Evidencia mínima            | No entregado     |

---

## 8. Conclusión
Con esta práctica el estudiante comprende el proceso de despliegue de **InfluxDB 2** en AWS, asegura su funcionamiento, y documenta su experiencia con un enfoque en **IoT y datos de sensores en tiempo real**.
````
