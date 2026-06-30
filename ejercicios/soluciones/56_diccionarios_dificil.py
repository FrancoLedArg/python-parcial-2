original = {"a": 1, "b": 2, "c": 3}
invertido = {}
for clave in original:
    invertido[original[clave]] = clave
print(invertido)
