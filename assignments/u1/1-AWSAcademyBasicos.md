<img width="568" alt="Screenshot 2025-01-29 at 12 15 32 p m" src="https://github.com/user-attachments/assets/22c50836-a301-4324-b37c-b57e810fdc72" />


# Práctica: Creación y gestión de una instancia EC2 con Asciinema

**Objetivo:**  
El estudiante será capaz de crear una instancia EC2 en AWS Academy, conectarse por SSH, instalar Asciinema, grabar una sesión de actualización del sistema operativo y herramientas básicas, y finalmente compartir el enlace de la grabación.

**Materiales:**
- Cuenta en AWS Academy
- Software de acceso SSH (puede ser mediante el panel de AWS o software como PuTTY o cualquier cliente SSH)
- Acceso a Internet

---

## Instrucciones:

### 1. Acceso a AWS Academy y creación de una instancia EC2:
- Ingresa a tu cuenta de **AWS Academy**.
- Crea una nueva **instancia EC2** con las siguientes especificaciones:
  - Selecciona una **Amazon Machine Image (AMI)** adecuada (por ejemplo, Ubuntu 20.04 LTS).
  - Escoge el **tipo de instancia** (recomendado: t2.micro).
  - Configura correctamente los **grupos de seguridad** (asegurándote de abrir el puerto 22 para SSH).

### 2. Conexión SSH:
- Utiliza el panel de AWS para conectarte por SSH o usa un cliente SSH (como PuTTY).
- Asegúrate de conectar usando una clave privada segura, y no expongas esta clave.

### 3. Instalación de Asciinema:
- Actualiza tu sistema con los siguientes comandos:
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
- Instala **Asciinema** usando el siguiente comando:
  ```bash
  sudo apt install asciinema
  ```
- Verifica que la instalación haya sido exitosa con:
  ```bash
  asciinema --version
  ```

### 4. Grabación con Asciinema:
- Inicia la grabación de la sesión de terminal:
  ```bash
  asciinema rec
  ```
- Escribe tu **nombre de usuario** o identificador en el terminal, precedido por el símbolo `#` (Ejemplo: `# Juan Pérez`).
- Ejecuta los comandos para actualizar el sistema y herramientas básicas:
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
- Detén la grabación con:
  ```bash
  Ctrl+D
  ```

### 5. Compartir el enlace de Asciinema:
- Una vez que se haya detenido la grabación, obtén el **enlace de la grabación** desde la interfaz de Asciinema.
- Accede al enlace de la grabación y **comparte el link** en **iDoceo** para su revisión.

**Nota Importante:**  
Recuerda que si no validas el enlace de grabación en un plazo de **7 días**, este se **expirará** y no podrá ser compartido ni revisado.

**RUBRICA**  
![Rubrica AWS Basico](https://github.com/user-attachments/assets/1b954623-d2dd-41db-b88a-b923bdd43a73)




