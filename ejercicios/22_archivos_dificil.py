"""
TEMA: Archivos
DIFICULTAD: Dificil
TIPO: Escribir solucion

ENUNCIADO:
Copia todas las lineas de mbox.txt que contienen "@gmail.com" a
datos/gmail.txt (solo esas lineas, con salto de linea).

PISTA:
Abri origen en "r", destino en "w". Escribi lineas que cumplan la condicion.

EJEMPLO:
gmail.txt debe tener 4 lineas From con gmail.com
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

