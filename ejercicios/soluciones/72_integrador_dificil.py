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
        if dominio not in conteo:
            conteo[dominio] = 0
        conteo[dominio] = conteo[dominio] + 1
f.close()
lista = list(conteo.items())
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[j][1] > lista[i][1]:
            lista[i], lista[j] = lista[j], lista[i]
for i in range(min(3, len(lista))):
    print(lista[i][0] + ":", lista[i][1])
