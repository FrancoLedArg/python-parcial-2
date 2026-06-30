"""
TEMA: Listas
DIFICULTAD: Facil
TIPO: Corregir codigo

ENUNCIADO:
Corregi el bucle para imprimir todos los elementos de la lista
(sin IndexError).

EXPLICACION:
range(len(nums)) genera 0, 1, 2 para lista de 3 elementos.
range(len(nums)+1) se pasa de indice.

AYUDA_MENTAL:
Validos: 0, 1, 2 para len=3. El indice 3 no existe.

EJEMPLO:
Salida: 1 2 3 (cada uno en linea)
"""

nums = [1, 2, 3]
for i in range(len(nums) + 1):
    print(nums[i])
