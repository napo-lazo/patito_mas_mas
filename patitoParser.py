import patitoLexer
from patitoLexer import tokens
import ply.yacc as yacc

class VirutalDirectory(object):
    def __init__(self):
        self.globalIntsRange = [1000, 2999]
        self.globalFloatsRange = [3000, 4999]
        self.globalCharsRange = [5000, 6999]
        self.globalBoolsRange = [7000, 8999]

class QuadrupleManager(object):
    def __init__(self):
        self.virutalDirectory = VirutalDirectory()
        #Falta ver que rollo con las matrices y operaciones unarias, por el momento solo operaciones binarias, revisar comparasiones entre enteros y flotantes
        self.semanticCube = {'+':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'}, 
                             '-':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'}, 
                             '*':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'}, 
                             '/':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'},
                             '>':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '>=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '<':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '<=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '==':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool', ('char', 'char'): 'char', ('bool', 'bool'): 'bool'},
                             '!=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool', ('char', 'char'): 'char', ('bool', 'bool'): 'bool'},
                             '&&':{('bool', 'bool'): 'bool'},
                             '||':{('bool', 'bool'): 'bool'}}
        self.jumpStack = []
        self.operationStack = []
        self.typeStack = []
        self.operandStack = []
        self.quadruplesList = []

# variablesTable guarda las variables globales y de las funciones
class VariablesTable(object):

    def __init__(self):
        #variablesTable tiene el formato de {nombreScope : {returnType : valor, variables : {nombreVar1 : {type : valor, value : valor}, nombreVar2 : {type : valor, value : valor}, etc}}} 
        self.variablesTable = {}
        self.currentScope = None
        self.currentType = None
        self.currentId = None

    def createScope(self, scopeName, returnType):
        self.variablesTable[scopeName] = {'returnType': returnType, 'variables' : {}}

    def createVariable(self, variableName):
        self.variablesTable[self.currentScope]['variables'][variableName] = {'type' : self.currentType}
    
    def variableExists(self, variableName):
        return self.variablesTable[self.currentScope]['variables'][variableName]
    
    def currentVariableValue(self):
        return self.variablesTable[self.currentScope]['variables'][self.currentId]['value']
    
    def assignValueToCurrentVariable(self, value):
        self.variablesTable[self.currentScope]['variables'][self.currentId]['value'] = value

 
variablesTable = VariablesTable()


# gramatica para el parser
def p_start(p):
    '''
    start : programa
    '''
    print(p[1])
    print()
    print(variablesTable.variablesTable)
    print()

# el programa termina con una token de EOF para saber poder reportar errores de brackets faltantes
def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON var funcion PRINCIPAL L_PARENTHESIS R_PARENTHESIS bloque EOF
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_variables(p):
    '''
    var : VAR var_seen varp
        | empty
    '''
    if len(p) != 2: 
        p[0] = (p[1], p[3])
        
        # borra el scope actual porque aqui ya se termina el procesamiento de las variables globales 
        variablesTable.currentScope = None
        
    else:
        p[0] = p[1]

# regla intermedia para asignar el scope actual como global
def p_var_seen(p):
    '''
    var_seen :
    '''
    variablesTable.createScope('global', 'void')
    variablesTable.currentScope = 'global'

def p_variablesp(p):
    '''
    varp : tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp
    '''
    p[0] = (p[1], p[3], p[4], p[6], p[7], p[9], p[10])

# regla intermedia para asignar el tipo actual de las variables que se estan declarando
def p_tipo_seen(p):
    '''
    tipo_seen :
    '''
    variablesTable.currentType = p[-1]

# regla intermedia para crear una variable del tipo actual en la tabla de variables del scope actual
def p_variable_seen(p):
    '''
    variable_seen : 
                  | error error 
    '''
    # primero se revisa si ya hay una variable con ese nombre
    try:
        variablesTable.variableExists(p[-1])

    # si no la hay se crea una de manera normal
    except:
        variablesTable.createVariable(p[-1])

    # de lo contrario se tira un error de variable duplicada
    else:
        print(f'ERROR: Variable {p[-1]} already exists')
        raise SyntaxError

    variablesTable.currentId = p[-1]

# regla intermedia que solo se encarga de eliminar el tipo actual
def p_delete_type(p):
    '''
    delete_type :
    '''
    variablesTable.currentType = None

def p_variablespp(p):
    '''
    varpp : COMMA ID variable_seen varppp varpp
          | empty
    '''
    if len(p) != 2:
        p[0] = (p[1], p[2], p[4], p[5])
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

    # despues de declarar las dimensiones se elimina el id actual
    variablesTable.currentId = None
    

def p_variablespppp(p):
    '''
    varpppp : varp
            | empty
    '''
    p[0] = p[1]


def p_dimDeclare(p):
    '''
    dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET
               | L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET error error  
    '''
    # revisa que el tama;o de las dimensiones sea mayor o igual a 1 de lo contrario tira un error
    if(p[2] <= 0):
        print('ERROR: Array size cant be less than 1')
        raise SyntaxError
    else:
        p[0] = (p[1], p[2], p[3])
    
    # revisa si ya hay un valor asignado a la variable
    try: 
        variablesTable.currentVariableValue()

    # si no lo hay entonces crea una lista llena de Nones del taman;o declarado
    except:
        variablesTable.assignValueToCurrentVariable([None] * int(p[2]))

    # de lo contrario itera cada elemento de la lista y lo reemplaza por una lista llena de Nones del tama;o asignado
    else:
        tempList = []

        for cell in variablesTable.currentVariableValue():
            tempList.append([None] * int(p[2]))

        # lo asigna como una copia, de lo contrario todas las listas estarian apuntando al mismo espacio de memoria ocasionando que al cambiar una se cambien todas
        variablesTable.assignValueToCurrentVariable(tempList.copy())

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
    llamadaFuncion : ID L_PARENTHESIS expresion llamadaFuncionp R_PARENTHESIS
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_llamadaFuncionp(p):
    '''
    llamadaFuncionp : COMMA expresion
                    | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else: 
        p[0] = p[1]

def p_funcionVacia(p):
    '''
    funcionVacia : ID L_PARENTHESIS expresion llamadaFuncionp R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])

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
    cicloNoCondicional : DESDE ID dimId ASSIGN expresion HASTA expresion HACER bloque EOF
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_empty(p):
    '''
    empty :
    '''
    pass

# si el tipo de la token reportada es de EOF entonces el error es de un bracket faltante
# de lo contrario solo se reporta un error generico 
# en ambos casos se reporta en que linea se encuentra el error
def p_error(p):

    if p.type == 'EOF':
        print(f'EOF inesperado en linea {p.lexer.lineno}')
        return
    if p != None:
        print(f"ERROR de sintaxis en linea {p.lexer.lineno}")
    else:
        print(p)
        print("ERROR de sintaxis")
        return 
    parser.restart()

parser = yacc.yacc()