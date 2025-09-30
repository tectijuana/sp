# Comparación entre Arquitecturas RISC y CISC en Sistemas Programables  
**Autor:** José Rito Portugal Laureán

**No. de Control:** 22211635

**Fecha de Investigación:** 14 de septiembre de 2025  

![ARMx86_Banner_2](https://github.com/user-attachments/assets/474e687c-cd06-4aae-8b2e-64cb9b09d87b)

---

## 📌 Introducción  

Las arquitecturas de procesadores **RISC** (Reduced Instruction Set Computer) y **CISC** (Complex Instruction Set Computer) representan dos enfoques fundamentales en el diseño de sistemas programables. Surgidas en diferentes contextos históricos y tecnológicos, cada una prioriza distintos aspectos como la eficiencia energética, la complejidad del hardware o la flexibilidad del software . Esta investigación analiza sus características, ventajas, desventajas y aplicaciones actuales, con base en fuentes confiables y actualizadas.  

---

## 📚 1. Contexto Histórico y Evolución  

![risc_vs_cisc_2](https://github.com/user-attachments/assets/d6c066ca-0ee4-4dae-bdd9-6583e4eb153e)

### 1.1 Orígenes de CISC  
La arquitectura **CISC** surgió en la década de 1970, cuando la memoria era costosa y los compiladores limitados. Su objetivo era reducir el tamaño del código mediante instrucciones complejas que ejecutaran múltiples operaciones en hardware, minimizando la dependencia de software. Ejemplos emblemáticos incluyen los procesadores x86 de Intel y AMD.

### 1.2 Nacimiento de RISC  
**RISC** emergió como una alternativa simplificada en los años 80, centrándose en instrucciones reducidas y de ejecución rápida. Diseñada para optimizar el rendimiento mediante segmentación (*pipelining*) y registros múltiples, se adoptó masivamente en dispositivos móviles y sistemas embebidos (ej.: ARM, MIPS).

### 1.3 Convergencia Actual  
Hoy, la distinción entre RISC y CISC se difumina: los procesadores CISC modernos (ej.: Intel Core) integran principios RISC como la ejecución fuera de orden, mientras que los RISC (ej.: ARMv9) añaden instrucciones especializadas.

---

## ⚙️ 2. Características Técnicas Comparadas  
<img width="600" height="400" alt="CISCvsRISC1" src="https://github.com/user-attachments/assets/ac12e3f4-d593-445a-be88-cf1fa4e44c52" />


### 2.1 Diseño de Instrucciones  
| **Aspecto**               | **CISC**                                                                 | **RISC**                                                                 |
|---------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Tamaño de instrucciones** | Variable (1-15 bytes)                                       | Fijo (4 bytes típicamente)                                  |
| **Ciclos por instrucción** | Múltiples (2-15 ciclos)                                     | Mayormente 1 ciclo                                          |
| **Modos de direccionamiento** | Múltiples y complejos                                       | Simplificados (ej.: registro-registro)                      |
| **Acceso a memoria**       | Directo (operaciones en memoria)                            | Solo mediante LOAD/STORE                                    |

### 2.2 Hardware y Microarquitectura  
- **CISC**: Utiliza **microprogramación** para decodificar instrucciones complejas en microoperaciones. Requiere más transistores, generando mayor consumo energético y calor.
- **RISC**: Emplea **hardware cableado** y segmentación (*pipelining*) para ejecución paralela. Optimiza el uso de registros y reduce accesos a memoria.

### 2.3 Eficiencia y Rendimiento  
- **CISC**: Ideal para código compacto y operaciones complejas. Ej.: operaciones matemáticas en un solo comando.
- **RISC**: Superior en operaciones simples y paralelizables. Ej.: procesamiento de señales en smartphones.
 
---

## 📊 3. Ventajas y Desventajas  
### 3.1 CISC  
| **Ventajas**                                      | **Desventajas**                                  |
|---------------------------------------------------|--------------------------------------------------|
| ✅ Código más compacto                | ❌ Mayor consumo energético          |
| ✅ Compatibilidad con software legacy  | ❌ Decodificación compleja           |
| ✅ Soporte para operaciones en memoria  | ❌ Menos eficiente en pipelining     |

### 3.2 RISC  
| **Ventajas**                                      | **Desventajas**                                  |
|---------------------------------------------------|--------------------------------------------------|
| ✅ Mayor eficiencia energética       | ❌ Código más extenso                |
| ✅ Ejecución en un ciclo              | ❌ Dependencia de compiladores optimizados  |
| ✅ Ideal para pipelining              | ❌ Limitaciones en instrucciones complejas  |

---

## 🌍 4. Aplicaciones Prácticas  
### 4.1 CISC en Sistemas Programables  
- **Computadoras personales y servidores**: Dominio de x86 en software empresarial y legacy.  
- **Sistemas de tiempo real crítico**: Donde la compactación de código es prioritario.  

### 4.2 RISC en Sistemas Programables  
- **Dispositivos móviles y IoT**: ARM en smartphones y consolas portátiles debido a su eficiencia energética.  
- **Supercomputación y embedded**: Procesadores MIPS y RISC-V en routers y sistemas integrados.  

### 4.3 Caso de Estudio: Convergencia ARM-x86  
Apple Silicon (ARM) en MacBooks demuestra cómo RISC alcanza a CISC en rendimiento crudo, mientras que Intel adopta núcleos híbridos (P-Cores/E-Cores) con inspiración RISC .  

---

## 🔮 5. Tendencias Futuras y Conclusiones  
### 5.1 Tendencias  
- **RISC-V**: Arquitectura de código abierto que promete personalización extrema .  
- **Computación heterogénea**: Integración de núcleos RISC y CISC en un mismo chip .  

### 5.2 Conclusión  
Aunque las arquitecturas RISC y CISC fueron diseñadas para contextos históricos distintos, hoy coexisten y convergen. **CISC** sigue siendo relevante en entornos donde la compatibilidad y compactación de código son críticas, mientras que **RISC** domina en eficiencia energética y aplicaciones móviles . La elección depende de factores específicos como el consumo energético, la complejidad del software y los requisitos de rendimiento.  

---

## 📖 Referencias
1. Profesional Review. (2021, 2 julio). *Diferencias RISC y CISC: Comparamos el diseño básico de CPU*. Recuperado el 14 de septiembre de 2025, de https://www.profesionalreview.com/2021/07/18/risc-vs-cisc/   

2. Block&Capital. (2025, 31 marzo). *CISC vs RISC: Dos mundos en la arquitectura de procesadores*. Recuperado el 14 de septiembre de 2025, de https://blockandcapital.com/es/cisc-vs-risc-dos-mundos-en-la-arquitectura-de-procesadores/   

3. Las Diferencias. (2021, 10 abril). *Diferencias Entre Arquitectura RISC y CISC*. Recuperado el 14 de septiembre de 2025, de https://lasdiferencias.com/arquitectura-risc-cisc/
