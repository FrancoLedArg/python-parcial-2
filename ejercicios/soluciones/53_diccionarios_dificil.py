texto = "the cat and the dog and the bird"
conteo = {}
for palabra in texto.split():
    if palabra not in conteo:
        conteo[palabra] = 0
    conteo[palabra] = conteo[palabra] + 1
max_palabra = None
max_cantidad = 0
for palabra in conteo:
    if conteo[palabra] > max_cantidad:
        max_cantidad = conteo[palabra]
        max_palabra = palabra
print(max_palabra)
