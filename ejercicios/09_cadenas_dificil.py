"""
TEMA: Cadenas
DIFICULTAD: Dificil
TIPO: Escribir solucion

ENUNCIADO:
Cuenta cuantas veces aparece la subcadena "na" en "banana" SIN que
cuente solapamientos. El resultado correcto es 2 (posiciones 2 y 4),
NO 3.

PISTA:
Recorre indice de 0 a len(texto)-2. En cada posicion, compara
texto[indice:indice+2] con "na". Si coincide, suma 1.

PISTA_2:
No uses .count("na") directamente: ese metodo no solapa pero el
ejercicio busca que entiendas el recorrido manual.

EJEMPLO:
Salida esperada: 2
"""

texto = "banana"

# --- ZONA DE TRABAJO ---

