texto = "hola"
conteo = {}
for letra in texto:
    if letra not in conteo:
        conteo[letra] = 0
    conteo[letra] = conteo[letra] + 1
for letra in sorted(conteo.keys()):
    print(letra + ":", conteo[letra])
