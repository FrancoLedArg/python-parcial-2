"""
TEMA: Referencias y alias
DIFICULTAD: Facil
TIPO: Corregir codigo / Predecir salida

ENUNCIADO:
Sin ejecutar mentalmente, escribi en comentarios que imprime cada print.
Luego ejecuta y verifica. Si hay sorpresa, explica por que.

EXPLICACION:
Las cadenas son inmutables. Reasignar a no cambia b.

AYUDA_MENTAL:
a y b apuntan a "hola". a = "chau" crea nuevo objeto; b sigue en "hola".

EJEMPLO:
Respuesta esperada en comentarios antes de ejecutar.
"""

a = "hola"
b = a
a = "chau"
print(b)
print(a is b)
