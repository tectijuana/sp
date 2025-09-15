<img width="512" height="256" alt="image" src="https://github.com/user-attachments/assets/71156c71-eae3-4ce8-94f3-17593c98def1" />


# Práctica: Instalación de Grafana en AWS (Ubuntu 20.04)

## Objetivo
El objetivo de esta actividad es que el estudiante despliegue **Grafana** en una instancia **EC2** con **Ubuntu 20.04**, utilizando la última metodología recomendada por los desarrolladores de Grafana (sin `apt-key`).  
Al finalizar la práctica tendrás un servidor Grafana funcionando, accesible desde el navegador, y conocerás la forma adecuada de iniciar sesión y realizar la configuración inicial.

---

## 1. Requisitos previos
- Cuenta activa en **AWS Academy** (o AWS).
- Conocimientos básicos de Linux.
- Instancia **EC2 Ubuntu 20.04 LTS** creada y con acceso (puerto **22 SSH** y **3000 TCP** abierto en el *Security Group*).

---

## 2. Instalación de Grafana

### 2.1 Actualizar el sistema
```bash
sudo apt update
sudo apt upgrade -y
```

### 2.2 Instalar dependencias necesarias
```bash
sudo apt-get install -y apt-transport-https software-properties-common wget
```

### 2.3 Importar la clave GPG y agregar el repositorio
```bash
wget -q -O - https://apt.grafana.com/gpg.key | \
  sudo gpg --dearmor -o /usr/share/keyrings/grafana.gpg

echo "deb [signed-by=/usr/share/keyrings/grafana.gpg] https://apt.grafana.com stable main" | \
  sudo tee /etc/apt/sources.list.d/grafana.list
```

### 2.4 Instalar Grafana
```bash
sudo apt update
sudo apt install -y grafana
```

### 2.5 Iniciar y habilitar el servicio
```bash
sudo systemctl enable --now grafana-server
sudo systemctl status grafana-server
```

---

## 3. Acceso a Grafana
- Abre tu navegador en:  
  `http://<IP_PUBLICA_EC2>:3000`
- Usuario por defecto: **admin**  
- Contraseña por defecto: **admin** (se pedirá cambiarla en el primer inicio de sesión):contentReference[oaicite:0]{index=0}.

---

## 4. Actividad práctica
1. Documenta los pasos en un archivo Markdown con **capturas de pantalla**:
   - Consola de AWS.
   - Estado del servicio.
   - Página de inicio de sesión de Grafana.
2. Cambia la contraseña de administrador y documenta el cambio.
3. Sube tu archivo final al repositorio GIST personal

---

## 5. Rúbrica de evaluación

| Criterio                        | Excelente (100%)                           | Satisfactorio (80%)         | Insuficiente (50%)      | Nulo (0%)     |
|--------------------------------|--------------------------------------------|-----------------------------|-------------------------|---------------|
| **Instancia EC2**              | Instancia creada y funcionando              | Errores menores             | Fallos graves           | No entregado  |
| **Instalación de Grafana**     | Servicio corriendo y accesible en el puerto 3000 | Instalación con errores menores | Servicio con errores | No entregado  |
| **Acceso y cambio de clave**   | Acceso correcto y clave cambiada            | Acceso con problemas menores | No se cambió la clave   | No entregado  |
| **Documentación y evidencias** | Markdown completo con capturas              | Markdown incompleto         | Evidencia mínima        | No entregado  |

---

## 6. Conclusión
Con esta práctica, el estudiante aprenderá a instalar y configurar **Grafana** en AWS, validar su funcionamiento y dejar evidencia.
