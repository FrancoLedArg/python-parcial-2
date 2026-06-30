import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
origen = open(DATOS / "mbox.txt")
destino = open(DATOS / "gmail.txt", "w")
for linea in origen:
    if "@gmail.com" in linea:
        destino.write(linea)
origen.close()
destino.close()
print("Listo")
