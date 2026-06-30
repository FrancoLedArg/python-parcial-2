"""
TEMA: Listas
DIFICULTAD: Dificil
TIPO: Completar codigo

ENUNCIADO:
Completa un histograma: cuenta cuantas veces aparece cada letra en "aba".

PISTA:
Lista de pares o dict. Con dict: if letra not in d: d[letra]=0; d[letra]+=1

EJEMPLO:
a: 2, b: 1 (imprimir cada par)
"""

texto = "aba"
histograma = {}

# --- ZONA DE TRABAJO ---
for letra in texto:
    pass  # TODO

for letra in sorted(histograma.keys()):
    print(letra + ":", histograma[letra])
