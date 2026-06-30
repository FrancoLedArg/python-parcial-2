"""
TEMA: Cadenas - SOLUCION
"""
linea = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
palabras = linea.split()
email = palabras[1]
dominio = email.split("@")[1]
print(dominio)
