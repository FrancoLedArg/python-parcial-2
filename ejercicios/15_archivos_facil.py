"""
TEMA: Archivos
DIFICULTAD: Facil
TIPO: Corregir codigo

ENUNCIADO:
El codigo lee notas.txt pero imprime lineas con doble salto.
Corregilo para que cada linea aparezca una sola vez.

EXPLICACION:
print(linea) agrega otro \n porque linea ya trae \n del archivo.

AYUDA_MENTAL:
Usa print(linea.strip()) o print(linea, end="").

EJEMPLO:
Cada linea del archivo, una sola vez.
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

f = open(DATOS / "notas.txt")
for linea in f:
    print(linea)
f.close()
