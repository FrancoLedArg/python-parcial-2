"""
TEMA: Referencias y alias
DIFICULTAD: Facil
TIPO: Corregir codigo / Predecir salida

ENUNCIADO:
Predice que imprime. Luego ejecuta. Explica la diferencia entre == e is.

EXPLICACION:
== compara valores. is compara si es el MISMO objeto en memoria.

AYUDA_MENTAL:
[1,2] == [1,2] es True pero [1,2] is [1,2] es False (dos listas distintas).
"""

x = [1, 2]
y = [1, 2]
z = x
print(x == y)
print(x is y)
print(x is z)
