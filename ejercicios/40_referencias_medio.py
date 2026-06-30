"""
TEMA: Referencias y alias
DIFICULTAD: Medio
TIPO: Predecir salida

ENUNCIADO:
Predice que imprime x e y. Ejecuta y explica el alias mutable.

PISTA:
y y x apuntan a la misma lista. y[0]=99 modifica el objeto compartido.

EJEMPLO:
x: [99, 2]
"""

x = [1, 2]
y = x
y[0] = 99
print(x)
print(y)
