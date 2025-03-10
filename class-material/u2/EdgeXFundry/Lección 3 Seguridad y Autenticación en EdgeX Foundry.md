# **Lección 3: Seguridad y Autenticación en EdgeX Foundry** 🔒  

---

## **1. Objetivo de la Lección**  
Al finalizar esta lección, el estudiante comprenderá cómo **EdgeX Foundry** implementa la seguridad y autenticación en su arquitectura. Se explorarán **Vault, Kong, JWT, encriptación de datos y control de acceso**, además de configuraciones de seguridad en servicios EdgeX.  

---

## **2. Introducción**  
### **2.1 Importancia de la Seguridad en IoT**  
Los sistemas IoT manejan información crítica, como datos de sensores industriales, dispositivos médicos o sistemas de monitoreo. Sin medidas de seguridad adecuadas, estos sistemas son vulnerables a ataques como:  
- **Intercepción de datos** (man-in-the-middle).  
- **Accesos no autorizados** a dispositivos y servicios.  
- **Modificación de datos** en tránsito.  

### **2.2 Seguridad en EdgeX Foundry**  
EdgeX Foundry integra varios mecanismos de seguridad, incluyendo:  
- **Vault**: Almacenamiento seguro de credenciales y secretos.  
- **Kong API Gateway**: Protección y autenticación de servicios.  
- **JWT (JSON Web Token)**: Control de acceso mediante tokens.  
- **TLS (Transport Layer Security)**: Encriptación de comunicación entre servicios.  

---

## **3. Vault: Almacenamiento Seguro de Credenciales**  
### **3.1 ¿Qué es Vault?**  
Vault es un servicio que protege información sensible como claves API, credenciales de bases de datos y certificados. En EdgeX, Vault se usa para:  
- Almacenar **contraseñas de microservicios**.  
- Proteger **claves de cifrado** de los datos.  
- Administrar **tokens de acceso** para los servicios de EdgeX.  

### **3.2 Comprobación del Estado de Vault**  
Para verificar si Vault está funcionando en un entorno EdgeX, ejecutar:  
```bash
docker ps | grep vault
```
Para acceder a Vault dentro del contenedor:  
```bash
docker exec -it edgex-vault sh
vault status
```

### **3.3 Recuperar una Clave Secreta**  
```bash
vault kv get secret/edgex/core-data
```
Para escribir una nueva clave:  
```bash
vault kv put secret/edgex/core-data password="edgex1234"
```

---

## **4. Kong API Gateway: Autenticación y Control de Acceso**  
### **4.1 ¿Qué es Kong?**  
Kong es un API Gateway que protege los servicios de EdgeX mediante autenticación y control de acceso.  
Se encarga de:  
- Gestionar **tokens JWT**.  
- Aplicar **restricciones de acceso** a microservicios.  
- Proteger **endpoints de API** con autenticación y autorización.  

### **4.2 Verificación del Estado de Kong**  
```bash
docker ps | grep kong
```
Para verificar si Kong está en funcionamiento:  
```bash
curl http://localhost:8001
```

### **4.3 Crear un Usuario en Kong**  
Para registrar un usuario en Kong:  
```bash
curl -X POST http://localhost:8001/consumers \
  --data "username=usuarioIOT"
```

### **4.4 Generar una API Key**  
```bash
curl -X POST http://localhost:8001/consumers/usuarioIOT/key-auth
```
Esto devolverá una clave API que puede usarse para acceder a servicios protegidos.

---

## **5. Control de Acceso con JWT**  
### **5.1 ¿Qué es JWT?**  
JSON Web Token (**JWT**) es un estándar de autenticación basado en tokens encriptados. EdgeX lo utiliza para:  
- Autenticar **usuarios y dispositivos**.  
- Controlar **permisos de acceso a APIs**.  

### **5.2 Obtener un Token JWT**  
```bash
curl -X POST http://localhost:8001/consumers/usuarioIOT/jwt
```
Este comando genera un token JWT para el usuario registrado en Kong.

### **5.3 Usar el Token JWT para Autenticación**  
Para acceder a un servicio protegido:  
```bash
curl -H "Authorization: Bearer <TOKEN>" http://localhost:59880/api/v3/ping
```
Si el token es válido, el servicio responderá con un mensaje de éxito.

---

## **6. Encriptación de Datos en EdgeX Foundry**  
### **6.1 Habilitar TLS en EdgeX**  
TLS (Transport Layer Security) cifra la comunicación entre los servicios de EdgeX.  

Para verificar si TLS está habilitado:  
```bash
cat /etc/edgex/security/tls-cert.pem
```
Para habilitar TLS en EdgeX:  
```yaml
Service:
  ServerBindAddr: 0.0.0.0
  ServerBindPort: 8443
  HTTPSCertFile: "/etc/edgex/security/tls-cert.pem"
  HTTPSKeyFile: "/etc/edgex/security/tls-key.pem"
```
Después de configurar, reiniciar EdgeX:  
```bash
docker-compose restart
```

---

## **7. Seguridad en los Servicios de EdgeX**  
### **7.1 Configuración de Seguridad en Core Services**  
Para activar autenticación en Core Data (`configuration.toml`):  
```toml
[Service]
RequireAuthentication = true
```

### **7.2 Proteger los Logs y Registros**  
Para restringir acceso a los logs:  
```bash
chmod 600 /var/log/edgex/*.log
```

---

## **8. Evaluación**  
### **8.1 Preguntas de Revisión**  
1. ¿Cuál es el propósito de Vault en EdgeX Foundry?  
2. ¿Cómo protege Kong los servicios de EdgeX?  
3. ¿Qué es JWT y cómo se usa en EdgeX?  

### **8.2 Práctica**  
1. Configurar y probar autenticación JWT en EdgeX.  
2. Habilitar TLS en un entorno EdgeX y verificar la comunicación segura.  
3. Proteger el acceso a Core Data con autenticación basada en API Keys.  

---

## **9. Conclusión**  
EdgeX Foundry implementa un enfoque integral de seguridad con **Vault, Kong, JWT y TLS**, garantizando la protección de datos y control de acceso en sistemas IoT. La correcta configuración de seguridad es clave para implementar EdgeX en entornos industriales y comerciales.  

---

### **Próxima Lección**  
**"Optimización y Despliegue de EdgeX Foundry en Producción"** 🚀
