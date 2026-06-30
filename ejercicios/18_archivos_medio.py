"""
TEMA: Archivos
DIFICULTAD: Medio
TIPO: Completar codigo

ENUNCIADO:
Completa el codigo para imprimir solo las lineas de mbox.txt que contienen
"@uct.ac.za".

PISTA:
"@" in linea  o  linea.find("@uct.ac.za") != -1

EJEMPLO:
Imprime 10 lineas (From y Return-Path con ese dominio).
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
    pass  # TODO

f.close()
