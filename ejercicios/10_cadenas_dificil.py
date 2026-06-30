"""
TEMA: Cadenas
DIFICULTAD: Dificil
TIPO: Corregir codigo

ENUNCIADO:
Corregi el formato para que imprima exactamente:
Nota: 8 de 10 (80%)
usando el operador % con las variables nota=8, total=10, porcentaje=80.0

PISTA:
%d es para enteros, %g o %f para floats, %s para cadenas.
El codigo mezcla tipos incorrectamente.

EJEMPLO:
Salida esperada: Nota: 8 de 10 (80%)
"""

nota = 8
total = 10
porcentaje = 80.0

# --- ZONA DE TRABAJO (corregir) ---
print("Nota: %s de %s (%d%%)" % (nota, total, porcentaje))

