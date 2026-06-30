"""
TEMA: Diccionarios
DIFICULTAD: Medio
TIPO: Corregir codigo

ENUNCIADO:
El codigo busca si "rojo" es clave pero usa mal el operador in.
Corregilo para detectar si "rojo" es CLAVE del diccionario.

PISTA:
"rojo" in colores busca claves. Para valores: "rojo" in colores.values()

EJEMPLO:
colores = {"primary": "rojo"} -> debe imprimir False (rojo es valor, no clave)
"""

colores = {"primary": "rojo", "secondary": "azul"}

# --- ZONA DE TRABAJO (corregir logica) ---
if "rojo" in colores:
    print("rojo es clave")
else:
    print("rojo NO es clave")
