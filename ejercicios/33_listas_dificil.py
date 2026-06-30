"""
TEMA: Listas
DIFICULTAD: Dificil
TIPO: Corregir codigo

ENUNCIADO:
El codigo deberia agregar los elementos [4, 5] a nums, pero falla.
Corregilo para que nums quede [1, 2, 3, 4, 5].

PISTA:
append agrega UN elemento (la lista entera). extend agrega cada elemento.

EJEMPLO:
Salida: [1, 2, 3, 4, 5]
"""

nums = [1, 2, 3]
nums.append([4, 5])
print(nums)
