"""
TEMA: Archivos
DIFICULTAD: Facil
TIPO: Escribir solucion

ENUNCIADO:
Lee datos/notas.txt e imprimi cada linea sin el salto de linea extra
al final (usa strip()).

EXPLICACION:
Cada linea leida incluye \n al final. strip() lo quita.

AYUDA_MENTAL:
for linea in f: print(linea.strip())

EJEMPLO:
Imprime las 5 lineas de notas.txt sin lineas vacias extra.
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

