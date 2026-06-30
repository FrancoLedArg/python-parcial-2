from rutas import DATOS

ARCHIVOS = ["notas.txt", "mbox.txt", "numeros.txt"]

errores = 0
for nombre in ARCHIVOS:
    ruta = DATOS / nombre
    if ruta.exists():
        print(f"OK  {nombre}")
    else:
        print(f"ERROR  {nombre} no encontrado en {DATOS}")
        errores += 1

if errores:
    raise SystemExit(1)

print(f"\nTodos los archivos de datos encontrados en {DATOS}")
