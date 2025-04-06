
## 🔧 ¿Qué quieres lograr?  FAKE SENSOR GPS

**Entrada:** Ruta marcada manualmente (por clics en un mapa).  
**Salida:** Lista de sentencias NMEA `$GPRMC`, `$GPGGA` u otras, simulando una ruta GPS.

---

## 🌐 Solución en pasos

### 1. Herramienta Online — [GeoJSON.io](https://geojson.io)
- Usa esta herramienta para **dibujar la ruta manualmente** en un mapa.
- Exporta el resultado como **GeoJSON** (puntos con latitud/longitud).

### 2. Conversión a NMEA (script personalizado)
Puedes usar este pequeño script en Python para convertir puntos de la ruta a `$GPRMC` (la sentencia NMEA más común para velocidad y tiempo).


```python
import datetime
import random

# Función para convertir coordenadas decimales a formato NMEA
def decimal_to_nmea(lat, lon):
    # Función interna para convertir un valor (latitud o longitud) a formato NMEA
    def to_nmea(val, is_lat):
        # Extrae los grados enteros a partir del valor absoluto
        deg = int(abs(val))
        # Calcula los minutos multiplicando la parte decimal por 60
        min = (abs(val) - deg) * 60
        # Determina el hemisferio: para latitud 'N' o 'S'; para longitud 'E' o 'W'
        hemi = ('N' if lat >= 0 else 'S') if is_lat else ('E' if lon >= 0 else 'W')
        # Devuelve la cadena formateada: grados (2 dígitos), minutos (7.4f) y el hemisferio
        return f"{deg:02d}{min:07.4f},{hemi}"

    # Retorna las conversiones para latitud y longitud
    return to_nmea(lat, True), to_nmea(lon, False)

# Función para generar una sentencia GPRMC en formato NMEA
def generate_gprmc(lat, lon, timestamp):
    # Convierte las coordenadas decimales a formato NMEA
    lat_str, lon_str = decimal_to_nmea(lat, lon)
    # Formatea la hora en formato HHMMSS.00
    time_str = timestamp.strftime("%H%M%S.00")
    # Formatea la fecha en formato DDMMYY
    date_str = timestamp.strftime("%d%m%y")
    # Genera una velocidad aleatoria entre 10 y 20 nudos, formateada a dos decimales
    speed = f"{random.uniform(10, 20):.2f}"  # velocidad en nudos
    # Genera un rumbo (heading) aleatorio entre 0 y 360 grados, formateado a dos decimales
    heading = f"{random.uniform(0, 360):.2f}"
    # Construye la sentencia GPRMC con los datos generados
    sentence = f"GPRMC,{time_str},A,{lat_str},{lon_str},{speed},{heading},{date_str},,,A"
    # Calcula el checksum (suma XOR de todos los caracteres de la sentencia)
    checksum = 0
    for c in sentence:
        checksum ^= ord(c)
    # Devuelve la sentencia completa en formato NMEA, incluyendo el símbolo '$' y el checksum en hexadecimal
    return f"${sentence}*{checksum:02X}"

# Ejemplo de uso: ruta con puntos fijos (latitud, longitud)
route = [(40.7128, -74.0060), (40.7138, -74.0070), (40.7148, -74.0080)]
# Obtiene el tiempo actual en UTC
now = datetime.datetime.utcnow()

# Itera sobre cada punto en la ruta, incrementando 10 segundos por cada punto
for i, (lat, lon) in enumerate(route):
    # Imprime la sentencia GPRMC generada para cada punto con el tiempo ajustado
    print(generate_gprmc(lat, lon, now + datetime.timedelta(seconds=i * 10)))

```


---

### 3. Simular en Wokwi
- Copia las NMEA sentences como entrada por UART (simulando un GPS en Wokwi).
- Puedes usar `Serial1.write()` o simular el GPS con un script en Python con `machine.UART()` en la Pico W.

---

## 🧪 Bonus: Visualización del camino

Si lo quieres hacer **full web**, se puede montar en:
- HTML + Leaflet.js (para marcar ruta)
- Generar automáticamente archivo `.nmea` descargable o stream MQTT

¿Quieres que te cree una versión básica de esta página en React o HTML para empezar? También te puedo generar un mockup completo con un botón para exportar la ruta en formato NMEA.

---

Requerimos:
1. Genere el código para la página web con Leaflet?
2. Te dé el script para simular este stream en Wokwi con UART?


