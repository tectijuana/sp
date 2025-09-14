# Seguridad en sistemas embebidos

## Datos del alumno:
**Nombre:** Quiñonez Agramon Angel Gabriel
**Numero de control:** 21210860
**Nickname:** AngelAgramon
**Feca¿ha:** 06/02/2025


Los sistemas embebidos, presentes en dispositivos IoT, automóviles, electrodomésticos, entre otros, necesitan implementar medidas de seguridad para evitar que sean vulnerables a ataques cibernéticos. A continuación, se detallan las principales técnicas de seguridad: **criptografía**, **autenticación** y **protección contra ataques**.

## Criptografía

![computerteamwork](https://github.com/user-attachments/assets/3e332057-5bcb-44f4-a13e-036a06e18817)

La criptografía es crucial para proteger la información sensible en sistemas embebidos. Algunas técnicas importantes incluyen:

- **Criptografía simétrica**: Utiliza una única clave para cifrar y descifrar la información. Ejemplos comunes son AES (Advanced Encryption Standard).
- **Criptografía asimétrica**: Utiliza un par de claves, una pública y una privada, para cifrar y descifrar datos. Ejemplos incluyen RSA y ECC (Elliptic Curve Cryptography).
- **Algoritmos hash**: Se utilizan para generar huellas digitales de datos, asegurando la integridad de los mismos. Ejemplo: SHA-256.

## Autenticación


La autenticación asegura que solo usuarios o dispositivos legítimos accedan a un sistema embebido:

- **Autenticación de dispositivos**: Verifica la identidad de los dispositivos antes de permitir la comunicación en redes IoT. Se puede hacer mediante certificados digitales o contraseñas seguras.
- **Autenticación multifactor (MFA)**: Involucra varios métodos de verificación como contraseñas, tokens de hardware o datos biométricos para confirmar la identidad de un usuario.
- **Firmas digitales**: Garantizan la autenticidad de los mensajes, asegurando que provienen de una fuente confiable y no han sido alterados.

## Protección contra ataques

Los sistemas embebidos deben estar preparados para resistir diversos tipos de ataques. Algunos de los más comunes son:

- **Ataques de fuerza bruta**: Se debe usar encriptación fuerte y autenticación robusta para evitar que un atacante adivine credenciales o claves de cifrado.
- **Ataques de canal lateral**: Técnicas como enmascaramiento y blindaje pueden mitigar la posibilidad de que un atacante obtenga información a través de la medición de consumo de energía, tiempos de procesamiento o emisiones electromagnéticas.
- **Ataques de inyección**: Implementar validaciones y sanitización de entradas en el software embebido para prevenir la inyección de código malicioso.
- **Actualizaciones seguras**: Utilizar actualizaciones de firmware firmadas y seguras, con mecanismos de verificación, para proteger los dispositivos contra versiones maliciosas o comprometidas.

## Conclusión

La seguridad en sistemas embebidos es vital para proteger tanto los dispositivos como la información que manejan. La criptografía, la autenticación robusta y las medidas de protección contra ataques son fundamentales para garantizar la integridad y confidencialidad en estos entornos.
