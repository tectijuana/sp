# ╔═══════════════════════════════════════════════════════════════╗
# ║  Programa:    🌤️ Mini Dashboard del Clima (Flask + Tailscale)  ║
# ║  Programador: [Tu Nombre]                                     ║
# ║  Curso:       Sistemas Programables (EmbeddedSP) TECNM / ITT  ║
# ║  Horario:     [999]                                           ║
# ║  Actividad:   U1 — 4-Flask, dashboard del clima               ║
# ║  Asciinema:   [URL de la grabación]                           ║
# ╚═══════════════════════════════════════════════════════════════╝
#
# Objetivo: servidor web Flask que consulta la API de OpenWeatherMap
# y muestra la temperatura y condiciones de una ciudad, con color de
# fondo según la temperatura.
#
# Recuerde iniciar su asciinema identificándose antes de cualquier comando:
#   $ echo "Programa app.py, por [Tu Nombre] de curso Sistemas Programables Horario [999] actividad 4-Flask"

from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "TU_API_KEY"
CITY = "NombreCiudad"

@app.route("/")
def clima():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    color = "lightblue" if temp < 10 else "lightgreen" if temp < 25 else "salmon"
    return f"""
    <html><body style='background-color:{color};'>
    <h1>Clima en {CITY}</h1>
    <p>Temperatura: {temp} °C</p>
    <p>Condiciones: {weather}</p>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
