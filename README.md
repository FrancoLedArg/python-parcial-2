# Ejercicios — Programación 1 (Python)

Banco de ejercicios alineado con el temario de cadenas, archivos, listas, referencias, diccionarios y tuplas (slides 40–88).

## Estructura del proyecto

```
python-ejercicios/
├── README.md              ← guía de uso (este archivo)
├── CONTENIDO.md           ← temario del examen
├── REFACTOR.md            ← guía de estudio
└── ejercicios/
    ├── 01_cadenas_facil.py … 76_cadenas_facil.py
    ├── rutas.py           ← resuelve ruta a datos/
    ├── verificar_datos.py
    ├── datos/             ← notas.txt, mbox.txt, etc.
    └── soluciones/
```

## Cómo ejecutar un ejercicio

1. Abrí un ejercicio, por ejemplo [`ejercicios/01_cadenas_facil.py`](ejercicios/01_cadenas_facil.py).
2. Escribí tu solución en la sección `# --- ZONA DE TRABAJO ---`.
3. Ejecutá con **Run Python File** (botón ▶ del IDE sobre el archivo abierto).

No hace falta abrir la terminal ni cambiar de carpeta: el IDE ejecuta el archivo que tenés abierto y [`ejercicios/rutas.py`](ejercicios/rutas.py) encuentra `ejercicios/datos/` automáticamente.

### Alternativa por consola

Desde el root del proyecto (`python-ejercicios/`):

```bash
python ejercicios/01_cadenas_facil.py
python ejercicios/verificar_datos.py
```

## Archivos de datos

Los ejercicios de archivos e integradores leen datos desde [`ejercicios/datos/`](ejercicios/datos/). La ruta se resuelve con el módulo [`ejercicios/rutas.py`](ejercicios/rutas.py).

Si un ejercicio falla con `FileNotFoundError`, ejecutá primero [`ejercicios/verificar_datos.py`](ejercicios/verificar_datos.py) con Run Python File (o el comando de consola de arriba). Debe mostrar `OK` para `notas.txt`, `mbox.txt` y `numeros.txt`.

## Soluciones

Las soluciones están en [`ejercicios/soluciones/`](ejercicios/soluciones/). Intentá resolver cada ejercicio al menos **15–20 minutos** antes de mirarlas.

## Ruta mínima de estudio (pre-examen)

No hace falta hacer los 76 ejercicios. Con esta selección (~35) cubrís lo esencial:

| Bloque | Ejercicios recomendados |
|--------|-------------------------|
| Cadenas | 01–04, 07–08, 10–11 |
| Archivos | 13–15, 17–18, 21 |
| Listas | 25–28, 30, 33–34 |
| Referencias | 37–40, 43 |
| Diccionarios | 46–49, 50, 53 |
| Tuplas | 57–60, 62–63 |
| Formato | 74–75 |
| Integradores | 69, 71, 73 |

Orden sugerido: seguí la numeración dentro de cada bloque (fácil → medio → difícil). Los archivos están en `ejercicios/NN_tema_dificultad.py`.

## Material adicional

- [`ejercicios/datos/alumnos.csv`](ejercicios/datos/alumnos.csv): archivo de ejemplo opcional para práctica futura (no usado por ningún ejercicio obligatorio).
- [`REFACTOR.md`](REFACTOR.md): guía de estudio con explicaciones conceptuales.
- [`CONTENIDO.md`](CONTENIDO.md): temario del examen.

## Estructura de nombres

```
ejercicios/NN_tema_dificultad.py
```

- `NN`: número de orden (01–76)
- `tema`: cadenas, archivos, listas, referencias, diccionarios, tuplas, formato, integrador
- `dificultad`: facil, medio, dificil

## Tipos de ejercicio

| Tipo | Qué tenés que hacer |
|------|---------------------|
| Escribir solucion | Completar la zona de trabajo desde cero |
| Completar codigo | Rellenar los `TODO` / `pass` |
| Corregir codigo | Encontrar y arreglar el error |
| Predecir salida | Decir qué imprime antes de ejecutar |
