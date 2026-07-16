# 🌐 Edge Computing con MQTT: Arquitectura Distribuida para IoT  

📚 **Materia:** Sistemas Programables  
🎓 **Carrera:** Ingeniería en Sistemas Computacionales  
👩‍🎓 **Estudiante:** Jennifer Nicole Macedo Cruz  
📅 **Turno:** 2PM TV  

---

## ✨ Introducción  
El **Internet de las Cosas (IoT)** conecta dispositivos, sensores y sistemas embebidos para recopilar e intercambiar datos. Sin embargo, enviar toda la información directamente a la nube genera retos importantes:  

- 🚦 **Altas latencias** en la transmisión de datos  
- 📡 **Sobrecarga en la red** y costos de ancho de banda  
- 🌐 **Dependencia total de la conectividad a internet**  

El **Edge Computing** surge como una alternativa para procesar la información **cerca de la fuente**, es decir, en los dispositivos o en nodos intermedios. Para la comunicación entre estos nodos y la nube, se utiliza **MQTT (Message Queuing Telemetry Transport)**, un protocolo ligero, confiable y diseñado especialmente para IoT.  

---

## ⚡ Edge Computing en IoT  
El **Edge Computing** consiste en trasladar parte del procesamiento de datos y el almacenamiento hacia dispositivos locales (*nodos de borde*).  

🔹 **Ventajas principales:**  
- ⏱️ **Menor latencia**: procesamiento en tiempo real.  
- 📶 **Optimización del ancho de banda**: solo se envían datos relevantes a la nube.  
- 🛡️ **Seguridad mejorada**: datos sensibles se procesan de manera local.  
- 🏭 **Confiabilidad**: aplicaciones críticas siguen operando incluso sin conexión a internet.  

En IoT, este enfoque es esencial para aplicaciones en **salud, ciudades inteligentes, vehículos autónomos y sistemas industriales**.  

---

## 🔗 MQTT como protocolo para Edge Computing  
**MQTT** es un protocolo de mensajería basado en el modelo **publicador/suscriptor**, con un **broker** como intermediario entre dispositivos.  

📌 **Características clave de MQTT:**  
- Funciona sobre **TCP/IP**.  
- Requiere pocos recursos, ideal para microcontroladores.  
- Usa **tópicos jerárquicos** para organizar la información.  
- Compatible con redes **intermitentes** o de bajo ancho de banda.  
- Soporta **calidad de servicio (QoS)** para garantizar la entrega de mensajes.  

> 📝 **Ejemplo simple:**  
> - Un sensor de temperatura publica en el tópico: `casa/sala/temperatura`.  
> - Una aplicación de control climático está suscrita y recibe automáticamente los datos.  

---

## 🏗️ Arquitectura Distribuida con Edge + MQTT  

1. **📡 Dispositivos IoT (Capa de percepción):**  
   - Sensores, actuadores, cámaras, microcontroladores.  
   - Capturan información del entorno.  

2. **🖥️ Nodo de Borde (Edge Node):**  
   - Procesa datos de forma local.  
   - Puede alojar un **broker MQTT** como Mosquitto.  
   - Aplica algoritmos de filtrado o decisiones rápidas.  

3. **☁️ Nube (Cloud Computing):**  
   - Recibe datos procesados o resumidos.  
   - Realiza análisis avanzados, almacenamiento masivo y aprendizaje automático.  

4. **👥 Usuarios y Aplicaciones Finales:**  
   - Acceden a dashboards, aplicaciones móviles o sistemas de monitoreo.  
   - Interactúan con los datos y controlan dispositivos en tiempo real.  

---

## 🚀 Ventajas de combinar Edge + MQTT  
- ⏱️ **Tiempo de respuesta inmediato** en aplicaciones críticas.  
- 📡 **Reducción de tráfico** en internet.  
- 📈 **Escalabilidad** al integrar múltiples nodos distribuidos.  
- 🔒 **Mayor seguridad** al mantener datos sensibles en el borde.  
- 🛠️ **Resiliencia**: el sistema sigue funcionando aún con fallos de conectividad.  

---

## 🌆 Caso de Uso: Smart City – Monitoreo Ambiental  
Imaginemos una ciudad inteligente con sensores distribuidos:  

- 🌍 **Sensores IoT** en calles y parques publican niveles de contaminación y temperatura vía MQTT.  
- 🖥️ **Nodos de borde** analizan la información localmente para detectar picos de contaminación.  
- 📲 **Alertas inmediatas** se envían a ciudadanos y autoridades sin depender totalmente de la nube.  
- ☁️ **La nube** almacena datos históricos y ejecuta modelos predictivos para anticipar problemas de calidad del aire.  

Este enfoque garantiza **reacciones inmediatas** y a la vez un **análisis a largo plazo**.  

---

## ✅ Conclusiones  
El uso combinado de **Edge Computing** y **MQTT** representa un cambio de paradigma en IoT:  

- 🌐 Se logra un **procesamiento más eficiente y descentralizado**.  
- 🔋 Se optimizan **recursos energéticos y de red**.  
- 🛡️ Se incrementa la **seguridad y confiabilidad** de los sistemas.  
- 🚀 Es ideal para sectores como **salud, industria 4.0, transporte, automatización y ciudades inteligentes**.  

💡 En definitiva, esta arquitectura se perfila como un **pilar fundamental en la transformación digital y el futuro del IoT**.  

---
