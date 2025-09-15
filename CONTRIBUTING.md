
# Guía de Contribución — Carpeta `assignments/temas`

<img src="https://github.com/tectijuana/sp/blob/main/resources/images/Cyberpunk%20Tux.PNG" width="50%">

Gracias por tu interés en mejorar los **temas de asignación** de este curso.
Aquí encontrarás las reglas para organizar, documentar y contribuir dentro de esta carpeta.

---

## Flujo de contribución

1. Haz **Fork** del repositorio.
2. Crea una rama descriptiva:

   ```bash
   git checkout -b tema/U05-protocolos-comunicacion
   ```
3. Aplica cambios y agrega documentación.
4. Haz un **Pull Request** describiendo con claridad tu aportación.

---

## Nomenclatura de carpetas y archivos

En `assignments/temas` cada tema debe seguir esta estructura:

* **Tema:** `T##-nombre/`
* Dentro de cada tema:

  * `README.md` → Introducción y explicación del tema
  * `recursos/` → Diagramas, simulaciones o imágenes de apoyo
  * `codigo/` → Ejemplos en C/C++, Python, o pseudocódigo
  * `referencias.md` → Bibliografía, enlaces o fuentes

**Reglas:**

* Todo en **kebab-case** (minúsculas, palabras separadas con guiones).
* Numeración secuencial en los temas: `T01`, `T02`, `T03`…
* Evitar espacios y caracteres especiales.

---

## Buenas prácticas

* Cada tema debe tener un **README.md claro y estructurado**.
* Incluye **diagramas o simulaciones** cuando sea posible (Wokwi, Fritzing, Proteus).
* El código debe estar probado en hardware real o simulador.
* Usa comentarios y estilos de programación consistentes.
* Cita fuentes o referencias cuando uses material externo.

---

## Uso de herramientas de IA

Puedes apoyarte en IA para:

* Generar o depurar código (C/C++, Python).
* Redactar o corregir documentación (README, instrucciones de uso).
* Proponer nombres o estructuras pedagógicas.
* Explicar conceptos técnicos de manera más clara.

**Recomendaciones:**

* No subir contenido sin **validación humana**.
* Si usaste IA, indica en el **Pull Request** cómo la utilizaste
  (ejemplo: *"README creado con ayuda de ChatGPT, revisado por estudiante"*).
* Agrega los *prompts* como anexo cuando sea relevante.
* Evita depender únicamente de IA para pruebas en hardware o prácticas críticas.

> Consulta la guía completa aquí: [AI\_GUIDANCE.md](https://github.com/tectijuana/sp/blob/main/AI_GUIDANCE.md)

---

## Revisión de PRs

* Los docentes revisarán cada Pull Request.
* Se podrán solicitar cambios antes de su aceptación.
* Una vez aprobado, se integrará en la rama principal.

---

**NOTA:** *Kebab-case es una convención en la que todas las palabras se escriben en minúsculas y separadas por guiones (-). Ejemplo: `t05-sensor-ultrasonico`.*

---
