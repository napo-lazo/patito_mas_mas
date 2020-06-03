# Compilador patito++

Este es el proyecto final de la clase de compiladores desarrollado por José Napoleón Lazo Celaya y Katia Carolina Tarín Contreras

# Caracteristicas
El lenguaje patito++ y el compilador es capaz de: 
    1. Interpretar expresiones aritméticas y relacionales
    2. Interpretar estatutos de input y output
    3. Manejar ciclos y condicionales
    4. Manejar cambio de contexto (Saltos, parametros, funciones)
    5. Manejar arreglos
    6. Manejar matrices, incluyendo operaciones de matrices y operadores especiales para sacar la determinante, inversa y traspuesta 

Las siguientes son las palabras reservadas del lenguaje:
Estructura: programa, principal, función, regresa, void
Variables: var, int, float, char
Lectura/Escritura: lee, escribe
Condicionales: si, entonces, sino
Ciclos: mientras, haz, desde, hasta, hacer

Ademas utilizamos los operadores:
'+' para sumar
'-' para restar
'*' para multiplicar
'/' para dividir
'=' para igualar
'&' AND
'|' OR
'<' lesser than
'>' greater than
'==' equal to
'?' inversa de una matriz
'$' determinante de una matriz
'¡' traspuesta de una matriz

# Sintaxis para operaciones basicas
- Decalaracion variables: Var int: a, b, c; float: d;
- Condicionales: si (<expresion>) haz { estatutos }
- Ciclo condicional: mientras (<expresion>) haz { estatutos }
- Ciclo no condicional: desde n = 0 hasta <expresion> hacer { estatutos } // esta operacion siempre es incremental entonces si el limite superior es inicialmente menor se ciclara
- Declaracion funcion: funcion void nombreFunc() <declaracion variables> { estatutos } 

# Como utilizar este compilador:

El compilador puede compilar código patito++ por archivo o consola. Para compilar un archivo asegúrese que se encuentre en el mismo directorio que los archivos del compilador.

Ejecute el archivo patito.py con el nombre del archivo de código que se quiere compilar como parámetro. 

# Estructura del compilador
La estructura del compilador está dividida en partes para mantener el proyecto ordenado.
- patito.py es el archivo que se manda a compilar. Recibe y compila un archivo texto en patito++ o compila desde consola
- patitoLexer.py es el analizador de lexico, contiene las expresiones regulares
- patitoParser.py contiene las reglas de gramatica, el cubo semántico, el generador de cuadruplos y el directorio de memoria
- virtualMachine.py como su nombre lo indica es la máquina virtual que ejecuta los cuádruplos  
- parserClasses.py contiene las definiciones de todas las clases necesarias que se necesitan en patitoParser.py como la tabla de variables, la memoria y directorio de funciones
- patitoLogger.py es un pequeño programa que guarda en un archivo prints e informacion necesaria para debuggear
