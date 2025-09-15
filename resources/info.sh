
#!/bin/bash
# info.sh - Muestra información básica del dispositivo en Termux

echo "===== Información del Dispositivo ====="
echo "Fabricante: $(getprop ro.product.manufacturer)"
echo "Modelo:     $(getprop ro.product.model)"
echo "Android:    $(getprop ro.build.version.release)"
echo "Kernel:     $(uname -r)"
echo "Arquitectura CPU: $(getprop ro.product.cpu.abi)"
echo "Número de serie:  $(getprop ro.serialno)"
echo
echo "===== CPU ====="
cat /proc/cpuinfo | grep -E "Hardware|Processor|model name" | uniq
echo
echo "===== Memoria RAM ====="
grep MemTotal /proc/meminfo

