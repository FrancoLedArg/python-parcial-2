"""
TEMA: Referencias y alias
DIFICULTAD: Medio
TIPO: Predecir salida

ENUNCIADO:
Predice que imprime original y resultado.

PISTA:
nums = nums * 2 crea NUEVA lista dentro de la funcion. original no cambia.

EJEMPLO:
original: [1, 2, 3]
resultado: [1, 2, 3, 1, 2, 3]
"""

def duplicar(nums):
    nums = nums * 2
    return nums

original = [1, 2, 3]
resultado = duplicar(original)
print(original)
print(resultado)
