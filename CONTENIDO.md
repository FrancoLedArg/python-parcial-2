Acá tenés el contenido completo de las diapositivas 40 a 88:

---

**Slide 40 — Ejercicios**

---

**Slide 41 — Cadenas**

Una cadena es una secuencia de caracteres. Puedes acceder a los caracteres de uno en uno con el operador corchete:
La segunda sentencia extrae el carácter en la posición del índice 1 de la variable fruta y la asigna a la variable letra. La expresión en los corchetes es llamada índice. El índice indica qué carácter de la secuencia quieres (de ahí el nombre).

---

**Slide 42 — Recorriendo una cadena mediante un bucle**

Muchos de los cálculos requieren procesar una cadena carácter por carácter. Frecuentemente empiezan desde el inicio, seleccionando cada carácter presente, haciendo algo con él, y continuando hasta el final. Este patrón de procesamiento es llamado un recorrido. Una manera de escribir un recorrido es con un bucle while:
¿Se podría hacer esto con un for?

---

**Slide 43 — Rebanado de una cadena**

Un segmento de una cadena es llamado rebanado. Seleccionar un rebanado es similar a seleccionar un carácter.
El operador [n:m] retorna la parte de la cadena desde el "n-ésimo" carácter hasta el "m-ésimo" carácter, incluyendo el primero pero excluyendo el último. Si omites el primer índice (antes de los dos puntos), el rebanado comienza desde el inicio de la cadena. Si omites el segundo índice, el rebanado va hasta el final de la cadena.

---

**Slide 44 — Los cadenas son inmutables**

Puede ser tentador utilizar el operador [] en el lado izquierdo de una asignación, con la intención de cambiar un carácter en una cadena. Por ejemplo:
(esto produce un error, ya que las cadenas no se pueden modificar)

---

**Slide 45 — El operador in**

La palabra in es un operador booleano que toma dos cadenas y regresa True si la primera cadena aparece como una subcadena de la segunda.
Los operadores de comparación funcionan en cadenas. Para ver si dos cadenas son iguales:

---

**Slide 46 — Métodos de cadenas**

Las cadenas son un ejemplo de objetos en Python. Un objeto contiene tanto datos (el valor de la cadena misma) como métodos, los cuales son efectivamente funciones que están implementadas dentro del objeto y que están disponibles para cualquier instancia del objeto.
Python tiene una función llamada dir la cual lista los métodos disponibles para un objeto. La función type muestra el tipo de un objeto y la función dir muestra los métodos disponibles.

---

**Slide 47 — Ejercicio**

Frecuentemente, queremos examinar una cadena para encontrar una subcadena.
Por ejemplo, si se nos presentara una serie de líneas con el siguiente formato:
`From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008`
y quisiéramos obtener únicamente la segunda parte de la dirección de correo (esto es, uct.ac.za) de cada línea...

---

**Slide 48 — El operador de formato**

El operador de formato % nos permite construir cadenas, reemplazando partes de las cadenas con datos almacenados en variables. Cuando lo aplicamos a enteros, % es el operador módulo. Pero cuando es aplicado a una cadena, % es el operador de formato.
El siguiente ejemplo usa %d para formatear un entero, %g para formatear un número de punto flotante, y %s para formatear una cadena.

---

**Slide 49 — Ejercicios**

---

**Slide 50 — Archivos**

La memoria secundaria no es eliminada cuando apagamos una computadora. Incluso, en el caso de una memoria USB, los datos que escribimos desde nuestros programas pueden ser retirados del sistema y transportados a otro sistema.
Nos vamos a enfocar principalmente en leer y escribir archivos como los que creamos en un editor de texto.

---

**Slide 51 — Abrir archivos**

Cuando queremos abrir o escribir un archivo (digamos, en el disco duro), primero debemos abrir el archivo. Cuando abres un archivo, le estás pidiendo al sistema operativo que encuentre el archivo por su nombre y se asegure de que existe.
Si el open es exitoso, el sistema operativo nos devuelve un manejador de archivo. El manejador de archivo no son los datos contenidos en el archivo, sino un "manejador" (handler) que podemos usar para leer los datos. Obtendrás un manejador de archivo si el archivo solicitado existe y si tienes los permisos apropiados para leerlo.
Si el archivo no existe, open fallará con un mensaje de error y no obtendrás un manejador para acceder al contenido del archivo.
Un archivo de texto puede ser considerado como una secuencia de líneas.

---

**Slide 52 — Lectura de archivos**

Aunque el manejador de archivo no contiene los datos de un archivo, es bastante fácil utilizarlo en un bucle for para leer a través del archivo y contar cada una de sus líneas.
Cuando el archivo es leído usando un bucle for de esta manera, Python se encarga de dividir los datos del archivo en líneas separadas utilizando el separador de línea. Python lee cada línea hasta el separador e incluye el separador como el último carácter en la variable line para cada iteración del bucle for.
Si sabes que el archivo es relativamente pequeño comparado al tamaño de tu memoria principal, puedes leer el archivo completo en una sola cadena utilizando el método read en el manejador de archivos.

---

**Slide 53 — Búsqueda a través de un archivo**

Cuando buscas a través de los datos de un archivo, un patrón muy común es leer el archivo, ignorar la mayoría de las líneas y solamente procesar líneas que cumplan con una condición particular. Podemos combinar el patrón de leer un archivo con métodos de cadenas para construir mecanismos de búsqueda sencillos.
Por ejemplo, si queremos leer un archivo e imprimir solo las líneas que comienzan con el prefijo "From:", podríamos usar el método de cadenas startswith para seleccionar solo aquellas líneas con el prefijo deseado.

---

**Slide 54 — Búsqueda a través de un archivo**

Podemos usar el método de cadenas find para simular la función de búsqueda de un editor de texto, que encuentra las líneas donde aparece la cadena de búsqueda en alguna parte. Puesto que find busca cualquier ocurrencia de una cadena dentro de otra y devuelve la posición de esa cadena o -1 si la cadena no fue encontrada, podemos escribir un bucle para mostrar las líneas que contienen la cadena "@uct.ac.za" (es decir, las que vienen de la Universidad de Cape Town en Sudáfrica).

---

**Slide 55 — Escritura de archivos**

Para escribir en un archivo, tienes que abrirlo en modo "w" (de write, escritura) como segundo parámetro.
Si el archivo ya existía previamente, abrirlo en modo de escritura causará que se borre todo el contenido del archivo, así que ¡ten cuidado! Si el archivo no existe, un nuevo archivo es creado.
El método write del manejador de archivos escribe datos dentro del archivo, devolviendo el número de caracteres escritos. El modo de escritura por defecto es texto para escribir (y leer) cadenas.

---

**Slide 56 — Modificar un archivo**

Para modificar (cambiar el contenido) de un archivo, debes usar el método write(). Existen dos alternativas (append o write) en base al modo que escojas para abrir el archivo.
"Append" significa agregar algo al final de una estructura o valor. El modo "a" (append) te permite abrir un archivo para agregar contenido al final del contenido existente.

---

**Slide 57 — Ejercicios**

---

**Slide 58 — Listas**

Así como una cadena, una lista es una secuencia de valores. En una cadena, los valores son caracteres; en una lista, pueden ser cualquier tipo. Los valores en una lista son llamados elementos o a veces ítems.
Hay varias formas de crear una nueva lista; la más simple es encerrar los elementos en corchetes ("[" y "]").
El primer ejemplo es una lista de 4 enteros. La segunda es una lista de tres cadenas. Los elementos de una lista no tienen que ser del mismo tipo.
Una lista dentro de otra lista está anidada. Una lista que no contiene elementos es llamada una lista vacía; puedes crear una con corchetes vacíos, [].
Puedes asignar los valores de una lista a variables.

---

**Slide 59 — Listas**

La sintaxis para acceder a elementos de una lista es la misma que para acceder a los caracteres de una cadena: el operador corchete. La expresión dentro de los corchetes especifica el índice. Recordemos que los índices empiezan en 0.
A diferencia de las cadenas, las listas son mutables porque pueden cambiar el orden de los elementos en una lista o reasignar un elemento en una lista.
Si un índice tiene un valor negativo, éste cuenta hacia atrás desde el final de la lista.
El operador in funciona también en listas.

---

**Slide 60 — Recorriendo una lista**

La forma más común de recorrer los elementos de una lista es con un bucle for. La sintaxis es la misma que para las cadenas.
Esto funciona bien si solamente necesitas leer los elementos de la lista. Pero si quieres escribir o actualizar los elementos, necesitas los índices. Una forma común de hacer eso es combinando las funciones range y len.

---

**Slide 61 — Operaciones de listas**

El operador + concatena listas.
De igual forma, el operador * repite una lista un determinado número de veces.
El operador de rebanado también funciona en listas.
Un operador de rebanado al lado izquierdo de una asignación puede actualizar múltiples elementos.

---

**Slide 62 — Métodos de listas**

Python provee métodos que operan en listas. Por ejemplo, append agrega un nuevo elemento al final de una lista.
extend toma una lista como argumento y agrega todos los elementos.
sort ordena los elementos de la lista de menor a mayor.
La mayoría de métodos no regresan nada; modifican la lista y regresan None.

---

**Slide 63 — Eliminando elementos**

Hay varias formas de eliminar elementos de una lista. Si sabes el índice del elemento que quieres, puedes usar pop. Si no provees un índice, la función elimina y retorna el último elemento. Si no necesitas el valor removido, puedes usar el operador del.
Si sabes qué elemento quieres remover (pero no sabes el índice), puedes usar remove.

---

**Slide 64 — Eliminando elementos**

Para remover más de un elemento, puedes usar del con un índice de rebanado.

---

**Slide 65 — Listas y funciones**

Hay un cierto número de funciones internas que pueden ser utilizadas en las listas que te permiten mirar rápidamente a través de una lista sin escribir tus propios bucles.

---

**Slide 66 — Listas y cadenas**

Una cadena es una secuencia de caracteres y una lista es una secuencia de valores, pero una lista de caracteres no es lo mismo que una cadena. Para convertir una cadena en una lista de caracteres, puedes usar list.
La función list divide una cadena en letras individuales. Si quieres dividir una cadena en palabras, puedes utilizar el método split.
Puedes llamar split con un argumento opcional llamado delimitador que especifica qué caracteres usar para delimitar las palabras.
join es el inverso de split. Este toma una lista de cadenas y concatena los elementos. join es un método de cadenas, así que tienes que invocarlo en el delimitador y pasar la lista como un parámetro.
En este caso el delimitador es un carácter de espacio, así que join agrega un espacio entre las palabras. Para concatenar cadenas sin espacios, puedes usar la cadena vacía, "", como delimitador.

---

**Slide 67 — Analizando líneas**

Normalmente cuando estamos leyendo un archivo queremos hacer algo con las líneas que no sea solamente imprimirlas como son. Frecuentemente queremos encontrar las "líneas interesantes" y después analizar la línea para encontrar alguna "parte interesante" en la línea. ¿Qué tal si quisiéramos imprimir el día de la semana de las líneas que comienzan con "From"?

---

**Slide 68 — Objetos y valores**

Si ejecutamos ciertas sentencias de asignación, sabemos que ambos a y b se refieren a una cadena, pero no sabemos si se refieren o apuntan a la misma cadena. Hay dos estados posibles:
Por un lado, a y b se refieren a dos objetos diferentes que tienen el mismo valor.
Por otro lado, apuntan al mismo objeto.
Para revisar si dos variables apuntan al mismo objeto, puedes utilizar el operador is.

---

**Slide 69 — Referencia – Alias**

Si a se refiere a un objeto y tú asignas b = a, entonces ambas variables se refieren al mismo objeto.
La asociación de una variable a un objeto es llamada una referencia. En este ejemplo, hay dos referencias al mismo objeto. Un objeto con más de una referencia tiene más de un nombre, así que decimos que el objeto es un alias.
Si el alias del objeto es mutable, los cambios hechos a un alias afectan al otro.

---

**Slide 70 — Listas como argumentos**

Cuando pasas una lista a una función, la función obtiene un apuntador a la lista.
El parámetro t y la variable letras son alias para el mismo objeto.
Es importante distinguir entre operaciones que modifican listas y operaciones que crean nuevas listas. Por ejemplo, el método append modifica una lista, pero el operador + crea una nueva lista.

---

**Slide 71 — Ejercicios**

---

**Slide 72 — Diccionarios**

Un diccionario es como una lista, pero más general. En una lista, los índices de posiciones tienen que ser enteros; en un diccionario, los índices pueden ser (casi) cualquier tipo.
Puedes pensar en un diccionario como una asociación entre un conjunto de índices (que son llamados claves) y un conjunto de valores. Cada clave apunta a un valor.
La asociación de una clave y un valor es llamada par clave-valor o a veces elemento.
La función dict crea un nuevo diccionario sin elementos.

---

**Slide 73 — Diccionarios**

Este formato de salida es también un formato de entrada. Por ejemplo, puedes crear un nuevo diccionario con tres elementos.
Los elementos de un diccionario nunca son indexados con índices enteros. En vez de eso, utilizas las claves para encontrar los valores correspondientes.

---

**Slide 74 — Diccionarios**

La función len funciona en diccionarios; ésta regresa el número de pares clave-valor.
El operador in funciona en diccionarios; éste te dice si algo aparece como una clave en el diccionario (aparecer como valor no es suficiente).
Para ver si algo aparece como valor en un diccionario, puedes usar el método values, el cual retorna los valores como una lista, y después puedes usar el operador in.

---

**Slide 75 — Ejercicios**

---

**Slide 76 — Diccionarios – Método GET**

Los diccionarios tienen un método llamado get que toma una clave y un valor por defecto. Si la clave aparece en el diccionario, get regresa el valor correspondiente; si no, regresa el valor por defecto.

---

**Slide 77 — Bucles y diccionarios**

Si utilizas un diccionario como una secuencia para una sentencia for, ésta recorre las claves del diccionario. Este bucle imprime cada clave y su valor correspondiente.
El bucle for itera a través de las claves del diccionario, así que debemos utilizar el operador índice para obtener el valor correspondiente para cada clave.

---

**Slide 78 — Bucles y diccionarios**

Si quieres imprimir las claves en orden alfabético, primero haces una lista de las claves en el diccionario utilizando el método keys disponible en los objetos de diccionario, y después ordenas esa lista e iteras a través de la lista ordenada, buscando cada clave e imprimiendo pares clave-valor ordenados.

---

**Slide 79 — Ejercicios**

---

**Slide 80 — Tuplas**

Una tupla es una secuencia de valores similar a una lista. Los valores guardados en una tupla pueden ser de cualquier tipo, y son indexados por números enteros. La principal diferencia es que las tuplas son inmutables. Las tuplas además son comparables y dispersables (hashables) de modo que las listas de tuplas se pueden ordenar y también usar tuplas como valores para las claves en diccionarios de Python.
Sintácticamente, una tupla es una lista de valores separados por comas. Aunque no es necesario, es común encerrar las tuplas entre paréntesis para ayudarnos a identificarlas rápidamente cuando revisemos código de Python.

---

**Slide 81 — Tuplas**

Otra forma de construir una tupla es utilizando la función interna tuple. Sin argumentos, ésta crea una tupla vacía.
Si el argumento es una secuencia (cadena, lista, o tupla), el resultado de la llamada a tuple es una tupla con los elementos de la secuencia.
La mayoría de los operadores de listas también funcionan en tuplas. El operador corchete indexa un elemento.
Pero si se intenta modificar uno de los elementos de la tupla, se produce un error.

---

**Slide 82 — Comparación de tuplas**

Los operadores de comparación funcionan con tuplas y otras secuencias. Python comienza comparando el primer elemento de cada secuencia. Si ambos elementos son iguales, pasa al siguiente elemento y así sucesivamente, hasta que encuentra elementos diferentes. Los elementos subsecuentes no son considerados (aunque sean muy grandes).

---

**Slide 83 — Asignación de tuplas**

Una de las características sintácticas únicas del lenguaje Python es la capacidad de tener una tupla en el lado izquierdo de una sentencia de asignación. Esto permite asignar más de una variable a la vez cuando hay una secuencia del lado izquierdo.
En el ejemplo correspondiente, hay una lista de dos elementos (la cual es una secuencia) y se asigna el primer y segundo elementos de la secuencia a las variables x y y en una única sentencia.
Una aplicación particularmente ingeniosa de asignación con tuplas permite intercambiar los valores de dos variables en una sola sentencia.
Generalizando más, el lado derecho puede ser cualquier tipo de secuencia (cadena, lista, o tupla). Por ejemplo, para dividir una dirección de e-mail en nombre de usuario y dominio, se podría usar este patrón.

---

**Slide 84 — Diccionarios y tuplas**

Los diccionarios tienen un método llamado items que retorna una lista de tuplas, donde cada tupla es un par clave-valor.
Como sería de esperar en un diccionario, los elementos no tienen ningún orden en particular. Aun así, puesto que la lista de tuplas es una lista, y las tuplas son comparables, ahora se puede ordenar la lista de tuplas. Convertir un diccionario en una lista de tuplas es una forma de obtener el contenido de un diccionario ordenado según sus claves.

---

**Slide 85 — Asignación múltiple con diccionarios**

La combinación de items, asignación de tuplas, y for, produce un buen patrón de diseño de código para recorrer las claves y valores de un diccionario en un único bucle.

---

**Slide 86 — Uso de tuplas como claves en diccionarios**

Dado que las tuplas son dispersables (hashable) y las listas no, si se quiere crear una clave compuesta para usar en un diccionario, se debe utilizar una tupla como clave. Se usaría por ejemplo una clave compuesta si se quisiera crear un directorio telefónico que mapea pares apellido-nombre con números telefónicos. Asumiendo que se han definido las variables apellido, nombre, y número, se podría escribir una sentencia de asignación de diccionario con esa clave compuesta.

---

**Slide 87 — Secuencias: cadenas, listas, y tuplas**

En muchos contextos, los diferentes tipos de secuencias (cadenas, listas, y tuplas) pueden intercambiarse. Así que, ¿cómo y por qué elegir uno u otro?
Para comenzar con lo más obvio, las cadenas están más limitadas que otras secuencias, debido a que los elementos tienen que ser caracteres. Además, son inmutables. Si necesitas la capacidad de cambiar los caracteres en una cadena (en vez de crear una nueva), quizá prefieras utilizar una lista de caracteres.
Las listas son más comunes que las tuplas, principalmente porque son mutables. Pero hay algunos casos donde es preferible utilizar tuplas:
1. En algunos contextos, como una sentencia return, resulta sintácticamente más simple crear una tupla que una lista. En otros contextos, es posible que prefieras una lista.
2. Si quieres utilizar una secuencia como una clave en un diccionario, debes usar un tipo inmutable como una tupla o una cadena.
3. Si estás pasando una secuencia como argumento de una función, el uso de tuplas reduce la posibilidad de comportamientos inesperados debido a la creación de alias (al ser inmutable).
Dado que las tuplas son inmutables, no proporcionan métodos como sort y reverse, que modifican listas ya existentes. Sin embargo, Python proporciona las funciones internas sorted y reversed, que toman una secuencia como parámetro y devuelven una secuencia nueva con los mismos elementos en un orden diferente.

---

**Slide 88 — Ejercicios**

---

¿Querés que te arme esto en un Word o PDF para tenerlo más a mano, o lo necesitás solo en el chat por ahora?