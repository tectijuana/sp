<img width="830" height="370" alt="image" src="https://github.com/user-attachments/assets/1969195f-a6fc-487a-959e-9e716bdf05c7" />


# Práctica: Instalación de Prometheus en AWS (Ubuntu 20.04/24.04)

## Objetivo
En esta práctica aprenderás a desplegar **Prometheus**, un sistema de monitorización y base de datos de series de tiempo, en una instancia **EC2** con **Ubuntu Server**.  
Al finalizar, tendrás un servidor Prometheus funcionando junto con **Node Exporter** para recolectar métricas del propio host, y sabrás cómo acceder a su interfaz web.

---

## 1. Requisitos previos
- Cuenta activa en **AWS Academy** (o AWS).
- Instancia **EC2 Ubuntu Server 20.04/24.04** creada con:
  - Puerto **22 (SSH)** abierto.
  - Puerto **9090 (Prometheus)** abierto.
  - Puerto **9100 (Node Exporter)** abierto.
- Conocimientos básicos de Linux y seguridad en AWS.

---

## 2. Instalación de Prometheus

### 2.1 Actualizar el sistema
```bash
sudo apt update
sudo apt upgrade -y
```

### 2.2 Instalar Prometheus y Node Exporter
En Ubuntu 20.04/24.04 los paquetes oficiales ya están disponibles:
```bash
sudo apt install -y prometheus prometheus-node-exporter
```

### 2.3 Verificar servicios
```bash
systemctl status prometheus
systemctl status prometheus-node-exporter
```

Ambos deben aparecer como **active (running)**.

---

## 3. Acceso a la interfaz web

- **Prometheus**:  
  `http://<IP_PUBLICA_EC2>:9090`

- **Node Exporter (métricas del sistema)**:  
  `http://<IP_PUBLICA_EC2>:9100/metrics`

---

## 4. Actividad práctica

1. Documenta la instalación con **capturas de pantalla**:
   - Consola AWS (Security Group con puertos 22, 9090 y 9100).
   - Estado de los servicios con `systemctl`.
   - Interfaz web de Prometheus mostrando el dashboard.
2. Consulta básica:  
   En la interfaz de Prometheus busca la métrica:
   ```
   up
   ```
   y documenta el resultado.
3. Sube tu reporte final al repositorio personal en la carpeta:  
   `assignments/u1/prometheus/<matrícula>.md`

---

## 5. Rúbrica de evaluación

| Criterio                          | Excelente (100%)                           | Satisfactorio (80%)        | Insuficiente (50%)     | Nulo (0%)     |
|-----------------------------------|--------------------------------------------|----------------------------|------------------------|---------------|
| **Instancia EC2**                 | Instancia creada y puertos configurados     | Errores menores            | Fallos graves          | No entregado  |
| **Instalación Prometheus**        | Instalado y corriendo en puerto 9090        | Instalación con errores    | Servicio con fallos    | No entregado  |
| **Instalación Node Exporter**     | Instalado y visible en puerto 9100          | Instalación con errores    | No responde            | No entregado  |
| **Documentación y evidencias**    | Markdown completo con capturas              | Markdown incompleto        | Evidencia mínima       | No entregado  |

---

## 6. Conclusión
Con esta práctica el estudiante comprende cómo instalar y usar **Prometheus** en Ubuntu sobre AWS Academy, validando la recolección de métricas en tiempo real y su acceso vía web.

