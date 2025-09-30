# Diseño de sistemas embebidos para monitoreo ambiental
**Autor**: *Solano Cortéz Iván Israel* 22210786

**INSTITUTO TECNOLÓGICO DE TIJUANA**

Materia: Sistemas Programables

Fecha: 2025-09-18

## Introducción
El cuidado del medio ambiente requiere conocer en tiempo real qué está pasando en aire, agua y suelo.

Para eso, se utilizan sistemas embebidos de monitoreo ambiental, que son dispositivos pequeños con sensores, procesadores y comunicación que recolectan datos y los envían para su análisis. Estos sistemas se usan en ciudades inteligentes, agricultura, control de
contaminación, calidad del agua y prevención de desastres naturales. Su diseño debe ser eficiente, confiable y de bajo consumo energético.

## Puntos principales
**¿Qué es?**
-Es un sistema ue combina sensores, un microcontrolador y un método de comunicación.

-Sirve para medir variables como temperatura, humedad, gases, partículas de polvo, ruido o calidad del agua.

**Componentes básicos**
-Sensores: capturan datos del entorno (aire, agua, suelo).

-Microcontrolador (ej. ESP32, STM32): procesa los datos.

-Comunicación: Wi-Fi, LoRa, NB-IoT, Bluetooth, según el alcance y la energía disponible.

-Fuente de energía: baterías, paneles solares, sistemas de bajo consumo.

-Plataforma de análisis: nube o servidor que guarda y muestra la información en gráficos, alarmas o reportes.

**Variables comunes a medir**

-Aire: temperatura, humedad, CO₂, partículas finas (PM2.5, PM10).

-Agua: pH, turbidez, oxígeno disuelto.

-Suelo: humedad, conductividad.

-Otros: radiación solar, ruido, nivel de ríos.

**Comunicación**

-LoRa/LoRaWAN: bajo consumo y gran alcance, ideal para zonas rurales o con nodos dispersos.

-NB-IoT o LTE-M: usan red celular, buena cobertura pero con costo extra.

-Wi-Fi: útil si hay energía y cobertura, aunque gasta más.

**Gestión de energía**

-Los sistemas deben consumir lo menos posible.

-Se usan modos de “sueño profundo” en el microcontrolador.

-Paneles solares con baterías permiten autonomía en lugares remotos.

**Procesamiento de datos**

-Se pueden filtrar datos directamente en el dispositivo.

-Algunos sistemas detectan anomalías y solo transmiten si pasa algo importante.

-El análisis más completo ocurre en la nube o servidores.

**Retos principales**

-Calibración de sensores (para que los datos sean confiables).

-Condiciones extremas (polvo, humedad, temperatura).

-Consumo energético en lugares sin electricidad.

-Costos de mantenimiento (revisar baterías y sensores).

**Buenas prácticas en el diseño**

-Definir bien qué se va a medir y con qué precisión.

-Proteger los sensores contra clima y suciedad.

-Usar comunicación de bajo consumo si hay muchos nodos.

-Incluir actualizaciones de software a distancia.

-Guardar siempre ubicación, hora y condiciones de calibración junto con los datos.

**Aplicaciones reales**

Redes de monitoreo de calidad del aire en ciudades.

Estaciones para medir contaminación en ríos o presas.

Sensores de humedad en agricultura inteligente.

Sistemas de alerta temprana ante incendios o inundaciones.

## Conclusión

-El diseño de sistemas embebidos para monitoreo ambiental es clave para la gestión sostenible de recursos.

Requiere equilibrio entre precisión de sensores, bajo consumo energético y conectividad confiable.
Con un buen diseño, se pueden tener sistemas autónomos que ayuden a prevenir riesgos y mejorar la calidad de vida.

## Referencias Formato APA

Bonilla, V., Ruiz, F., Zamora, S., & Gómez, J. (2023). A Systematic Literature Review of LoRaWAN: Sensors and Applications in Agriculture, Health, and Environmental Monitoring. Sensors, 23(17), Article 10261. 
PMC

Gerndt, M., … (2025). Energy-Aware Duty Cycle Management for Solar-Powered IoT Sensors. Sensors, 25(14), Article 4500. 
MDPI

H. Zhao, et al. (2024). A LoRaWAN-based environmental sensing network for monitoring soil moisture dynamics. Science of The Total Environment, [volumen]. 
ScienceDirect

Jabbar, W. A., et al. (2024). Development of LoRaWAN-based IoT system for water quality monitoring in rural regions. 
ScienceDirect

Landi, G., et al. (2024). Design of Environmental Sensor Board for Energy Harvesting. Electronics, 13(19), Article 3801. 
MDPI

Rosca, C. M., et al. (2025). Integration of AI in Self-Powered IoT Sensor Systems. Applied Sciences, 15(13), Article 7008. 
MDPI

Trigkas, A., et al. (2025). Edge Intelligence in Urban Landscapes. Electronics, 14(14), Article 2890.
