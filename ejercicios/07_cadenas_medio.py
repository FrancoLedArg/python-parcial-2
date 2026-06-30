"""
TEMA: Cadenas
DIFICULTAD: Medio
TIPO: Corregir codigo

ENUNCIADO:
Este codigo deberia imprimir "Tiene arroba" solo si la linea contiene "@".
Corregilo. CUIDADO: find() devuelve -1 cuando no encuentra, y -1 es truthy
en un if... no, espera: en Python -1 es truthy! Ese es el error.

PISTA:
No uses if linea.find("@"): porque -1 se evalua como True.
Compara explicitamente: find(...) != -1  o  usa  "@" in linea

EJEMPLO:
Con linea = "hola@mundo" -> Tiene arroba
Con linea = "sin arroba" -> (nada)
"""

linea = "sin arroba"

# --- ZONA DE TRABAJO (corregir) ---
if linea.find("@"):
    print("Tiene arroba")

