# **Diseño de sistemas programables para control de drones**
## Castillo Enriquez Hugo - 22211532

Un sistema programado es un circuito electrónico que contiene un microprocesador o un microcontrolador integrado en el mismo. Mediante un programa informático almacenado en una memoria interna, se realiza el control y la gestión del sistema.

## **Drones**
Los drones son uno de los dispositivos más utilizados en la actualidad, cada vez son más las ventajas presentes gracias a estos equipos, ya sea para control fronterizo, labores informativas, cultivo agrícola, etc., son variados los usos que se les dan de forma habitual. El desarrollo de software para el control de drones es un mercado en auge que se va posicionando cada vez más.

Los drones han transformado varios ámbitos de aplicación, ya que son capaces de realizar funciones civiles, como vigilar el tráfico o cultivos agrícolas, retransmitir imágenes aéreas, entregar mercancías, transportarlas, realizar servicios forestales, de emergencia, de rescate y de salvamento de personas, entre muchas otras aplicaciones. 

<img width="830" height="553" alt="image" src="https://github.com/user-attachments/assets/4b4b6e2d-9f62-40fb-94ca-09d6d86b342c" />


## **¿Qué son las aplicaciones de control de drones?**
Existen diferentes SDKs (Software Development Kit - Kit de Desarrollo de Software) de los que pueden disponer los desarrolladores para crear aplicaciones para el control de drones, así como aplicaciones que permiten manejarlos desde un teléfono inteligente. Estas aplicaciones envían señales de radio para controlar el dron.

Asimismo, los SDK permiten a los usuarios controlar el dron desde cualquier sistema conectado al piloto automático de la aeronave a través de una interfaz disponible de serie. Incluso, hay APIs, disponibles que permiten al desarrollador crear un algoritmo capaz de controlar el dron usando cualquier tipo de lenguaje de programación y para distintos sistemas operativos.

## **¿Qué es el desarrollo de software para drones?**
El proceso de creación, desarrollo e implementación de software que permite a los drones realizar actividades sofisticadas, ya sea de forma independiente o bajo supervisión humana, se denomina Desarrollo de Software para Drones. Este software, que actúa como el cerebro del dron, combina hardware como sensores, cámaras, módulos GPS y conexiones de red para un funcionamiento impecable. El proceso implica varias capas críticas:

- Operando directamente en el controlador de vuelo del dron, ejecuta funciones en tiempo real como estabilización, navegación y procesamiento de datos del sensor.
- Ofrece a los pilotos o sistemas automatizados interfaces para controlar protocolos de emergencia, cargas útiles y trayectorias de vuelo.
- Para usos que incluyen topografía, agricultura y construcción, el software de mapeo con drones permite que los drones recopilen, procesen y muestren datos geoespaciales.
- Aplicaciones de escritorio o móviles que permiten a los usuarios planificar misiones, rastrear aeronaves y examinar datos recopilados.
- Permitir la integración con sistemas de terceros, plataformas en la nube o procesos corporativos personalizados.

## **Conclusiones clave para el mercado de software para drones**
- Impulsados ​​por sectores como la agricultura, la construcción y la logística, los drones comerciales cubren más del _60%_ de la demanda de software.
- Para la agrimensura, la minería y la inspección de infraestructura, el uso de software de mapeo con drones está aumentando rápidamente.
- Norteamérica, Europa y Asia-Pacífico son las principales áreas de desarrollo de software para drones. India y China muestran una notable expansión.
- El mejor software de control de drones ahora estandariza las capacidades impulsadas por IA, incluido el análisis de datos en tiempo real, la navegación autónoma y la detección de objetos.
- Más del _70%_ de los operadores de drones planifican misiones, almacenan datos y gestionan flotas utilizando sistemas basados ​​en la nube.
- Las grandes empresas están impulsando el desarrollo de software empresarial personalizado a medida que buscan soluciones personalizadas para la integración de datos, la seguridad y la gestión de flotas.

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/3811920c-4cee-48ef-9047-67c799df8754" />

## **Componentes clave de la arquitectura del software de drones**
### 1. Adquisición y procesamiento de datos de sensores
Este módulo, que procesa datos en tiempo real, recopila información de sensores integrados como GPS, IMU, cámaras y LiDAR. Sus algoritmos avanzados proporcionan un conocimiento situacional preciso mediante el filtrado de ruido, la calibración de lecturas y la fusión de flujos de datos. Aplicaciones como el software de mapeo de drones y la navegación autónoma dependen de la integración de sensores.

### 2. Sistema de control de vuelo (FCS)
Responsable de estabilizar el dron, ejecutar las órdenes de vuelo y controlar los protocolos de seguridad, el FCS es el núcleo del software de control de drones. Mantiene las rutas de vuelo preferidas interpretando la entrada del piloto o las instrucciones autónomas y modificando las superficies de control y la velocidad del motor. Un FCS robusto garantiza una respuesta rápida a los cambios ambientales y una maniobrabilidad precisa.

### 3. Sistema de comunicación
Un sistema de comunicación confiable conecta el dron con otros drones, servicios en la nube o centros de control terrestre. Esto incluye protocolos de datos seguros, módulos 4G/5G y transceptores de radio. Para mantener la conexión y evitar la pérdida de datos, el software de comunicación controla la telemetría, la entrega de comandos y los procedimientos de seguridad.

### 4. Sistema de gestión de carga útil
Muchos drones llevan cargas útiles especializadas, como cámaras, sensores, paquetes de entrega o pulverizadores agrícolas. Estos dispositivos están controlados por el sistema de gestión de carga útil, que también coordina la recopilación de datos y la distribución de energía. La integración personalizada de la carga útil suele ser un factor diferenciador clave para los servicios de desarrollo de software para drones .

### 5. Sistema de gestión de energía 
Maximizar el tiempo de vuelo y la seguridad depende de una gestión eficaz de la energía. Si los niveles de energía disminuyen, este programa monitorea el estado de la batería, pronostica el tiempo de vuelo restante y activa procedimientos de aterrizaje de emergencia o regreso al punto de origen. Los sistemas avanzados maximizan el consumo de energía según los perfiles de la misión y los requisitos de la carga útil.

### 6. Interfaz de usuario(UI) y Software de la Estación de Control Terrestre(GCS)
El GCS(Ground Control Station Software - Software de la Estación de Control Terrestre) y la interfaz de usuario ofrecen a los usuarios funciones sencillas para la visualización de datos, la monitorización en tiempo real y la planificación de misiones. Entre las funciones se incluyen registros de misión, paneles de telemetría, transmisiones de vídeo en directo y mapas interactivos. Tanto para usuarios principiantes como experimentados, una interfaz de usuario bien diseñada es fundamental, ya que mejora la usabilidad y reduce el riesgo operativo.

### 7. Kit de desarrollo de software y capa API
Las API y los SDK permiten a los desarrolladores crear aplicaciones a medida, conectarse con sistemas de terceros o mejorar las funciones de los drones. Los servicios líderes de desarrollo de software facilitan la innovación rápida y la expansión del ecosistema al proporcionar SDK robustos de control de vuelo, acceso a datos e integración en la nube. 

### 8. Sistema operativo y middleware
La mayoría de los drones operan con distribuciones ligeras de Linux o sistemas operativos embebidos en tiempo real (RTOS). El middleware garantiza un flujo de datos constante y la gestión de recursos gestionando la comunicación entre el hardware, los sensores y las capas de aplicación. El software de programación de drones se basa en el sistema operativo y el middleware, lo que facilita la modularidad y la escalabilidad.

## Conclusiones
El diseño de drones y sus respectivos controladores representa un campo en constante evolución. Gracias a el uso de microcontroladores es posible el desarrollo de estos drones y el mismo constante crecimiento en el campo lleva a un gran avance de oportunidades e ideas de implementación en drones. Como se menciona en la investigación, los drones tienen muchas aplicaciones en la vida cotidiana, asi como muchas de las tecnologías actuales, para reducir la mano de obre o por decirlo de otra manera _facilitar_ muchos trabajos de alto rendimiento (agricultura, entrega de mercancia, videovigilancia, étc.).

Con el avance tecnológico que se lleva a cabo día con día asegura que los drones son una pequeña parte del gran esquema de herramientas que podrán agilizar el trabajo en muchas industrias para cada vez ser más eficientes.



## Referencias
- Ramirez, O. (2023, 12 diciembre). Desarrollo de software para control de drones. Bambu Mobile. https://bambu-mobile.com/desarrollo-de-software-para-control-de-drones 
- Sharma, A. (2025, 7 julio). The Ultimate Guide to Drone Software Development: From Idea to Flight. A3Logics. https://www-a3logics-com.translate.goog/blog/drone-software-development/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
- Elbachouti Khalil, W. E. K. (2023). Implementación de Máquina de Estados Finita en Microcontrolador para optimizar el control del sistema de energía de un dron híbrido pila de combustible-batería [Trabajo Fin de Grado Grado en Ingeniería Electrónica Industrial y Automática]. UNIVERSITAT POLITÈCNICA DE VALÈNCIA.
- Colaboradores de Wikipedia. (2019, 21 octubre). Sistema programado. Wikipedia, la Enciclopedia Libre. https://es.wikipedia.org/wiki/Sistema_programado#:~:text=Un%20sistema%20programado%20es%20un,y%20la%20gesti%C3%B3n%20del%20sistema.
