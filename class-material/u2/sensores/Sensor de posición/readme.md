# Sanchez Salinas Eduardo Josuse 20210637
# Sensores de Posición  

## 1. Sensor de Posición: Encoder  

### Funcionamiento  
El encoder es un dispositivo electromecánico utilizado para convertir el movimiento mecánico (como la rotación) en señales eléctricas, que pueden ser interpretadas por un sistema de control.  
- Existen dos tipos principales: **incrementales** y **absolutos**.  
- En los encoders incrementales, se generan pulsos según el movimiento, mientras que los absolutos proporcionan una posición precisa en todo momento.  

### Aplicaciones  
- **Automatización industrial**: para medir la rotación de motores y ejes.  
- **Robótica**: para controlar la posición y el movimiento de los actuadores.  
- **Dispositivos de entrada**: como los ratones de computadora.  

### Ventajas y desventajas  
| **Encoder** |   |
|------------|-----------------------------|
| **Ventajas** | - Alta precisión.  <br> - Respuesta rápida.  <br> - Capacidad de medir tanto posición como velocidad. |
| **Desventajas** | - Sensible a interferencias electromagnéticas.  <br> - Requiere procesamiento de señales.  <br> - Puede ser costoso según la resolución. |


### Ejemplo práctico  
- Control de un servomotor para el posicionamiento preciso de un brazo robótico.  

---
<img src="https://github.com/user-attachments/assets/e50a48e0-2b94-478f-a9d3-265ec548e331" alt="66J8005-40" width="300">


## 2. Sensor de Posición: GPS (Sistema de Posicionamiento Global)  

### Funcionamiento  
- El GPS funciona mediante la recepción de señales de al menos **4 satélites**, que permiten calcular la ubicación en términos de **latitud, longitud y altitud**.  
- Usa el principio de la **trilateración**, calculando la distancia a los satélites con la información de tiempo enviada por estos.  

### Aplicaciones  
- **Navegación vehicular**: Guía de autos y rutas de transporte.  
- **Geolocalización**: En smartphones y sistemas de seguimiento en tiempo real.  
- **Agricultura de precisión**: Para monitorear la ubicación exacta de equipos en campos.  

### Ventajas y desventajas 

| **GPS** |   |
|------------|-----------------------------|
| **Ventajas** | - Cobertura global.  <br> - No requiere contacto físico.  <br> - Precisión suficiente para la mayoría de aplicaciones. |
| **Desventajas** | - Menos preciso en entornos urbanos.  <br> - Alto consumo energético.  <br> - Depende de la visibilidad de los satélites. |


### Ejemplo práctico  
- Sistema de navegación de vehículos, proporcionando direcciones en tiempo real.  

---
![download](https://github.com/user-attachments/assets/115d857a-5c2c-46ca-9f26-f59f856a21ef)

## 3. Sensor de Posición: Potenciómetro  

### Funcionamiento  
El potenciómetro es un tipo de **resistor variable** que ajusta su resistencia en función de la posición de un **eje rotatorio o deslizante**.  
- La variación de la resistencia se convierte en una **señal analógica** proporcional a la posición.  

### Aplicaciones  
- **Control de volumen** en dispositivos electrónicos.  
- **Sistemas de control de ángulo** en motores eléctricos.  
- **Medición de desplazamientos lineales** en aplicaciones de automatización.  

### Ventajas y desventajas  

| **Potenciómetro** |   |
|-------------------|-----------------------------|
| **Ventajas** | - Fácil de usar y económico.  <br> - Baja demanda de energía.  <br> - Precisión suficiente para aplicaciones básicas. |
| **Desventajas** | - Se desgasta con el uso.  <br> - Menos preciso que otros sensores.  <br> - Limitado a movimientos pequeños. |

### Ejemplo práctico  
- Control del volumen de un amplificador o ajuste de la posición de un servo motor en robótica.  
![download](https://github.com/user-attachments/assets/adfed6dc-0318-4fb6-95ce-c84a95831aec)




