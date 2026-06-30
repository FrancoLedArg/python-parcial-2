"""
TEMA: Integrador
DIFICULTAD: Dificil
TIPO: Escribir solucion

ENUNCIADO:
Mini-analisis mbox: filtra lineas From, extrae dominio, cuenta en dict,
imprime resultados ordenados alfabeticamente por dominio.

PISTA:
Combina: archivo + startswith + split + dict + sorted(keys).

EJEMPLO:
Reporte completo de dominios en mbox.txt
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

