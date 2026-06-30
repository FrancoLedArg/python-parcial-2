"""
TEMA: Archivos
DIFICULTAD: Dificil
TIPO: Completar codigo

ENUNCIADO:
De cada linea "From ... HH:MM:SS ..." en mbox.txt, extrae e imprime la hora
(campo en posicion 5 despues de split).

PISTA:
palabras = linea.split() -> hora = palabras[5]

EJEMPLO:
Primera hora: 09:14:16
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

f = open(DATOS / "mbox.txt")

# --- ZONA DE TRABAJO ---
for linea in f:
    if linea.startswith("From "):
        pass  # TODO

f.close()
