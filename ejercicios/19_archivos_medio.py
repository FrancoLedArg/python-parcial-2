"""
TEMA: Archivos
DIFICULTAD: Medio
TIPO: Corregir codigo

ENUNCIADO:
El codigo deberia AGREGAR una linea al final de un archivo de log,
pero borra todo el contenido anterior. Corregilo.

PISTA:
Modo "w" sobrescribe. Para agregar al final usa "a" (append).

EJEMPLO:
Despues de ejecutar dos veces, el archivo debe tener dos lineas "Fin de sesion".
"""


import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS

log = DATOS / "log_temp.txt"
log.write_text("Linea inicial\n")

f = open(log, "w")
f.write("Fin de sesion\n")
f.close()
