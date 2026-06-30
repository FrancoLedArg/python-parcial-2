"""
TEMA: Tuplas
DIFICULTAD: Medio
TIPO: Predecir salida

ENUNCIADO:
Predice el resultado de la comparacion e imprime explicacion en comentario.

PISTA:
Python compara elemento a elemento. (1,2,999) vs (1,2,3): compara 999 vs 3 en pos 2.

EJEMPLO:
Resultado: False
"""

resultado = (1, 2, 999) < (1, 2, 3)
print(resultado)
