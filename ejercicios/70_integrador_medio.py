"""
TEMA: Integrador
DIFICULTAD: Medio
TIPO: Completar codigo

ENUNCIADO:
De mbox.txt, construye lista de tuplas (usuario, dominio) para cada linea From.

PISTA:
usuario, dominio = email.split("@"); append tupla a lista.

EJEMPLO:
Lista con 11 tuplas
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

f = open(DATOS / "mbox.txt")
pares = []

# --- ZONA DE TRABAJO ---
for linea in f:
    if linea.startswith("From "):
        pass  # TODO

f.close()
print(len(pares))
print(pares[0])
