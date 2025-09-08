# ✅ Actividad práctica 2: Instalación y prueba de **Dashing** (Dashboard en terminal para Python)

![](https://raw.githubusercontent.com/FedericoCeratto/dashing/gh-pages/tty.gif)

https://github.com/FedericoCeratto/dashing

# 📊 Dashing en Python

**Dashing** es una librería de Python diseñada para crear **dashboards en la terminal** de manera sencilla y visual.

Funciona mediante **bloques (*tiles*)** que pueden ser:

* 📝 Textos
* 📜 Logs
* 📊 Indicadores (*gauges*)
* 📈 Gráficas

Estos bloques se organizan en **contenedores horizontales (HSplit)** o **verticales (VSplit)**.

---

## 🔧 Uso en un ambiente de sensores

En un escenario con sensores, **Dashing** puede servir como un **panel en tiempo real** para mostrar datos recolectados, por ejemplo:

* 🌡️ Lecturas de **temperatura** y **humedad** en barras **verticales y horizontales**.
* 💡 Estados de **dispositivos** como interruptores, luces o motores representados en *gauges*.
* 📜 **Historial de eventos** en forma de logs que se actualizan con cada nueva lectura.
* 📈 **Gráficas dinámicas** que muestran la evolución de una variable como **presión, velocidad o flujo**.

---

## 🚀 Ventaja principal

La gran ventaja de Dashing es que todo se presenta **directamente en la consola**, sin necesidad de un navegador o entorno gráfico.

Esto lo hace especialmente útil en:

* 🔌 **Sistemas embebidos**
* 🖥️ **Servidores remotos**
* ⚡ **Despliegues ligeros** donde los sensores envían datos constantemente

---

## 📋 Lista de verificación par la instalación

### 🔧 Preparación

* [ ] ⚙️ Verificar que **Python 3** está instalado

  ```bash
  python3 --version
  ```
* [ ] 📥 Instalar **Dashing** con pip

  ```bash
  pip install dashing
  ```
* [ ] 🔎 Comprobar instalación mostrando la versión

  ```bash
  python3 -c "import dashing, sys; print('dashing versión', dashing.__version__)"
  ```

---

### 🔄 Instalación alternativa (código fuente)

* [ ] 🌀 Clonar el repositorio oficial

  ```bash
  git clone https://github.com/FedericoCeratto/dashing.git
  ```
* [ ] 📂 Entrar a la carpeta del proyecto

  ```bash
  cd dashing
  ```
* [ ] 📦 Instalar en el entorno actual

  ```bash
  pip install .
  ```

---

### ▶️ Ejecución del demo

* [ ] 📂 Localizar el script de ejemplo

  ```
  dashing/examples/demo.py
  ```
* [ ] 🚀 Ejecutar el script con Python 3

  ```bash
  cd dashing/examples
  python3 demo.py
  ```
* [ ] 👀 Observar el panel en la terminal:

  * 📊 Medidores horizontales y verticales
  * 📝 Texto con mensaje "Hello World, this is dashing."
  * 📜 Log con marcas de tiempo
  * 📈 Gráficos animados en tiempo real (\~25 FPS)
* [ ] ❌ Finalizar la ejecución con **Ctrl + C**

---

### 📌 Conclusión

* [ ] Comprender que **Dashing** es una herramienta ligera para crear tableros en terminal.
* [ ] Reconocer que su instalación es rápida con `pip install dashing`.
* [ ] Explorar los ejemplos incluidos para personalizar dashboards.

