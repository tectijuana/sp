# Sensores de Flujo

Este repositorio contiene información sobre los sensores de flujo y sus diferentes tipos: térmico, turbina y electromagnético. Se describen su funcionamiento, aplicaciones, ventajas y desventajas, además de ejemplos prácticos y referencias técnicas.

## Tipos de Sensores de Flujo

### 1. Sensor de Flujo Térmico
!(https://www.pce-iberica.es/medidor-detalles-tecnicos/images/sensor-flujo-ss-20-200-500.jpg)
#### **Funcionamiento**
Los sensores de flujo térmico miden la velocidad del fluido utilizando la transferencia de calor. Un elemento calefactor calienta el fluido, y sensores de temperatura detectan el cambio térmico para determinar el caudal.

#### **Aplicaciones**
- Medición de gases en procesos industriales.
- Control de flujo en sistemas de ventilación.
- Medición de consumo de aire en motores.

#### **Ventajas**
- No tiene partes móviles, lo que reduce el mantenimiento.
- Alta precisión en la medición de gases.
- Adecuado para flujos muy bajos.

#### **Desventajas**
- Puede verse afectado por cambios de temperatura ambiente.
- No es ideal para líquidos debido a la conductividad térmica variable.

---

### 2. Sensor de Flujo de Turbina

#### **Funcionamiento**
Este sensor mide el flujo mediante una turbina que gira proporcionalmente a la velocidad del fluido. Un sensor magnético o óptico detecta las rotaciones y calcula el caudal.

#### **Aplicaciones**
- Control de flujo en sistemas hidráulicos.
- Medición de consumo de agua y combustible.
- Industria alimentaria y farmacéutica.

#### **Ventajas**
- Alta precisión en líquidos limpios.
- Respuesta rápida a cambios de flujo.
- Costo relativamente bajo.

#### **Desventajas**
- Puede obstruirse con impurezas.
- No adecuado para fluidos con alta viscosidad.
- Requiere mantenimiento periódico.

---

### 3. Sensor de Flujo Electromagnético

#### **Funcionamiento**
Estos sensores generan un campo magnético y miden la diferencia de voltaje inducida por el flujo de un fluido conductor, utilizando la ley de Faraday.

#### **Aplicaciones**
- Medición de flujo en tuberías de agua potable y residuales.
- Industria química y de tratamiento de aguas.
- Sistemas de riego automatizados.

#### **Ventajas**
- Sin partes móviles, lo que minimiza el desgaste.
- Puede medir líquidos con partículas en suspensión.
- Precisión alta y estable.

#### **Desventajas**
- Solo funciona con fluidos conductores.
- Puede ser costoso en comparación con otros sensores.
- Sensible a interferencias electromagnéticas.

---

## Ejemplos Prácticos

### **Ejemplo 1: Sensor de Flujo de Turbina en un Sistema de Riego**
Un sensor de flujo de turbina se instala en una tubería de riego para medir el consumo de agua y detectar fugas. Los datos se envían a un microcontrolador como Arduino para el monitoreo en tiempo real.

### **Ejemplo 2: Sensor Electromagnético en el Control de Agua Residual**
En una planta de tratamiento de agua, se usa un sensor electromagnético para medir el caudal de agua residual tratada, asegurando que el volumen de salida cumpla con las regulaciones ambientales.

## Referencias Técnicas

1. [Principios de sensores de flujo térmico](https://www.omega.com/prodinfo/thermalmassflowmeters.html)
2. [Guía de sensores de flujo de turbina](https://www.instrumentationtools.com/turbine-flow-meter/)
3. [Funcionamiento de sensores electromagnéticos](https://www.krohne.com/en/products/flow-measurement/electromagnetic-flow-meters)
