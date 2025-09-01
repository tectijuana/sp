

<div align="center">

<img width="568" alt="Screenshot 2025-01-29 at 12 15 32 p. m." src="https://github.com/user-attachments/assets/22c50836-a301-4324-b37c-b57e810fdc72" />

# Práctica: Creación y Gestión de una Instancia EC2 con Asciinema

</div>

---

### 🎯 **Objetivo**

El estudiante será capaz de:

* Crear una instancia EC2 en AWS Academy.
* Conectarse mediante SSH.
* Instalar y utilizar Asciinema para grabar una sesión de terminal.
* Ejecutar la actualización del sistema operativo y herramientas básicas.
* Compartir el enlace de la grabación.

---

### 📋 **Materiales necesarios**

* Cuenta activa en **AWS Academy**.
* Cliente SSH (puede ser desde el navegador de AWS, **PuTTY** o cualquier otro).
* Conexión a Internet estable.

---

## 🛠️ **Instrucciones**

### 1. Acceso a AWS y creación de la instancia EC2

1. Ingresa a tu cuenta de **AWS Academy**.
2. Crea una nueva instancia **EC2** con las siguientes especificaciones:

   * **AMI**: Ubuntu 20.04 LTS (u otra versión compatible).
   * **Tipo de instancia**: `t2.micro` (recomendada).
   * Configura correctamente los **grupos de seguridad**:

     * Asegúrate de **habilitar el puerto 22 (SSH)**.

---

### 2. Conexión mediante SSH

* Conéctate a tu instancia usando:

  * El panel web de AWS, o
  * Un cliente SSH como **PuTTY** o **Terminal** (Linux/macOS).
* Utiliza tu **clave privada (.pem)** de forma segura. **No compartas** este archivo.

---

### 3. Instalación de Asciinema

1. Actualiza tu sistema operativo:

   ```bash
   sudo apt update
   sudo apt upgrade
   ```
2. Instala Asciinema:

   ```bash
   sudo apt install asciinema
   ```
3. Verifica la instalación:

   ```bash
   asciinema --version
   ```

---

### 4. Grabación de sesión con Asciinema

1. Inicia la grabación:

   ```bash
   asciinema rec
   ```
2. En el terminal, escribe tu **nombre o identificador**, precedido por `#` (ejemplo: `# Juan Pérez`).
3. Ejecuta nuevamente la actualización del sistema:

   ```bash
   sudo apt update
   sudo apt upgrade
   ```
4. Finaliza la grabación presionando:

   ```bash
   Ctrl + D
   ```

---

### 5. Compartir la grabación

* Al terminar, **copia el enlace** generado por Asciinema.
* Asegúrate de acceder al enlace para **validarlo** (si no se valida en 7 días, se eliminará).
* Comparte el enlace en **iDoceo** para su evaluación.

---

### ⚠️ Nota importante

> Si no validas el enlace de Asciinema en un plazo máximo de **7 días**, este se **expirará** y **no podrá recuperarse**.

---

### 📊 **Rúbrica de evaluación**

<div align="center">

![Rúbrica AWS Básico](https://github.com/user-attachments/assets/1b954623-d2dd-41db-b88a-b923bdd43a73)

</div>

