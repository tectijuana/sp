# Integración de sensores MEMS en plataformas programables

## Galeana Leja Jesus Eduardo - 22211565

# Introducción

### Sensor MEMS (Micro-Electro-Mechanical Systems)
Un sensor MEMS es un sistema microelectromecánico que nos permite detectar cambios magnéticos, mecánicos e incluso químicos, para convertirlos en información eléctrica. Dependiendo de la construcción que contenga, los sensores MEMS pueden medir presión, movimiento, aceleración, temperatura o gas, permitiendo realizar funciones importantes en los dispositivos electrónicos.

![Imagen de un sensor MEMS](https://www.bosch-sensortec.com/media/boschsensortec/products/product_overview/16_10/bosch_sensortec-productoverview-stage-16-9_res_800x450.jpg)

### Plataforma programable.
Una plataforma programable es aquella que permite crear un entorno para crear programas por medio de algún lenguaje específico, por lo que los lenguajes de programación, los sistemas operativos o las consolas de videojuegos podrían entrar dentro de la categoría de plataforma programable.

# Integración de sensores MEMS en Arduino
Un estudiante de la universidad politécnica de Cataluña realizó un proyecto que tomó de base la investigación de los sensores MEMS para una variedad de magnitudes físicas. Para realizar esta labor, el alumno decidió hacer un sistema de hardware que incluía un stack de placas, contando entre estas placas, con una placa Arduino DUE que se encarga de comunicar a los componentes con la placa base.

![Imagen de un Arduino DUE](https://www.openhacks.com/uploadsproductos/arduinodue_front.jpg)

Se utilizan dos sensores dentro del sistema, siendo un sensor de referencia LIS3MDL, utilizado como un sensor magnético de tres ejes con una resolución de 16 bits, y el otro es un sensor de temperatura LM95071, el cual cuenta con una resolución de temperatura de señal de 13 bits y una sensibilidad de 0.03125˚C/LSB, permitiendo un rango desde -40˚C hasta 150˚C. 
Para comunicar el sensor de temperatura con el Arduino, se utiliza una comunicación SPI.

Para poder implementar el sensor de temperatura en Arduino, el alumno realizó el sketch en Arduino para poder comunicarse con el sensor, verificando el que funcionara correctamente por medio del monitor serie. Para que contenga un funcionamiento correcto, requiere de la recepción de dos bytes, por lo cual implementó SPI_CONTINUE dentro de la transmisión de la siguiente forma:

```text
byte response1 = SPI.transfer(53, 0x00, SPI_CONTINUE);
byte response2 = SPI.transfer(53, 0x00);
```

Posteriormente, se procede a juntar los dos bytes dentro de un mismo integer para prescindir de los bits más significativos, multiplicando por 0,031125 (LSB) para obtener el resultado en grados celsius.
```text
value=response1<<8;
value = value | response2;
value = value>>2;
value=value*0.031125;
```

Esto le permitió realizar el envío de datos por medio de la comunicación SPI, así como realizar la medida del sensor de temperatura por medio de Instrumentino, faltando únicamente la implementación de la lectura de datos. Esta última se consigue por medio de una función dentro de Controlino llamada cmdSpiRead, la cual permite retornar un valor al software de Instrumentino en Instrumentino return SPI.transfer(53,strtol(argV[i], NULL, 10)).

Para inicializar el sensor magnético, utilizó la variable ScaleLIS3mDL junto con la variable Valpot dentro de Controlino, las cuales permiten inicializar el magnetómetro y el potenciómetro con los valores deseados
```text
#define ScaleLIS3MDL 0x00
#define ValPot 0xFA
```
La variable se manda a llamar posteriormente dentro del setup() del programa utilizando la función mag.writeReg(LIS3MDL::CTRL_REG2,ScaleLIS3MDL).

# Conclusión
El uso de una plataforma programable es una parte fundamental para el uso de los sensores MEMS, ya que estas plataformas permiten que se puedan utilizar dichos sensores de forma correcta dentro de un sistema, así como programar las funciones que pueden llegar a tener dichos sensores, como se pudo apreciar en el caso del sensor de temperatura dentro del sistema de Controlino.

# Referencias
* Euroinnova International Online Education. (2024, 5 julio). plataformas de programacion. https://www.euroinnova.com/blog/plataformas-de-programacion#plataformas-de-programacion
* MEMS sensors. (s. f.). Bosch Sensortec. https://www.bosch-sensortec.com/about-us/our-company/mems/
* Forrellad Munné, E. (2017). MEMS Sensor Data Acquisition Framework Based on Arduino Platform (Trabajo de Fin de Grado). Universitat Politècnica de Catalunya. https://upcommons.upc.edu/handle/2117/106686.

 ```text
Asistencia de IA: Se utilizó la IA para obtener fuentes de información acerca del tema abarcado en la investigación.
Herramienta: ChatGPT (GPT-5)
Fecha: 17/09/2025
  ```

