"""
TEMA: Cadenas - SOLUCION
"""
texto = "banana"
contador = 0
for i in range(len(texto) - 1):
    if texto[i:i+2] == "na":
        contador = contador + 1
print(contador)
