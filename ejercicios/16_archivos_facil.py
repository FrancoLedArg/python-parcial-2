"""
TEMA: Archivos
DIFICULTAD: Facil
TIPO: Completar codigo

ENUNCIADO:
Completa el codigo para verificar si existe datos/notas.txt antes de abrirlo.
Si existe, imprimi "Existe". Si no, imprimi "No encontrado".

EXPLICACION:
Path.exists() devuelve True si el archivo esta en disco.

AYUDA_MENTAL:
ruta = DATOS / "notas.txt"
if ruta.exists(): ...

EJEMPLO:
Salida esperada: Existe
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

ruta = DATOS / "notas.txt"

# --- ZONA DE TRABAJO ---

