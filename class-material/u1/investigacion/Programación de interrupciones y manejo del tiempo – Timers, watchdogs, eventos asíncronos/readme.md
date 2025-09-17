# Programación de interrupciones y manejo del tiempo – Timers, watchdogs, eventos asíncronos.

## Datos del alumno
- Nombre: Barboza Uribe Gilberto Yahir
- Número de control:22210285
- Fecha: 15/09/2025
- Nombre de usuario: yahir barboza

---
# Programación de interrupciones y manejo del tiempo  
## Timers, Watchdogs y eventos asíncronos

---

## 1. Introducción
- Los sistemas embebidos requieren **control preciso del tiempo** y **respuesta inmediata a eventos**.  
- Se utilizan **interrupciones, timers, watchdogs y eventos asíncronos** para lograr confiabilidad y funcionamiento en tiempo real.

---

## 2. Interrupciones
- **Definición:** Señal que pausa la ejecución normal de un programa para atender un evento prioritario.  
- **Tipos:**
  - Externas → hardware (ej. botón, puerto serie).
  - Internas → generadas por el procesador (ej. desbordamiento de timer).
  - Software → activadas por instrucciones del programa.  
- **Ventajas:**
  - Eficiencia → evita polling.
  - Respuesta rápida en tiempo real.  
- **Desventajas:**
  - Mal manejo puede causar bloqueos.
  - Exceso de interrupciones → saturación del procesador.

---

## 3. Timers (temporizadores)
- **Definición:** Periféricos que cuentan ciclos de reloj o intervalos de tiempo.  
- **Funciones:**
  - Medir intervalos.
  - Generar retardos precisos.
  - Control de eventos periódicos.
  - Generar PWM.  
- **Tipos:**
  - Conteo ascendente/descendente.
  - Comparación → interrupción cuando el contador = valor definido.
  - Captura → guarda valor al detectar evento externo.

---

## 4. Watchdogs (perros guardianes)
- **Definición:** Timer especial que reinicia el sistema si detecta fallos o bloqueos.  
- **Funcionamiento:** El software debe “alimentarlo” periódicamente; si no lo hace → reset automático.  
- **Aplicaciones:**
  - Sistemas críticos: médicos, automotrices, aeroespaciales.  
- **Ventajas:**
  - Confiabilidad.
  - Autorecuperación del sistema.  

---

## 5. Eventos asíncronos
- **Definición:** Ocurren de forma inesperada o independiente del flujo principal.  
- **Ejemplos:**
  - Dato recibido por UART, SPI, I2C.
  - Activación de sensor.
  - Fin de conversión de ADC.  
- **Manejo:**
  - Interrupciones.
  - Callbacks (funciones asociadas).
  - Colas de mensajes (en RTOS).

---

## 6. Relación entre elementos
- **Timers** → generan interrupciones periódicas.  
- **Watchdog** → tipo especial de timer para seguridad.  
- **Eventos asíncronos** → gestionados mediante interrupciones de timers o periféricos.  

---

## 7. Ejemplo práctico
1. **Timer** genera interrupción cada 1 ms para leer sensor.  
2. Si sensor detecta señal → interrupción externa (evento asíncrono).  
3. Si programa se cuelga y no atiende al **watchdog** → reinicio automático del sistema.  

---

## 8. Conclusión
- La programación de interrupciones y el manejo del tiempo son **pilares en sistemas embebidos**.  
- **Timers →** precisión temporal.  
- **Watchdogs →** seguridad y recuperación.  
- **Eventos asíncronos →** interacción eficiente con el entorno.  
- En conjunto permiten sistemas **confiables, seguros y en tiempo real**.

