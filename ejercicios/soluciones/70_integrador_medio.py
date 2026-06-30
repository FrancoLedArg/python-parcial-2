import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
f = open(DATOS / "mbox.txt")
pares = []
for linea in f:
    if linea.startswith("From "):
        email = linea.split()[1]
        usuario, dominio = email.split("@")
        pares.append((usuario, dominio))
f.close()
print(len(pares))
print(pares[0])
