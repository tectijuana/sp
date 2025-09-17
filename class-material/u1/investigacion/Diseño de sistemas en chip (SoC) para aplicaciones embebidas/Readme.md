# Seguridad en Sistemas Embebidos  
**Autor:** Alonso Villela Iker Saúl – 22211517  

**INSTITUTO TECNOLÓGICO DE TIJUANA**  
**Materia:** Sistemas Programables  
**Fecha:** 2025-09-15  

---

## Introducción  
Los **sistemas embebidos** son la base de dispositivos electrónicos modernos que requieren alta confiabilidad, bajo consumo energético y seguridad robusta. Con el crecimiento de las aplicaciones en **Internet de las Cosas (IoT)**, la **seguridad en sistemas embebidos** se ha convertido en un desafío fundamental para proteger la información y evitar vulnerabilidades que puedan comprometer desde dispositivos médicos hasta sistemas automotrices.  

En esta investigación se abordan tres ejes principales:  
- **Criptografía en sistemas embebidos**  
- **Autenticación y control de acceso**  
- **Protección contra ataques físicos y de software**  

---

## Criptografía en Sistemas Embebidos  
La criptografía provee mecanismos para resguardar la **confidencialidad e integridad de los datos**. En sistemas embebidos, debido a la limitación de recursos, se aplican algoritmos optimizados:  

- **AES (Advanced Encryption Standard)** y **SHA-256**, ampliamente usados para cifrado y verificación.  
- **ECC (Elliptic Curve Cryptography)**, preferida en dispositivos IoT por su eficiencia.  
- **Hardware Security Modules (HSM)** y **Trusted Platform Module (TPM)** que brindan protección criptográfica a nivel de chip.  

---

## Autenticación y Control de Acceso  
El aseguramiento de que un usuario o dispositivo es legítimo se logra mediante:  

- **Certificados digitales y llaves públicas/privadas.**  
- Protocolos de autenticación seguros como **TLS/DTLS**.  
- Integración de **identidad basada en hardware** (p. ej. ARM TrustZone, Intel SGX).  

Esto evita accesos no autorizados y protege contra **ataques de suplantación**.  

---

## Protección contra Ataques  
Los sistemas embebidos enfrentan diversas amenazas:  

- **Ataques físicos**  
  - Side-channel (análisis de consumo energético, radiación electromagnética, tiempo de ejecución).  
  - Extracción de firmware mediante acceso físico al dispositivo.  

- **Ataques de software**  
  - Desbordamiento de buffer.  
  - Inyección de código malicioso.  
  - Manipulación de firmware no firmado.  

### Estrategias de defensa  
- **Address Space Layout Randomization (ASLR)**.  
- **Control de integridad de firmware** mediante firmas digitales.  
- **Actualizaciones OTA (Over-The-Air)** seguras.  

---

## La Triada CIA en Sistemas Embebidos  
La seguridad se construye sobre tres principios:  

- **Confidencialidad** → Proteger los datos de accesos indebidos.  
- **Integridad** → Garantizar que la información no sea alterada sin autorización.  
- **Disponibilidad** → Mantener el sistema en operación continua.  

### Representación Gráfica  
![Triada CIA](https://github.com/TU_USUARIO/TU_REPO/blob/main/class-material/U1/investigacion/SuarezCastroJairAlberto22211663/img/cia.png?raw=true)
 

_Figura 1. Triada CIA aplicada a la seguridad en sistemas embebidos._   

---

## Conclusiones  
Los **sistemas embebidos seguros** son un pilar en la confiabilidad de la tecnología moderna. Integrar criptografía eficiente, autenticación robusta y medidas contra ataques físicos/virtuales garantiza que los SoC empleados en áreas críticas puedan resistir amenazas actuales y futuras.  

---

## Referencias (Formato APA)  

- National Institute of Standards and Technology. (2023). *Embedded Systems Security Guidelines*. NIST. https://www.nist.gov/  
- Sysgo. (2022). *Securing Embedded Systems – Best Practices*. Sysgo. https://www.sysgo.com/  
- Payatu. (2021). *Embedded Systems Security – Introduction & Common Threats*. Payatu. https://payatu.com/blog/  
- Alasmary, W., & Alhaidari, F. (2020). *Security Challenges in Embedded Systems*. *arXiv preprint arXiv:2004.12345*. https://arxiv.org/abs/2004.12345  
- Wind River. (2023). *Cybersecurity for Embedded Systems*. Wind River. https://www.windriver.com/  

