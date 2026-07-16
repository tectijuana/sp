# Paso B — Práctica: Detección inteligente de anomalías IoT mediante VPN F5 BIG-IP

> Subtema [8-VPN](readme.md) · Paso **B** de 3 · Anterior: [Paso A — Teoría](a-teoria-vpn.md) · Siguiente: [Paso C — Demo AWS Academy](c-demo-aws-academy.md)
>
> ⚠️ Esta práctica asume acceso al F5 BIG-IP institucional. El soporte `--protocol=f5` de OpenConnect es experimental y debe validarse antes de impartir la práctica. Para el ensayo sin infraestructura institucional, usar el [paso C](c-demo-aws-academy.md).

---

## 1. Nombre de la práctica

**Monitoreo remoto de sensores IoT y detección de anomalías mediante MQTT, inteligencia artificial y VPN F5 BIG-IP.**

## 2. Propósito

El estudiante implementará un sistema IoT distribuido capaz de:

* Conectarse de forma remota a la red institucional mediante OpenConnect.
* Enviar telemetría de sensores utilizando MQTT.
* Procesar los datos con un modelo de inteligencia artificial.
* Detectar comportamientos anormales en tiempo real.
* Visualizar resultados con Node-RED o un cliente MQTT.
* Comprobar que el broker no es accesible sin la VPN.

OpenConnect puede conectarse a servidores F5 BIG-IP mediante la opción `--protocol=f5`. El soporte se documenta como experimental, por lo que el procedimiento de autenticación institucional debe probarse antes de impartir la práctica.

## 3. Duración estimada

**Tres horas de laboratorio.**

| Etapa                            |   Duración |
| -------------------------------- | ---------: |
| Introducción y arquitectura      | 20 minutos |
| Conexión mediante VPN            | 20 minutos |
| Configuración del entorno Python | 20 minutos |
| Publicación de datos IoT         | 35 minutos |
| Implementación del modelo de IA  | 45 minutos |
| Visualización y pruebas          | 25 minutos |
| Elaboración de conclusiones      | 15 minutos |

## 4. Resultados de aprendizaje

Al concluir, el estudiante podrá:

1. Explicar la función de una VPN en una arquitectura IoT.
2. Utilizar OpenConnect para acceder a servicios internos.
3. Implementar el patrón publicación–suscripción con MQTT.
4. Representar telemetría mediante mensajes JSON.
5. Aplicar un algoritmo no supervisado de detección de anomalías.
6. Configurar controles básicos de autenticación y autorización.
7. Diferenciar entre seguridad de red, autenticación MQTT y cifrado TLS.

## 5. Arquitectura

```text
Computadora del estudiante
│
├── OpenConnect
│       │
│       ▼
│   F5 BIG-IP APM
│       │
│       ▼
│   Red institucional privada
│       │
│       ├── Broker Mosquitto MQTT
│       │       ├── Telemetría IoT
│       │       └── Resultados de IA
│       │
│       └── Node-RED
│               └── Dashboard o monitor de eventos
│
├── simulador.py
└── analizador.py
```

El broker MQTT y Node-RED permanecen dentro de la red institucional. El estudiante únicamente puede alcanzarlos después de establecer la VPN.

Mosquitto es un broker de código abierto compatible con MQTT 5.0, 3.1.1 y 3.1. Permite configurar autenticación, archivos de contraseñas y listas de control de acceso.

## 6. Consideración sobre el dispositivo IoT

OpenConnect no se instala directamente en un ESP32 o sensor básico.

Para esta práctica, la computadora del estudiante funciona como:

* Cliente VPN.
* Gateway IoT.
* Simulador de sensores.
* Cliente MQTT.
* Nodo de procesamiento de inteligencia artificial.

En una extensión con hardware, el ESP32 puede enviar datos por USB serial, Bluetooth o una conexión local a la computadora. Después, la computadora publica esos datos al broker institucional a través de la VPN.

## 7. Recursos requeridos

### Infraestructura del docente

* Servidor o máquina virtual dentro de la red institucional.
* Eclipse Mosquitto.
* Node-RED.
* Certificado TLS para el broker.
* Acceso al F5 BIG-IP institucional.
* Una cuenta VPN por estudiante o equipo.
* Una cuenta MQTT por equipo.

### Equipo del estudiante

* Linux, macOS, FreeBSD o Windows.
* OpenConnect.
* Python 3.
* Certificado de la autoridad certificadora del broker: `ca.crt`.
* Editor de código.
* Credenciales VPN.
* Credenciales MQTT.

La biblioteca Eclipse Paho proporciona un cliente MQTT para Python con soporte para MQTT, TLS, reconexión y comunicación TCP.

## 8. Preparación del servidor

Para los ejemplos se utilizarán los siguientes datos ficticios:

```text
Servidor VPN: vpn.institucion.edu
Grupo VPN: IoT-Lab
Broker MQTT: broker-iot.interno
Dirección privada: 10.20.30.10
Puerto MQTT/TLS: 8883
Node-RED: http://10.20.30.10:1880
```

Estos valores deben reemplazarse por las direcciones institucionales.

### 8.1 Política de acceso en F5 BIG-IP

El grupo VPN de la práctica deberá tener acceso únicamente a los servicios necesarios:

```text
10.20.30.10 TCP 8883  MQTT sobre TLS
10.20.30.10 TCP 1880  Node-RED
```

No es necesario proporcionar acceso a toda la red institucional.

### 8.2 Configuración básica de Mosquitto

Archivo sugerido:

```text
/etc/mosquitto/conf.d/iot-lab.conf
```

Contenido:

```ini
listener 8883

cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/broker.crt
keyfile /etc/mosquitto/certs/broker.key

allow_anonymous false

password_file /etc/mosquitto/passwd
acl_file /etc/mosquitto/acl

persistence true
persistence_location /var/lib/mosquitto/

log_type error
log_type warning
log_type notice
```

Mosquitto recomienda utilizar cifrado cuando se emplean nombres de usuario y contraseñas, porque las credenciales serían vulnerables si se transmitieran sin protección.

### 8.3 Creación de cuentas

Ejemplo para el primer equipo:

```bash
sudo mosquitto_passwd -c /etc/mosquitto/passwd equipo01
```

Para agregar más equipos:

```bash
sudo mosquitto_passwd /etc/mosquitto/passwd equipo02
sudo mosquitto_passwd /etc/mosquitto/passwd equipo03
```

### 8.4 Lista de control de acceso

Archivo:

```text
/etc/mosquitto/acl
```

Contenido:

```ini
user equipo01
topic readwrite curso/iot/equipo01/telemetria
topic readwrite curso/iot/equipo01/resultado

user equipo02
topic readwrite curso/iot/equipo02/telemetria
topic readwrite curso/iot/equipo02/resultado

user equipo03
topic readwrite curso/iot/equipo03/telemetria
topic readwrite curso/iot/equipo03/resultado
```

Esta configuración impide que un equipo publique o lea datos pertenecientes a otro equipo. Mosquitto permite complementar la autenticación con controles de acceso por tópico.

### 8.5 Reinicio del broker

```bash
sudo systemctl restart mosquitto
sudo systemctl status mosquitto
```

## 9. Estructura de tópicos MQTT

Cada equipo utilizará dos tópicos:

```text
curso/iot/equipo01/telemetria
curso/iot/equipo01/resultado
```

Ejemplo de telemetría:

```json
{
  "equipo": "equipo01",
  "timestamp": "2026-07-15T18:30:00+00:00",
  "temperatura": 24.8,
  "humedad": 48.2,
  "vibracion": 0.16,
  "anomalia_generada": false
}
```

Ejemplo de resultado generado por la IA:

```json
{
  "equipo": "equipo01",
  "timestamp": "2026-07-15T18:30:00+00:00",
  "estado": "normal",
  "anomalia": false,
  "puntuacion": 0.1034
}
```

## 10. Conexión mediante OpenConnect

### Linux, macOS o FreeBSD

```bash
sudo openconnect \
  --protocol=f5 \
  --authgroup=IoT-Lab \
  --user=NUMERO_DE_CONTROL \
  vpn.institucion.edu
```

### Windows PowerShell

```powershell
openconnect.exe `
  --protocol=f5 `
  --authgroup=IoT-Lab `
  --user=NUMERO_DE_CONTROL `
  vpn.institucion.edu
```

Cuando el servidor no utilice grupos de autenticación, se elimina:

```text
--authgroup=IoT-Lab
```

No se debe escribir la contraseña directamente en el comando.

OpenConnect utiliza `--protocol=f5` para seleccionar el protocolo F5 BIG-IP. Su compatibilidad puede verse afectada por formularios de autenticación con JavaScript, comprobaciones propietarias del dispositivo o determinados flujos SAML y MFA.

## 11. Comprobación de conectividad

### Resolución del nombre interno

```bash
nslookup broker-iot.interno
```

### Linux, macOS o FreeBSD

```bash
nc -vz broker-iot.interno 8883
```

### Windows PowerShell

```powershell
Test-NetConnection broker-iot.interno -Port 8883
```

Resultado esperado:

```text
TcpTestSucceeded : True
```

La prueba debe repetirse después de desconectar la VPN. En ese momento, la conexión al puerto `8883` deberá fallar.

Esta comprobación demuestra que el servicio MQTT no está expuesto directamente a Internet.

## 12. Preparación del proyecto Python

Crear una carpeta:

```bash
mkdir practica-iot-vpn
cd practica-iot-vpn
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activación en Linux, macOS o FreeBSD:

```bash
source .venv/bin/activate
```

Activación en Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las bibliotecas:

```bash
python -m pip install --upgrade pip
pip install paho-mqtt numpy scikit-learn
```

Los entornos creados con `venv` mantienen los paquetes del proyecto separados de la instalación global de Python.

## 13. Variables de entorno

### Linux, macOS o FreeBSD

```bash
export MQTT_BROKER=broker-iot.interno
export MQTT_USER=equipo01
export MQTT_PASSWORD='CONTRASEÑA_ASIGNADA'
export MQTT_TEAM=equipo01
export MQTT_CA=ca.crt
```

### Windows PowerShell

```powershell
$env:MQTT_BROKER="broker-iot.interno"
$env:MQTT_USER="equipo01"
$env:MQTT_PASSWORD="CONTRASEÑA_ASIGNADA"
$env:MQTT_TEAM="equipo01"
$env:MQTT_CA="ca.crt"
```

Las credenciales no deberán colocarse directamente dentro del código fuente.

## 14. Programa generador de telemetría

Guardar como:

```text
simulador.py
```

```python
import json
import math
import os
import random
import ssl
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


BROKER = os.getenv("MQTT_BROKER", "broker-iot.interno")
PORT = 8883
USER = os.getenv("MQTT_USER")
PASSWORD = os.getenv("MQTT_PASSWORD")
TEAM = os.getenv("MQTT_TEAM", "equipo01")
CA_FILE = os.getenv("MQTT_CA", "ca.crt")

TOPIC = f"curso/iot/{TEAM}/telemetria"

connected = False


def validate_configuration() -> None:
    missing = []

    if not USER:
        missing.append("MQTT_USER")

    if not PASSWORD:
        missing.append("MQTT_PASSWORD")

    if missing:
        raise RuntimeError(
            "Faltan las variables de entorno: " + ", ".join(missing)
        )

    if not os.path.isfile(CA_FILE):
        raise FileNotFoundError(
            f"No se encontró el certificado de la CA: {CA_FILE}"
        )


def on_connect(client, userdata, flags, reason_code, properties):
    global connected

    if reason_code == 0:
        connected = True
        print(f"Conexión establecida con {BROKER}:{PORT}")
    else:
        print(f"Error de conexión MQTT: {reason_code}")


def generate_sample(sample_number: int) -> dict:
    # Las primeras 80 muestras representan comportamiento normal.
    anomaly = sample_number >= 80 and sample_number % 25 == 0

    temperature = (
        24.0
        + 1.2 * math.sin(sample_number / 12)
        + random.uniform(-0.25, 0.25)
    )

    humidity = (
        48.0
        + 2.0 * math.sin(sample_number / 17)
        + random.uniform(-0.6, 0.6)
    )

    vibration = 0.15 + random.uniform(-0.025, 0.025)

    if anomaly:
        temperature += random.uniform(8.0, 12.0)
        vibration += random.uniform(1.0, 1.8)

    return {
        "equipo": TEAM,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperatura": round(temperature, 2),
        "humedad": round(humidity, 2),
        "vibracion": round(vibration, 3),
        "anomalia_generada": anomaly,
    }


def main() -> None:
    validate_configuration()

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id=f"{TEAM}-simulador",
    )

    client.username_pw_set(USER, PASSWORD)

    client.tls_set(
        ca_certs=CA_FILE,
        cert_reqs=ssl.CERT_REQUIRED,
    )

    client.tls_insecure_set(False)
    client.on_connect = on_connect

    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()

    try:
        while not connected:
            time.sleep(0.2)

        for sample_number in range(180):
            payload = generate_sample(sample_number)
            message = json.dumps(payload)

            result = client.publish(
                TOPIC,
                message,
                qos=1,
                retain=False,
            )

            result.wait_for_publish()

            print(
                f"{sample_number:03d} "
                f"T={payload['temperatura']:5.2f} "
                f"H={payload['humedad']:5.2f} "
                f"V={payload['vibracion']:5.3f} "
                f"inyectada={payload['anomalia_generada']}"
            )

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nSimulación interrumpida.")

    finally:
        client.disconnect()
        client.loop_stop()


if __name__ == "__main__":
    main()
```

La API 2.x de Paho introdujo una versión explícita para las funciones callback. El ejemplo utiliza `CallbackAPIVersion.VERSION2` para evitar depender de la interfaz anterior.

## 15. Programa de inteligencia artificial

Guardar como:

```text
analizador.py
```

```python
import json
import os
import ssl
from datetime import datetime, timezone

import numpy as np
import paho.mqtt.client as mqtt
from sklearn.ensemble import IsolationForest


BROKER = os.getenv("MQTT_BROKER", "broker-iot.interno")
PORT = 8883
USER = os.getenv("MQTT_USER")
PASSWORD = os.getenv("MQTT_PASSWORD")
TEAM = os.getenv("MQTT_TEAM", "equipo01")
CA_FILE = os.getenv("MQTT_CA", "ca.crt")

TELEMETRY_TOPIC = f"curso/iot/{TEAM}/telemetria"
RESULT_TOPIC = f"curso/iot/{TEAM}/resultado"

BASELINE_SIZE = 60

baseline = []
model = None


def validate_configuration() -> None:
    missing = []

    if not USER:
        missing.append("MQTT_USER")

    if not PASSWORD:
        missing.append("MQTT_PASSWORD")

    if missing:
        raise RuntimeError(
            "Faltan las variables de entorno: " + ", ".join(missing)
        )

    if not os.path.isfile(CA_FILE):
        raise FileNotFoundError(
            f"No se encontró el certificado de la CA: {CA_FILE}"
        )


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(TELEMETRY_TOPIC, qos=1)
        print(f"Suscripción activa: {TELEMETRY_TOPIC}")
    else:
        print(f"Error de conexión MQTT: {reason_code}")


def publish_result(
    client,
    source_message: dict,
    state: str,
    anomaly: bool,
    score,
) -> None:
    result = {
        "equipo": TEAM,
        "timestamp": source_message.get(
            "timestamp",
            datetime.now(timezone.utc).isoformat(),
        ),
        "estado": state,
        "anomalia": anomaly,
        "puntuacion": score,
        "temperatura": source_message["temperatura"],
        "humedad": source_message["humedad"],
        "vibracion": source_message["vibracion"],
    }

    client.publish(
        RESULT_TOPIC,
        json.dumps(result),
        qos=1,
        retain=False,
    )

    print(json.dumps(result, indent=2))


def on_message(client, userdata, message):
    global model

    try:
        payload = json.loads(message.payload.decode("utf-8"))

        features = [
            float(payload["temperatura"]),
            float(payload["humedad"]),
            float(payload["vibracion"]),
        ]

        if model is None:
            baseline.append(features)

            if len(baseline) < BASELINE_SIZE:
                publish_result(
                    client=client,
                    source_message=payload,
                    state=f"entrenando {len(baseline)}/{BASELINE_SIZE}",
                    anomaly=False,
                    score=None,
                )
                return

            model = IsolationForest(
                n_estimators=150,
                contamination=0.05,
                random_state=42,
            )

            model.fit(np.asarray(baseline))

            publish_result(
                client=client,
                source_message=payload,
                state="modelo_preparado",
                anomaly=False,
                score=None,
            )

            print("Modelo entrenado.")
            return

        sample = np.asarray([features])

        prediction = int(model.predict(sample)[0])
        score = float(model.decision_function(sample)[0])

        anomaly = prediction == -1
        state = "anomalia" if anomaly else "normal"

        publish_result(
            client=client,
            source_message=payload,
            state=state,
            anomaly=anomaly,
            score=round(score, 6),
        )

    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Mensaje inválido: {error}")

    except Exception as error:
        print(f"Error procesando mensaje: {error}")


def main() -> None:
    validate_configuration()

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id=f"{TEAM}-analizador",
    )

    client.username_pw_set(USER, PASSWORD)

    client.tls_set(
        ca_certs=CA_FILE,
        cert_reqs=ssl.CERT_REQUIRED,
    )

    client.tls_insecure_set(False)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, keepalive=60)

    print(f"Analizador iniciado para {TEAM}")

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nAnalizador detenido.")
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
```

`IsolationForest` es un algoritmo no supervisado orientado a detección de valores atípicos. Aísla observaciones mediante selecciones aleatorias de variables y puntos de división; normalmente, los valores anormales requieren menos divisiones para ser aislados.

## 16. Ejecución de la práctica

### Terminal 1: conexión VPN

```bash
sudo openconnect \
  --protocol=f5 \
  --authgroup=IoT-Lab \
  --user=NUMERO_DE_CONTROL \
  vpn.institucion.edu
```

La terminal deberá permanecer abierta.

### Terminal 2: analizador de IA

```bash
python analizador.py
```

Al principio aparecerán mensajes semejantes a:

```json
{
  "estado": "entrenando 15/60",
  "anomalia": false,
  "puntuacion": null
}
```

Después de recibir 60 muestras:

```text
Modelo entrenado.
```

### Terminal 3: simulador IoT

```bash
python simulador.py
```

Durante las primeras muestras se generará comportamiento normal. Después de la muestra 80, el simulador inyectará periódicamente valores anormales de temperatura y vibración.

Ejemplo:

```text
084 T=25.12 H=46.92 V=0.155 inyectada=False
100 T=34.87 H=47.31 V=1.542 inyectada=True
```

El analizador deberá producir un resultado semejante a:

```json
{
  "equipo": "equipo01",
  "estado": "anomalia",
  "anomalia": true,
  "puntuacion": -0.142736,
  "temperatura": 34.87,
  "humedad": 47.31,
  "vibracion": 1.542
}
```

## 17. Visualización con Node-RED

Node-RED incluye nodos MQTT de entrada y salida que se conectan a un broker mediante una configuración compartida.

El estudiante deberá construir el siguiente flujo:

```text
MQTT In
   │
   ▼
JSON
   │
   ├──────────────► Debug
   │
   ▼
Switch: msg.payload.anomalia
   │
   ├── false ─────► Indicador normal
   │
   └── true ──────► Alerta de anomalía
```

### Configuración del nodo MQTT In

```text
Servidor: broker-iot.interno
Puerto: 8883
TLS: activado
CA: ca.crt
Usuario: equipo01
Contraseña: contraseña asignada
Tópico: curso/iot/equipo01/resultado
QoS: 1
```

### Configuración del nodo Switch

Condición:

```text
msg.payload.anomalia == true
```

### Variables que pueden graficarse

```text
msg.payload.temperatura
msg.payload.humedad
msg.payload.vibracion
msg.payload.puntuacion
```

## 18. Pruebas de seguridad

### Prueba 1: acceso sin VPN

1. Detener OpenConnect.
2. Ejecutar la prueba de conectividad al puerto 8883.
3. Intentar iniciar `simulador.py`.

Resultado esperado:

```text
No se puede establecer conexión con broker-iot.interno.
```

### Prueba 2: acceso con VPN

1. Establecer OpenConnect.
2. Ejecutar nuevamente la prueba.

Resultado esperado:

```text
El puerto 8883 es accesible.
```

### Prueba 3: aislamiento entre equipos

El equipo 01 intentará publicar en:

```text
curso/iot/equipo02/telemetria
```

Resultado esperado:

```text
Publicación rechazada por la política ACL del broker.
```

### Prueba 4: validación TLS

Cambiar temporalmente el nombre correcto del broker por una dirección o nombre que no corresponda con el certificado.

Resultado esperado:

```text
Error de validación del certificado.
```

No deberán utilizarse mecanismos como:

```python
client.tls_insecure_set(True)
```

Tampoco deberán desactivarse las verificaciones de certificado en OpenConnect.

## 19. Preguntas para el reporte

1. ¿Qué función cumple F5 BIG-IP dentro de la arquitectura?
2. ¿Qué diferencia existe entre la VPN y el cifrado TLS de MQTT?
3. ¿Por qué el broker no debe configurarse con acceso anónimo?
4. ¿Qué ventaja proporciona una ACL por equipo?
5. ¿Por qué se entrenó el modelo con las primeras 60 muestras?
6. ¿Qué variables influyeron más en la detección de anomalías?
7. ¿Qué sucede cuando se desconecta la VPN?
8. ¿Por qué no se instala OpenConnect directamente en el ESP32?
9. ¿Qué falsos positivos observó el equipo?
10. ¿Qué cambios serían necesarios para utilizar sensores reales?

## 20. Evidencias solicitadas

Cada equipo entregará:

* Captura de la conexión VPN, sin mostrar contraseñas.
* Resultado de la prueba al puerto 8883.
* Código de `simulador.py`.
* Código de `analizador.py`.
* Cinco mensajes de telemetría en formato JSON.
* Dos eventos clasificados como normales.
* Dos eventos clasificados como anomalías.
* Captura del flujo de Node-RED.
* Captura de la gráfica de temperatura o vibración.
* Resultado de la prueba sin VPN.
* Resultado de la prueba de acceso a un tópico no autorizado.
* Respuestas a las preguntas del reporte.
* Conclusiones individuales.

## 21. Rúbrica de evaluación

| Criterio                                    |  Puntos |
| ------------------------------------------- | ------: |
| Conexión correcta mediante OpenConnect y F5 |      15 |
| Validación de conectividad interna          |      10 |
| Publicación correcta de telemetría MQTT     |      15 |
| Formato y calidad de los mensajes JSON      |      10 |
| Implementación del modelo Isolation Forest  |      20 |
| Identificación de anomalías                 |      10 |
| Visualización en Node-RED                   |      10 |
| Pruebas de seguridad y ACL                  |       5 |
| Reporte y conclusiones                      |       5 |
| **Total**                                   | **100** |

## 22. Criterios de funcionamiento satisfactorio

La práctica se considera funcional cuando:

```text
1. El broker solamente es accesible mediante la VPN.
2. El cliente valida correctamente el certificado TLS.
3. El simulador publica datos en su tópico autorizado.
4. El analizador recibe al menos 60 muestras.
5. El modelo identifica los eventos anormales inyectados.
6. Node-RED muestra datos y alertas.
7. Un equipo no puede acceder a los tópicos de otro.
```

## 23. Problemas frecuentes

| Problema                                   | Causa probable                           | Corrección                                                    |
| ------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------- |
| La VPN conecta, pero el broker no responde | Ruta o política de F5 incorrecta         | Revisar la ACL y las rutas asignadas al grupo VPN             |
| El nombre interno no se resuelve           | DNS institucional no asignado por la VPN | Configurar DNS interno o usar una entrada temporal controlada |
| Error de certificado TLS                   | El nombre no coincide con el certificado | Utilizar el nombre DNS incluido en el certificado             |
| MQTT responde “not authorized”             | Usuario, contraseña o ACL incorrectos    | Revisar la cuenta y el tópico asignado                        |
| El analizador permanece entrenando         | No recibe suficientes mensajes           | Revisar el tópico y ejecutar el simulador                     |
| Todas las muestras aparecen normales       | Anomalías poco diferenciadas             | Revisar valores de temperatura y vibración                    |
| OpenConnect no completa la autenticación   | Flujo F5 no compatible                   | Revisar SAML, MFA, JavaScript o comprobaciones de dispositivo |
| Funciona con IP, pero no con nombre        | Problema de DNS interno                  | Verificar la configuración DNS entregada por F5               |

## 24. Consideraciones de seguridad

La VPN protege el acceso a la red, pero no sustituye los demás controles. La arquitectura deberá aplicar:

```text
VPN F5 BIG-IP
        +
MQTT sobre TLS
        +
Usuario y contraseña
        +
ACL por tópico
        +
Broker no expuesto a Internet
```

Para una implementación de producción, el simulador y el analizador utilizarían cuentas MQTT independientes, permisos mínimos, certificados administrados institucionalmente y registros centralizados de auditoría.

---

➡️ Continúa con el [Paso C — Demo experimental en AWS Academy (ocserv)](c-demo-aws-academy.md)
