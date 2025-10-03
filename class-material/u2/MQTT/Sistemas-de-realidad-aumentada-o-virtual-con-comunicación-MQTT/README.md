![ITT Wallpaper](recursos/wallpaper_itt.png)
# Sistemas de Realidad Aumentada/Virtual con comunicación MQTT

**Autor:** Javier Machado Sanchez
  
**Institución:** Instituto Tecnológico de Tijuana
  
**Materia:** Sistemas Programables
  
**Profesor:** Rene Solis Reyes
  
**Fecha:** 30 de Septiembre del 2025
## Introducción
La realidad aumentada (AR) y la realidad virtual (VR) han dejado de ser tecnologías aisladas enfocadas únicamente al entretenimiento. Hoy son piezas clave en áreas como el mantenimiento industrial, la educación, la telemedicina o la robótica. Su valor está en la interacción en tiempo real y la capacidad de generar experiencias compartidas entre varios usuarios o dispositivos.
  
En paralelo, el Internet de las Cosas (IoT) conecta sensores, actuadores y máquinas a redes globales, permitiendo monitoreo y control remoto. La convergencia entre AR/VR e IoT abre la puerta a escenarios donde un usuario puede, por ejemplo, ver en sus gafas AR el estado de una máquina industrial, o controlar un robot desde un entorno VR.
  
Para que esto sea posible, se necesitan protocolos de comunicación que sean ligeros, confiables y en tiempo real. Uno de los más usados en IoT es MQTT (Message Queuing Telemetry Transport), diseñado originalmente para comunicaciones en entornos con poco ancho de banda y recursos limitados.
## Fundamentos
### Realidad Aumentada, Virtual y Mixta
- **Realidad Aumentada (AR):** combina elementos digitales con el mundo físico, superponiendo datos en la visión del usuario. Ejemplo: ver lecturas de sensores de una máquina directamente sobre su superficie mediante gafas AR.
- **Realidad Virtual (VR):** crea entornos totalmente digitales e inmersivos. Es común en simulación de procesos industriales o en formación de personal.
- **Realidad Mixta (MR):** fusiona ambos mundos, permitiendo interactuar con objetos físicos y virtuales al mismo tiempo.
  
Todas estas tecnologías requieren baja latencia (tiempos de respuesta menores a 20 ms en VR para evitar mareo, según *Blanco-Novoa et al., 2020*) y sincronización constante entre múltiples usuarios o dispositivos.
### Protocolo MQTT
MQTT trabaja con un modelo publicar/suscribir. Los dispositivos publican mensajes en “topics” y los interesados se suscriben a esos temas a través de un broker que centraliza la comunicación (OASIS, 2019).
  
Ventajas principales según *Deshpande et al., 2023*:
- **Ligereza:** los paquetes son muy pequeños, ideales para dispositivos móviles o wearables de AR/VR.
- **Confiabilidad:** permite distintos niveles de garantía (QoS 0, 1 y 2).
- **Escalabilidad:** un broker puede gestionar miles de clientes concurrentes.
  
Limitaciones:
- No fue diseñado para multimedia (video, audio o gráficos 3D). Su uso se concentra en telemetría, estados y control de dispositivos.
- Puede generar cuellos de botella si todo se concentra en un único broker.
## Estado Actual de la Tecnología
Varios proyectos han demostrado la utilidad de MQTT en sistemas AR/VR:
- **Colaboración en MR:** *Waldow & Fuhrmann (2019)* desarrollaron una plataforma donde usuarios en diferentes dispositivos podían interactuar en un mismo espacio de realidad mixta. MQTT permitió que los cambios de estado se transmitieran casi en tiempo real entre todos los clientes.
- **Framework IoT + AR/MR:** *Blanco-Novoa et al. (2020)* propusieron un marco de código abierto que integra dispositivos IoT y gafas AR/MR. Se usó Microsoft HoloLens para visualizar y controlar un enchufe inteligente, con Node-RED como capa intermedia y MQTT como protocolo de mensajería.
- **Robótica + AR:** *Rante et al. (2022)* mostraron un caso donde un brazo robótico Dobot podía ser manipulado a través de comandos enviados por MQTT, mientras la interfaz AR mostraba información de estado al usuario.
- **Teleoperación con VR:** *Luu et al. (2025)* diseñaron un sistema en el que un robot era teleoperado mediante un entorno VR, transmitiendo órdenes y datos de sensores a través de MQTT. Se analizaron diferentes configuraciones de QoS y cómo estas afectaban la latencia.
- **Seguridad en AR para IoT:** *Fuentes et al. (2021)* propusieron un modelo de gestión de dispositivos IoT con AR y añadieron consideraciones de seguridad en la capa MQTT, asegurando la comunicación con TLS y autenticación robusta.
## Desafíos Principales
1. **Latencia:**
   - En AR/VR la latencia perceptible puede arruinar la experiencia.
   - Si el broker MQTT está muy alejado, aumenta el tiempo de ida y vuelta.
   - Solución: edge computing y brokers distribuidos *(MQTT-ST, Zhang et al., 2019)*.
2. **Consistencia del estado:**
   - En experiencias colaborativas, todos los usuarios deben ver el mismo entorno.
   - MQTT asegura la entrega de mensajes, pero no sincroniza estados por sí mismo; se requieren capas adicionales de control *(Waldow & Fuhrmann, 2019)*.
3. **Seguridad:**
   - MQTT por defecto no encripta los mensajes.
   - Es necesario usar TLS, autenticación por certificados o tokens *(Fuentes et al., 2021)*.
4. **Interoperabilidad:**
   - Los dispositivos AR/VR son diversos (HoloLens, Oculus, móviles).
   - La integración de MQTT con frameworks como Node-RED o WebRTC es clave para lograr compatibilidad.
## Propuesta Conceptual
La arquitectura más práctica para integrar AR/VR con MQTT es híbrida:
- **MQTT:** se usa para enviar datos ligeros: estados de objetos, lecturas de sensores, comandos de control.
- **WebRTC/UDP:** se emplean para multimedia (voz, video, modelos 3D).
- **Edge + Cloud:** se instalan brokers cercanos al usuario para latencia baja y uno central en la nube para coordinación global.
- **Middleware (Node-RED, APIs):** traduce entre distintos dispositivos y protocolos.
  
**Caso de ejemplo:**
En mantenimiento industrial, un técnico con gafas AR recibe información en vivo de sensores de la máquina (temperatura, vibraciones) vía MQTT. Desde otro lugar, un experto con un casco VR ve el mismo modelo de la máquina y puede guiar al técnico. Ambos comparten el mismo entorno porque los estados están sincronizados gracias a MQTT.
## Conclusiones y Futuros Caminos
MQTT demuestra ser un protocolo clave para unir el mundo físico del IoT con experiencias inmersivas en AR y VR. Su ligereza, escalabilidad y simplicidad lo convierten en la mejor opción para transmitir datos de control y estado.
  
No obstante, no resuelve todo: necesita complementarse con otros protocolos para multimedia, mejorar en seguridad y trabajar con arquitecturas distribuidas para reducir la latencia.
  
A futuro, la combinación de MQTT + edge computing + 5G promete experiencias AR/VR verdaderamente colaborativas y en tiempo real. Además, la integración con inteligencia artificial en el borde permitirá que los sistemas no solo transmitan datos, sino que los interpreten y actúen sobre ellos en el mismo entorno inmersivo.
## Declaración de Uso de IA
### Primer asistencia
**Asistencia de IA:** Pedí recursos bibliograficos referentes al tema de interes con el siguiente prompt: "*Tengo que hacer esta investigación sobre este tema: Sistemas de Realidad Aumentada/Virtual con comunicación MQTT. Dame recursos donde se aborde esta cuestión.*"
La IA regresó diversos articulos y ensayos.
  
**Herramienta:** ChatGPT 5
  
**Fecha:** 30/09/2025 15:32:00
### Segunda asistencia
**Asistencia de IA:** Cree una estructura basandome en el contenido de algunos de los recursos que me proporcionó la AI, tambien una serie de ideas o puntos a tocar y pedí apoyo en la redacción con el siguiente prompt: "*Utiliza las refeerencias de apoyo para redactar y desarrollar las idas que te proporcionaré. Sigue la estructura que te brindaré. Adjunto las referencias, la estructura y las ideas a desarrollar.*"

**Herramienta:** ChatGPT 5
  
**Fecha:** 30/09/2025 18:12:00

## Referencias
[Ir a las referencias bibliográficas](referencias.md)
