"""
TEMA: Tuplas
DIFICULTAD: Facil
TIPO: Corregir codigo

ENUNCIADO:
Corregi el codigo que intenta modificar una tupla (inmutable).

EXPLICACION:
Las tuplas no permiten t[i] = valor. Crea una nueva tupla si necesitas cambiar.

AYUDA_MENTAL:
t = (1, t[1], 3) en vez de t[0] = 1 si queres otro primer elemento.

EJEMPLO:
Imprimir tupla con 1 al inicio: (1, 2, 3) partiendo de (0, 2, 3)
"""

t = (0, 2, 3)
t[0] = 1
print(t)
