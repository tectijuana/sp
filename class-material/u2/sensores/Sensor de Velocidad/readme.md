#### 📌 Sensor de Velocidad
**Nombre:** Carlos Alberto Iñiguez Gallego<br>
**Número de Control:** 19211660<br>
**GitHub:** [CarlosAlberto193](https://github.com/CarlosAlberto193)

# ¿Que es un Sensor de Velocidad?
En la era actual, donde la eficiencia y la precisión son elementos esenciales para mantener la competitividad en la industria, y los distintos tipos de sensores de velocidad se han convertido en una pieza fundamental en el rompecabezas de la producción. La demanda de productos más rápidos y de mayor calidad ha llevado a una creciente dependencia de estos dispositivos, que se han vuelto cada vez más sofisticados y versátiles.

Son dispositivos electrónicos diseñados para medir la velocidad de objetos en movimiento. Estos objetos pueden ser desde una cinta transportadora en una planta de envasado hasta las aspas de un aerogenerador en un parque eólico. La información que proporcionan estos sensores es invaluable para optimizar procesos, mejorar la seguridad y garantizar un control preciso en la producción.

En este documento, analizaremos el funcionamiento, aplicaciones, ventajas y desventajas de tres tipos de sensores de velocidad: sensores de efecto Hall, encoders y sensores de corrientes de Foucault.

## 1️⃣Sensor de Efecto Hall1️⃣
<p align="center">
  <img src="https://paraarduino.com/wp-content/uploads/2023/12/modulo_efecto_hall_ky-003.jpg" width="500">
</p>
Edwin Herbert Hall obtuvo los primeros indicios del efecto que ahora lleva su nombre durante octubre de 1879; El efecto Hall es descrito usualmente como la potencia diferencial que aparece perpendicular a las líneas del flujo de una corriente eléctrica, cuando ésta es sometida a la fuerza perpendicular de un campo magnético.

El efecto Hall implica necesariamente un material conductor a través del cual transita corriente eléctrica y sobre la cual se ejerce una fuerza magnética de manera perpendicular. En términos prácticos, a una placa conductora se le aplica un voltaje en sus extremos, por lo que, los electrones comienzan a fluir linealmente del polo negativo al positivo; sin embargo, al acercarles un imán de forma perpendicular, las cargas positivas y negativas son enviadas hacia los extremos transversales y se produce, con ello el voltaje transversal Hall (VH).

### Aplicaciones
- Servomotores.
- Sensores de Torniquetes para Control de Acceso.
- Sensores de Velocidad
- Sistema de Inyección de Motores Automovilísticos
- Medición de Control, Potencia y Campo Magnético
- Control de Motores Lineales
- Sensores de Proximidad
- Control de Rotación

### Ventajas y Desventajas
| Ventajas | Desventajas |
|----------|-------------|
| Alta precisión en la medición de velocidad rotacional. | Sensibles a interferencias electromagnéticas, lo que puede afectar la precisión. |
| Sin contacto físico, lo que reduce el desgaste mecánico. | Requieren un imán o campo magnético para funcionar. |
| Funciona en ambientes hostiles (suciedad, agua, polvo). | Limitados a detectar materiales ferromagnéticos. |
| Larga vida útil, ya que no tiene partes móviles. | Dependencia de la distancia, el rendimiento varía según la posición del sensor. |

### Ejemplo Practico
Este código lee un sensor de efecto Hall conectado al pin 5 de Arduino y, dependiendo de su estado, enciende o apaga un LED en el pin 13.
```c
const int HALLPin = 5;
const int LEDPin = 13;

void setup() {
  pinMode(LEDPin, OUTPUT);
  pinMode(HALLPin, INPUT);
}

void loop() {
  if(digitalRead(HALLPin)==HIGH)
  {
    digitalWrite(LEDPin, HIGH);   
  }
  else
  {
    digitalWrite(LEDPin, LOW);
  }
}

```

## 2️⃣Sensor Doppler2️⃣
<p align="center">
  <img src="https://uelectronics.com/wp-content/uploads/2019/08/FRONT-800x800.jpg" width="500">
</p>
Un medidor de flujo ultrasónico (medidor de flujo Doppler no intrusivo) es un medidor de flujo volumétrico que requiere partículas o burbujas en el flujo. Los medidores de flujo ultrasónicos son ideales para aplicaciones de aguas residuales o cualquier líquido sucio que sea conductivo o a base de agua.

El principio de funcionamiento básico emplea el cambio de frecuencia (efecto Doppler) de una señal ultrasónica cuando la reflejan partículas suspendidas o burbujas de gas (discontinuidades) en movimiento. Esta técnica de medición usa el fenómeno físico de una onda de sonido que cambia de frecuencia cuando se refleja en una discontinuidad en movimiento en un líquido que está fluyendo. Las ondas ultrasónicas se transmiten a un tubo con líquidos que fluyen, y las discontinuidades reflejan la onda de ultrasonido con una frecuencia ligeramente diferente que es directamente proporcional al flujo del líquido.

### Aplicaciones
- Sirenas de las ambulancias
- Mediciones en astronomía
- Radares de tráfico
- Detección de Movimiento en Sistemas de Seguridad y Alarmas Perimetrales.
- Medición de Velocidad en Procesos Industriales, como Cintas Transportadoras.
- Monitoreo de Vibraciones y Maquinaria Rotativa para Mantenimiento Predictivo.


### Ventajas y Desventajas
| Ventajas | Desventajas |
|----------|-------------|
| No requiere contacto físico con el objeto, lo que reduce el desgaste y la interferencia mecánica. | Es más caro que sensores mecánicos o infrarrojos, debido a su tecnología avanzada. |
| Ideal para detectar movimientos pequeños y medir velocidades en tiempo real. | Puede verse afectado por otros dispositivos electrónicos cercanos. |
| Puede operar en lluvia, niebla o de noche, a diferencia de sensores ópticos. | Si el objeto no refleja bien la señal, la medición puede ser imprecisa. |
| Se usa en tráfico, meteorología, medicina, seguridad e industria. | Para obtener mediciones correctas, debe ajustarse según la distancia y el entorno. |

### Ejemplo Practico
Este código lee un sensor de radar conectado al pin 2 de Arduino y, si detecta un objeto (HIGH), hace parpadear un LED en el pin 13 con un retraso de 50 ms; de lo contrario, el LED permanece apagado.
```c
const int LEDPin = 13;
const int RadarPin = 2;

void setup()
{
  pinMode(LEDPin, OUTPUT);
  pinMode(RadarPin, INPUT);
}

void loop()
{
  int value= digitalRead(RadarPin);

  if (value == HIGH)
  {
    digitalWrite(LEDPin, HIGH);
    delay(50);
    digitalWrite(LEDPin, LOW);
    delay(50);
  }
  else
  {
    digitalWrite(LEDPin, LOW);
  }
```
## 3️⃣Sensor Encoder3️⃣
<p align="center">
  <img src="https://http2.mlstatic.com/D_NQ_NP_689002-MLM40853808730_022020-O.webp" width="500">
</p>
Un encoder es un dispositivo de detección que proporciona una respuesta. Los Encoders convierten el movimiento en una señal eléctrica que puede ser leída por algún tipo de dispositivo de control en un sistema de control de movimiento, tal como un mostrador o PLC. El encoder envía una señal de respuesta que puede ser utilizado para determinar la posición, contar, velocidad o dirección.

### Aplicaciones
- Utilizado por Fabricantes de Cintas Transportadoras
- Manejo de Materiales
- Industria de Impresion y Etiquetado
- Fabricante de Maquinas Personalizadas
- Embalaje
- Serie R
### Ventajas y Desventajas
| Ventajas | Desventajas |
|----------|-------------|
| Especialmente en los encoders ópticos, permiten mediciones exactas de posición y velocidad. | En los encoders ópticos, los contaminantes pueden afectar la precisión de la lectura. |
| En el caso de encoders ópticos o magnéticos, no hay contacto directo con las partes móviles. | Si no se instalan correctamente (Rigurosamente), pueden generar errores en la medición. |
| Se integran fácilmente en sistemas de control automatizados. | En el caso de encoders absolutos, para mantener la posición. |
| Los incrementales son ideales para velocidad y los absolutos para posición exacta sin necesidad de reinicio. | Encoders de alta resolución o con tecnología avanzada pueden ser costosos. |
### Ejemplo Practico
Este código lee un encoder rotatorio conectado a los pines 9 y 10 de Arduino, detecta cambios en los estados de los canales A y B para determinar la dirección de giro, ajusta un contador de posición dentro de un rango de 0 a 255 y muestra el valor actualizado en el monitor serial si ha cambiado.
```c
const int channelPinA = 9;
const int channelPinB = 10;
unsigned char stateChannelA;
unsigned char stateChannelB;
unsigned char prevStateChannelA = 0;
const int maxSteps = 255;
int prevValue;
int value;
const int timeThreshold = 5; 
unsigned long currentTime;
unsigned long loopTime;
bool IsCW = true;
void setup() {
  Serial.begin(9600);
  pinMode(channelPinA, INPUT);
  pinMode(channelPinB, INPUT);
  currentTime = millis();
  loopTime = currentTime;
  value = 0;
  prevValue = 0;
}
void loop() {
  currentTime = millis();
  if (currentTime >= (loopTime + timeThreshold))
  {
    stateChannelA = digitalRead(channelPinA);
    stateChannelB = digitalRead(channelPinB);
    if (stateChannelA != prevStateChannelA)  // Para precision simple if((!stateChannelA) && (prevStateChannelA))
    {
      if (stateChannelB) // B es HIGH, es CW
      {
        bool IsCW = true;
        if (value + 1 <= maxSteps) value++; // Asegurar que no sobrepasamos maxSteps
      }
      else  // B es LOW, es CWW
      {
        bool IsCW = false;
        if (value - 1 >= 0) value = value--; // Asegurar que no tenemos negativos
      }
    }
    prevStateChannelA = stateChannelA;  // Guardar valores para siguiente
    // Si ha cambiado el valor, mostrarlo
    if (prevValue != value)
    {
      prevValue = value;
      Serial.print(value);
    }
    loopTime = currentTime;  // Actualizar tiempo
  }
  
  // Otras tareas
}
```

## 📠Referencias Tecnicas
### Sensor de Efecto Hall
Datasheets oficiales: A3144 Hall Effect Sensor, Allegro Microsystems.

Guías técnicas: "Understanding Hall Effect Sensors," Texas Instruments, 2019.

Ejemplos de implementación: Arduino Documentation, Hall Effect Sensor Projects on GitHub.
### Sensor Doppler
Datasheets oficiales: RCWL-0516 Doppler Radar Sensor Module.

Guías técnicas: "Doppler Radar Fundamentals," National Instruments, 2020.

Ejemplos de implementación: Arduino Doppler Radar Applications, GitHub Projects.
### Sensor Encoder
Datasheets oficiales: EC11 Encoder, Bourns Inc.

Guías técnicas: "Rotary Encoders: Types and Applications," Encoders Technology, 2021.

Ejemplos de implementación: Arduino Encoder Projects, GitHub Implementations.

## 🔖Bibliografia
- Structuralia. (2023, noviembre 13). Los tipos de sensores de velocidad y sus aplicaciones en la industria. Structuralia. https://blog.structuralia.com/tipos-sensores-velocidad
- Scribd. (n.d.). Tipos de sensores para microcontroladores. Scribd. https://es.scribd.com/document/386715803/Tipos-de-Sensores-Para-Microcontroladores
- Urany. (n.d.). Adquiere precisión con efecto Hall. Urany.net. https://urany.net/blog/adquiere-precisi%C3%B3n-con-efecto-hall
- Llamas, L. (n.d.). Detectar campos magnéticos con Arduino y sensor Hall A3144. Luis Llamas. https://www.luisllamas.es/detectar-campos-magneticos-con-arduino-y-sensor-hall-a3144/
- Omega. (n.d.). Medidor de flujo ultrasónico. Omega. https://mx.omega.com/prodinfo/medidor-de-flujo-ultrasonico.html
- OneAir. (n.d.). ¿Qué es el efecto Doppler?. OneAir. https://www.oneair.es/que-es-el-efecto-doppler/
- Llamas, L. (n.d.). Arduino Motion Detector RCWL-0516. Luis Llamas. https://www.luisllamas.es/en/arduino-motion-detector-rcwl-0516/
- Encoder. (n.d.). ¿Qué es un encoder?. Encoder. https://www.encoder.com/article-que-es-un-encoder
- LogicBus. (n.d.). Aplicación de encoders en la industria. LogicBus. https://www.logicbus.com.mx/encoder-app-industria
- Llamas, L. (n.d.). Arduino encoder rotativo. Luis Llamas. https://www.luisllamas.es/arduino-encoder-rotativo/
