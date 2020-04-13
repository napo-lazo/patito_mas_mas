import ply.lex as lex
import ply.yacc as yacc

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
    'LETRERO'
] + list(reserved.values())

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

t_ignore = r' '

def t_error(t):
    print('Illegal characters')
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    '''
    start : programa
    '''
    print(p[1])

def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON var funcion PRINCIPAL L_PARENTHESIS R_PARENTHESIS bloque
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_variables(p):
    '''
    var : VAR varp
        | empty
    '''
    if len(p) == 3: 
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_variablesp(p):
    '''
    varp : tipo COLON ID varppp varpp SEMICOLON varpppp
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_variablespp(p):
    '''
    varpp : COMMA ID varppp varpp
          | empty
    '''
    if len(p) == 5:
        p[0] = (p[1], p[2], p[3], p[4])
    else:
        p[0] = p[1]

def p_variablesppp(p):
    '''
    varppp : dimDeclare
           | dimDeclare dimDeclare
           | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_variablespppp(p):
    '''
    varpppp : varp
            | empty
    '''
    p[0] = p[1]

def p_dimDeclare(p):
    '''
    dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET
    '''
    if(p[2] <= 0):
        print('ERROR: Array size cant be less than 1')
        raise SyntaxError
    else:
        p[0] = (p[1], p[2], p[3])

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
    '''
    p[0] = p[1]

def p_funcion(p):
    '''
    funcion : FUNCION funcionp
            | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_funcionp(p):
    '''
    funcionp : tipoRetorno ID L_PARENTHESIS parametro R_PARENTHESIS var bloque funcion
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_parametro(p):
    '''
    parametro : tipo ID parametrop
              | empty
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else: 
        p[0] = p[1]

def p_parametrop(p):
    '''
    parametrop : COMMA tipo ID parametrop
               | empty
    '''
    if len(p) == 5:
        p[0] = (p[1], p[2], p[3], p[4])
    else:
        p[0] = p[1]

def p_tipoRetorno(p):
    '''
    tipoRetorno : tipo
                | VOID
    '''
    p[0] = p[1]

#agregar recursividad
def p_bloque(p):
    '''
    bloque : L_CURLY_BRACKET bloquep R_CURLY_BRACKET
    '''
    p[0] = (p[1], p[2], p[3])

def p_bloquep(p):
    '''
    bloquep : estatuto bloquep
            | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_estatuto(p):
    '''
    estatuto : asignacion
             | funcionVacia
             | regresa
             | lectura
             | escritura
             | decision
             | cicloCondicional
             | cicloNoCondicional
    '''
    p[0] = p[1]

def p_asignacion(p):
    '''
    asignacion : ID dimId ASSIGN expresion SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_dimId(p):
    '''
    dimId : dim
                | dim dim
                | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_dim(p):
    '''
    dim : L_SQUARE_BRACKET expresion R_SQUARE_BRACKET
    '''
    p[0] = (p[1], p[2], p[3])

def p_expresion(p):
    '''
    expresion : relacional expresionp
              | NOT relacional expresionp
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = (p[1], p[2])

def p_expresionp(p):
    '''
    expresionp : AND expresion
               | OR expresion
               | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_relacional(p):
    '''
    relacional : aritmetica relacionalp
    '''
    p[0] = (p[1], p[2])

def p_relacionalp(p):
    '''
    relacionalp : EQUALS relacional
                | NOT_EQUAL relacional
                | LESS_THAN relacional
                | LESS_THAN_EQUAL relacional
                | GREATER_THAN relacional
                | GREATER_THAN_EQUAL relacional
                | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_aritmetica(p):
    '''
    aritmetica : factor aritmeticap
    '''
    p[0] = (p[1], p[2])

def p_aritmeticap(p):
    '''
    aritmeticap : SUM aritmetica
                | SUBTRACT aritmetica
                | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_factor(p):
    '''
    factor : matriz factorp
    '''
    p[0] = (p[1], p[2])

def p_factorp(p):
    '''
    factorp : MULTIPLY factor
            | DIVIDE factor
            | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_matriz(p):
    '''
    matriz : cte matrizp
    '''
    p[0] = (p[1], p[2])

def p_matrizp(p):
    '''
    matrizp : DETERMINANT
            | TRANSPOSED
            | INVERSE
            | empty
    '''
    p[0] = p[1]

def p_cte(p): 
    '''
    cte : CTE_INT
        | CTE_FLOAT
        | CTE_CHAR
        | llamadaFuncion
        | ID dimId
        | L_PARENTHESIS expresion R_PARENTHESIS
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_llamadaFuncion(p):
    '''
    llamadaFuncion : ID L_PARENTHESIS parametro R_PARENTHESIS
    '''
    p[0] = (p[1], p[2], p[3], p[4])

def p_funcionVacia(p):
    '''
    funcionVacia : ID L_PARENTHESIS parametro R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_regresa(p):
    '''
    regresa : REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_lectura(p):
    '''
    lectura : LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_lecturap(p):
    '''
    lecturap : ID dimId lecturapp
    '''
    p[0] = (p[1], p[2], p[3])

def p_lecturapp(p):
    '''
    lecturapp : COMMA lecturap
              | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_escritura(p):
    '''
    escritura : ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_escriturap(p):
    '''
    escriturap : LETRERO escriturapp
               | expresion escriturapp
    '''
    p[0] = (p[1], p[2])

def p_escriturapp(p):
    '''
    escriturapp : COMMA escriturap
                | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_decision(p):
    '''
    decision : SI L_PARENTHESIS expresion R_PARENTHESIS HAZ bloque decisionp
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_decisionp(p):
    '''
    decisionp : SINO bloque
              | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_cicloCondicional(p):
    '''
    cicloCondicional : MIENTRAS L_PARENTHESIS expresion R_PARENTHESIS HAZ bloque
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])

def p_cicloNoCondicional(p):
    '''
    cicloNoCondicional : DESDE ID dimId ASSIGN expresion HASTA expresion HACER bloque
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    print("ERROR de sintaxis")

parser = yacc.yacc()

# Loop to view all the tokens created by a user input

# lexer.input(input())

# while True:
#     tok = lexer.token()

#     if not tok:
#         break
    
#     print(tok)


# use ctrl c to break out of the loop
while True:
    try:
        s = input()
    except EOFError:
        break

    parser.parse(s)