# ANÁLISIS COMPARATIVO DE BUSES DE COMUNICACIÓN DE ALTA VELOCIDAD
---
No. Control: 22211528

Nombre: Bernal Aguirre Roberto Eduardo

Fecha: 18/09/2025

---
## 1. Introducción

Los buses de comunicación de alta velocidad son esenciales para transferir datos de manera eficiente entre componentes de un sistema.  
En este análisis se comparan:

- **PCIe (Peripheral Component Interconnect Express)**: interfaz estándar para comunicación host ↔ dispositivo.  
- **AXI (Advanced eXtensible Interface)**: protocolo de interconexión on-chip dentro de SoCs y FPGAs.

---

## 2. Buses Analizados

- **PCIe**
  - Conexión punto a punto, escalable por lanes (x1, x4, x8, x16)
  - Usado en SSDs NVMe, GPUs, NICs y tarjetas de expansión.
- **AXI**
  - Bus/interconexión on-chip, flexible y parametrizable
  - Usado dentro de SoCs para comunicación entre CPU, DMA, memorias y periféricos.

---

## 3. Arquitectura y Topología

- **PCIe**
  - Topología: punto-a-punto con lanes seriales.
  - Capas: PHY (SERDES), Data Link (flow control, CRC), Transaction Layer (TLPs).  
- **AXI**
  - Canales independientes: AW, W, B, AR, R
  - Soporta ráfagas, IDs, transacciones fuera de orden.

---

## 4. Rendimiento y Latencia

- **PCIe**
  - Throughput escalable por lanes y generación (PCIe 3.0, 4.0, 5.0)
  - Latencia mayor que AXI, menos determinista.
- **AXI**
  - Latencia baja y determinista
  - Throughput depende de ancho de bus, frecuencia y longitud de ráfaga

---

## 5. Ordenamiento y Concurrencia

- **PCIe**
  - Reglas de ordering y completion
  - Soporta múltiples transacciones concurrentes, pero requiere coherencia adicional para DMA.
- **AXI**
  - IDs permiten múltiples transacciones out-of-order
  - Burst y arbitraje configurable para máxima eficiencia

---

## 6. Fiabilidad y Manejo de Errores

- **PCIe**
  - CRC, retransmisión automática, diagnóstico y reporting
- **AXI**
  - Integridad confiable por diseño on-chip; no incluye CRC nativo

---

## 7. Complejidad de Implementación

- **PCIe**
  - Alta complejidad física y lógica (PHY, serdes, drivers)
- **AXI**
  - Relativamente simple en HDL, IP cores disponibles, menos overhead de verificación

---

## 8. Uso Típico

| Bus  | Dominio | Ejemplos de uso |
|------|---------|----------------|
| PCIe | Off-chip | SSD NVMe, GPU, NIC, tarjetas de expansión |
| AXI  | On-chip | CPU ↔ DMA ↔ Memoria ↔ Periféricos en SoC |

---

## 9. Seguridad y Consumo

- **PCIe**
  - ACS, IOMMU, SR-IOV para aislamiento
  - Consumo alto por serdes
- **AXI**
  - Firewalls on-chip, TrustZone
  - Consumo medio-bajo, optimizable según frecuencia y ancho

---

## 10. Tabla Comparativa

| Aspecto | PCIe | AXI |
|---------|------|-----|
| Dominio típico | Off-chip | On-chip |
| Topología | Punto-a-punto, lanes | Bus/crossbar, masters/slaves |
| Latencia | Alta | B


---
## 11. Referencias

1. Crucial. (s.f.). *PCIe: Una interfaz más rápida*. Recuperado de [https://www.crucial.mx/articles/about-ssd/pcie-a-faster-interface](https://www.crucial.mx/articles/about-ssd/pcie-a-faster-interface)  
2. Lenovo. (s.f.). *¿Qué es PCIe y cómo funciona?* Recuperado de [https://www.lenovo.com/mx/es/glosario/que-es-pcie/?orgRef=https%253A%252F%252Fwww.google.com%252F&srsltid=AfmBOooddQBaw-asfebmzpRYzR05pJPd7_TfnmHkDmk_UIHxfGrgh5-Z](https://www.lenovo.com/mx/es/glosario/que-es-pcie/?orgRef=https%253A%252F%252Fwww.google.com%252F&srsltid=AfmBOooddQBaw-asfebmzpRYzR05pJPd7_TfnmHkDmk_UIHxfGrgh5-Z)  
3. HardZone. (s.f.). *Velocidad PCI Express: tipos, versiones y anchos de banda*. Recuperado de [https://hardzone.es/tutoriales/rendimiento/velocidad-pci-express-pcie](https://hardzone.es/tutoriales/rendimiento/velocidad-pci-express-pcie)  
4. All About Circuits. (2021). *Introduction to the Advanced Extensible Interface (AXI)*. Recuperado de [https://www.allaboutcircuits.com/technical-articles/introduction-to-the-advanced-extensible-interface-axi](https://www.allaboutcircuits.com/technical-articles/introduction-to-the-advanced-extensible-interface-axi)

---
---
Asistencia de IA: Consulté a ChatGPT para el acomodo de la información y generar su estructura.

Herramienta: ChatGPT (GPT-5)

Fecha: 2025-09-18

Plataforma: N/A.
