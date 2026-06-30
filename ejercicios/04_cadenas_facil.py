"""
TEMA: Cadenas
DIFICULTAD: Facil
TIPO: Corregir codigo

ENUNCIADO:
El siguiente codigo intenta cambiar la primera letra de saludo a "H",
pero falla. Corregilo para que imprima "Hola" sin usar input().

EXPLICACION:
Las cadenas son INMUTABLES: no podes hacer saludo[0] = "H".
Debes crear una nueva cadena concatenando partes.

AYUDA_MENTAL:
En vez de modificar, construi: "H" + el resto de la cadena original.

EJEMPLO:
Salida esperada: Hola
"""

saludo = "hola"

# --- ZONA DE TRABAJO (corregir) ---
saludo[0] = "H"
print(saludo)

