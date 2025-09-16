![ITT Wallpaper](recursos/wallpaper_itt.png)
# Optimización de consumo energético en sistemas IoT
**Autor:** Javier Machado Sanchez
  
**Institución:** Instituto Tecnológico de Tijuana
  
**Materia:** Sistemas Programables
  
**Profesor:** Rene Solis Reyes
  
**Fecha:** 15 de Septiembre del 2025
## Introducción
El Internet de las Cosas (IoT, por sus siglas en inglés) constituye una de las tecnologías más transformadoras de la actualidad, con aplicaciones que abarcan desde los hogares inteligentes hasta la medicina personalizada. Sin embargo, esta masificación trae consigo un reto central: el consumo energético. Los dispositivos IoT suelen depender de baterías o de fuentes de energía limitadas, lo que genera la necesidad de optimizar su funcionamiento para prolongar la vida útil, reducir costos y garantizar la fiabilidad del sistema. En este trabajo se analizan dos ámbitos clave para ilustrar las estrategias de optimización energética: los edificios inteligentes y los sistemas de salud, apoyándonos en estudios recientes publicados en Sustainability (MDPI, 2023) y Scientific Reports (Nature, 2025).
## Consumo energético en sistemas IoT
El consumo energético en IoT depende principalmente de tres factores: la recolección de datos mediante sensores, el procesamiento de la información y la transmisión hacia servidores o la nube. Entre estos, la comunicación inalámbrica suele ser el componente más costoso en términos de energía. Así, se han desarrollado múltiples enfoques para disminuir la necesidad de transmisiones constantes, mejorar la eficiencia de los protocolos de comunicación y emplear técnicas de gestión inteligente de energía.  
  
En general, la problemática se manifiesta en dos dimensiones: por un lado, la sostenibilidad y reducción de costos operativos, y por otro, la autonomía y seguridad en aplicaciones críticas. Ambas perspectivas pueden observarse en los casos de estudio que se presentan a continuación.
## Optimización energética en edificios inteligentes
En el contexto de los edificios inteligentes, la meta principal consiste en lograr la máxima eficiencia energética sin sacrificar el confort de los ocupantes ni la calidad de los servicios. El estudio de Wang (2023) propone un modelo de optimización basado en la formación de clústeres inteligentes y en el uso de algoritmos metaheurísticos como el Particle Swarm Optimization (PSO).  
  
El principio es simple: en lugar de que cada sensor transmita datos directamente a un servidor central, los nodos se agrupan en clústeres y un nodo líder (cluster head) concentra la información antes de enviarla. De esta manera, se reduce significativamente el número de transmisiones, que son el principal factor de gasto energético.
  
Además, se plantean mecanismos de gestión adaptativa, donde los nodos entran en modo activo o de reposo según las condiciones ambientales o la demanda de información. Este enfoque no solo extiende la vida útil de los sensores, sino que también repercute en la sostenibilidad global del edificio al disminuir los costos de energía.
  
La optimización en este ámbito tiene, por tanto, una doble dimensión: tecnológica y ambiental. La reducción del consumo energético en sistemas IoT aplicados a edificios contribuye a los objetivos de eficiencia energética y de desarrollo sostenible, además de representar un ahorro económico significativo para las instituciones y empresas que los implementan.
## Optimización energética en sistemas de salud
En el caso de los sistemas de monitoreo de salud basados en IoT, el reto energético se vuelve aún más complejo, pues se suma la necesidad de garantizar seguridad y fiabilidad en la transmisión de los datos médicos. Según Alatawi (2025), los dispositivos biomédicos enfrentan una tensión entre el consumo energético y la protección de los datos sensibles, ya que las técnicas de cifrado y autenticación, indispensables para preservar la privacidad, requieren un gasto adicional de energía.
  
Para enfrentar este desafío, se han diseñado estrategias específicas. Una de ellas es el control de transmisión basado en umbrales, en el que los sensores solo envían datos cuando estos exceden un rango crítico o muestran cambios relevantes. De esta forma, se evitan transmisiones innecesarias que drenarían la batería rápidamente. Otra técnica es la implementación de modos de reposo o suspensión, que permiten a los dispositivos desactivar temporalmente sus radios y procesadores. Finalmente, el escalado dinámico de potencia ajusta el voltaje y la frecuencia de los componentes en función de la carga de trabajo, logrando un balance entre eficiencia y rendimiento.
  
El objetivo en este ámbito no es únicamente prolongar la vida útil de los dispositivos, sino asegurar que los pacientes reciban monitoreo continuo y seguro. Una interrupción por agotamiento energético puede comprometer la salud o incluso la vida de un paciente, por lo que la fiabilidad se convierte en una prioridad ineludible.
## Seguridad y eficiencia: un dilema compartido
Tanto en edificios inteligentes como en sistemas de salud, la seguridad y la eficiencia energética están interconectadas. Mientras que en los edificios la seguridad se enfoca más en la protección de la infraestructura y la continuidad del servicio, en el área de salud la seguridad adquiere un carácter vital. En ambos casos, los algoritmos y protocolos deben ser lo suficientemente ligeros para no incrementar el consumo energético, pero robustos para garantizar la integridad de la información.
  
Al comparar los dos casos, se observa que los edificios inteligentes priorizan la sostenibilidad y la reducción de costos operativos, mientras que los sistemas de salud priorizan la continuidad del servicio y la seguridad de los datos. Sin embargo, ambos convergen en la necesidad de aplicar mecanismos adaptativos y algoritmos de optimización que ajusten dinámicamente el consumo energético sin sacrificar la calidad del servicio.
  
Las investigaciones recientes apuntan hacia un futuro en el que la optimización energética en IoT se apoyará cada vez más en la inteligencia artificial, capaz de predecir patrones de consumo y ajustar el comportamiento de los dispositivos en tiempo real. Asimismo, se espera que el desarrollo de protocolos de comunicación más eficientes y de hardware de bajo consumo contribuya a reducir la huella energética de estos sistemas. Otra línea prometedora es la integración de los nodos IoT con fuentes de energía renovable y tecnologías de energy harvesting, que permitirían extender la autonomía de los dispositivos y reducir la dependencia de baterías.
## Conclusiones
La optimización del consumo energético en sistemas IoT es un campo crucial que combina aspectos tecnológicos, económicos y sociales. Los edificios inteligentes y los sistemas de salud ofrecen ejemplos claros de cómo los desafíos energéticos adoptan formas distintas según el contexto, pero también de cómo las soluciones convergen en torno a la gestión adaptativa, el uso de algoritmos de optimización y la búsqueda de equilibrio entre eficiencia y calidad del servicio.
  
El desarrollo de estas tecnologías no solo apunta a un IoT más sostenible y económico, sino también más seguro y confiable, capaz de responder a las demandas de un mundo cada vez más interconectado.
## Declaración de uso de inteligencia artificial
### Primer asistencia
**Asistencia de IA:** Pedí recursos bibliograficos referentes al tema de interes con el siguiente prompt: "*Tengo que hacer esta investigación sobre este tema: Optimización de consumo energético en sistemas IoT. Dame recursos donde se aborde esta cuestión*". La IA regresó diversos articulos y ensayos, de los cuáles seleccioné dos.
  
**Herramienta:** ChatGPT 5
  
**Fecha:** 15/09/2025 15:40:00
### Segunda asistencia
**Asistencia de IA:** Pedí revisión y mejora en la redacción de un texto estructurado por mí. Utilicé el siguiente prompt: "*Revisa ortografía y mejora la redacción para un resultado más profesional. Respeta la estructura de los parrafos y las ideas plasmadas. Adjunto el texto.*". Revisé el resultado y no realicé ningún cambio al mismo.

**Herramienta:** ChatGPT 5
  
**Fecha:** 15/09/2025 20:25:00
