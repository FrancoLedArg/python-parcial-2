"""
TEMA: Referencias y alias
DIFICULTAD: Dificil
TIPO: Predecir salida / Trampa

ENUNCIADO:
Predice que imprime a y b. Explica la diferencia entre a=a+[3] y a.append(3).

PISTA:
a = a + [3] crea nueva lista y reasigna a. b sigue apuntando a la original.
a.append(3) modifica la lista compartida.

EJEMPLO:
Caso 1 vs Caso 2 — ejecuta ambos mentalmente.
"""

# Caso con concatenacion
a = [1, 2]
b = a
a = a + [3]
b.append(4)
print("a:", a)
print("b:", b)
