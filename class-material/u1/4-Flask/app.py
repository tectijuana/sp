# ╔═══════════════════════════════════════════════════════════════╗
# ║        🌤️ Mini Dashboard del Clima con Flask + Tailscale       ║
# ║        Lenguajes de Interfaz - TECNM / ITT - 2025              ║
# ║        Autor: [Tu Nombre]                                      ║
# ║        Descripción: Servidor Flask consultando OpenWeatherMap  ║
# ╚═══════════════════════════════════════════════════════════════╝

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
