import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
dominios = []
f = open(DATOS / "mbox.txt")
for linea in f:
    if linea.startswith("From "):
        palabras = linea.split()
        email = palabras[1]
        dominio = email.split("@")[1]
        if dominio not in dominios:
            dominios.append(dominio)
f.close()
out = open(DATOS / "salida_dominios.txt", "w")
for d in dominios:
    out.write(d + "\n")
out.close()
print("Dominios escritos:", len(dominios))
