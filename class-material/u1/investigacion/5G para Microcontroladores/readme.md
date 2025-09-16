#  5G para Microcontroladores

### Peralta Vigil Fernando Yael - 22211632

***
![Imagen referente a 5G en Microcontroladores](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhSazQsQJUWPA9FaIFHj0YmHUH0IBf5XwXIw&s)

La integración de la conectividad 5G en dispositivos basados en microcontroladores abre nuevas posibilidades en el Internet de las Cosas (IoT), permitiendo transmisión de datos de alta velocidad, latencia ultra-baja y soporte masivo de dispositivos. Casos prácticos incluyen hogares inteligentes (domótica), ciudades inteligentes (gestión de tráfico, infraestructura), robótica móvil (drones y robots industriales) y monitoreo ambiental remoto. Por ejemplo, sistemas de automatización del hogar aprovechan la 5G para integrar múltiples sensores y actuadores con mayor fiabilidad.

* Domótica inteligente: sensores y actuadores conectados por 5G permiten automatizar funciones del hogar (iluminación, seguridad, clima) con respuesta rápida y mayor rango operativo. Estudios indican que 5G puede revolucionar la domótica con velocidades muy altas y latencia mínima.

* Ciudades inteligentes: se han prototipado plataformas de monitoreo urbano (p.ej., sensores de tráfico o contaminación) basadas en microcontroladores con módem 5G, facilitando la recolección de datos en entornos urbanos densos.

* Robótica y vehículos autónomos: equipos como UAV o robots móviles usan módulos 5G externos para transmisión de video y telemetría en tiempo real. Barros et al. (2023) evalúan módulos 5G para drones y resaltan su viabilidad pese a limitaciones de tamaño y peso.

* Industria 4.0 y manufactura: en fábricas se ensayan sistemas IoT avanzados con 5G para control y mantenimiento predictivo, beneficiándose de la baja latencia y sincronización en tiempo real.

* Monitorización remota: sensores ambientales (calidad de aire, agua, clima) pueden transmitir grandes volúmenes de datos sin demoras apreciables, permitiendo dashboards en la nube accesibles desde cualquier lugar.

### Ventajas

El 5G aporta al IoT varias ventajas técnicas clave, la tecnología inteligente de próxima generación ofrece “tasas de transferencia de datos más rápidas, mayor ancho de banda, mayor capacidad, menor latencia y respuesta más ágil”

* Alta velocidad y capacidad

* Baja latencia

* Conectividad masiva

* Eficiencia espectral y energética 

* Soporte nativo

### Desafíos de implementación

Integrar 5G en microcontroladores IoT también plantea retos importantes. Gkagkas et al. (2025) hallaron que si bien el ESP32 (microcontrolador) es de bajo consumo, el uso de un módulo 5G externo (con un Raspberry Pi en su estudio) incrementa drásticamente el consumo de energía del sistema, limitando su autonomía

* Consumo energético y alimentacion

* Complejidad de hardware

* Costo y despliegue de infraestructura

* Seguridad e interoperabilidad

* Integración y actualizaciones

### Compatibilidad

La compatibilidad entre los microcontroladores y la tecnología 5G es un aspecto crítico. Actualmente muy pocos SoC (System-on-Chip) IoT incluyen soporte 5G nativo. En la práctica esto significa que un dispositivo basado en MCU (como Arduino, ESP32, STM32, etc.) debe conectarse a través de un módulo externo (por ejemplo, un módem USB, una tarjeta celular en formato M.2 o HAT de Raspberry Pi).

* Módulos externos

* Limitaciones de diseño

*  Compatibilidad con estándares

## Referencias

1. Gkagkas, G., Karamerou, V., Michalas, A., Dossis, M., & Vergados, D. J. (2025). The behavior of an IoT sensor monitoring system using a 5G network and its challenges in 6G networking. Electronics, 14(16), 3167. https://www.mdpi.com/2079-9292/14/16/3167

2. Martín-Sacristán, D., Ravelo, C., Trelis, P., Ortiz, M., Fuentes, M., & Martínez, S. (2025). Development of a 5G-connected ultra-wideband radar platform for traffic monitoring in a campus environment. Sensors, 25(10), 3203. https://www.mdpi.com/1424-8220/25/10/3203

3. Barros, G., Boshoff, M., Luong, T., & Kuhlenkötter, B. (2023). Deployment of a 5G networking module for robotics and IoT applications. Procedia CIRP, 107, 535–540. https://www.sciencedirect.com/science/article/pii/S2212827123007655?via%3Dihub

4. Palarimath, S., Maqsood, M., Pyingkodi, M., Thenmozhi, K., & [los demás autores]. (2023, junio). Powering IoT Systems with 5G Wireless Communication: A Comprehensive Review. En Proceedings of the 8th International Conference on Communication and Electronics Systems (ICCES 2023). IEEE. https://doi.org/10.1109/ICCES57224.2023.10192678

## Asistencia de IA

Asistencia de IA: Pedí a Chat GPT que me diera referencias con respecto al tema de microcontroladores y 5G
Herramienta: Chat GPT (GPT-5)
Fecha: 2025-09-14
Plataforma de hardware utilizada: Chrome

Asistencia de IA: Pedí a Chat GPT que me ayudara a acomodar mis anotaciones de una manera más limpia y presentable
Herramienta: Chat GPT (GPT-5)
Fecha: 2025-09-15
Plataforma de hardware utilizada: Chrome
