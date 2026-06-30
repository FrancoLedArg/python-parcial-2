import sys
from pathlib import Path

_ej = Path(__file__).resolve().parent
if _ej.name == "soluciones":
    _ej = _ej.parent
sys.path.insert(0, str(_ej))
from rutas import DATOS
log = DATOS / "log_temp.txt"
log.write_text("Linea inicial\n")
f = open(log, "a")
f.write("Fin de sesion\n")
f.close()
print("Corregido: modo append")
