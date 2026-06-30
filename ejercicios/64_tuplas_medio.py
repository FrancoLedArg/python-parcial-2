"""
TEMA: Tuplas
DIFICULTAD: Medio
TIPO: Corregir codigo

ENUNCIADO:
El codigo intenta crear tupla de un elemento pero falla.
Corregilo para que t sea tupla (5,) no entero 5.

PISTA:
(5) es int. (5,) es tupla de un elemento — la coma es obligatoria.

EJEMPLO:
type(t) debe ser tuple, len(t) == 1
"""

t = (5)
print(type(t))
print(len(t))
