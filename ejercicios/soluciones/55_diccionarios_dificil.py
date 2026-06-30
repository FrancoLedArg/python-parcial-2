d = {"a": 1, "b": 0, "c": 3, "d": 0}
for clave in list(d.keys()):
    if d[clave] == 0:
        del d[clave]
print(d)
