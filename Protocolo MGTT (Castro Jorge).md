# 📘 Jorge Luis Castro Alvarado — *MQTT 5 Essentials*

Este documento resume y explica en detalle los capítulos del libro **“MQTT 5 Essentials” (HiveMQ)**.  
Su objetivo es servir como guía de referencia para aprender y aplicar el protocolo MQTT en proyectos IoT y sistemas distribuidos.

---

## 🟦 Volumen I — Fundamentos de MQTT

### Capítulo 1 — Introducing MQTT
- **Qué es:** protocolo de mensajería ligero basado en **publicación/suscripción**.  
- **Historia:** creado en 1999 por IBM y Eurotech para monitoreo de oleoductos vía satélite.  
- **Principios de diseño:** bajo consumo de ancho de banda, mínima complejidad, independencia del payload, escalabilidad.  
- **Ventajas:** ideal para IoT, M2M, hogares inteligentes, industria y aplicaciones móviles con red inestable.  
- **Ejemplo:** un sensor de temperatura envía datos a un broker, y múltiples clientes (app móvil, dashboard web, sistema de alertas) pueden suscribirse a esos datos.

---

### Capítulo 2 — Publish / Subscribe Pattern
- **Modelo clásico:** Cliente A publica → Broker → Cliente B recibe.  
- **Comparación:** más flexible que cliente-servidor directo porque desacopla productores y consumidores.  
- **Tipos de acoplamiento:**  
  - **Espacial:** publicador y suscriptor no necesitan conocerse.  
  - **Temporal:** no importa si uno está desconectado, los mensajes pueden esperar.  
  - **Sincronización:** comunicación asíncrona, no bloqueante.  
- **Ventaja clave:** permite que miles de dispositivos trabajen con un solo broker central.  
- **Ejemplo:** en un sistema de riego, sensores de humedad publican datos, y varias apps (panel web, control automático, notificaciones) consumen la misma información.

---

### Capítulo 3 — Client, Broker & Connection Establishment
- **Broker:** servidor central que recibe todos los mensajes y los distribuye.  
- **Cliente:** cualquier dispositivo, app o servicio que publique o se suscriba.  
- **Proceso de conexión:**  
  - Cliente envía **CONNECT** (con `ClientID`, `Clean Start`, `Keep Alive`, credenciales).  
  - Broker responde con **CONNACK** (aceptación, códigos de retorno, estado de sesión).  
- **Keep Alive:** temporizador que asegura que la conexión sigue activa.  
- **Importancia:** la conexión inicial define seguridad, persistencia y políticas de sesión.  

---

### Capítulo 4 — Publish, Subscribe & Unsubscribe
- **Publicar:** se usa paquete **PUBLISH**, incluye Topic, QoS, Retain flag y Payload.  
- **Suscribirse:** **SUBSCRIBE** especifica qué topics seguir; broker responde con **SUBACK** confirmando QoS aceptado.  
- **Cancelar:** **UNSUBSCRIBE** elimina suscripciones activas.  
- **Rol del broker:** garantiza la entrega según el QoS negociado.  
- **Ejemplo:** un sensor publica en `casa/sala/temperatura`; la app de control se suscribe a ese topic.

---

### Capítulo 5 — Topics & Best Practices
- **Estructura:** jerárquica con `/` (ej. `casa/sala/luces`).  
- **Comodines:**  
  - `+` → un nivel (`casa/+/luces`).  
  - `#` → múltiples niveles (`casa/#`).  
- **Reservados:** los que empiezan con `$` (ej. `$SYS/`).  
- **Buenas prácticas:**  
  - No empezar con `/`.  
  - Evitar `#` global porque consume recursos.  
  - Diseñar jerarquías lógicas y escalables.  
- **Ejemplo:** `fabrica/linea1/motor1/estado`.

---

### Capítulo 6 — Quality of Service (QoS)
- **QoS 0:** entrega sin garantía (“fire and forget”).  
- **QoS 1:** entrega al menos una vez (puede duplicar mensajes).  
- **QoS 2:** entrega exactamente una vez (más intercambio de paquetes).  
- **Trade-off:** mayor fiabilidad implica más latencia y ancho de banda.  
- **Ejemplo:**  
  - QoS 0 para datos de sensores frecuentes (temperatura).  
  - QoS 1 para alertas de seguridad.  
  - QoS 2 para transacciones críticas (banca, pagos).

---

### Capítulo 7 — Persistent Sessions & Queuing
- **Persistencia:** broker recuerda suscripciones y mensajes pendientes cuando un cliente se desconecta.  
- **Mensajes en cola:** si el cliente vuelve, recibe lo acumulado (según QoS).  
- **Flags:** `Clean Start` y `Session Expiry Interval` controlan este comportamiento.  
- **Ejemplo:** un dispositivo móvil recibe todos los mensajes acumulados al reconectarse después de perder señal.

---

### Capítulo 8 — Retained Messages
- **Función:** broker guarda el último mensaje publicado con el flag *retained*.  
- **Ventaja:** nuevos suscriptores reciben inmediatamente el estado más reciente.  
- **Eliminar:** publicar payload vacío con retained=true.  
- **Ejemplo:** un sensor de puerta publica “cerrada” como retained; cualquier nuevo cliente ve el estado actual sin esperar un nuevo evento.

---

### Capítulo 9 — Last Will and Testament (LWT)
- **Qué es:** mensaje predefinido enviado por el broker si el cliente se desconecta abruptamente.  
- **Uso típico:** informar estado de conexión (“device offline”).  
- **Ejemplo:** en IoT industrial, si un robot pierde conexión, el broker publica un aviso de falla en su topic LWT.

---

### Capítulo 10 — Keep Alive & Client Take-Over
- **Keep Alive:** intervalo máximo entre mensajes antes de considerar desconexión.  
- **Client Take-Over:** si un cliente se conecta con el mismo `ClientID`, la sesión anterior se cierra.  
- **Beneficio:** asegura que solo una instancia de cliente exista con ese ID.  

---

### Capítulo 11 — MQTT over WebSockets
- **Función:** permite usar MQTT en navegadores y apps web.  
- **Ventajas:** compatibilidad con firewalls y fácil integración con dashboards en tiempo real.  
- **Seguridad:** usar TLS para cifrado.  
- **Ejemplo:** dashboard web mostrando datos de sensores en vivo vía MQTT/WebSocket.

---

## 🟧 Volumen II — MQTT 5 (novedades)

### Capítulo 1 — Introduction to MQTT 5
- **Ratificado en 2019 por OASIS.**  
- Mantiene simplicidad pero añade funciones críticas: escalabilidad, interoperabilidad, gestión de errores clara.  
- **Objetivo:** facilitar grandes despliegues en la nube con miles/millones de dispositivos.

---

### Capítulo 2 — Foundational Changes
- `Clean Start` reemplaza a `Clean Session`.  
- `Session Expiry Interval` para controlar cuánto tiempo se conserva la sesión.  
- **AUTH packet:** permite autenticación avanzada.  
- Más tipos de datos (ej. valores binarios y UTF-8 mejorado).  

---

### Capítulo 3 — Why Upgrade to MQTT 5
- Manejo de errores detallado con **reason codes**.  
- **Shared subscriptions**, **topic aliases**, **user properties**.  
- **Expiración de mensajes/sesiones.**  
- Facilita integración en arquitecturas cloud-native.  

---

### Capítulo 4 — Session & Message Expiry
- **Session Expiry:** cuánto dura la sesión tras desconexión.  
- **Message Expiry:** caducidad de mensajes no entregados.  
- Evita sobrecargar clientes con mensajes viejos.  

---

### Capítulo 5 — Client Feedback & Negative ACKs
- **Reason Codes:** broker da feedback claro (ej. “QoS no soportado”).  
- Controla mejor límites de recursos: tamaño máximo de payload, cantidad de subscripciones, etc.  
- Hace que clientes puedan adaptarse dinámicamente.  

---

### Capítulo 6 — User Properties
- Pares clave/valor tipo *headers HTTP*.  
- Transportan metadatos para trazabilidad y routing.  
- Ejemplo: incluir ID de cliente, prioridad o versión de firmware.  

---

### Capítulo 7 — Shared Subscriptions
- **Sintaxis:** `$share/GROUPID/TOPIC`.  
- Distribuye mensajes de un mismo topic entre varios clientes.  
- Ideal para balanceo de carga en clusters de consumidores.  

---

### Capítulo 8 — Payload Format Description
- Permite especificar formato del payload: JSON, XML, binario, etc.  
- Se indican con propiedades `Payload Format Indicator` y `Content Type`.  
- Mejora la interoperabilidad entre sistemas distintos.  

---

### Capítulo 9 — Request-Response Pattern
- Introduce soporte nativo para request/response:  
  - `Response Topic` indica dónde responder.  
  - `Correlation Data` enlaza petición y respuesta.  
- Ejemplo: un cliente envía petición de configuración y recibe respuesta de varios servidores.  

---

### Capítulo 10 — Topic Aliases
- **Optimización:** topic largo se reemplaza por un entero.  
- Reduce uso de ancho de banda en redes con mensajes frecuentes.  
- Ejemplo: en telemetría industrial, evita repetir cadenas largas de topics en cada mensaje.  

---

### Capítulo 11 — Enhanced Authentication
- Nuevo **AUTH packet** con soporte para múltiples rondas de autenticación.  
- Compatible con métodos modernos: OAuth2, Kerberos, certificados.  
- Aporta seguridad empresarial avanzada.  

---

### Capítulo 12 — Flow Control
- **Receive Maximum:** controla número máximo de mensajes en vuelo.  
- Evita saturar clientes lentos o redes débiles.  
- Fundamental para sistemas con dispositivos heterogéneos (ej. sensores muy simples junto a servidores potentes).

---

## ✅ Conclusión
MQTT 5 mantiene la **ligereza y simplicidad** que hicieron popular al protocolo, pero agrega funciones para hacer frente a entornos **complejos, escalables y seguros**.  
Es la base ideal para proyectos IoT modernos, desde sensores domésticos hasta plataformas industriales a gran escala.

## 📚 Fuente

Este resumen se basa en el libro:

**Naik, G. (2019).** *MQTT 5 Essentials*. HiveMQ.  
Disponible en: [https://www.hivemq.com/mqtt-essentials/](https://www.hivemq.com/mqtt-essentials/)
