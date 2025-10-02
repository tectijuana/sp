**Instituto Tecnológico de Tijuana**

**Ing. Sistemas Computacionales**

**Prof. René Solis Reyes**

**Sistemas Programables**

**Luis Manuel Ramón Hernández 22211639**

# Aplicaciones médicas conectadas mediante MQTT en tiempo real

## Introducción
El protocolo MQTT (Message Quening Telemetry Transport) está revolucionando la atención médica al permitir la conexión de dispositivos médicos en tiempo real
lo que facilita el monitoreo remoto y la recopilación instantánea de datos del paciente. Su diseño ligero y eficiente lo hace ideal para su uso en dispositivos
con recursos limitados, como sendores portátles y rquipos de monitoreo en el hogar.

**Aplicaciones médicas en tiempo real**

Las aplicaciones de MQTT en el campo de la medicina son variadas y se centran en mejorar la atención del paciente y la eficiencia de los servicios de salud.

<img width="557" height="350" alt="image" src="https://github.com/user-attachments/assets/959715ea-5564-44ce-9c53-64cbb5c1a8b8" />

**Monitoreo remoto de pacientes**

Una de las aplicaciones más signicativas de MQTT es el monitoreo remoto de pacientes. Los dispositivos médicos equipados con sensores, como monitores de glucosa, 
oxímetros de pulso y monitores de electrocardiograma (ECG), pueden transmitir datos vitales en tiempo real a una plataforma central. Esto permite a los profesionales
de la salud supervisar continuamente el estado de los pacientes, especialmente aquellos con enfermedades crónicas, y recibir alertas inmediantas sobre cualquier anoma-
lía. Por ejemplo, un sistema puede medir la temperatura corporal y enviar los datos a un intermediario MQTT, permitiendo que un médico o familiar monitoree al paciente
a distancia.

<img width="740" height="494" alt="image" src="https://github.com/user-attachments/assets/e13a92f1-592a-4943-a4e3-8478a2ef9d58" />


**Dispositivos médicos portátiles**

Los dispositivos portátiles, como los relojes inteligentes y las pulseras de fitness, integran cada vez más sensores de grado médico. A tráves de MQTT, estos dispositivos
pueden enviar datos sobre la frecuencia cardiaca, los niveles de oxígeno en la sangre y la calidad de sueño a una aplicación móvil o a la nube. Esta información puede ser 
analizada para detectar patrones y posibles problemas de salud de manera proactiva.

<img width="650" height="434" alt="image" src="https://github.com/user-attachments/assets/a310c234-d729-49b3-9fed-9c23aed7eadc" />


**Integración de dispositivos médicos**

En entornos hospitalarios, MQTT facilita la integración de diversos dispositivos médicos. Equipos como bombas de infusión, ventiladores y monitores de signos vitales pueden
comunicarse entre sí y con los sistemas centrales del hospital. Esto permite una visión unificada de los datos del paciente, lo que mejora la coordinación de la atención y 
reduce la posibilidad de errores.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/8fcb61c8-0660-47d4-8112-f2eaebbe3e37" />


**Seguridad en la transmisión de datos**

La seguridad es una preocupación primordial en el ámbito de la salud. Para proteger la información sensible de los pacientes, las implementaciones de MQTT en aplicaciones mé-
dicas utilizan diversas medidas de seguridad. El uso de TLS (Transport Layer Security) para cifrar los datos en tránsito es fundamental. Además, se emplean mecanismos de auten-
ticación, como nombres de usuario y contraseñas, así como certificados de cliente X.509, para garantizar que solo los dispositivos y usuarios autorizados puedan acceder a la red.
La encriptación de la carga útil (payload) de los mensajes añade una capa adicional de seguridad.

<img width="1700" height="1000" alt="image" src="https://github.com/user-attachments/assets/8982b258-8a7f-4b0e-8d80-5f29fc6b0b62" />


## Fuentes

Para la elaboración de esta información se han consultado las siguientes fuentes:

Blue Goat Cyber. (s.f.). Ensuring cybersecurity for medical devices with MQTT technology. Recuperado el 30 de septiembre de 2025, de https://www.spanishdict.com/translate/sigue%20estando%20disponible%20este%20artculo%3F

D-Medva. (s.f.). Wearables & IoT in healthcare: Connected care for better patient outcomes. Recuperado el 30 de septiembre de 2025, de https://www.spanishdict.com/translate/sigue%20estando%20disponible%20este%20artculo%3F

DEV Community. (s.f.). Security considerations for healthcare IoT device management. Recuperado el 30 de septiembre de 2025, de https://www.spanishdict.com/translate/sigue%20estando%20disponible%20este%20artculo%3F

HiveMQ. (s.f.). MQTT security fundamentals: How to secure MQTT in IoT. Recuperado el 30 de septiembre de 2025, de https://www.spanishdict.com/translate/sigue%20estando%20disponible%20este%20artculo%3F

InterSystems. (s.f.). Integrating medical device data with InterSystems IRIS for health. Recuperado el 30 de septiembre de 2025, de https://www.spanishdict.com/translate/sigue%20estando%20disponible%20este%20artculo%3F

IoT For All. (s.f.). Using MQTT to build real-time medical lab solutions. Recuperado el 30 de septiembre de 2025, de https://www.spanishdict.com/translate/sigue%20estando%20disponible%20este%20artculo%3F
