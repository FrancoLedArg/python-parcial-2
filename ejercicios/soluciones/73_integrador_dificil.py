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
        dominio = linea.split()[1].split("@")[1]
        conteo[dominio] = conteo.get(dominio, 0) + 1
f.close()
print("=== Reporte mbox ===")
for dominio in sorted(conteo.keys()):
    print(dominio + ": " + str(conteo[dominio]))
print("Total emails:", sum(conteo.values()))
