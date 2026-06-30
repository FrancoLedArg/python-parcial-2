"""
TEMA: Cadenas - SOLUCION
"""
texto = "banana"
contador = 0
for letra in texto:
    if letra in "aeiou":
        contador = contador + 1
print(contador)
