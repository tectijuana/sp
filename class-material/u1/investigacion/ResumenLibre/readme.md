## Sistemas Programables

**Alumno:** Pozos Flores Norberto  
**Matrícula:** 22210336  
**Docente:** Rene Reyes  
**Fecha:** 29/09/2025  

---

# MQTT & MQTT 5 Essentials (HiveMQ)

El libro explica los fundamentos del protocolo **MQTT**, muy usado en el **Internet de las Cosas (IoT)**, y las mejoras introducidas en **MQTT 5**.

---

## MQTT Essentials (v3.1.1)

###  Introducción
- Protocolo ligero, binario y eficiente.
- Diseñado para dispositivos con recursos limitados y redes poco fiables.
- Ideal para **IoT** y **M2M (machine-to-machine)**.

### Patrón Publish/Subscribe
- **Clientes publican** mensajes en *temas (topics)*.
- **Suscriptores reciben** mensajes de los temas que siguen.
- **Broker** actúa como intermediario:
  - Filtra mensajes.
  - Distribuye a suscriptores.
  - Gestiona autenticación y sesiones.

### Clientes y Broker
- Cliente: puede publicar, suscribirse o ambas cosas.
- Broker: núcleo del sistema, administra conexiones, sesiones y seguridad.

### Temas y buenas prácticas
- Los temas son jerárquicos:  
  `casa/sala/temperatura`
- Comodines:
  - `+` → un nivel.
  - `#` → varios niveles.
- Recomendaciones:
  - Evitar `/` al inicio.
  - No usar espacios.
  - Mantenerlos cortos y claros.

### Calidad de Servicio (QoS)
- **QoS 0:** “a lo sumo una vez” (fire & forget).
- **QoS 1:** “al menos una vez” (puede duplicarse).
- **QoS 2:** “exactamente una vez” (más seguro, más lento).

### Sesiones persistentes
- Guardan suscripciones y mensajes no entregados.
- Útiles cuando los clientes se desconectan frecuentemente.

###  Mensajes retenidos
- El broker guarda el **último valor publicado** de un tema.
- Útil para que un nuevo suscriptor reciba un estado inicial inmediato.

###  Last Will and Testament (LWT)
- Mensaje que avisa cuando un cliente se desconecta inesperadamente.

###  Keep Alive
- “Pings” para comprobar que la conexión sigue activa.
- Previene conexiones medio abiertas.

###  MQTT sobre WebSockets
- Permite usar MQTT en navegadores y apps web.
- Ejemplo: paneles en tiempo real, notificaciones.

---

##  MQTT 5 Essentials

###  Objetivos de la versión 5
- Mejor escalabilidad.
- Mayor robustez en redes poco fiables.
- Mejor manejo de errores y feedback.
- Extensibilidad con nuevas propiedades.

###  Novedades principales
- **Propiedades de usuario:** metadatos en cabecera.
- **Negative ACKs (razones de error):** feedback detallado.
- **Expiración de mensajes y sesiones.**
- **Suscripciones compartidas:** balanceo entre clientes.
- **Formato de carga (Payload format).**
- **Topic Alias:** nombres más cortos para eficiencia.
- **Request/Response pattern:** comunicación estilo petición-respuesta.
- **Autenticación mejorada:** soporte para OAuth, Kerberos, etc.
- **Control de flujo:** evitar sobrecargas en clientes o broker.
- **Paquete AUTH:** permite reautenticación sin cerrar la conexión.

---

##  Conclusión
- **MQTT 3.1.1:** rápido, ligero y base del IoT.
- **MQTT 5:** mantiene la simplicidad, pero añade mejoras críticas para:
  - Escalabilidad masiva.
  - Integraciones empresariales.
  - Seguridad y confiabilidad.

---
