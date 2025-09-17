# Ciberseguridad en IoT: Vulnerabilidades y Técnicas de Mitigación en Dispositivos Embebidos

## Introducción

La proliferación de dispositivos IoT (Internet de las Cosas) ha transformado múltiples sectores, pero también ha introducido nuevos riesgos de seguridad, especialmente en dispositivos embebidos.

## Principales Vulnerabilidades en IoT

**Contraseñas débiles o predeterminadas**

Muchos dispositivos IoT al configurarlos te dan credenciales génericas, como usuario admin o contraseñas desde 0000 hasta 1234, a pesar de que algunos fabricantes te recomiendan que les cambies las credenciales, muchos usuarios las ignoran, y debido a que los dispositivos IoT reducen sus costos y hay mas fabricantes para hacerlos, también hay falta de seguridad. 

**Actualizaciones de firmware insuficientes**

Muchos dispositivos IoT que son baratos y de fácil acceso, al hacerse en masa, reciben pocas o nulas actualizaciones, en la actualidad, esto es demasiado peligroso, pues las herramientas de cracking evolucionan cada día más rápido, dejando dispositivos vulnerables a estas herramientas.

**Comunicación no cifrada**

Los dispositivos IoT generan una estimación de 80 zettabytes de datos por año (eso equivale a 80 mil millones de terabytes), donde asegurar esos datos es todo un reto, muchos dispositivos IoT usan encriptación desactualizada o no la encriptan del todo, y como estos datos son suceptibles a ser interceptados, una filtración puede revelar información delicada como las rutinas o ubicación del usuario.

**Falta de protecciones de privacidad**

Muchos dispositivos IoT toman demasiados datos personales, como ubicación, salud y rutinas del usuario, esto sin una clara politica de transparencia o sin la concientización del usuario.

**Vulnerabilidades en los proveedores**

La compra y venta de dispositivos IoT involucra diferentes actores, incrementando el riesgo de componentes de hardware o software, una cadena débil sin control incrementa el riesgo de backdoors o malware, un incidente de 2025 reveló malware pre-instalado en sensores IoT low-cost, afectando sistemas industriales.

## Técnicas de Mitigación

**Uso de contraseñas fuertes y únicas**

Personaliza el nombre de usuario y la contraseña asignada, utilizando contraseñas seguras para acceder a tu dispositivo y cuenta asociada, y si es posible, usar autenticación de dos pasos mediante una aplicación o mensajes SMS.

**Implementación de actualizaciones automáticas y seguras**

Verificar si las actualizaciones de software de tu dispositivo se realizan de manera automática o no, y procura mantenerlo actualizado.

**Cifrado de datos en tránsito y en reposo**

Hacer uso de encriptación punto a punto y protocolos como TLS 1.3, los fabricantes deben priorizar estos cifrados y los usuarios deben revisar que se cumplan estos estándares de encriptación.

**Políticas claras y transparentes**

Leer los Términos y Condiciones de los dispositivos proporcionados por el fabricante, y si es posible, usar dispositivos de compañias reconocidas con sus respectivas certificaciones.

**Auditorías de seguridad**

Implementar auditorías y asegurar los procesos de manufactura, que los proveedores sean vendedores confiables y verificar la integridad de los componentes, tambien asegurar que cumplan con los certificados como la NOM o la FCC.


## Fuentes bibliográficas

GeeksforGeeks. (2025, 15 julio). Most Common Threats to Security and Privacy of IoT Devices. GeeksforGeeks. https://www.geeksforgeeks.org/blogs/most-common-threats-to-security-and-privacy-of-iot-devices/

Fredricpaul. (2024, 22 septiembre). 10 IoT vulnerabilities to avoid. Network World. https://www.networkworld.com/article/966868/10-iot-vulnerabilities-to-avoid.html/

El IFT publica el análisis de Ciberseguridad en los dispositivos de Internet de las Cosas (IoT). (Comunicado 29/2024) 9 de abril | Instituto Federal de Telecomunicaciones - IFT. (s. f.). https://www.ift.org.mx/comunicacion-y-medios/comunicados-ift/es/el-ift-publica-el-analisis-de-ciberseguridad-en-los-dispositivos-de-internet-de-las-cosas-iot#:~:text=9%20de%20abril-,El%20IFT%20publica%20el%20an%C3%A1lisis%20de%20Ciberseguridad%20en%20los%20dispositivos,9%20de%20abril%20de%202024.&text=Se%20realiz%C3%B3%20un%20an%C3%A1lisis%20a,de%20seguridad%20en%20los%20dispositivos/


