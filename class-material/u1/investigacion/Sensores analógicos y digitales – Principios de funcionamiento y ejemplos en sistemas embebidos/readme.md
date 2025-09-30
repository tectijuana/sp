# Sensores analógicos y digitales – Principios de funcionamiento y ejemplos en sistemas embebidos

**Autor:** Jiménez Montes Luis Alessandro  

## Introducción
Los sensores son dispositivos fundamentales en los sistemas embebidos, ya que permiten captar información del entorno y transformarla en señales que el sistema puede procesar. Se dividen principalmente en sensores analógicos y digitales, de acuerdo con el tipo de señal de salida que generan.  

## Sensores analógicos
Un sensor analógico produce una señal continua que varía proporcionalmente a la magnitud física que mide.  
- **Ejemplos:**  
  - **Sensor de temperatura LM35** → entrega una salida de voltaje proporcional a la temperatura.  
  - **Micrófonos** → convierten ondas sonoras en variaciones de voltaje.  
  - **Sensores de luz LDR** → varían su resistencia según la intensidad luminosa.  

En los sistemas embebidos, estas señales analógicas deben ser convertidas a digital mediante un **ADC (Convertidor Analógico-Digital)** para que el microcontrolador las procese.  

## Sensores digitales
Un sensor digital entrega una señal ya procesada en forma de bits o niveles lógicos (0 y 1). Esto evita la necesidad de un ADC y facilita la comunicación con el microcontrolador.  
- **Ejemplos:**  
  - **Sensor de temperatura DHT11/DHT22** → envía datos de temperatura y humedad en formato digital.  
  - **Acelerómetro MPU6050** → proporciona datos en I2C o SPI.  
  - **Sensores de proximidad infrarrojos digitales** → detectan la presencia o ausencia de un objeto.  

## Comparación
| Característica         | Sensor Analógico                     | Sensor Digital                           |
|-------------------------|--------------------------------------|------------------------------------------|
| Señal de salida         | Continua (voltaje o corriente)       | Discreta (niveles lógicos o datos)       |
| Procesamiento requerido | Conversión ADC                       | Lectura directa por microcontrolador     |
| Precisión               | Depende del ADC y ruido              | Generalmente más estable y precisa       |
| Ejemplo                 | LM35, LDR, micrófono                 | DHT11, MPU6050, sensores IR digitales    |

## Conclusión
La correcta selección entre un sensor analógico o digital depende de las necesidades de precisión, costo y complejidad del sistema embebido. Los sensores analógicos son útiles en aplicaciones que requieren señales continuas y mayor resolución, mientras que los digitales simplifican la integración y reducen la carga de procesamiento.  

---
