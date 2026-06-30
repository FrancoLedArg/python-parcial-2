"""
TEMA: Integrador
DIFICULTAD: Medio
TIPO: Escribir solucion

ENUNCIADO:
Lee mbox.txt, cuenta cuantos emails hay por dominio (solo lineas From)
e imprime cada dominio con su cantidad.

PISTA:
if startswith("From "), extrae dominio, acumula en dict.

EJEMPLO:
gmail.com: 4
uct.ac.za: 5
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

