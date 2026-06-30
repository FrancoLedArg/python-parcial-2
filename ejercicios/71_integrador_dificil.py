"""
TEMA: Integrador
DIFICULTAD: Dificil
TIPO: Corregir codigo

ENUNCIADO:
Pipeline roto: debe contar dominios de lineas From en mbox.txt.
Encontrar y corregir TODOS los errores.

PISTA:
Revisa startswith, indice de split, nombre del dict, incremento del contador.

EJEMPLO:
uct.ac.za debe ser el dominio mas frecuente (5)
"""


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
    if linea.startswith("From:"):
        email = linea.split()[0]
        dominio = email.split("@")[0]
        if dominio not in conteo:
            conteo[dominio] = 0
        conteo[dominio] = conteo[dominio] + 2
f.close()
for d in sorted(conteo.keys()):
    print(d + ":", conteo[d])
