<img width="546" alt="Screenshot 2025-02-24 at 2 09 42 p m" src="https://github.com/user-attachments/assets/ca3ef569-c3e2-4ed6-9f6f-e1bea41bc9fc" />


**Actividad 1.5: ¿Qué sensores tiene tu smartphone?**
s  
**Fecha de entrega:** Ver IDoceo
**Puntaje:** 100 puntos (parcial sobre Practicas)

**Descripción:**  
En esta actividad, exploraremos los sensores que integran los dispositivos móviles y cómo interactúan con ellos mediante aplicaciones. Deberás utilizar una app que te permita identificar los sensores en tu smartphone y presentar un informe claro y conciso. Dependera del tipo de celular sección 1 es para Iphone 

#**Seccion 1 iOS:**

1. **Descargar Aplicaciones:**
   - **iPhone:** "Sensor-app"
   
   Ambas aplicaciones son gratuitas. Además, descarga **LOOM** para grabar tu presentación (disponible para Android e iPhone).

2. **Tarea Principal:**
   - Encuentra la aplicación que te permita identificar los sensores de tu dispositivo móvil. Graba un video de tu pantalla donde demuestres los sensores disponibles.
   - Si no cuentas con un smartphone compatible, puedes hacer una BINA (video en colaboración) con un compañero del grupo. Asegúrate de notificarlo mediante un mensaje privado.

3. **Formato de Entrega:**
   - En el video, **comenta los sensores** que se encuentran en tu dispositivo. Presenta un formato de lista con la explicación de cada sensor detectado.
   - La grabación debe ser clara y concisa. Si eres beneficiario de una beca, puedes extender el tiempo de grabación, de lo contrario, limita el video a un máximo de 5 minutos.
   - **LOOM** tiene un editor integrado. Utilízalo para cortar cualquier error y asegurarte de que el contenido sea lo más efectivo posible dentro del tiempo asignado.

4. **Entrega:**
   - **URL de la grabación** en LOOM (verifica que funcione correctamente). Asegúrate de no recargar la página antes de que el video se haya procesado por completo, ya que esto podría corromper la grabación.  
   - **Nota importante:** LOOM tarda de 2 a 3 minutos en procesar el video. Si no esperas a que se cargue completamente, es posible que el video aparezca con una línea gris en el centro y debas repetirlo.

**Criterios de Evaluación:**

| **Criterio**                                        | **Puntaje**    |
|-----------------------------------------------------|----------------|
| **Explicación detallada de las secciones de la app** | 100%           |
| **Explicación parcial de las secciones de la app**  | 80%            |
| **Explicación insuficiente**                        | 50%            |
| **No entregado en tiempo y forma**                  | 0%             |

---
# Entrega el Link de LOOM (no archivo) en Idoceo, este da 5 minutos máx de grabación es un vistazo a sus sensores.

----

#**Seccion 2 Android:**
---


# Práctica: Exploración de Sensores en Android con Termux

## 🎯 Objetivo
El estudiante será capaz de:
- Identificar los sensores disponibles en su dispositivo Android mediante Termux.  
- Usar scripts de Bash para listar y leer valores de sensores en vivo.  
- Documentar la información en formato tabla y generar evidencia en video con **Asciinema**.  
- Publicar resultados y documentación asciinema

---

## 📋 Instrucciones

### 1. Preparación del entorno
1. Instala **Termux** y **Termux:API** desde F-Droid.  
2. En Termux, instala los paquetes necesarios:
   ```bash
   pkg update && pkg upgrade -y
   pkg install termux-api asciinema nano -y
   ```

---

### 2. Script de información del dispositivo

Crea el archivo `info.sh` con:

```bash
#!/bin/bash
echo "===== Información del Dispositivo ====="
echo "Fabricante: $(getprop ro.product.manufacturer)"
echo "Modelo:     $(getprop ro.product.model)"
echo "Android:    $(getprop ro.build.version.release)"
echo "Kernel:     $(uname -r)"
echo "Arquitectura CPU: $(getprop ro.product.cpu.abi)"
echo "Número de serie:  $(getprop ro.serialno)"
echo
echo "===== CPU ====="
cat /proc/cpuinfo | grep -E "Hardware|Processor|model name" | uniq
echo
echo "===== Memoria RAM ====="
grep MemTotal /proc/meminfo
```

Guarda y dale permisos:

```bash
chmod +x info.sh
./info.sh
```

---

### 3. Script de sensores

Crea `sensores.sh` con:

```bash
#!/bin/bash
echo "===== Sensores disponibles ====="
termux-sensor -l
echo
echo "Para ver datos en vivo de un sensor específico:"
echo "Ejemplo: termux-sensor -s AccelSensor"
```

Permisos y ejecución:

```bash
chmod +x sensores.sh
./sensores.sh
```

---

### 4. Tabla de referencia de sensores

Completa en tu cuaderno o documento de portal la siguiente tabla con al menos **5 sensores reales detectados en tu teléfono**:

# Tabla de Sensores en Android (para Termux)

| `<NOMBRE_SENSOR>`       | Descripción breve                                      |
|--------------------------|--------------------------------------------------------|
| **AccelSensor**          | Acelerómetro: mide la aceleración en los ejes X, Y, Z. |
| **GyroscopeSensor**      | Giroscopio: mide la rotación del dispositivo.          |
| **MagneticFieldSensor**  | Magnetómetro: mide el campo magnético (brújula).       |
| **OrientationSensor**    | Orientación: combina sensores para dar ángulos de giro.|
| **ProximitySensor**      | Proximidad: detecta objetos cercanos (ej. llamada).    |
| **LightSensor**          | Sensor de luz: mide la iluminación ambiental.          |
| **PressureSensor**       | Barómetro: mide la presión atmosférica.                |
| **HumiditySensor**       | Humedad relativa del ambiente.                         |
| **TemperatureSensor**    | Temperatura ambiente.                                  |
| **GameRotationVector**   | Orientación optimizada para juegos (más estable).      |
| **StepCounter**          | Contador de pasos (pedometer).                         |
| **StepDetector**         | Detecta un paso en el momento que ocurre.              |
| **HeartRateSensor**      | Ritmo cardíaco (si el dispositivo lo soporta).         |
| **AmbientTemperature**   | Temperatura ambiente (algunos modelos antiguos).       |

---

### 5. Actividad práctica

* Selecciona **3 sensores distintos** (ejemplo: `AccelSensor`, `GyroscopeSensor`, `LightSensor`).
* Muestra los valores en vivo con:

  ```bash
  termux-sensor -s AccelSensor -s GyroscopeSensor -s LightSensor
  ```
* EJEMPLO: Deja correr el comando **30 segundos** moviendo el teléfono para observar cambios.
* Evalua el resto, puede que algunos no funcionen en su modelo
* Se grabará en su Asciinema

---

### 6. Evidencia en Asciinema

Graba toda tu sesión (ejecución de `info.sh`, `sensores.sh`, y captura de sensores en vivo) con:

```bash
asciinema rec practica_sensores_phone
```

Cuando termines:

```bash
exit
```

Recuperar la grabación antes de 7 dias para que no se purge por el sistema. Ya sucedio a unos del grupo, no reclamaron el link se expiro.

---

### 7. Documentación en el portal

En el portal sube:

* Enlance bien documentado en Ascinema.org
* La tabla de sensores completada.
* Breve conclusión sobre qué sensores detectó tu dispositivo y cuáles no funcionan.

---

## ✅ Rúbrica de evaluación (100 pts)

| Criterio                               | Excelente (100%)                         | Satisfactorio (80%)  | Insuficiente (50%)          | Nulo (0%)     |
| -------------------------------------- | ---------------------------------------- | -------------------- | --------------------------- | ------------- |
| **Ejecución del script `info.sh`**     | Correcto y completo                      | Ejecución parcial    | Errores graves              | No se realizó |
| **Ejecución del script `sensores.sh`** | Lista completa y funcional               | Lista parcial        | Con errores                 | No se realizó |
| **Tabla de sensores en portal**        | 5+ sensores documentados                 | 3-4 sensores         | 1-2 sensores                | Ninguno       |
| **Evidencia en Asciinema**             | Grabación completa y con nombre correcto, portal documentado en markdown | Grabación incompleta | Archivo dañado o incompleto | No entregado  |
| **Conclusión personal**                | Clara y reflexiva                        | Superficial          | Muy breve                   | No entregada  |


