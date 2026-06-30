import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
ruta = DATOS / "notas.txt"
if ruta.exists():
    print("Existe")
else:
    print("No encontrado")
