"""
TEMA: Integrador
DIFICULTAD: Dificil
TIPO: Escribir solucion

ENUNCIADO:
Mostra los 3 dominios mas frecuentes en mbox.txt (lineas From).
Si hay empate, orden alfabetico basta para desempatar.

PISTA:
Construi dict de conteos, converti a lista de tuplas, ordena por (-cantidad, dominio).

EJEMPLO:
uct.ac.za, gmail.com, ...
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

