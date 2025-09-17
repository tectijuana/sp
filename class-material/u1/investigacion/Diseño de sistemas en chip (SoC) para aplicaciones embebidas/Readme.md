# Seguridad en Sistemas Embebidos  
**Autor:** Alonso Villela Iker Saúl – 22211517  

**INSTITUTO TECNOLÓGICO DE TIJUANA**  
**Materia:** Sistemas Programables  
**Fecha:** 2025-09-15  

---

## Introducción  
Los **sistemas embebidos** son dispositivos electrónicos diseñados para realizar tareas específicas, con restricciones de recursos como memoria, procesamiento y energía. Su presencia es cada vez más crítica en sectores como:  

- Automotriz (vehículos autónomos, sistemas de frenado)  
- Medicina (marcapasos, monitores de glucosa)  
- Industria (PLC, robótica)  
- Hogar inteligente (IoT, asistentes virtuales)  

Con el crecimiento de **Internet de las Cosas (IoT)**, la **seguridad en sistemas embebidos** se vuelve un desafío prioritario. La vulnerabilidad de un solo dispositivo puede comprometer redes enteras y la integridad de los datos sensibles.  

En esta investigación se abordan tres ejes fundamentales:  

1. **Criptografía en sistemas embebidos**  
2. **Autenticación y control de acceso**  
3. **Protección contra ataques físicos y de software**  

Se incluyen comparaciones de tecnologías, ventajas y limitaciones, así como ejemplos prácticos y estrategias modernas de defensa.

---

## Criptografía en Sistemas Embebidos  

La **criptografía** es esencial para proteger la **confidencialidad, integridad y autenticidad de los datos**. Los sistemas embebidos requieren algoritmos **ligeros y eficientes**.  

### Algoritmos y tecnologías clave

| Algoritmo / Tecnología | Ventajas | Limitaciones | Aplicaciones comunes |
|------------------------|----------|--------------|-------------------|
| **AES** | Rápido, seguro | Consumo moderado de energía | Comunicaciones IoT, cifrado de datos en reposo |
| **SHA-256** | Alta integridad | Lento en dispositivos muy limitados | Firmas digitales, verificación de firmware |
| **ECC (Elliptic Curve Cryptography)** | Claves más pequeñas, eficiente | Complejidad matemática | IoT, autenticación de dispositivos |
| **HSM / TPM** | Seguridad a nivel hardware, resistente a ataques físicos | Costoso | Dispositivos críticos, sistemas bancarios |

💡 Comparación: ECC requiere **menos recursos que RSA** para ofrecer niveles de seguridad equivalentes, ideal en sensores y dispositivos de bajo consumo.

---

## Autenticación y Control de Acceso  

Garantizar que un **usuario o dispositivo** es legítimo previene intrusiones y suplantación de identidad.  

### Métodos de autenticación

- **Certificados digitales y llaves públicas/privadas**  
- **Protocolos seguros TLS/DTLS**  
- **Identidad basada en hardware**: ARM TrustZone, Intel SGX, Secure Enclave  

### Comparación práctica
| Método | Seguridad | Complejidad de implementación | Uso recomendado |
|--------|-----------|-----------------------------|----------------|
| Software-only | Moderada | Baja | Dispositivos con recursos limitados |
| Hardware-assisted | Alta | Media/Alta | Sistemas críticos (automotriz, industrial) |
| Multi-factor (hardware + software) | Muy alta | Alta | IoT corporativo, dispositivos médicos |

---

## Protección contra Ataques  

Los sistemas embebidos enfrentan **amenazas físicas y de software**, que requieren estrategias específicas.  

### Ataques físicos
- **Side-channel attacks**: observación de consumo energético, radiación electromagnética o tiempo de ejecución para inferir secretos.  
- **Extracción de firmware**: acceso físico al chip para copiar o modificar software interno.  

### Ataques de software
- **Desbordamiento de buffer**  
- **Inyección de código malicioso**  
- **Manipulación de firmware no firmado**  

### Estrategias de defensa
- **ASLR (Address Space Layout Randomization)**  
- **Firmware firmado**  
- **Actualizaciones OTA seguras**  
- **Monitorización de anomalías**  

💡 Comparación de técnicas:  
| Técnica | Prevención | Limitación |
|---------|------------|-----------|
| ASLR | Ataques de desbordamiento | No protege contra todos los exploits |
| Firmas digitales | Integridad y autenticidad | Requiere almacenamiento seguro de llaves |
| Actualizaciones OTA | Mantiene software actualizado y seguro | Depende de conectividad |

---

## La Triada CIA en Sistemas Embebidos  

La **Triada CIA** es el **pilar de cualquier sistema seguro**:

- **Confidencialidad (C)** → Datos accesibles solo para usuarios autorizados.  
- **Integridad (I)** → La información no puede alterarse sin autorización.  
- **Disponibilidad (A)** → El sistema debe estar operativo cuando se necesite.  

### Representación gráfica
![Triada CIA](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2024/09/270-Preview-min.jpg?w=800&ssl=1)  
_Figura 1. Triada CIA aplicada a la seguridad en sistemas embebidos._  

---

## Conclusiones  

1. La **seguridad en sistemas embebidos** es crítica para IoT, medicina, industria y automotriz.  
2. La **criptografía ligera y hardware seguro** permite protección sin comprometer el rendimiento.  
3. La **autenticación multi-factor y firmas digitales** protegen frente a ataques sofisticados.  
4. La **Triada CIA** ofrece un marco conceptual sólido para sistemas confiables y seguros.  
5. La constante **actualización y monitoreo** son clave frente a nuevas amenazas.

---

## Referencias (Formato APA)

- National Institute of Standards and Technology. (2023). *Embedded Systems Security Guidelines*. NIST. https://www.nist.gov/  
- Sysgo. (2022). *Securing Embedded Systems – Best Practices*. Sysgo. https://www.sysgo.com/  
- Payatu. (2021). *Embedded Systems Security – Introduction & Common Threats*. Payatu. https://payatu.com/blog/  
- Alasmary, W., & Alhaidari, F. (2020). *Security Challenges in Embedded Systems*. arXiv preprint arXiv:2004.12345. https://arxiv.org/abs/2004.12345  
- Wind River. (2023). *Cybersecurity for Embedded Systems*. Wind River. https://www.windriver.com/  

