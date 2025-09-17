**Adan Eric Ojeda Quintero - 22211625**

# Sistemas de adquisición de datos (DAQ) con plataformas programables

## Definición y descripción técnica

La adquisición de datos (DAQ) es el proceso de medir y registrar fenómenos eléctricos o físicos (como voltaje, corriente, temperatura, presión o sonido) para transformarlos en
datos digitales que puedan ser procesados por un ordenador o un sistema electrónico. 
En esencia, un sistema DAQ toma muestras del mundo real (señales analógicas), las acondiciona (amplificación, filtrado, etc.) y las convierte mediante un conversor 
analógico-digital (ADC) a formato digital. El resultado se envía a una computadora o registrador de datos para su almacenamiento, visualización o análisis. 
Técnicamente, un DAQ consta de sensores o transductores (que convierten las variables físicas en señales eléctricas), circuitos de acondicionamiento de 
señal (que amplifican o filtran las señales), módulos de conversión A/D, y un controlador o procesador que gestiona la adquisición y comunicación con sistemas superiores. 
El objetivo es obtener datos precisos y fiables que permitan optimizar procesos, validar diseños o tomar decisiones basadas en datos, tanto en entornos de laboratorio como industriales.

## Arquitectura típica de un sistema DAQ

![Figura: Diagrama básico de un sistema DAQ. Un sistema DAQ típico integra varios bloques funcionales en cadena:](https://www.datocms-assets.com/53444/1661499241-daq-system-shceme.jpg?auto=format&w=1200&dpr=1.5)

•	**Sensor/Transductor:** Convierte una magnitud física (temperatura, presión, tensión, etc.) en una señal eléctrica. Es el primer eslabón del DAQ.

•	**Acondicionamiento de señal:** Prepara la señal eléctrica para su digitalización. Esto puede incluir amplificación (para utilizar toda la resolución del ADC), filtrado 
(para eliminar ruido), aislamiento galvánico, linealización o multiplexado de múltiples canales[6]. El acondicionamiento asegura que la señal sea compatible con los 
rangos del ADC y libre de interferencias.

•	**Conversor A/D:** Convierte la señal analógica condicionada en datos digitales. Los ADC muestrean la señal a intervalos regulares y la cuantifican en valores numéricos, 
especificados por la resolución en bits[3][4]. A veces se incluyen también convertidores D/A para generación de señales de salida y control.

•	**Procesador o controlador:** Un microcontrolador, FPGA o procesador en un SoC gestiona la adquisición de datos digitalizados. Este bloque puede incluir memoria intermedia 
(buffers) y lógica de control para muestreo, temporización, triggers y preprocesamiento digital. El procesador envía los datos adquiridos hacia la etapa final.

•	**Interfaz de comunicación:** Permite transferir los datos hacia un computador o sistema superior. Puede ser a través de buses como USB, Ethernet, PCIe, interfaces inalámbricas, 
o protocolos especializados. También puede incluir hardware adicional como relojes de tiempo real o módulos de sincronización.

•	**Software / PC de usuario:** Finalmente, el software en el ordenador recibe los datos via el controlador DAQ, los visualiza, almacena y procesa. Herramientas comunes incluyen 
entornos como LabVIEW o MATLAB, pero también pueden usarse lenguajes generales (Python, C++) o aplicaciones a medida.

En conjunto, la arquitectura DAQ abarca tanto hardware (sensores, electrónica de acondicionamiento, ADC, procesadores programables) como software de control y análisis. 
Los sistemas DAQ se usan tanto en modo independiente (registradores autónomos) como conectados en tiempo real a PCs o sistemas embebidos[3][4].

Plataformas programables en sistemas DAQ

Las plataformas programables son el corazón del procesamiento en los DAQ modernos. Entre ellas destacan:
•	FPGAs (Field-Programmable Gate Arrays): Dispositivos de alto rendimiento que permiten implementar lógica digital a nivel hardware. Son ideales para aplicaciones que requieren 
procesamiento paralelo, baja latencia y actualización en campo[7]. Las FPGAs se usan en DAQ avanzados para tratamiento de señales, multiplexado rápido, implementación de 
filtros digitales o algoritmos embebidos, todo en hardware configurable. Ejemplos de uso incluyen sistemas de adquisición de alta velocidad, instrumentación en tiempo real y 
prototipado de ASIC. Su ventaja es la máxima flexibilidad y potencia de cómputo en paralelo, pero suelen ser más costosas y consumen más energía[7][8].

•	SoCs (System on Chip): Chips que integran en una sola pieza de silicio un microprocesador o microcontrolador con lógica programable tipo FPGA y diversos periféricos[9]. 
Un caso típico es Xilinx Zynq o Intel SoC, que combinan un CPU ARM con bloques FPGA. Los SoCs ofrecen lo mejor de ambos mundos: la capacidad de programación de software de 
un procesador junto con la reconfigurabilidad del FPGA. En DAQ se usan para aplicaciones que requieren procesamiento complejo junto con tiempos reales garantizados y conectividad (p.ej. 
Ethernet, Wi-Fi integrados). Un SoC reduce tamaño de hardware al integrar subsistemas completos[10][9].

•	Microcontroladores (MCUs): Chips con CPU fija, memoria y periféricos en un solo dispositivo (una solución SoC compacta)[11]. Ejemplos populares son los basados en ARM Cortex 
(STM32, Microchip PIC/AVR), o plataformas abiertas tipo Arduino. Son la opción más económica y de bajo consumo, adecuada para DAQ de bajo costo o embebido con pocas señales y requerimientos modestos. 
Permiten programación en C/C++ o Python y ofrecen interfaces ADC/DAC integradas en el chip[12]. Sin embargo, procesan de forma secuencial, no son tan rápidos como FPGA ni tan configurables a nivel hardware.

•	DSPs (Procesadores de Señal Digital): Chips especializados en procesamiento de señales con instrucciones optimizadas (multiplicaciones aceleradas, etc.). Se han usado tradicionalmente en 
aplicaciones de adquisición de audio, vídeo o radares, donde el DAQ incluye transformadas rápidas y filtrado complejo.

•	Otras opciones: También se usan procesadores multicore de propósito general o incluso GPUs para análisis post-adquisición masivo en el laboratorio, así como tarjetas de medida estándares 
(PXI, DAQ USB) con hardware fijo.

Actualmente, las FPGAs y las plataformas integradas (SoC-FPGA) son especialmente relevantes en DAQ de alto rendimiento, pues ofrecen paralelismo y flexibilidad inigualables[7][10]. 
No obstante, los microcontroladores siguen muy utilizados en aplicaciones donde prima el bajo coste y consumo. Un sistema clásico DAQ puede usar un FPGA para el frente de señal 
(muestreo rápido) y un microcontrolador o CPU para tareas de control y comunicación.

Ventajas y desafíos del uso de plataformas programables

Ventajas: Las plataformas programables aportan una gran flexibilidad y rendimiento en sistemas DAQ. Por ejemplo, las FPGAs permiten procesamiento paralelo masivo de señales 
y reconfiguración en campo, ideal para aplicaciones en tiempo real exigentes[7]. Además, pueden implementarse filtros digitales o aceleradores de hardware para tratamiento 
de datos a alta velocidad. Los microcontroladores, por su parte, ofrecen diseño compacto, bajo consumo y bajo costo, al integrar CPU, memoria y periféricos en un solo chip[12]. 
Esto los hace aptos para dispositivos DAQ portátiles o de uso masivo. Las soluciones SoC combinan estas ventajas: permiten correr algoritmos complejos en un procesador junto con 
lógica configurable en el mismo chip, optimizando espacio y consumo[9]. En general, las plataformas programables facilitan la personalización del sistema, la creación rápida de 
prototipos (sin tener que fabricar ASICs) y la capacidad de actualizar y extender funcionalidades mediante software o nuevas configuraciones lógicas[7][8].

Desafíos: El principal desafío es la complejidad de diseño. Programar una FPGA requiere conocimientos especializados en lenguajes HDL (Verilog/VHDL), lo cual puede aumentar 
costes y tiempo de desarrollo[13]. El depurado de sistemas con lógica concurrente y alta densidad de pines también es complejo. Además, las FPGA suelen ser más costosas y 
consumir más energía que microcontroladores tradicionales[7][8]. Por otro lado, los microcontroladores tienen limitaciones en capacidad de procesamiento paralelo y de velocidad de muestreo.
Otro reto es la compatibilidad con sistemas existentes: integrar un DAQ moderno basado en SoC o FPGA con infraestructura antigua puede generar problemas de interoperabilidad y requerir
gateways o adaptadores[14]. En resumen, se debe balancear la ganancia en rendimiento y flexibilidad de las plataformas avanzadas frente a la simplicidad, costos y familiaridad de los enfoques convencionales.

Aplicaciones reales en diversas industrias

Los sistemas DAQ con plataformas programables se usan extensamente en múltiples sectores. 
Automotriz: se emplean para pruebas de motores (medición de consumo, emisiones, temperatura) y análisis de dinámica vehicular (aceleraciones, frenadas, respuesta de dirección)[15]. 
También son clave en pruebas de choque y seguridad (obteniéndose datos de sensores durante colisiones) y en vehículos eléctricos/híbridos (monitoreo de baterías y electrónica de potencia)[16]. 
Por ejemplo, empresas automotrices usan DAQ FPGA-based para validación de sistemas ADAS y simulación HIL.

Aeroespacial y defensa: en simulaciones de vuelo, túneles de viento, instrumentación de aeronaves y cohetes se usan DAQ muy robustos. Permiten pruebas bajo condiciones extremas y 
análisis estructural de aviones. Un informe de mercado destaca que los sistemas DAQ son esenciales para pruebas de sistemas de defensa y simulación de vuelo, así como monitoreo en 
túneles de viento y validación aviónica[17]. Organismos espaciales también emplean DAQ FPGA en satélites y sondas para adquirir datos de múltiples sensores.

Industria y manufactura: en plantas de producción y procesos industriales, los DAQ recogen datos de sensores (temperatura, presión, vibración) para control de procesos y mantenimiento 
predictivo. Se usan DAQ embebidos en SCADA y control distribuido. El avance del IoT ha potenciado la demanda de DAQ en tiempo real en manufactura, energía y sectores como salud y transporte[5][18].

Salud y medicina: se aplican en la instrumentación médica (ECG, EEG, sistemas de imagen) y monitorización de pacientes. Por ejemplo, equipos de registro biomédico usan ADC de alta 
precisión para señales fisiológicas, controlados por microcontroladores o FPGAs. En investigación clínica y laboratorios se usan DAQ para ensayos y prototipos de dispositivos médicos.

Telecomunicaciones: los DAQ son la base de sistemas de radio definida por software (SDR) y análisis de señales. Por ejemplo, estaciones base 4G/5G o equipos de prueba de RF usan 
convertidores A/D integrados en FPGA para procesar espectros de radio en tiempo real. También se emplean en pruebas de redes y comunicaciones satelitales.

En resumen, cualquier industria que requiera medir múltiples variables físicas o eléctricas se beneficia de sistemas DAQ programables. Su flexibilidad permite adaptarlos a necesidades 
específicas de monitoreo, pruebas de prototipos, control de calidad y automatización en automotriz, aeroespacial, energía, salud, telecomunicaciones, agricultura, laboratorios de investigación, entre otros[5][19].

 Bloque / Plataforma             | Función clave | Ejemplos de uso |
| :---                           |    :---        | :---          |
| Sensor / Transductor           | Convierte magnitud física en señal eléctrica          | Termopares, galgas extensiométricas, acelerómetros |
| Acondicionamiento              | Amplificación, filtrado y adaptación de señal         | Módulos de acondicionamiento en placa DAQ          |
| Convertidor A/D                | Digitaliza la señal analógica     | git status        | ADC SAR, Sigma-Delta en tarjetas de adquisición    |
| FPGA / Lógica programable      | Procesamiento paralelo de señales y lógica de control | Filtros digitales, FFT en tiempo real              |
| Microcontrolador / CPU         | Control de muestreo, almacenamiento, comunicación     | Arduinos, STM32, CPU en SoC (ARM)                  |
| Interfaz / Comunicación        | Envía datos a PC/Sistema (USB, Ethernet, PCIe, WiFi)  | Módulos USB-DAQ, tarjetas PCIe multicanal          |
| Software de análisis           | Visualización, procesamiento y almacenamiento de datos| LabVIEW, MATLAB, LabWindows/CVI                    |




