"""
TEMA: Archivos
DIFICULTAD: Dificil
TIPO: Escribir solucion

ENUNCIADO:
Lee datos/numeros.txt (un entero por linea) y calcula el promedio.
Imprime con 2 decimales usando formato %.

PISTA:
Acumula suma, cuenta lineas, divide. float() para convertir cada linea.

EJEMPLO:
Salida esperada: Promedio: 20.00
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

