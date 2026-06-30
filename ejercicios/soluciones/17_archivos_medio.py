import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
contador = 0
f = open(DATOS / "mbox.txt")
for linea in f:
    if linea.startswith("From "):
        contador = contador + 1
f.close()
print(contador)
