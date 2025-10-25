https://r72.cooltext.com/d.php?renderid=494723026043826&extension=png<img width="413" height="79" alt="image" src="https://github.com/user-attachments/assets/d9db4077-29a3-4ea1-96ee-76ef4ab6310f" />

---

# 🧠 CUESTIONARIO TÉCNICO – IoT Vehicular en el Mundo Real

> **Objetivo:** Que el estudiante entienda cómo llevar la simulación a un prototipo real, abordando sensores físicos, electrónica embarcada, comunicaciones celulares y provisión de dashboards en producción.

---

## 📦 Sección 1: Sensores físicos reales

1. **GPS**

   * ¿Qué módulos GPS son compatibles con Raspberry Pi Pico W o ESP32?
   * ¿Qué protocolo de comunicación utiliza normalmente un GPS (UART, I2C, SPI)?
   * ¿Cómo se alimenta un módulo GPS típico y qué corriente requiere?

2. **Temperatura del motor**

   * ¿Qué tipos de sensores existen para medir temperatura en motores (termistores, sensores digitales, RTD)?
   * ¿Cuál es el rango de temperatura típico de operación de un motor diésel?
   * ¿Qué componente electrónico necesitas para leer un sensor analógico desde un microcontrolador?

3. **Nivel de combustible**

   * ¿Cómo funciona un sensor de nivel resistivo y uno de ultrasonido?
   * ¿Dónde se colocan físicamente estos sensores?
   * ¿Qué desafíos eléctricos presenta su integración?

4. **Frenado brusco**

   * ¿Qué tipo de sensor se usa para detectar frenado violento (acelerómetro)?
   * ¿Cómo interpretar un frenado brusco con datos del eje X de un MPU6050?
   * ¿Qué problemas puede haber con ruido o lecturas falsas?

---

## ⚡ Sección 2: Electrónica asociada

5. **Adaptación de señales**

   * ¿Cómo adaptarías una señal de 0–5V de un sensor a un ADC de 3.3V?
   * ¿Qué tipo de protección eléctrica usarías (TVS, optoacopladores, zener)?
   * ¿Cuándo es mejor usar un ADC externo (ej. ADS1115)?

6. **Alimentación eléctrica**

   * ¿Cómo alimentas de forma estable una Raspberry Pi Pico W desde la batería del camión?
   * ¿Qué tipo de regulador de voltaje es mejor en automoción: lineal o conmutado?
   * ¿Qué protecciones instalarías ante picos, cortos, interferencia electromagnética?

7. **Montaje físico**

   * ¿Qué tipo de encapsulado usarías (IP65, IP67)?
   * ¿Cómo asegurarías las conexiones físicas contra vibración y polvo?
   * ¿Qué normas de instalación automotriz existen?

---

## 📡 Sección 3: Módem celular, eSIM/SIM y conectividad IoT

8. **Módems y protocolos**

   * ¿Qué módulos celulares pueden integrarse a un sistema IoT (ej: SIM7600, Quectel EC25, BG96)?
   * ¿Cuál es la diferencia entre GSM, LTE-M y NB-IoT?
   * ¿Qué protocolos de transmisión se usan típicamente: MQTT, HTTP, CoAP, TCP?

9. **Tarjetas SIM / eSIM para IoT**

   * ¿Qué es una **eSIM M2M**? ¿Cómo se programa?
   * ¿Qué proveedores globales ofrecen SIMs IoT multioperador (ej: Hologram.io, 1NCE, Twilio Super SIM)?
   * ¿Qué métricas debes tener en cuenta al contratar un plan IoT (MB por mes, red disponible, roaming)?

10. **Plan de datos y cobertura**

* ¿Cuánto consumo mensual estimado tendría un vehículo que publica datos cada 15 segundos?
* ¿Cómo proteger los datos transmitidos por GSM (VPN, TLS, APN privado)?
* ¿Qué sucede si el vehículo se mueve a zonas sin cobertura? ¿Cómo almacenar datos localmente?

---

## 🧠 Sección 4: Reflexión técnica y ética

11. **Edge vs Cloud**

* ¿Qué ventajas tendría hacer una parte del procesamiento de alertas en el microcontrolador (edge)?
* ¿Cómo reducirías el tráfico hacia la nube sin perder datos importantes?

12. **Privacidad y seguridad**

* ¿Qué riesgos representa monitorear vehículos en tiempo real (privacidad del conductor)?
* ¿Cómo protegerías la identidad del vehículo y el acceso al sistema?

13. **Proveedor de dashboards**

* ¿Qué diferencias existen entre montar un dashboard en tu propio servidor (Ej: EC2) y usar uno de proveedor?
* ¿Qué ventajas ofrecen herramientas como Flespi, Ubidots, Datacake o ThingsBoard?

---

## 🎓 Instrucciones al estudiante

* Responde en un documento digital, entregable como parte del informe técnico del proyecto.
* Justifica tus respuestas con esquemas, datasheets o referencias válidas.
* Se permite investigación externa: proveedores reales, fichas técnicas, videos de uso en campo.

---

## ✨ ¿Quieres un dashboard de proveedor?

> Como actividad adicional:

* Investiga proveedores de dashboards comerciales con planes gratuitos.
* Crea una cuenta en uno (Flespi, Datacake, ThingsBoard, etc.).
* Intenta conectar uno de tus vehículos simulados y mostrar el valor en tiempo real.

---

