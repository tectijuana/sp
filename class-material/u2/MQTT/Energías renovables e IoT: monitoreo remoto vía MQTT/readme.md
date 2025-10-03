# Energías renovables e IoT: monitoreo remoto vía MQTT

**Autor:** Oscar Paul Martinez Herrera

**Institución:** Instituto Tecnológico de Tijuana

**Materia:** Sistemas Programables

**Profesor:** Rene Solis Reyes

**Fecha:** 30 de Septiembre del 2025

## ¿Qué es MQTT?
MQTT es un protocolo de mensajería ligero basado en el modelo publicar/suscribirse.
- Fue diseñado para sistemas con recursos limitados y redes poco confiables.
- Los dispositivos IoT actúan como clientes MQTT, conectándose a un broker que administra la distribución de mensajes.
- Su fortaleza está en la desacoplación: el publicador (ej. sensor solar) no necesita conocer al suscriptor (ej. sistema SCADA), solo al broker

## Flujo de comunicación en monitoreo remoto de energías renovables

### Publicadores (sensores IoT)
- Sensores en paneles solares: voltaje, corriente, temperatura.
- Sensores en turbinas eólicas: velocidad del viento, rpm, potencia generada.
- Cada sensor envía sus datos en un topic MQTT. Ejemplo:
energia/solar/panel1/voltaje = 32.5V
energia/eolica/turbina2/potencia = 450kW

### Broker MQTT
- Recibe todos los datos enviados.
- Filtra y reenvía los mensajes a los suscriptores interesados.
- Puede funcionar en la nube o en un servidor local, garantizando escalabilidad y fiabilidad.

### Suscriptores (sistemas de control y usuarios)
- Plataforma web o móvil para visualizar producción en tiempo real.
- Base de datos para registrar históricos.
- Sistemas de alerta que reciben mensajes cuando la producción baja de un umbral crítico.

## Características de MQTT útiles en IoT energético
- **Ligereza y eficiencia:** cada mensaje tiene muy poca sobrecarga, ideal para sensores conectados por redes móviles o satelitales.
- **Calidad de servicio (QoS):** garantiza entrega de mensajes con tres niveles (0, 1, 2), lo que asegura confiabilidad incluso en redes inestables.
- **Persistencia:** el broker puede almacenar mensajes y entregarlos cuando un dispositivo vuelva a estar en línea.
- **Retained Messages:** permiten que un nuevo suscriptor obtenga inmediatamente el último valor registrado, útil para conocer el estado actual de un panel o turbina al instante.
- **Last Will & Testament (LWT):** notifica si un dispositivo se desconecta inesperadamente, lo que ayuda a detectar fallas en campo.
