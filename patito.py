import ply.lex as lex

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
    'lectura' : 'LECTURA',
    'escribe' : 'ESCRIBE',
    'si' : 'SI',
    'haz' : 'HAZ',
    'sino' : 'SINO',
    'mientras' : 'MIENTRAS',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'hacer' : 'HACER'
}

tokens = [
    'ID',
    'SEMICOLON', 
    'COLON',
    'L_SQUARE_BRACKET',
    'R_SQUARE_BRACKET',
    'CTE_INT',
    'COMMA',
    'LPARENTHESIS',
    'RPARENTHESIS',
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
    'LETRERO'
] + list(reserved.values())

def t_CTE_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'[0-9]+'
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
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
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

t_ignore = r' '

def t_error(t):
    print('Illegal characters')
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(input())

while True:
    tok = lexer.token()

    if not tok:
        break
    
    print(tok)