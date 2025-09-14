REPOSITORIO: https://github.com/HeyPuter/puter



## 1. Objetivos de la actividad

1. **Familiarizarse con la plataforma puter.com**: comprender sus principales funcionalidades, su interfaz y las opciones de integración con hardware y servicios externos.  
2. **Configurar sensores y recolectar datos**: establecer la comunicación entre dispositivos (microcontroladores o tarjetas de desarrollo) y la plataforma para la lectura de datos.  
3. **Diseñar y personalizar un dashboard**: visualizar y analizar la información proporcionada por los sensores en tiempo real.  
4. **Implementar casos de uso o disparadores**: programar acciones o notificaciones en base a umbrales y eventos detectados por los sensores.  
5. **Evaluar rendimiento, usabilidad y escalabilidad**: discutir las limitaciones y posibles mejoras en el uso de puter.com para proyectos de distinta complejidad.  

---

## 2. Materiales y requisitos

1. **Cuenta en puter.com**: cadaestudiante debe contar con una cuenta activa para acceder a la plataforma.  
2. **Dispositivo de desarrollo** (opcional según las necesidades y tipo de sensor):  
   - Placas como Arduino, ESP32, Raspberry Pi o similares.  
3. **Sensores**:  
   - Sensor(es) de temperatura y humedad (DHT11 o DHT22).  
   - Sensor de luz (LDR o fotocélula).  
   - Sensor de movimiento (PIR) u otro sensor que se desee integrar.  
4. **Conexión a internet**: necesaria para la comunicación con la plataforma.  
5. **Computador personal** con el entorno de desarrollo requerido (IDE de Arduino, Visual Studio Code, etc.) y herramientas de programación (por ejemplo, Python, C/C++ o el lenguaje que se use para configurar el firmware del dispositivo).

---

## 3. Descripción de la actividad paso a paso

### 3.1. Fase de preparación
1. **Registro y configuración en puter.com**:  
   - Crear una cuenta o iniciar sesión.  
   - Familiarizarse con la interfaz básica: panel de control, secciones para administrar dispositivos y vistas de dashboard.  
2. **Instalación de librerías y herramientas**:  
   - Si se trabaja con Arduino o ESP32, instalar las librerías que recomiende puter.com para la comunicación.  
   - Verificar la compatibilidad de los controladores de sensores con la plataforma (generalmente, se habilitan mediante código en el firmware).

### 3.2. Conexión de sensores y envío de datos
1. **Montaje del circuito**:  
   - Conectar el microcontrolador con uno o varios sensores (temperatura, humedad, luz, etc.).  
   - Asegurar la alimentación y la correcta disposición de pines (I/O, GND, VCC).  
2. **Programación del firmware**:  
   - Añadir el código para leer los valores del sensor a intervalos regulares.  
   - Integrar las librerías o APIs de puter.com para enviar los datos al servidor (por HTTP, MQTT, WebSockets, etc., según disponga la plataforma).  
   - Configurar parámetros de conexión (SSID, contraseña de WiFi, token o clave de la cuenta de puter.com, etc.).  
3. **Pruebas iniciales**:  
   - Verificar en la consola serie (o logs de la aplicación) que se están enviando datos correctamente.  
   - Comprobar en el panel de puter.com que los valores del sensor aparecen en tiempo real.

### 3.3. Creación de un dashboard personalizado
1. **Selección de widgets**:  
   - En la sección de dashboards de puter.com, agregar gráficos de línea, indicadores numéricos, medidores de aguja u otros componentes para visualizar las variables (temperatura, humedad, etc.).  
2. **Configuración de rangos y alertas**:  
   - Ajustar los límites de visualización (por ejemplo, para mostrar rangos de temperatura esperados).  
   - Programar alertas o notificaciones vía correo o mensajes push cuando se superen umbrales críticos.  
3. **Diseño y usabilidad**:  
   - Organizar los widgets en el dashboard para una lectura clara y atractiva.  
   - Integrar información contextual, como fecha y hora o estado de la red.

### 3.4. Implementación de casos de uso avanzados (opcional)
1. **Acciones automáticas basadas en eventos**:  
   - Configurar reglas o scripts en puter.com para que, si la temperatura supera cierto valor, se encienda un ventilador (controlado por un pin del microcontrolador).  
   - Enviar un mensaje de alerta a un servidor externo o un chatbot cuando se detecte movimiento.  
2. **Integración con servicios externos**:  
   - Conectar puter.com con plataformas IoT populares (IFTTT, Node-RED, etc.) para ampliar las posibilidades de automatización.  
   - Combinar datos de varios sensores en diferentes ubicaciones para un análisis comparativo.  

---

## 4. Evaluación y análisis de resultados

1. **Colecta y análisis de datos**:  
   - Observar en el dashboard la evolución de las mediciones en distintos momentos del día.  
   - Exportar datos (si la plataforma lo permite) para un análisis más detallado (estadística, IA básica, etc.).  
2. **Evaluación de la estabilidad y rendimiento**:  
   - Analizar la frecuencia de actualización de datos (latencia, retardo).  
   - Verificar si ocurren desconexiones o fallos de sincronización con la plataforma.  
3. **Pruebas de escalabilidad** (si hay recursos disponibles):  
   - Añadir más sensores o aumentar la tasa de lectura de datos para observar cómo se comporta la plataforma.  
   - Medir el consumo de recursos (RAM, CPU en el microcontrolador), así como el uso de ancho de banda de la red.

---

## 5. Discusión y retroalimentación

1. **Ventajas y desventajas de puter.com**:  
   - Facilidad de uso e integración.  
   - Nivel de documentación, foros o soporte técnico.  
   - Opciones de personalización del dashboard.  
2. **Seguridad y privacidad**:  
   - Revisión de los métodos de autenticación de dispositivos y cifrado de datos.  
   - Implementación o ausencia de herramientas para gestionar usuarios y roles.  
3. **Sostenibilidad y costos**:  
   - Comparar el plan gratuito y los planes de pago (si existen), así como los límites de uso.  
   - Estimar la factibilidad de usar puter.com en proyectos a gran escala o proyectos académicos.

---

## 6. Sugerencias de mejora y adaptaciones

1. **Mejoras en la plataforma**:  
   - Solicitar nuevas funcionalidades, como mayor variedad de widgets, integración simplificada con nubes externas o soporte para protocolos adicionales (MQTT, CoAP, etc.).  
   - Proponer un sistema más robusto de gestión de usuarios y permisos (ideal para entornos corporativos o industriales).  
2. **Adaptaciones para proyectos específicos**:  
   - **Aplicaciones agroindustriales**: usar sensores de humedad del suelo, pH o radiación solar y crear reglas para riego automatizado.  
   - **Seguridad y videovigilancia**: integrar cámaras IP o detección de rostros y disparar alertas basadas en algoritmos de visión.  
   - **Control industrial**: combinar el dashboard con PLCs o sistemas SCADA, donde puter.com funja como interfaz de supervisión.  
3. **Próximos pasos**:  
   - Implementar **analíticas avanzadas** (reglas basadas en IA o Machine Learning) directamente en la plataforma o en un servidor intermedio.  
   - Explorar **OTA (Over-The-Air)** para actualizaciones de firmware, si puter.com ofrece o facilita esta opción.  
   - Investigar la posibilidad de migrar datos históricos a servicios de Big Data para realizar predicciones a largo plazo.

---

## 7. Presentación final

Como cierre de la actividad, cada equipo o estudiante presentará:  
1. **El sistema funcionando** en tiempo real (dashboard mostrando lecturas de los sensores).  
2. **Principales hallazgos** en cuanto a facilidad de uso, confiabilidad y eficiencia.  
3. **Propuesta de mejora** o limitación detectada y posibles soluciones.  
4. **Análisis de viabilidad** del uso de puter.com en un proyecto a mayor escala o con requerimientos de seguridad más estrictos.

---

### Conclusión

Esta actividad permite evaluar de forma completa la plataforma **puter.com**, desde la configuración de los sensores y la comunicación con el dispositivo, hasta la visualización de datos y la generación de acciones automatizadas. Al finalizar, los participantes podrán **valorar la pertinencia y conveniencia** de utilizar puter.com en futuros desarrollos, identificando fortalezas, limitaciones y posibles adaptaciones para proyectos específicos. Con ello, se fomenta la **visión crítica** y la **experimentación** de los estudiantes o desarrolladores, sentando bases sólidas para la **implementación de soluciones IoT** en diferentes dominios.
