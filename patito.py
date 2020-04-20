from patitoLexer import lexer
from patitoParser import parser
import sys

# si se pasa el nombre de un archivo al correr el script, se compila ese archivo
if(len(sys.argv) == 2):
    try:
        with open(sys.argv[1]) as inputFile:
            s = ''
            for line in inputFile:
                s += line
            
            # se pasa el lexer nuevo al parser para poder hacer uso de la token EOF
            parser.parse(s, lexer=lexer)
    except:
        print(f"el archivo {sys.argv[1]} no existe")

# de lo contrario solo se compila lo que se escriba en la terminal
else:
    # use ctrl c to break out of the loop
    while True:
        try:
            s = input()
        except EOFError:
            break

        parser.parse(s, lexer=lexer)