"""
TEMA: Archivos
DIFICULTAD: Medio
TIPO: Escribir solucion

ENUNCIADO:
Lee mbox.txt, extrae los dominios unicos de lineas "From ...@dominio ...",
y escribilos (uno por linea) en datos/salida_dominios.txt.

PISTA:
Usa una lista o set para no repetir. split() y split("@") ayudan.

EJEMPLO:
Debe incluir uct.ac.za, gmail.com, hotmail.com, yahoo.com
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

