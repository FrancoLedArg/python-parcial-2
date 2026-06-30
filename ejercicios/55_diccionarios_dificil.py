"""
TEMA: Diccionarios
DIFICULTAD: Dificil
TIPO: Corregir codigo

ENUNCIADO:
El codigo intenta eliminar claves con valor 0 mientras itera el dict.
Corregilo creando una lista de claves a borrar primero.

PISTA:
No modifiques un dict durante for clave in d. Copia claves: list(d.keys())

EJEMPLO:
Queda {a: 1, c: 3}
"""

d = {"a": 1, "b": 0, "c": 3, "d": 0}
for clave in d:
    if d[clave] == 0:
        del d[clave]
print(d)
