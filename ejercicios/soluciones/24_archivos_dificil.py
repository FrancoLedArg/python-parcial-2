import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
f = open(DATOS / "numeros.txt")
total = 0
cantidad = 0
for linea in f:
    total = total + float(linea.strip())
    cantidad = cantidad + 1
f.close()
promedio = total / cantidad
print("Promedio: %.2f" % promedio)
