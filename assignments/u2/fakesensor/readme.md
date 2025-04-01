
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

def decimal_to_nmea(lat, lon):
    def to_nmea(val, is_lat):
        deg = int(abs(val))
        min = (abs(val) - deg) * 60
        hemi = ('N' if lat >= 0 else 'S') if is_lat else ('E' if lon >= 0 else 'W')
        return f"{deg:02d}{min:07.4f},{hemi}"

    return to_nmea(lat, True), to_nmea(lon, False)

def generate_gprmc(lat, lon, timestamp):
    lat_str, lon_str = decimal_to_nmea(lat, lon)
    time_str = timestamp.strftime("%H%M%S.00")
    date_str = timestamp.strftime("%d%m%y")
    speed = f"{random.uniform(10, 20):.2f}"  # knots
    heading = f"{random.uniform(0, 360):.2f}"
    sentence = f"GPRMC,{time_str},A,{lat_str},{lon_str},{speed},{heading},{date_str},,,A"
    checksum = 0
    for c in sentence:
        checksum ^= ord(c)
    return f"${sentence}*{checksum:02X}"

# Demo with fixed points
route = [(40.7128, -74.0060), (40.7138, -74.0070), (40.7148, -74.0080)]
now = datetime.datetime.utcnow()

for i, (lat, lon) in enumerate(route):
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
3. Ambos?

