# Practica # 0 
## Creación de instancia EC2 Ubuntu AWS y Raspberry Pi 4 AVH
### Joel Cuevas Estrada - 22210298
## Crearción y ejecución de instancia EC2
Primero se ingresa a AWS y se inicia sesión, posteriormente nos vamos a la opción de instancias | EC2 donde se mirara un menú como este:

![image](https://github.com/user-attachments/assets/cded1885-ca7a-44f4-b760-7c8344ed0627)

Damos click en "Lanzar instancias" y en el siguiente menú:

![image](https://github.com/user-attachments/assets/51f96af5-fb75-4cc2-a093-358dcab0ce60)

Seleccionamos Ubuntu en la sección de "Imágenes de aplicaciones y sistemas operativos (Imagen de máquina de Amazon)" y le asignamos un nombre a la instancia en "Nombres y etiquetas", el aprtado de tipo de instancia lo dejamos como t2.micro. Para proceder a crear un par de claves .pem y las guardamos en el dispositivo IMPORTANTE recordar el directorio donde se guardaron la clave .pem

Luego al crear y ejecutar la instancia procedemos a conectarnos desde consola en el directorio donde se guardó la clave pem, utilizando SSH en Windows 11 corriendo este codigo:

````powershell
ssh -i "papure.pem" ubuntu@ec2-54-161-232-226.compute-1.amazonaws.com
````

### Practica #0 dentro de Ubuntu EC2 AWS
Una vez dentro se realizó la practica ejecutando los siguientes comandos en la consola

````bash
sudo apt update
````

````bash
sudo apt upgrade
````
Se mostrará como se ejecutaron los comandos en el siguiente link:

## Grabación Asciinema:

[![asciicast](https://asciinema.org/a/SItBv8O4tXgllJ40lNpYmnGVt.svg)](https://asciinema.org/a/SItBv8O4tXgllJ40lNpYmnGVt)

## Creción y ejecución de Raspberry Pi 4 AVH

[![asciicast](https://asciinema.org/a/nvPs2VpgasCCBkBCJCLbh5GG3.svg)](https://asciinema.org/a/nvPs2VpgasCCBkBCJCLbh5GG3)
