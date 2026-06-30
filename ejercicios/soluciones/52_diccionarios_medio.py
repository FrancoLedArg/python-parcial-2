oracion = "the quick brown fox jumps over the lazy dog"
conteo = {}
for palabra in oracion.split():
    if palabra not in conteo:
        conteo[palabra] = 0
    conteo[palabra] = conteo[palabra] + 1
for palabra in sorted(conteo.keys()):
    print(palabra + ":", conteo[palabra])
