"""
TEMA: Archivos
DIFICULTAD: Facil
TIPO: Completar codigo

ENUNCIADO:
Completa el codigo para abrir datos/notas.txt, contar sus lineas e imprimir el total.

EXPLICACION:
open() devuelve un manejador. Un for sobre el manejador lee linea por linea.
No olvides close() al terminar.

AYUDA_MENTAL:
contador = 0, for linea in archivo: contador += 1, print(contador), close().

EJEMPLO:
Salida esperada: 5
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

archivo = None  # TODO: abrir DATOS / "notas.txt" en modo lectura
contador = 0

# --- ZONA DE TRABAJO ---

print(contador)
