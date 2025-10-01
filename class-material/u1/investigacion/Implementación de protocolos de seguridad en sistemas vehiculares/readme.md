# Protocolos de comunicación vehicular y seguridad

Los vehículos modernos cuentan con decenas de unidades de control electrónico (ECU) que se interconectan mediante redes internas. Estas comunicaciones internas emplean principalmente protocolos de bus como **CAN**, **LIN**, **FlexRay** y **Ethernet automotriz** . Tradicionalmente estos protocolos no incorporaban mecanismos criptográficos; por ejemplo, CAN es “el protocolo más extendido a nivel global” pero es también “bastante antiguo y con bastantes deficiencias y vulnerabilidades demostradas” . LIN es una extensión de bajo costo de CAN (hasta 20 kbit/s) usado en funciones secundarias (climatización, espejos, etc.) , mientras que FlexRay (hasta 10 Mbit/s) y Ethernet (ancho de banda aún mayor) fueron diseñados para sistemas de control en tiempo real (dirección *by-wire*, chasis) y transmisión de datos masivos (cámaras, sensores LIDAR). Ninguno de estos protocolos incluye seguridad por diseño: ni cifrado de datos ni autenticación de mensaje. En general, si un atacante logra inyectar tramas con ID falsos en CAN o FlexRay, puede interferir con órdenes críticas (p. ej. frenar o desviar la dirección) sin que el bus lo detecte.

- **CAN bus:** Protocolo estrella de vehículos, soporte hasta 1 Mbit/s. Ventajas de tiempo real y tolerancia a fallos, pero con mensajes cortos (8 bytes) y sin cifrado ni autenticación . Las colisiones se resuelven por arbitraje bit a bit, pero en él “no hay ningún mecanismo mediante el cual defenderse” de inyecciones maliciosas de trama .
- **LIN bus:** Bus más simple y lento (20 kbit/s), con un maestro único. Se usa en subsistemas de baja criticidad (bombas, limpiaparabrisas, asientos), lo que reduce su exposición a ataques graves. LIN tampoco contempla seguridad intrínseca.
- **FlexRay:** Bus determinista de alta velocidad (hasta 10 Mbit/s) usado en sistemas críticos (*steer-by-wire*, chasis activo). Ofrece sincronización por tiempo y redundancia de canales, lo que mejora la confiabilidad ante fallos de hardware. Sin embargo, tampoco incorporaba inicialmente cifrado ni integridad, por lo que podría ser vulnerable a inyecciones de datos. En la práctica, FlexRay suele operar en dominios aislados de alta seguridad, pero carece de protección criptográfica nativa.
- **Ethernet automotriz:** Es la red troncal emergente en vehículos actuales, basada en Ethernet (frecuentemente *BroadR-Reach*). Brinda gran ancho de banda para flujos de video y datos V2X. A diferencia de buses clásicos, Ethernet permite aplicar protocolos estándar de seguridad (por ejemplo **MACsec** a nivel 2, **IPsec/TLS** a nivel de red) para cifrar y autenticar tramas. Estas medidas mitigan ataques externos e internos, pero requieren procesadores más potentes. En resumen, los protocolos de comunicación en vehículos (CAN/LIN/FlexRay/Ethernet) están evolucionando hacia arquitecturas segmentadas con gateways y medidas de seguridad añadidas, pero en su base heredada siguen siendo inseguros contra ciberataques a inyecciones de trama.

---

## Retos en sistemas críticos de vehículos

La interconexión de muchas ECU crea superficies de ataque extensas. Un reto principal es proteger sistemas críticos (frenos, dirección, ADAS). Sin defensas fuertes, “las ECU de los frenos y la transmisión del vehículo pueden ser vulnerables al control de los hackers” . Los autos modernos pueden tener **hasta 100 ECU** y más de **100 millones de líneas de código** , provenientes de múltiples proveedores. Esto multiplica los vectores de ataque: ninguna empresa controla todo el software ni el hardware. 

Además, los métodos de seguridad comunes introducen latencia y carga adicional. Como advierte la literatura, aplicar cifrado o autenticación estándar (como se haría en TI) “introducirá tiempo de cálculo y desempeño de procesamiento adicionales” y esto “puede conducir a riesgos de seguridad, ya que componentes relacionados con el frenado o la dirección podrían dejar de responder bajo carga” . En otras palabras, proteger con criptografía sistemas que requieren respuestas en milisegundos puede colisionar con la seguridad funcional. Los retos actuales incluyen además la seguridad en comunicaciones externas (Wi-Fi, Bluetooth, V2X) y la actualización *over-the-air* (OTA) de software, que son vectores adicionales de intrusión. 

---

## Soluciones emergentes y medidas de seguridad

Para mitigar estas amenazas se investigan múltiples contramedidas:

- **Cifrado y autenticación:** Se estudia añadir mecanismos criptográficos a los protocolos. Por ejemplo, extender CAN con códigos de autenticación de mensaje (MAC) o cifrado simétrico puede impedir inyecciones no autorizadas, pero exige acordar claves secretas en cada ECU. Proyectos como EVITA (Unión Europea, 2008) exploraron módulos de seguridad con HSM (Hardware Security Module) para CAN y FlexRay. En Ethernet automotriz ya es viable usar estándares como AES-GCM vía MACsec (IEEE 802.1AE) o TLS/IPsec en mayores capas, ofreciendo confidencialidad e integridad de datos. AUTOSAR ha definido perfiles SecOC (Onboard Communication security) que añaden autenticación a mensajes CAN y FlexRay.
- **Detección de intrusos (IDS):** Monitorear el tráfico de red para identificar anomalías. Un enfoque es el *fingerprinting* del hardware: cada ECU tiene ligeras variaciones en su reloj o transceptor eléctrico. Sistemas IDS basados en esos “perfiles de ECU” pueden detectar cuando llega una señal CAN desde un dispositivo desconocido. Por ejemplo, se ha demostrado que calculando la huella digital del cristal oscilador de cada ECU y verificándola en tiempo real se puede “buscar cualquier anomalía… en la forma de una incongruencia entre el equipo aprobado y la huella digital del equipo que intenta comunicarse” . Esto permite marcar inmediatamente cualquier trama CAN falsificada (por ejemplo, un ataque sobre frenos o dirección) como no procedente. 
- **Segregación de redes y gateways seguros:** Se promueve una arquitectura de dominios, donde los buses de alta criticidad (frenos, motor) están aislados de CAN de confort (infotainment, USB) por gateways que filtran mensajes. Estos gateways pueden validar remitentes, limitar IDs y detectar tráfico sospechoso. Además, se usan firewalls entre unidades externas (telemática, entretenimiento) y la red vehículo, así como redundancia (frenos dobles, modos degradados) para que un ataque no produzca un fallo total.
- **Gestión de claves y dispositivos seguros:** Incorporar módulos de seguridad hardware en ECU (TPM, HSM) para manejar claves criptográficas y firmar actualizaciones. Esto fortalece la autenticación mutua entre ECUs y verifica la integridad del firmware. Junto con esto, se potencian prácticas de *seguridad por diseño*: desarrollar el software con chequeos de vulnerabilidades, protocolos formales de pruebas (fuzzing de CAN, análisis de integridad) y sistemas de actualización firmada *OTA* para parchear brechas en campo.
- **Vigilancia continua y respuesta:** Integrar en la nube o en centros especializados la recopilación de telemetría de ciberseguridad, de modo que eventos inusuales (picos de tráfico, fallos repetidos) se analicen centralmente. Esto permite lanzar contramedidas rápidas a nivel de flota, reforzar reglas de IDS y mantener actualizadas las defensas ante nuevas técnicas de ataque.

---

## Estándares internacionales y normativas

En los últimos años han surgido normas para guiar estos esfuerzos. La **ISO/SAE 21434:2021** establece los requisitos de ingeniería de ciberseguridad para vehículos de carretera, abarcando todo el ciclo de vida (diseño, producción, operación, mantenimiento) . Se centra en la gestión de riesgos y promueve “incorporar la ciberseguridad en los productos de automoción a lo largo de su vida útil” , aunque **no prescribe tecnologías concretas**. Paralelamente, los reglamentos de la UNECE (WP.29) R155 y R156 exigen a los fabricantes implementar sistemas de gestión de la ciberseguridad certificados (CSMS) y sistemas de actualización segura de software (SUMS). En particular, R155 establece que los fabricantes deben mitigar un listado de riesgos y demostrar una estrategia de ciberseguridad en sus vehículos . Estos requisitos obligatorios se complementan con estándares como SAE J3061 (guías de proceso) y AUTOSAR Safety&Sec, todos dirigidos a homogeneizar mejores prácticas. 

---

## Buenas prácticas comparativas y líneas de mejora

En comparación con las arquitecturas antiguas **no seguras**, las siguientes prácticas son recomendadas hoy día:

- **Arquitectura por dominios:** Reemplazar redes planas por jerarquías de dominios (chasis, tren motriz, infotainment) con gateways que apliquen políticas de seguridad. Esto confina los ataques a zonas limitadas.
- **Seguridad integrada desde el diseño (Security by Design):** Incluir expertos en ciberseguridad desde las fases iniciales. Definir requisitos de protección (confidencialidad, integridad) junto con requisitos funcionales.
- **Criptografía adecuada:** Adoptar cifrado y autenticación en todos los niveles posibles (TLS/DTLS para comunicaciones IP, MACsec para enlaces Ethernet, MACs/AES para CAN). Balancear la carga criptográfica para no afectar la seguridad funcional; por ejemplo, usar aceleradores hardware o algoritmos ligeros en ECUs.
- **Detección activa:** Implementar IDS/IPS específicos para vehicular (p. ej. basados en comportamiento o fingerprinting) que supervisen el bus y alerten ante anomalías en tiempo real .
- **Gestión de claves y actualizaciones:** Emplear PKI vehicular, certificados únicos para cada ECU y canales seguros de provisioning. Asegurar que todas las actualizaciones de software estén firmadas digitalmente.
- **Pruebas y validación continua:** Realizar ataques de penetración (red teaming), simulaciones de fallo y análisis estático/dinámico del código en cada desarrollo. Utilizar herramientas de verificación formal para protocolos críticos.
- **Cumplimiento normativo:** Adoptar los marcos ISO/SAE 21434 y UNECE R155/156 como referencia de procesos, realizando auditorías periódicas del Sistema de Gestión de Ciberseguridad (CSMS) y manteniendo certificaciones vigentes.

En resumen, la seguridad vehicular exige un enfoque multinivel: mejora de protocolos (añadiendo cifrado/autenticación), arquitectura segura (gateways y dominios), detección de intrusiones y cumplimiento de normas internacionales. Si bien los desafíos técnicos (latencia, complejidad) son grandes, la convergencia de mejores prácticas industriales y normativas está estableciendo un marco más confiable para los **vehículos conectados y autónomos** del futuro.

---

## Referencias

Camacho, R. (2025). *Por qué es importante la ciberseguridad automotriz*. Parasoft. Recuperado de https://es.parasoft.com/blog/why-automotive-cybersecurity-is-important/ 

INCIBE (2019). *Los coches inteligentes: ¿preparados ante amenazas?* INCIBE-CERT. Recuperado de https://www.incibe.es/incibe-cert/blog/los-coches-inteligentes-preparados-amenazas 

Applus+ Laboratories. (2022). *UNECE WP.29 R155/R156: los nuevos reglamentos de ciberseguridad para vehículos*. Recuperado de https://www.appluslaboratories.com/global/es/news/publications/nuevos-reglamentos-ciberseguridad-vehiculos 

SGS Spain. (2023). *ISO/SAE 21434 Certification – Road Vehicles Cybersecurity Engineering*. Recuperado de https://www.sgs.com/es-es/services/iso-sae-21434-certificacion-de-vehiculos-de-carretera-ingenieria-de-ciberseguridad 

QAD Blog (2019). Domínguez, C. *Ciberseguridad automotriz*. Recuperado de https://www.qad.com/es-MX/blog.mx/-/blogs/ciberseguridad-automotriz  

Excelsior Staff (2024). *Sistemas de detección de intrusos (IDS): Por fin para los vehículos*. Excelsior University. Recuperado de https://www.excelsior.edu/es/article/intrusion-detection-systems-ids-finally-for-the-vehicles/ 
