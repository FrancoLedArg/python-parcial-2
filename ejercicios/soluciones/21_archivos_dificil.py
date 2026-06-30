import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
f = open(DATOS / "mbox.txt")
for linea in f:
    if linea.startswith("From "):
        palabras = linea.split()
        print(palabras[5])
f.close()
