# Seguridad en sistemas embebidos – Criptografía, autenticación, protección contra ataques 
**Autor:** Suarez Castro Jair Alberto - 22211663  

**INSTITUTO TECNOLÓGICO DE TIJUANA**

**Materia:** Sistemas programables

**Asistencia de IA:** Consulté a ChatGPT sobre fuentes o sitios web confiables para obtener la información del tema.
**Herramienta:** ChatGPT (GPT-5)

**Fecha:** 2025-09-15

---

## Introducción
Los sistemas embebidos son dispositivos electrónicos diseñados para realizar funciones específicas dentro de un aparato más grande. A diferencia de las computadoras de propósito general, estos sistemas cuentan con recursos limitados en memoria, energía y procesamiento. Aun así, hoy en día están presentes en automóviles, dispositivos médicos, electrodomésticos y equipos conectados a internet.

[<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/31e33030-ec90-4a4a-a6e6-13c4e4c6281a" />](https://upload.wikimedia.org/wikipedia/commons/2/2c/ADSL_modem_router_internals_labeled.jpg)

La gran importancia de estos sistemas hace que su seguridad sea un tema crítico. Un ataque exitoso puede poner en riesgo no solo datos, sino también la integridad de las personas o la funcionalidad de infraestructuras completas.

---

## Criptografía en Sistemas Embebidos
La criptografía se utiliza para garantizar que la información transmitida o almacenada esté protegida contra accesos no autorizados. En los sistemas embebidos se aplica principalmente para:  

- Cifrar datos sensibles, como información médica o financiera.  
- Asegurar que la información no se modifique en el trayecto (integridad).  
- Validar que el software que se ejecuta sea legítimo mediante firmas digitales.  

Uno de los principales desafíos es que muchos algoritmos criptográficos tradicionales requieren demasiados recursos para ser implementados en dispositivos pequeños. Como respuesta, se han desarrollado algoritmos de **criptografía ligera**, entre los que destaca **Ascon**, estandarizado recientemente por el NIST (2025) como una de las soluciones más adecuadas para equipos con limitaciones de hardware.  

### 
<img src="https://i0.wp.com/semiengineering.com/wp-content/uploads/Cadence_embedded-security-using-cryptography-fig2.png?fit=640%2C217&ssl=1" 
     alt="Seguridad en sistemas embebidos" 
     width="800" height="400">

---

## Autenticación en Sistemas Embebidos
La autenticación permite verificar la identidad de usuarios, dispositivos o programas. En sistemas embebidos se puede aplicar de varias maneras:  

- **Autenticación de dispositivos**, asegurando que un equipo conectado a la red es realmente quien dice ser.  
- **Autenticación de usuarios**, mediante contraseñas u otros mecanismos de acceso.  
- **Arranque seguro (Secure Boot)**, que consiste en verificar que el firmware esté firmado digitalmente por el fabricante antes de ejecutarse.

## La triada CIA y cómo contribuye a una política de seguridad en sistemas embebidos
<img src="https://www.windriver.com/sites/default/files/2022-02/cia-triad-updated.png" 
     alt="Seguridad en sistemas embebidos" 
     width="800" height="400">


De esta forma se evita que un atacante pueda instalar software malicioso o modificar el funcionamiento del sistema.

---

## Protección contra Ataques

La protección contra ataques en sistemas embebidos es una de las áreas más críticas dentro de la seguridad, ya que estos dispositivos suelen operar en entornos donde están expuestos a múltiples amenazas, tanto remotas como físicas. La combinación de limitaciones de hardware, conectividad constante y la importancia de sus funciones los convierte en objetivos atractivos para atacantes.

### Ataques de red o software

Estos ataques buscan comprometer la comunicación entre dispositivos o alterar el software que ejecutan. Entre los más comunes encontramos:

- Ataques de intermediario (Man-in-the-Middle, MITM): donde un atacante intercepta las comunicaciones entre dos dispositivos para robar o modificar la información.

- Inyección de malware: que permite ejecutar código malicioso en el dispositivo, ya sea por vulnerabilidades en el firmware o por actualizaciones no seguras.

- Credenciales débiles o expuestas: contraseñas simples o claves mal protegidas que facilitan el acceso no autorizado.

**Medidas de defensa:**

- Uso de protocolos cifrados como TLS para proteger las comunicaciones.

- Implementación de firmas digitales en software y firmware para evitar la ejecución de código alterado.

- Gestión robusta de claves criptográficas, evitando almacenamiento en memoria insegura.

- Políticas estrictas de credenciales (rotación de contraseñas, multifactor).

### Ataques físicos

Cuando el atacante tiene acceso directo al dispositivo, puede emplear técnicas avanzadas que explotan las propiedades físicas del hardware. Los más relevantes son:

- Ataques de canal lateral (Side-Channel Attacks, SCA): en los que se analizan señales externas del dispositivo, como el consumo de energía, la radiación electromagnética o los tiempos de ejecución, para extraer claves secretas o información confidencial. Estos ataques son peligrosos porque no requieren alterar el software.

- Ataques por inyección de fallos (Fault Injection Attacks): donde se manipulan las condiciones del dispositivo, por ejemplo mediante voltajes anómalos, fluctuaciones de reloj o láseres, con el fin de alterar la ejecución normal y forzar errores que revelen información o permitan eludir mecanismos de seguridad.

**Medidas de defensa:**

- Uso de Secure Elements o Trusted Platform Modules (TPM), que almacenan claves y operaciones críticas en un entorno aislado y resistente a manipulaciones físicas.

- Implementación de algoritmos criptográficos resistentes a ataques de canal lateral.

- Sensores de tamper que detecten manipulaciones físicas y bloqueen el dispositivo.

- Diseño redundante de hardware que dificulte la explotación de inyecciones de fallos.

### Actualizaciones inseguras

El ciclo de vida del firmware es otro punto débil. Si un atacante logra instalar versiones antiguas o no verificadas, el dispositivo queda expuesto a vulnerabilidades ya conocidas.

- Downgrade attacks (ataques de retroceso): obligan al sistema a aceptar versiones antiguas del firmware que no tienen los parches de seguridad más recientes.

- Actualizaciones falsas: firmware malicioso distribuido por un canal no confiable.

**Medidas de defensa:**

- Uso de actualizaciones firmadas digitalmente (OTA firmadas), asegurando que solo software autorizado por el fabricante pueda instalarse.

- Protección contra rollback, impidiendo que se instalen versiones anteriores.

- Canales de actualización cifrados y autenticados.

---

## Tabla de Seguridad en Sistemas Embebidos

| Área             | Amenaza principal                   | Contramedida destacada |
|------------------|-------------------------------------|-------------------------|
| Criptografía     | Claves robadas o débiles            | Criptografía ligera (Ascon) |
| Autenticación    | Dispositivos falsos o firmware malicioso | Arranque seguro y firmas digitales |
| Ataques físicos  | Extracción de claves por hardware   | Secure elements, mitigaciones contra SCA |
| Actualizaciones  | Instalación de versiones inseguras  | OTA firmadas y protección contra rollback |


<img src="https://intechhouse.com/wp-content/uploads/2023/05/Embedded-Systems-Security-IMG3.jpg" 
     alt="Seguridad en sistemas embebidos" 
     width="800" height="400">
     
---
## Conclusión
La seguridad en sistemas embebidos es un tema fundamental debido a la relevancia que estos dispositivos tienen en la vida diaria y en infraestructuras críticas. La criptografía protege datos y firmware, la autenticación evita accesos indebidos y la protección contra ataques fortalece al sistema frente a riesgos tanto físicos como digitales.  

Un diseño que integre todas estas medidas no solo mejora la confiabilidad, sino que también genera confianza en el uso de tecnologías que cada día están más presentes en nuestra vida cotidiana.

---

## Referencias (formato APA)

- National Institute of Standards and Technology. (2025, agosto 28). *NIST Finalizes Lightweight Cryptography Standard to Protect Small Devices* [News release]. NIST. https://www.nist.gov/news-events/news/2025/08/nist-finalizes-lightweight-cryptography-standard-protect-small-devices  

- National Institute of Standards and Technology. (2025). *Ascon-Based Lightweight Cryptography Standards for Constrained Devices (NIST Special Publication 800-232)*. NIST. https://csrc.nist.gov/pubs/sp/800/232/final  

- Sysgo. (2022, octubre 6). *Trusted Platform Module (TPM) in Embedded System Security*. Sysgo Blog. https://www.sysgo.com/blog/article/trusted-platform-module-tpm-in-embedded-system-security  

- Payatu. (2020, junio 30). *Side-Channel Attack Basics*. Payatu Blog. https://payatu.com/blog/side-channel-attack-basics/  

- Farahmand, F., Moradi, A., & Poschmann, A. (2023, abril 13). *A Comprehensive Survey on the Implementations, Attacks, and Countermeasures of the Current NIST Lightweight Cryptography Standard*. arXiv. https://arxiv.org/abs/2304.06222  

