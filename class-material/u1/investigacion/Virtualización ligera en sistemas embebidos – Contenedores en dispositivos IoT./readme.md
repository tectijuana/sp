 **Karla Itzel Vazquez Cruz 22211671**


### **Virtualización ligera en sistemas embebidos – Contenedores en dispositivos IoT**

La virtualización ligera a través de contenedores, como Docker o LXC, se ha posicionado como una tecnología fundamental para los **sistemas embebidos** y **dispositivos IoT (Internet of Things)**. A diferencia de la virtualización tradicional con máquinas virtuales, los contenedores ofrecen mayor eficiencia en el uso de recursos, portabilidad y escalabilidad.

![LXC](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Linux_Containers_logo.svg/1200px-Linux_Containers_logo.svg.png)
![Docker](https://www.stackhero.io/assets/src/images/servicesLogos/openGraphVersions/docker.png?d87f4381)


-----

### **Virtualización ligera vs. Virtualización tradicional**

| Característica | Máquinas Virtuales | Contenedores |
|---|---|---|
| Consumo de recursos | Alto (emulación completa del SO) | Bajo (comparten kernel del host) |
| Tiempo de arranque | Lento (minutos) | Rápido (segundos) |
| Adecuado para IoT | No | Sí |

-----

### **Beneficios principales en dispositivos IoT**

Los contenedores son ideales para el ecosistema IoT debido a sus múltiples ventajas:

  * **Ligereza:** Utilizan una mínima cantidad de memoria y CPU, lo que es crucial para hardware limitado.
  * **Portabilidad:** Un mismo contenedor puede ejecutarse de manera consistente en diferentes entornos, desde un PC hasta un dispositivo en el borde de la red.
  * **Actualizaciones remotas:** Facilitan las actualizaciones de firmware y software de forma segura y uniforme.
  * **Aislamiento de procesos:** Mejoran la seguridad al aislar cada aplicación en su propio entorno, evitando que una falla en una afecte a las demás.

-----

### **Aplicaciones comunes**

  * **Sensores inteligentes:** Utilizan contenedores para ejecutar aplicaciones que recopilan datos y los envían a través de protocolos como MQTT.
  * **Gateways IoT:** Emplean contenedores para aislar servicios de conectividad, enrutamiento y procesamiento de datos en el edge.
  * **Actualizaciones OTA (Over-The-Air):** Permiten actualizar una aplicación en un contenedor específico sin afectar el resto del sistema, lo que reduce el riesgo de fallas y simplifica el mantenimiento.

-----

### **Arquitectura básica**

En esta arquitectura, el **hardware** del dispositivo ejecuta un sistema operativo anfitrión que, a su vez, corre un **motor de contenedores**. Dentro de este motor, se ejecutan las **aplicaciones en contenedores**, cada una con su propio entorno aislado pero compartiendo el kernel del sistema anfitrión.

-----

### **Comandos de ejemplo con Docker**

```bash
# Descargar una imagen ligera de MQTT
docker pull eclipse-mosquitto:latest

# Ejecutar el contenedor en el puerto 1883
docker run -it -p 1883:1883 eclipse-mosquitto

# Listar los contenedores en ejecución
docker ps
```

-----

### **Conclusiones**

La virtualización ligera mediante contenedores se ha convertido en una solución esencial para el ecosistema IoT. Su capacidad para optimizar recursos, mejorar la seguridad y facilitar el despliegue la convierte en una tecnología fundamental para el desarrollo y la gestión de dispositivos conectados.

-----

### **Referencias**

  * Morabito, R. (2017). *Virtualization on internet of things edge devices with container technologies: A performance evaluation*. IEEE Access, 5, 8835-8850. [https://doi.org/10.1109/ACCESS.2017.2704444](https://doi.org/10.1109/ACCESS.2017.2704444)
  * Dautov, R., Distefano, S., & Buyya, R. (2019). *Hierarchical data fusion for smart IoT applications*. IEEE Internet of Things Journal, 6(2), 3416-3427. [https://doi.org/10.1109/JIOT.2018.2874535](https://doi.org/10.1109/JIOT.2018.2874535)
  * Felter, W., Ferreira, A., Rajamony, R., & Rubio, J. (2015). *An updated performance comparison of virtual machines and Linux containers*. IEEE International Symposium on Performance Analysis of Systems and Software, 171-172. [https://doi.org/10.1109/ISPASS.2015.7095802](https://doi.org/10.1109/ISPASS.2015.7095802)
