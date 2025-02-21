## Información Personal

- **Nombre completo**: Molina Fabela Edgar Fabinan
- **Github**: MolinaEdgar
- **Numero de control**: 22210780
- **Correo electrónico**: L22210780@tectijuana.edu.mx

# Investigación sobre Sensores de Corriente (Shunt, Efecto Hall, Rogowski)

Los **sensores de corriente** son esenciales para medir la intensidad de la corriente eléctrica en diversos sistemas y aplicaciones. Cada tipo de sensor tiene características particulares que lo hacen adecuado para ciertas condiciones. A continuación, se describe cada tipo de sensor en detalle, seguido de una tabla comparativa para resumir sus características clave.

---

## 1. Sensor de Corriente Shunt

### Funcionamiento Detallado:
El **sensor de corriente Shunt** funciona mediante una resistencia muy baja que se coloca en serie con el conductor a medir. La corriente que pasa por el conductor genera una caída de voltaje proporcional a la corriente, que se puede medir. La relación entre la caída de voltaje y la corriente sigue la ley de Ohm: 

### Aplicaciones:
- **Electrónica de potencia**: Se usan en fuentes de alimentación, controladores de carga de baterías y sistemas de medición de corriente en dispositivos electrónicos.
- **Automatización industrial**: Para controlar y medir el consumo de energía en equipos industriales.

### Ventajas:
- **Bajo costo**: Es una solución económica para medir corriente.
- **Alta precisión**: Ofrecen mediciones muy precisas para corriente continua.
- **Simplicidad**: La implementación es simple, solo requiere colocar la resistencia en serie con el conductor.

### Desventajas:
- **Requiere contacto**: Necesita estar en contacto directo con el conductor.
- **Limitado a corriente continua**: No es ideal para medir corriente alterna.
- **Genera caída de voltaje**: Puede afectar el funcionamiento del sistema si no se calcula adecuadamente.
![image](https://github.com/user-attachments/assets/89eadc76-8e99-43a6-a277-462df3a69b5f)

---

## 2. Sensor de Corriente por Efecto Hall

### Funcionamiento Detallado:
El **sensor de Efecto Hall** se basa en el principio de que cuando una corriente eléctrica pasa a través de un conductor, genera un campo magnético que induce un voltaje transversal en el conductor. Este voltaje es proporcional a la intensidad de la corriente. El sensor mide este voltaje generado, y con base en ello, calcula la corriente.

### Aplicaciones:
- **Medición de corriente sin contacto**: Muy utilizado en sistemas de protección eléctrica y control de motores.
- **Sistemas de energía renovable**: En paneles solares, generadores eólicos, etc.

### Ventajas:
- **Aislado galvánicamente**: No requiere contacto con el conductor, lo que mejora la seguridad.
- **Versatilidad**: Puede medir tanto corriente continua (DC) como alterna (AC).
- **Rango de corriente amplio**: Puede medir corrientes altas y bajas sin afectar el sistema.

### Desventajas:
- **Costo más alto**: Comparado con los sensores Shunt, los sensores Hall son más costosos.
- **Interferencias magnéticas**: Sensibles a campos magnéticos externos que pueden alterar la medición.
![image](https://github.com/user-attachments/assets/b024a397-39fd-4e46-b036-fca732e6e278)

---

## 3. Sensor de Corriente Rogowski

### Funcionamiento Detallado:
El **sensor Rogowski** es un transformador de corriente sin núcleo. Utiliza una bobina flexible que se coloca alrededor del conductor. El campo magnético generado por la corriente induce una señal en la bobina, que es proporcional a la tasa de cambio de la corriente. Para obtener la corriente real, se debe integrar esta señal.

### Aplicaciones:
- **Monitoreo de corriente alterna en sistemas industriales**: Usado principalmente en transformadores y generadores.
- **Redes de distribución de energía eléctrica**: Ideal para mediciones en sistemas de alta potencia.

### Ventajas:
- **Diseño flexible**: Se puede instalar sin interrumpir el suministro eléctrico o modificar el sistema.
- **Ideal para corriente alterna**: Eficaz para medir corrientes altas de AC.
- **No saturación**: Puede medir grandes corrientes sin que el sensor se sature.

### Desventajas:
- **Solo corriente alterna**: No puede medir corriente continua (DC).
- **Requiere integración electrónica**: Para obtener una medición precisa de la corriente, se necesita integrar la señal.
![image](https://github.com/user-attachments/assets/c03526e5-37c9-4b29-bd43-a61679628186)

---

## Tabla Comparativa de Sensores de Corriente (Shunt, Efecto Hall, Rogowski)

| **Características**               | **Sensor de Corriente Shunt**                  | **Sensor de Corriente por Efecto Hall**           | **Sensor de Corriente Rogowski**                 |
|-----------------------------------|-----------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| **Definición**                    | Resistencia de bajo valor en serie con el conductor que mide la caída de tensión. | Utiliza el principio del Efecto Hall, que mide el voltaje inducido por un campo magnético generado por la corriente. | Bobina flexible que detecta el campo magnético generado por la corriente en el conductor. |
| **Tipo de Corriente**             | **Corriente continua (DC)**                   | **Corriente continua (DC)** y **alternante (AC)** | **Corriente alterna (AC)**                       |
| **Aislamiento Galvánico**         | No, requiere contacto físico con el conductor. | Sí, no requiere contacto con el conductor.       | Sí, no requiere contacto con el conductor.       |
| **Precisión**                     | Alta precisión para corriente continua (DC).  | Alta precisión para ambos tipos de corriente (AC y DC). | Alta precisión para corriente alterna (AC).     |
| **Rango de Corriente**            | Limitado a corrientes bajas a medias.         | Amplio, incluye tanto corrientes bajas como altas. | Amplio, especialmente adecuado para corrientes altas (AC). |
| **Costo**                         | Bajo costo.                                   | Costo medio a alto debido a la complejidad.       | Costo medio, aunque puede ser más costoso que los de tipo Shunt. |
| **Sensibilidad a Interferencias** | Baja sensibilidad, depende de la calidad del material. | Puede ser afectado por interferencias magnéticas externas. | Baja sensibilidad a interferencias.              |
| **Aplicaciones Típicas**          | Equipos electrónicos de bajo consumo, fuentes de alimentación, automatización. | Medición de corriente sin contacto, equipos de potencia y protección, sistemas de energía renovable. | Medición de corriente alterna en sistemas de distribución eléctrica, monitoreo industrial, y protección de redes. |
| **Ventajas**                      | Económico, fácil de implementar, alta precisión para corriente DC. | Aislado galvánicamente, no requiere contacto, adecuado para AC y DC, rango amplio. | Instalación flexible, ideal para medición de corrientes altas de AC, no se satura. |
| **Desventajas**                   | No adecuado para grandes corrientes o corriente alterna, caída de tensión. | Costo más alto, sensibilidad a interferencias.     | Solo mide corriente alterna, requiere integración electrónica para obtener resultados precisos. |
| **Tamaño y Flexibilidad**         | Requiere espacio físico en el circuito para la resistencia. | Sensores más grandes y menos flexibles.           | Muy flexible, fácil de colocar alrededor del conductor sin interrumpir el sistema. |

---

## Resumen de las Comparaciones Clave:

- **Shunt**: Ideal para medir **corriente continua (DC)** en aplicaciones de bajo costo, donde la caída de tensión no afecta el sistema. Es sencillo, preciso y económico, pero limitado en el rango de corriente y solo apto para corriente continua.
  
- **Efecto Hall**: Perfecto para aplicaciones que requieren mediciones sin contacto y para medir tanto **corriente continua (DC)** como **corriente alterna (AC)**. Es versátil, ofrece aislamiento galvánico y tiene un rango de medición amplio, aunque es más caro que los sensores Shunt.

- **Rogowski**: Este sensor es la mejor opción para medir **corriente alterna (AC)** en aplicaciones de alta potencia, como en sistemas industriales y de distribución de energía. Es flexible, no se satura y tiene un rango de corriente amplio, pero solo es útil para corriente alterna y requiere integración electrónica.

---
