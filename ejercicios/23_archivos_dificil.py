"""
TEMA: Archivos
DIFICULTAD: Dificil
TIPO: Corregir codigo

ENUNCIADO:
El codigo intenta leer linea por linea despues de read() completo.
Corregilo para contar lineas correctamente.

PISTA:
Despues de read(), el puntero esta al final. Usa SOLO for linea in f
O SOLO read().splitlines(), no ambos.

EJEMPLO:
Salida esperada: cantidad de lineas en notas.txt (5)
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

f = open(DATOS / "notas.txt")
contenido = f.read()
contador = 0
for linea in f:
    contador = contador + 1
f.close()
print(contador)
