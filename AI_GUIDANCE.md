# AI_GUIDANCE.md – Uso responsable de IA en el curso *Sistemas Embebidos*

Este documento establece las pautas para el uso ético y responsable de herramientas de **Inteligencia Artificial (IA)** en el curso de *Sistemas Embebidos*.

## 🎯 Objetivo
Aprovechar la IA como apoyo al aprendizaje en el desarrollo de aplicaciones embebidas, sin sustituir el razonamiento técnico, la experimentación en hardware ni el trabajo individual.

## ✅ Usos recomendados
- Solicitar explicaciones de conceptos teóricos (ej. comunicación UART, I2C, SPI, interrupciones, manejo de timers).
- Generar ejemplos de código **de referencia** en C, C++ o ensamblador para microcontroladores.
- Apoyarse en la IA para comparar distintas formas de implementar controladores o algoritmos.
- Usar IA para documentar código y generar comentarios claros.
- Traducir documentación técnica de manuales de microcontroladores.

## 🚫 Usos no permitidos
- Entregar programas completos generados por IA como propios sin pruebas ni comprensión.
- Usar IA para diseñar proyectos de hardware sin validación experimental.
- Confiar en la IA para cálculos eléctricos, temporizaciones o consumo energético sin verificarlos con datasheets o pruebas reales.

## 📋 Recomendaciones prácticas
1. **Valida siempre en hardware real**: La IA puede sugerir código que compile, pero no siempre funciona en microcontroladores.
2. **Consulta el datasheet**: Usa IA como complemento, nunca como reemplazo de la documentación oficial.
3. **Transparencia**: Declara el uso de IA en tus entregas.
4. **Aprendizaje activo**: Comprende cada línea de código sugerido antes de implementarla.

## 📌 Declaración sugerida en prácticas y proyectos

```text
Asistencia de IA: Explique qué pidió, qué recibió y qué cambios realizó.
Herramienta: (ChatGPT u otra)
Fecha:
Plataforma de hardware utilizada:
```

## 📌 Ejemplo
```text
Asistencia de IA: Consulté a ChatGPT sobre cómo configurar interrupciones externas en un PIC18. Usé su código como guía, pero lo adapté al compilador XC8 y validé en hardware real.
Herramienta: ChatGPT (GPT-5)
Fecha: 2025-08-25
Plataforma: PIC18F4550 en protoboard con oscilador externo de 20 MHz.
```

---

> ℹ️ En sistemas embebidos, la IA es útil como **asistente teórico y de documentación**, pero el **trabajo experimental en laboratorio** es insustituible.
