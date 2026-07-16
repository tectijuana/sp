**Nombre:** Jahziel Amado López Angulo  
**Número de Control:** 22211593  
**Correo electrónico:** l22211593@tectijuana.edu.mx  
**GitHub:** [Jahziel43](https://github.com/Jahziel43)  

---
# Verificación formal de flujos de datos en sistemas MQTT

## Introducción
El Internet de las Cosas (IoT) está cada vez más presente en la vida diaria: desde sensores en casas inteligentes hasta sistemas de monitoreo en hospitales y fábricas. Para que todos estos dispositivos puedan comunicarse entre sí, se necesitan **protocolos de comunicación** que transmitan los datos de manera rápida y con poco consumo de recursos. Uno de los más usados es **MQTT (Message Queuing Telemetry Transport)**.

Aunque MQTT es muy eficiente, cuando se utiliza en sistemas críticos surge una preocupación importante: ¿cómo asegurarnos de que los datos siempre lleguen completos, a tiempo y de forma segura? Para responder a esta necesidad se utilizan técnicas llamadas **verificación formal**, que permiten comprobar con métodos matemáticos que un sistema funciona como se espera.

## Marco teórico
### El protocolo MQTT
MQTT funciona bajo un esquema de **publicador/suscriptor**:
- Los **publicadores** envían mensajes con datos (por ejemplo, la temperatura medida por un sensor).  
- El **broker** recibe esos mensajes y se encarga de distribuirlos.  
- Los **suscriptores** son los que reciben la información (por ejemplo, una app que muestra la temperatura en pantalla).  

Este modelo es muy útil porque el publicador no necesita saber quién recibe los datos, solo los envía al broker. Sin embargo, puede haber problemas como:
- Pérdida de mensajes.  
- Duplicación de información.  
- Retrasos en la entrega.  
- Riesgos de seguridad si alguien no autorizado logra acceder.  

### La verificación formal
La **verificación formal** es un conjunto de técnicas matemáticas que permiten comprobar que un sistema cumple con ciertas reglas. En lugar de solo hacer pruebas prácticas, la verificación formal analiza todos los posibles escenarios que pueden ocurrir en un sistema.  

En el caso de MQTT, algunas reglas que se pueden verificar son:  
- Que los mensajes lleguen siempre al destino en el nivel de confiabilidad definido.  
- Que no haya bloqueos en el envío o recepción de datos.  
- Que solo los dispositivos autorizados accedan a la información.  

## Metodología
El proceso de aplicar verificación formal a MQTT se puede entender en pasos:
1. **Representar el sistema**: se modela el broker, los publicadores y los suscriptores como un diagrama de estados.  
2. **Definir reglas a cumplir**: por ejemplo, que todos los mensajes de un sensor lleguen a la aplicación receptora.  
3. **Aplicar herramientas de análisis**: se usan programas especializados para revisar todos los escenarios posibles.  
4. **Detectar errores y corregirlos**: si se encuentra un fallo en el modelo, se ajusta antes de implementar el sistema real.  

## Ejemplos prácticos
- En un **hospital**, un sensor de oxígeno en sangre envía datos a un monitor. Con verificación formal, se puede garantizar que el mensaje nunca se pierda ni llegue tarde, evitando riesgos para el paciente.  
- En una **ciudad inteligente**, los semáforos conectados mediante IoT necesitan sincronizarse. Con verificación formal se revisa que no haya mensajes perdidos que puedan causar fallos en la coordinación.  

## Análisis y discusión
Aunque MQTT es un protocolo ligero y muy útil, no fue diseñado para manejar por sí solo todos los problemas de seguridad y confiabilidad. Aquí es donde la verificación formal se vuelve importante:  
- Aporta confianza en que el sistema funcionará correctamente incluso en situaciones extremas.  
- Ayuda a detectar errores antes de que ocurran en la práctica.  
- Permite aumentar la seguridad contra accesos no autorizados.  

## Conclusiones
La verificación formal de flujos de datos en sistemas MQTT es un paso fundamental para garantizar la confiabilidad en el IoT. Al combinar la simplicidad de MQTT con el rigor matemático de la verificación formal, es posible construir sistemas más seguros y confiables, especialmente en áreas críticas como la salud, el transporte y la automatización industrial.  
En resumen, la verificación formal no complica a MQTT, sino que lo complementa, aportando seguridad y confiabilidad donde más se necesita.

## Referencias
- Amazon Web Services (AWS). (s. f.). *¿Qué es MQTT?* Recuperado de https://aws.amazon.com/es/what-is/mqtt/  

- Inria Chile. (2022). *Internet de las cosas (IoT): Libro blanco*. Recuperado de https://www.inria.cl/sites/default/files/2022-12/libro-blanco-iot-es.pdf  

- Hernández Martín, F. J. (2024). *Análisis de la Tecnología de Mensajería MQTT* (Memoria). Universidad de Málaga. Recuperado de https://riuma.uma.es/xmlui/bitstream/handle/10630/35683/Hern%C3%A1ndez%20Mart%C3%ADn%20Francisco%20Javier%20Memoria.pdf?sequence=1  

- Vidal-Silva, C. L. (2019). *Una propuesta de algoritmo Spin / Promela para el análisis y diagnóstico de errores en diagramas de secuencia UML*. Revista (SciELO). Recuperado de https://www.scielo.cl/scielo.php?pid=S0718-07642019000100263&script=sci_arttext  

- Novus Blog. (2025). *Cómo configurar un Broker MQTT paso a paso*. Recuperado de https://blog.novus.com.br/como-configurar-un-broker-mqtt-paso-a-paso/?lang=es  

- Paessler AG. (s. f.). *MQTT — ¿Qué es y para qué se usa?* Recuperado de https://www.paessler.com/es/it-explained/mqtt  
