# Simulación de Sensor de Sonido (Micrófono Electret, MEMS, Dinámico)

**Presentado por:** Brandon Orozco Hernández  
**Número de control:** 21212577  

## Introducción
Los sensores de sonido o micrófonos convierten las ondas de sonido en señales eléctricas. Existen varios tipos de micrófonos, entre ellos:

- **Electret**: Basados en un material con carga permanente.
- **MEMS**: Microelectromecánicos, usados en dispositivos modernos.
- **Dinámicos**: Funcionan mediante inducción electromagnética.

## Funcionamiento de los Sensores de Sonido
Cada tipo de sensor tiene un principio de operación distinto:

- **Electret**: Contiene un diafragma y una placa con carga permanente que varía su capacitancia con el sonido.
- **MEMS**: Usa estructuras microelectromecánicas que detectan cambios de presión sonora.
- **Dinámico**: Usa una bobina móvil dentro de un campo magnético para generar voltaje proporcional a la vibración.

## Aplicaciones
Los sensores de sonido tienen múltiples aplicaciones, como:

- Reconocimiento de voz en asistentes virtuales.
- Grabación de audio y música.
- Sistemas de vigilancia y seguridad.
- Medición de ruido ambiental.

## Ventajas y Desventajas

| Tipo de Micrófono | Ventajas | Desventajas |
|------------------|----------|------------|
| Electret | Económico, buena sensibilidad | Necesita alimentación, ruido de fondo |
| MEMS | Pequeño, bajo consumo | Puede tener menor calidad de audio |
| Dinámico | Robusto, alta calidad | Tamaño y peso elevados |

## Simulación en Python
Para simular un sensor de sonido, podemos generar una señal de audio y visualizarla con `matplotlib`.

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulación de una onda de sonido (señal de micrófono)
fs = 44100  # Frecuencia de muestreo
T = 1       # Duración en segundos
t = np.linspace(0, T, fs*T, endpoint=False)
frecuencia = 440  # Frecuencia de la onda (Hz)
senal = np.sin(2 * np.pi * frecuencia * t)

# Visualizar la señal
plt.plot(t[:1000], senal[:1000])
plt.title("Señal Simulada del Micrófono")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()
```

## Conclusión
Los sensores de sonido juegan un papel clave en múltiples industrias. La elección del sensor depende de la aplicación y los requerimientos específicos de sensibilidad, tamaño y calidad de audio.

## Referencias
- "Electret Microphones", Texas Instruments.
- "MEMS Microphones Overview", Knowles Electronics.
- "Dynamic Microphones", Shure Inc.

  
![image](https://github.com/user-attachments/assets/220092c1-86ab-4b75-915a-39606b614574)
![image](https://github.com/user-attachments/assets/c9c12f88-42eb-4cba-9b82-dfbc112f9d41)
