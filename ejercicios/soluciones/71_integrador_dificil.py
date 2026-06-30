import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
conteo = {}
f = open(DATOS / "mbox.txt")
for linea in f:
    if linea.startswith("From "):
        email = linea.split()[1]
        dominio = email.split("@")[1]
        if dominio not in conteo:
            conteo[dominio] = 0
        conteo[dominio] = conteo[dominio] + 1
f.close()
for d in sorted(conteo.keys()):
    print(d + ":", conteo[d])
