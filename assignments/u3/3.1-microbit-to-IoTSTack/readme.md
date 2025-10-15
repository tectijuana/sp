# Microbit para envio de datos a Serial Console


🐍 Python 3
🟨 JavaScript (Node.js)
🦀 Rust
🦫 Go
💠 C# (.NET)
🧩 TypeScript
🟥 Node-RED

⸻

🧠 Código del micro:bit (común para todos)

Primero, carga este código MicroPython en tu micro:bit.
Es el mismo para todos los ejemplos:

from microbit import *
import time

while True:
    temp = temperature()
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print("TEMP:{},ACC:({},{},{})".format(temp, x, y, z))
    time.sleep(1)


⸻

🐍 Python 3

Instalación

pip install pyserial

Código

import serial
import time

puerto = 'COM3'  # cambia según tu sistema
velocidad = 115200

ser = serial.Serial(puerto, velocidad)
time.sleep(2)

print("Recibiendo datos del micro:bit...\n")

try:
    while True:
        linea = ser.readline().decode('utf-8').strip()
        print(linea)
except KeyboardInterrupt:
    ser.close()
    print("Conexión cerrada.")


⸻

🟨 JavaScript (Node.js)

Instalación

npm install serialport

Código

import { SerialPort, ReadlineParser } from 'serialport';

const port = new SerialPort({ path: 'COM3', baudRate: 115200 });
const parser = port.pipe(new ReadlineParser({ delimiter: '\r\n' }));

console.log('Recibiendo datos del micro:bit...\n');

parser.on('data', (line) => {
  console.log(line);
});

⚠️ Asegúrate de usar "type": "module" en package.json
o ejecuta con node --experimental-modules.

⸻

🦀 Rust

Cargo.toml

[dependencies]
serialport = "4.3.0"

Código (src/main.rs)

use std::time::Duration;
use std::io::{self, BufRead};
use serialport::SerialPort;

fn main() {
    let puerto = "COM3";
    let velocidad = 115200;

    let serial = serialport::new(puerto, velocidad)
        .timeout(Duration::from_millis(1000))
        .open();

    match serial {
        Ok(port) => {
            let reader = io::BufReader::new(port);
            println!("Recibiendo datos del micro:bit...\n");
            for line in reader.lines() {
                if let Ok(data) = line {
                    println!("{}", data);
                }
            }
        }
        Err(e) => eprintln!("Error: {}", e),
    }
}


⸻

🦫 Go (Golang)

Instalación

go get github.com/tarm/serial

Código

package main

import (
	"bufio"
	"fmt"
	"log"
	"github.com/tarm/serial"
)

func main() {
	c := &serial.Config{Name: "COM3", Baud: 115200}
	s, err := serial.OpenPort(c)
	if err != nil {
		log.Fatal(err)
	}
	defer s.Close()

	fmt.Println("Recibiendo datos del micro:bit...\n")

	scanner := bufio.NewScanner(s)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}


⸻

💠 C# (.NET)

Código (Program.cs)

using System;
using System.IO.Ports;

class Program
{
    static void Main()
    {
        SerialPort puerto = new SerialPort("COM3", 115200);
        puerto.Open();
        Console.WriteLine("Recibiendo datos del micro:bit...\n");

        while (true)
        {
            string linea = puerto.ReadLine();
            Console.WriteLine(linea);
        }
    }
}

Ejecución

dotnet new console -n MicrobitReader
cd MicrobitReader
dotnet run


⸻

🧩 TypeScript (Node.js + ES Modules)

Instalación

npm install serialport
npm install -D typescript @types/node

Código (index.ts)

import { SerialPort, ReadlineParser } from 'serialport';

const port = new SerialPort({ path: 'COM3', baudRate: 115200 });
const parser = port.pipe(new ReadlineParser({ delimiter: '\r\n' }));

console.log('Recibiendo datos del micro:bit...\n');

parser.on('data', (line: string) => {
  console.log(line);
});

Ejecución

npx tsc index.ts && node index.js


⸻

🟥 Node-RED

Instalación
	1.	Instalar Node-RED:

npm install -g node-red


	2.	Instalar el nodo Serial:

npm install node-red-node-serialport


	3.	Conectar el micro:bit y verificar el puerto (por ejemplo COM3).

⸻

Flujo JSON listo para importar

Copia y pega en Node-RED → Menú → Importar → Pegar → Importar

[
    {
        "id": "2b8ef2d1b4a0a8e0",
        "type": "tab",
        "label": "Microbit Serial Reader",
        "disabled": false,
        "info": ""
    },
    {
        "id": "fb36c08c4bdb0c09",
        "type": "serial in",
        "z": "2b8ef2d1b4a0a8e0",
        "name": "Microbit Serial",
        "serial": "b2cfc28a8a8f07b8",
        "x": 160,
        "y": 120,
        "wires": [["d02efad5b8bb5a2a"]]
    },
    {
        "id": "d02efad5b8bb5a2a",
        "type": "function",
        "z": "2b8ef2d1b4a0a8e0",
        "name": "Procesar datos",
        "func": "let line = msg.payload.trim();\n// Ejemplo: TEMP:25,ACC:(-128,12,-1024)\n\nif (line.startsWith(\"TEMP:\")) {\n    let tempMatch = line.match(/TEMP:(\\d+)/);\n    let accMatch = line.match(/ACC:\\((-?\\d+),(-?\\d+),(-?\\d+)\\)/);\n\n    if (tempMatch && accMatch) {\n        msg.payload = {\n            temperatura: parseInt(tempMatch[1]),\n            accel_x: parseInt(accMatch[1]),\n            accel_y: parseInt(accMatch[2]),\n            accel_z: parseInt(accMatch[3])\n        };\n        return msg;\n    }\n}\nreturn null;",
        "outputs": 1,
        "noerr": 0,
        "x": 370,
        "y": 120,
        "wires": [["7489b7a7fd64dc6f"]]
    },
    {
        "id": "7489b7a7fd64dc6f",
        "type": "debug",
        "z": "2b8ef2d1b4a0a8e0",
        "name": "Datos del micro:bit",
        "active": true,
        "tosidebar": true,
        "complete": "payload",
        "x": 610,
        "y": 120,
        "wires": []
    },
    {
        "id": "b2cfc28a8a8f07b8",
        "type": "serial-port",
        "serialport": "COM3",
        "serialbaud": "115200",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": "",
        "responsetimeout": "10000"
    }
]


⸻

Resultado en el panel “Debug”

msg.payload : Object
{
  "temperatura": 25,
  "accel_x": -128,
  "accel_y": 12,
  "accel_z": -1024
}


⸻


Estos ejemplos permiten recibir datos del micro:bit por USB Serial (COMx) en cualquier lenguaje moderno o entorno IoT:

Lenguaje / Entorno	Librería principal	Tipo de conexión
Python	pyserial	Serial USB
JavaScript	serialport	Serial USB
Rust	serialport	Serial USB
Go	tarm/serial	Serial USB
C# (.NET)	System.IO.Ports	Serial USB
TypeScript	serialport	Serial USB
Node-RED	node-red-node-serialport	Serial USB


⸻

¿Quieres que te genere la versión con Bluetooth (BLE) para todos estos lenguajes también (usando el micro:bit sin cable USB)?
