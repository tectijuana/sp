#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════╗
# ║  Programa:    info.sh — Información básica del dispositivo    ║
# ║  Programador: MC. René Solis R.                               ║
# ║  Curso:       Sistemas Programables (EmbeddedSP) TECNM / ITT  ║
# ║  Horario:     [999]                                           ║
# ║  Actividad:   Recursos — Diagnóstico del dispositivo (Termux) ║
# ║  Asciinema:   [URL de la grabación]                           ║
# ╚═══════════════════════════════════════════════════════════════╝
#
# Objetivo: mostrar información de hardware y sistema del dispositivo
# Android desde Termux, usando getprop y los pseudo-archivos /proc.
#
# Recuerde iniciar su asciinema identificándose antes de cualquier comando:
#   $ echo "Programa info.sh, por MC. René Solis R. de curso Sistemas Programables Horario [999] actividad [ZZZZ]"

echo "===== Información del Dispositivo ====="
# getprop consulta las propiedades del sistema Android
echo "Fabricante: $(getprop ro.product.manufacturer)"
echo "Modelo:     $(getprop ro.product.model)"
echo "Android:    $(getprop ro.build.version.release)"
echo "Kernel:     $(uname -r)"
echo "Arquitectura CPU: $(getprop ro.product.cpu.abi)"
echo "Número de serie:  $(getprop ro.serialno)"
echo
echo "===== CPU ====="
# /proc/cpuinfo describe los núcleos; uniq evita líneas repetidas
cat /proc/cpuinfo | grep -E "Hardware|Processor|model name" | uniq
echo
echo "===== Memoria RAM ====="
grep MemTotal /proc/meminfo
