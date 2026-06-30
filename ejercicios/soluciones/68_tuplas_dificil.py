conteo = {"a": 3, "b": 7, "c": 2}
max_clave = None
max_valor = None
for clave, valor in conteo.items():
    if max_valor is None or valor > max_valor:
        max_valor = valor
        max_clave = clave
print(max_clave, max_valor)
