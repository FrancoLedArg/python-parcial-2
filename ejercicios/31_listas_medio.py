"""
TEMA: Listas
DIFICULTAD: Medio
TIPO: Completar codigo

ENUNCIADO:
Elimina TODOS los 1 de la lista sin crear un bucle infinito.

PISTA:
while 1 in lista: lista.remove(1)  funciona pero es lento.
Mejor: crear nueva lista sin los 1, o remove en while con cuidado.

EJEMPLO:
Salida esperada: [3, 4, 5]
"""

numeros = [3, 1, 4, 1, 5]

# --- ZONA DE TRABAJO ---

print(numeros)
