"""
TEMA: Referencias y alias
DIFICULTAD: Medio
TIPO: Completar codigo

ENUNCIADO:
Completa el codigo para agregar 4 al final de nums usando append sobre
un alias. Demostra que nums original cambia (mismo objeto en memoria).

PISTA:
alias = nums crea un alias, no una copia. append sobre alias modifica nums.

EJEMPLO:
Salida esperada: [1, 2, 3, 4]
"""

nums = [1, 2, 3]
alias = nums

# --- ZONA DE TRABAJO ---
# TODO: usar alias.append(4)

print(nums)
