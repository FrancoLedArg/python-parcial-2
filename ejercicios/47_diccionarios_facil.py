"""
TEMA: Diccionarios
DIFICULTAD: Facil
TIPO: Corregir codigo

ENUNCIADO:
El codigo falla con KeyError si la clave no existe. Corregilo usando get.

EXPLICACION:
d["x"] falla si "x" no es clave. d.get("x", 0) devuelve 0 por defecto.

AYUDA_MENTAL:
edades.get("Pedro", 0)

EJEMPLO:
Salida: 25 luego 0
"""

edades = {"Ana": 25}
print(edades["Ana"])
print(edades["Pedro"])
