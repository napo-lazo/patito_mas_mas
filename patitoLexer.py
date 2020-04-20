import ply.lex as lex

# La clase ProxyLexer recibe la instancia del lexer original y una token de tipo EOF
# La clase no aporta nada extra a la funcionalidad original del lexer, solo se encarga de agregar
# una token de EOF al final de la lectura de tokens 
class ProxyLexer(object):
    def __init__(self, originalLexer, EOF):
        self.lexer = originalLexer
        self.eof = EOF
        self.end = False

    def token(self):
        tok = self.lexer.token()
        # print(tok)
        if tok is None:
            if self.end:
                self.end = False
            else:
                self.end = True
                tok = lex.LexToken()
                tok.type = self.eof
                tok.value = None
                tok.lexpos = self.lexer.lexpos
                tok.lineno = self.lexer.lineno
        return tok
    
    def __getattr__(self, name):
            return getattr(self.lexer, name)


# diccionario de palabras reservadas
reserved = {
    'programa' : 'PROGRAMA',
    'var' : 'VAR',
    'char' : 'CHAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'funcion' : 'FUNCION',
    'void' : 'VOID',
    'principal' : 'PRINCIPAL',
    'regresa' : 'REGRESA',
    'lee' : 'LECTURA',
    'escribe' : 'ESCRIBE',
    'si' : 'SI',
    'haz' : 'HAZ',
    'sino' : 'SINO',
    'mientras' : 'MIENTRAS',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'hacer' : 'HACER'
}

# lista de los tipos de tokens
tokens = [
    'ID',
    'SEMICOLON', 
    'COLON',
    'L_SQUARE_BRACKET',
    'R_SQUARE_BRACKET',
    'CTE_INT',
    'COMMA',
    'L_PARENTHESIS',
    'R_PARENTHESIS',
    'L_CURLY_BRACKET',
    'R_CURLY_BRACKET',
    'ASSIGN',
    'NOT',
    'AND',
    'OR',
    'EQUALS',
    'NOT_EQUAL',
    'LESS_THAN',
    'LESS_THAN_EQUAL',
    'GREATER_THAN',
    'GREATER_THAN_EQUAL',
    'SUM',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'DETERMINANT',
    'TRANSPOSED',
    'INVERSE',
    'CTE_FLOAT',
    'CTE_CHAR',
    'LETRERO',
    'EOF'
] + list(reserved.values())

# expresiones regulares para asignar el tipo de token al input recibido
def t_CTE_FLOAT(t):
    r'\-?[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'\-?[0-9]+'
    t.value = int(t.value)
    return t

def t_CTE_CHAR(t):
    r'\'.\''
    t.value = t.value[1]
    return t

def t_LETRERO(t):
    r'\".+\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[A-Za-z][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_L_SQUARE_BRACKET = r'\['
t_R_SQUARE_BRACKET = r'\]'
t_COMMA = r'\,'
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_L_CURLY_BRACKET = r'\{'
t_R_CURLY_BRACKET = r'\}'
t_ASSIGN = r'\='
t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQUALS = r'\=\='
t_NOT_EQUAL = r'\!\='
t_LESS_THAN = r'\<'
t_LESS_THAN_EQUAL = r'\<\='
t_GREATER_THAN = r'\>'
t_GREATER_THAN_EQUAL = r'\>\='
t_SUM = r'\+'
t_SUBTRACT = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_DETERMINANT = r'\$'
t_TRANSPOSED = r'\¡'
t_INVERSE = r'\?'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print('Illegal characters')
    t.lexer.skip(1)

# se instancia un lexer
originalLexer = lex.lex()

# despues este lexer es pasado a la clase ProxyLexer y se guarda como un lexer nuevo
lexer = ProxyLexer(originalLexer, 'EOF')

# Loop to view all the tokens created by a user input

# lexer.input(input())

# while True:
#     tok = lexer.token()

#     if not tok:
#         break
    
#     print(tok)