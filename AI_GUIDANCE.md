# AI_GUIDANCE.md  
**Uso responsable y profesional de Inteligencia Artificial en el curso de *Sistemas Embebidos***

## 📘 Guía para estudiantes  
Este documento establece las pautas para el uso ético, reflexivo y técnicamente riguroso de herramientas de **Inteligencia Artificial (IA)** en el contexto del desarrollo de software y hardware embebido.

---

## 🎯 Objetivo

Aprovechar herramientas de IA como apoyo en el **aprendizaje técnico, la documentación y la exploración de código**, sin sustituir la **validación experimental**, el **razonamiento ingenieril** ni el **trabajo personal** sobre plataformas de hardware reales.

---

## ✅ Usos recomendados y valorados
- Solicitar explicaciones de conceptos clave: comunicación UART, I2C, SPI, interrupciones, timers, ADC, DMA.
- Generar **ejemplos de código de referencia** en C, C++ o ensamblador.
- Explorar variantes en la implementación de controladores, protocolos o rutinas de bajo nivel.
- Apoyarse en IA para generar **comentarios explicativos** o documentación técnica del código.
- Traducir o resumir secciones complejas de manuales técnicos o datasheets.

---

## 🚫 Usos no permitidos
- Entregar código generado por IA sin comprender su funcionamiento ni realizar pruebas en hardware.
- Utilizar IA para diseñar esquemas eléctricos o temporizaciones sin consultar **fuentes oficiales ni validar experimentalmente**.
- Delegar en IA la selección de componentes o estimación de consumo energético sin análisis ingenieril.

---

## 🧠 Buenas prácticas recomendadas

1. **Valida en hardware real**  
   La IA puede generar código que compila, pero solo tú puedes verificar su funcionamiento en un entorno físico.

2. **Consulta siempre el datasheet**  
   Usa la IA como apoyo complementario, pero **la fuente oficial es el fabricante**.

3. **Transparencia profesional**  
   Declara claramente qué parte de tu trabajo fue asistida por IA.

4. **Prompts técnicos y reflexión**  
   Formula preguntas específicas y registra tus *prompts*. Evalúa críticamente las respuestas.

5. **Explora con criterio múltiples herramientas**  
   Puedes usar ChatGPT, Copilot, Perplexity, etc., pero sé selectivo y consciente de sus limitaciones.

6. **Incluye reflexión final**  
   Comenta qué aprendiste, qué ajustaste y cómo validaste tus resultados.

---

## 📝 Formato obligatorio de declaración en prácticas o proyectos

```markdown
### Asistencia de Inteligencia Artificial

- **Prompts utilizados**:
  - "¿Cómo configurar el módulo ADC del PIC18F4550 en modo continuo con interrupciones?"
  - "Genera un ejemplo de manejo de SPI en STM32 con HAL."

- **Herramientas utilizadas**:
  - ChatGPT (GPT-4o)
  - GitHub Copilot

- **Cambios y validación**:
  - El código generado fue modificado para adaptarse al compilador XC8.
  - Se realizaron pruebas en protoboard con señales de entrada reales.
  - Verifiqué el funcionamiento usando lógica de test con LEDs y osciloscopio.

- **Reflexión personal**:
  La IA me ayudó a clarificar la configuración inicial, pero tuve que corregir errores de temporización. Esto reforzó mi entendimiento del ciclo de reloj y del manejo de interrupciones.

- **Fecha**: 2025-09-18  
- **Plataforma de hardware utilizada**: PIC18F4550 en protoboard, oscilador de 20 MHz  
