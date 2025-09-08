

# ✅ Actividad práctica 2: Instalación y prueba de **Dashing** (Dashboard en terminal para Python)

![]*https://raw.githubusercontent.com/FedericoCeratto/dashing/gh-pages/tty.gif)

## 📋 Lista de verificación

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

