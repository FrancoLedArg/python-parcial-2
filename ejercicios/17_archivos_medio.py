"""
TEMA: Archivos
DIFICULTAD: Medio
TIPO: Escribir solucion

ENUNCIADO:
Cuenta cuantas lineas en datos/mbox.txt empiezan exactamente con "From "
(seguido de un email, no "From:").

PISTA:
Usa linea.startswith("From ") dentro del bucle for.

EJEMPLO:
Salida esperada: 11
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

# --- ZONA DE TRABAJO ---

