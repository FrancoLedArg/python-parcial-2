import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
f = open(DATOS / "notas.txt")
contador = 0
for linea in f:
    contador = contador + 1
f.close()
print(contador)
