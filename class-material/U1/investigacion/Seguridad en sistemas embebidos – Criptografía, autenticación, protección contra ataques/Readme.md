# Seguridad en Sistemas Embebidos  
**Autor:** Suarez Castro Jair Alberto - 22211663  

---

## Introducción
Los sistemas embebidos son dispositivos electrónicos diseñados para realizar funciones específicas dentro de un aparato más grande. A diferencia de las computadoras de propósito general, estos sistemas cuentan con recursos limitados en memoria, energía y procesamiento. Aun así, hoy en día están presentes en automóviles, dispositivos médicos, electrodomésticos y equipos conectados a internet.

### Ejemplo de sistema embebido
[<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/31e33030-ec90-4a4a-a6e6-13c4e4c6281a" />](https://upload.wikimedia.org/wikipedia/commons/2/2c/ADSL_modem_router_internals_labeled.jpg)

La gran importancia de estos sistemas hace que su seguridad sea un tema crítico. Un ataque exitoso puede poner en riesgo no solo datos, sino también la integridad de las personas o la funcionalidad de infraestructuras completas.

---

## Criptografía en Sistemas Embebidos
La criptografía se utiliza para garantizar que la información transmitida o almacenada esté protegida contra accesos no autorizados. En los sistemas embebidos se aplica principalmente para:  

- Cifrar datos sensibles, como información médica o financiera.  
- Asegurar que la información no se modifique en el trayecto (integridad).  
- Validar que el software que se ejecuta sea legítimo mediante firmas digitales.  

Uno de los principales desafíos es que muchos algoritmos criptográficos tradicionales requieren demasiados recursos para ser implementados en dispositivos pequeños. Como respuesta, se han desarrollado algoritmos de **criptografía ligera**, entre los que destaca **Ascon**, estandarizado recientemente por el NIST (2025) como una de las soluciones más adecuadas para equipos con limitaciones de hardware.  

---

## Autenticación en Sistemas Embebidos
La autenticación permite verificar la identidad de usuarios, dispositivos o programas. En sistemas embebidos se puede aplicar de varias maneras:  

- **Autenticación de dispositivos**, asegurando que un equipo conectado a la red es realmente quien dice ser.  
- **Autenticación de usuarios**, mediante contraseñas u otros mecanismos de acceso.  
- **Arranque seguro (Secure Boot)**, que consiste en verificar que el firmware esté firmado digitalmente por el fabricante antes de ejecutarse.


De esta forma se evita que un atacante pueda instalar software malicioso o modificar el funcionamiento del sistema.

---

## Protección contra Ataques

### Ataques de red o software
Incluyen la interceptación de datos (ataques de intermediario), la instalación de malware y el uso de contraseñas débiles.  
**Medidas de defensa:** uso de protocolos de comunicación cifrada, contraseñas seguras y actualizaciones constantes.  

### Ataques físicos
Se dan cuando alguien tiene acceso directo al dispositivo. Aquí encontramos ataques de canal lateral, donde se analizan consumos eléctricos o tiempos de ejecución para descubrir claves secretas, o ataques por inyección de fallos, que buscan alterar el funcionamiento del hardware.  
**Medidas de defensa:** uso de chips especializados como TPM o secure elements, algoritmos resistentes y sensores que detectan manipulación física.  

### Actualizaciones inseguras
Un sistema que permite instalar versiones antiguas del firmware queda expuesto a vulnerabilidades conocidas.  
**Medidas de defensa:** actualizaciones firmadas digitalmente y protección contra retrocesos (rollback).  

---

## Tabla de Seguridad en Sistemas Embebidos

| Área             | Amenaza principal                   | Contramedida destacada |
|------------------|-------------------------------------|-------------------------|
| Criptografía     | Claves robadas o débiles            | Criptografía ligera (Ascon) |
| Autenticación    | Dispositivos falsos o firmware malicioso | Arranque seguro y firmas digitales |
| Ataques físicos  | Extracción de claves por hardware   | Secure elements, mitigaciones contra SCA |
| Actualizaciones  | Instalación de versiones inseguras  | OTA firmadas y protección contra rollback |

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

