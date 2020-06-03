import patitoLexer
from parserClasses import FunctionDirectory, QuadrupleManager
from patitoLexer import tokens
import ply.yacc as yacc
from virutalMachine import VirtualMachine
from sys import exit

funcDir = FunctionDirectory()
quadrupleManager = QuadrupleManager()

# Gramatica para el parser

def p_start(p):
    '''
    start : programa
    '''
    #inicializa una maquina virtual con los valores obtenidos del compilador
    myMachine = VirtualMachine(quadrupleManager.exportData(), funcDir.turnCtesIntoList(), funcDir.eras)

    myMachine.executeProgram()


    #limpia toda la informacion para poder volver a compilar sin problemas
    quadrupleManager.clearData()

# Definicion de programa
# El programa termina con una token de EOF para saber poder reportar errores de brackets faltantes
def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON jump var funcion clear_scope PRINCIPAL update_jump L_PARENTHESIS R_PARENTHESIS bloque EOF
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

# Crea un salto
def p_jump(p):
    '''
    jump :
    '''
    quadrupleManager.generateJump('jump')

# Elimina un scope
def p_clear_scope(p):
    '''
    clear_scope :
    '''
    temp = funcDir.currentScope
    funcDir.currentScope = None
    del(temp)

# Regla de variables
def p_variables(p):
    '''
    var : VAR var_seen varp
        | empty
    '''
    if len(p) != 2: 
        p[0] = (p[1], p[3])
        
    else:
        p[0] = p[1]

# Regla intermedia para asignar el scope actual como global
def p_var_seen(p):
    ''' 
    var_seen :
    '''
    if funcDir.currentScope is None:
        funcDir.createScope('global', 'void')
        funcDir.currentScope = 'global'

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
    funcDir.currentType = p[-1]

# regla intermedia para crear una variable del tipo actual en la tabla de variables del scope actual
def p_variable_seen(p):
    '''
    variable_seen : 
    '''
    try:
        funcDir.variableExists(p[-1])

    # si no la hay se crea una de manera normal
    except:
        funcDir.createVariable(p[-1], quadrupleManager.virutalDirectory.generateAddressForVariable(funcDir.currentScope, funcDir.currentType))

    # de lo contrario se tira un error de variable duplicada
    else:
        print(f'ERROR: Variable "{p[-1]}" ya existe en el scope {funcDir.currentScope}')
        exit()

    funcDir.currentId = p[-1]

# regla intermedia que solo se encarga de eliminar el tipo actual
def p_delete_type(p):
    '''
    delete_type :
    '''
    temp = funcDir.currentType
    funcDir.currentType = None   
    del(temp)

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

    # despues de declarar las dimensiones y actualizar el contador de memoria virtual se elimina el id actual
    temp = funcDir.currentId
    if funcDir.isVariableArray():
        quadrupleManager.virutalDirectory.setSpaceForArray(funcDir.currentScope, funcDir.currentType, funcDir.getArrayDimensionsSize() - 1)
    funcDir.currentId = None
    del(temp)
    

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
        exit()
    else:
        p[0] = (p[1], p[2], p[3])
    
    if not funcDir.isVariableArray():
        funcDir.setVariableAsArray()
           
    funcDir.addArrayDimensionSize(p[2])

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
    funcionp : tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque end_func funcion
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])


# Agrega una funcion al directorio de funciones
def p_create_func_scope(p):
    '''
    create_func_scope : 
    '''
    if p[-1] == 'global':
        print('Error: global es una palabra reservada')
        exit()
    try:
        funcDir.scopeExists(p[-1])
    except:

        try:
            funcDir.variableExists(p[-1])
        except:
            pass
        else:
            print(f'Ya existe una variable que se llama {p[-1]}')
            exit()

        if p[-2] != 'void':
            funcDir.currentType = p[-2]
            try:
                funcDir.scopeExists('global')
            except:
                funcDir.createScope('global', 'void')
                funcDir.createVariable(p[-1], quadrupleManager.virutalDirectory.generateAddressForVariable('global', p[-2]))
            else:
                funcDir.createVariable(p[-1], quadrupleManager.virutalDirectory.generateAddressForVariable('global', p[-2]))
            funcDir.currentType = None
        
        funcDir.createScope(p[-1], p[-2])
        funcDir.currentScope = p[-1]
        funcDir.addFunctionStart(quadrupleManager)
    else:
        print(f'Error: {p[-1]} ya existe')
        exit()

# Borra las temporales y acaba la funcion 
def p_end_func(p):
    '''
    end_func :
    '''
    if funcDir.callFromReturn == 0 and not funcDir.isVoid(funcDir.currentScope):
        print(f'La funcion {funcDir.currentScope} necesita un estatuto de retorno')
        exit()
    funcDir.callFromReturn = 0
    funcDir.createEra(quadrupleManager.virutalDirectory)
    quadrupleManager.virutalDirectory.resetLocalAddresses()
    quadrupleManager.generateEndFunc()
    funcDir.currentScope = None

def p_parametro(p):
    '''
    parametro : tipo ID save_param parametrop
              | empty
    '''
    if len(p) == 5:
        p[0] = (p[1], p[2], p[4])
    else: 
        p[0] = p[1]

def p_save_param(p):
    '''
    save_param :
    '''
    funcDir.addParameterToList(p[-1], p[-2], quadrupleManager.virutalDirectory.generateAddressForVariable(p[-1], p[-2]))

def p_parametrop(p):
    '''
    parametrop : COMMA tipo ID save_param parametrop
               | empty
    '''
    if len(p) == 6:
        p[0] = (p[1], p[2], p[3], p[5])
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
    asignacion : ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

# Agrega un operando al stack, verifica si este ya esta declarado
def p_operand_seen(p):
    '''
    operand_seen :
    '''
    funcDir.currentId = p[-1]
    quadrupleManager.operandStack.append(funcDir.getVirtualAddressOfVariable(p[-1]))
    try:
        quadrupleManager.typeStack.append(funcDir.getTypeOfVariable(p[-1]))
    except:
        print(f'ERROR: la variable {p[-1]} no ha sido declarada')
        exit()

def p_dimId(p):
    '''
    dimId : is_array create_dim dim pop_array
          | is_array create_dim dim dim pop_array
          | empty
    '''
   
    if len(p) == 2 and funcDir.isVariableArray():
        if len(funcDir.getArrayDimensions(funcDir.currentId)) == 1:
            print(f'La variable "{funcDir.currentId}" necesita ser indexada')
            exit()
        quadrupleManager.matDimStack.append((funcDir.currentId, funcDir.getVirtualAddressOfVariable(funcDir.currentId), funcDir.getArrayDimensions(funcDir.currentId)))
    funcDir.currentId = None

def p_pop_array(p):
    '''
    pop_array :
    '''
    if len(quadrupleManager.dimStack[-1][1]) != 0:
        print('Error: falto un indice para acceder al valor de la matriz')
        exit()
    quadrupleManager.dimStack.pop()

def p_is_array(p):
    '''
    is_array :  
    '''
    if not funcDir.constantVirtualAddressExists(quadrupleManager.operandStack[-1]):
        funcDir.addCteVirtualAddress(quadrupleManager.operandStack[-1], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
    quadrupleManager.matTypeStack.append(quadrupleManager.typeStack[-1])
    quadrupleManager.typeStack[-1] = 'int'

    if not funcDir.isVariableArray():
        print(f'Error: variable "{funcDir.currentId}" no es un arreglo')
        exit()

def p_dim(p):
    '''
    dim : L_SQUARE_BRACKET bracket_seen expresion R_SQUARE_BRACKET bracket_seen
    '''
    p[0] = (p[1], p[2], p[3])

def p_create_dim(p):
    '''
    create_dim :
    '''
    dim = funcDir.getArrayDimensions(funcDir.currentId)
    quadrupleManager.dimStack.append((funcDir.currentId, dim, len(dim)))

# Genera todo los cuadruplos de arreglos
def p_bracket_seen(p):
    '''
    bracket_seen :
    '''
    if p[-1] == ']':
        dim = quadrupleManager.dimStack[-1][1][0]

        if not funcDir.constantExists(dim):
            funcDir.addConstant(dim, quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
        
        quadrupleManager.quadruplesList.append(('VERIFY', quadrupleManager.operandStack[-1], -1, funcDir.getVirtualAddressOfVariable(dim)))
        quadrupleManager.quadrupleCounter += 1
        if len(quadrupleManager.dimStack[-1][1]) > 1:
            if quadrupleManager.typeStack[-1] != 'int':
                print('Error: solo se puede indexar un arreglo con valores enteros')
                exit()
            if not funcDir.constantExists(quadrupleManager.dimStack[-1][1][-1]):
                funcDir.addConstant(quadrupleManager.dimStack[-1][1][-1], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
            quadrupleManager.operandStack.append(quadrupleManager.dimStack[-1][1][-1])
            quadrupleManager.dimStack[-1][1].pop(0)
            quadrupleManager.typeStack.append('int')
            quadrupleManager.operationStack.append('*')
            quadrupleManager.applyOperation(['*'], funcDir)
        else:
            if quadrupleManager.typeStack[-1] != 'int':
                print('Error: solo se puede indexar un arreglo con valores enteros')
                exit()
            if len(quadrupleManager.dimStack[-1][1]) != quadrupleManager.dimStack[-1][2]:
                quadrupleManager.operationStack.append('+')
                quadrupleManager.applyOperation(['+'], funcDir)

            if not funcDir.constantVirtualAddressExists(quadrupleManager.operandStack[-2]):
                funcDir.addCteVirtualAddress(quadrupleManager.operandStack[-2], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')

            quadrupleManager.operationStack.append('+')
            quadrupleManager.applyOperation(['+'], funcDir)
            pointerAddress = quadrupleManager.virutalDirectory.generateAddressForVariable('pointer', 'int')
            aux = quadrupleManager.quadruplesList.pop()
            quadrupleManager.quadruplesList.append((aux[0], funcDir.getCteVirtualAddress(aux[1]), aux[2], pointerAddress))
            quadrupleManager.operandStack.pop()
            quadrupleManager.operandStack.append(pointerAddress)
            quadrupleManager.typeStack[-1] = quadrupleManager.matTypeStack.pop()
            quadrupleManager.dimStack[-1][1].pop()

        quadrupleManager.operationStack.pop()
    else:
        quadrupleManager.operationStack.append('(')

# regla intermedia que se encarga de realizar los quadruplos de operiones logicas
def p_apply_operation_assign(p):
    '''
    apply_operation_assign : 
    '''
    quadrupleManager.applyOperation(['='], funcDir)


# falta ver que rollo con el not
def p_expresion(p):
    '''
    expresion : relacional apply_operation_expresion expresionp
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = (p[1], p[2])

def p_expresionp(p):
    '''
    expresionp : AND operation_seen expresion
               | OR operation_seen expresion
               | empty
    '''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

# regla intermedia que se encarga de realizar los quadruplos de operiones logicas
def p_apply_operation_expresion(p):
    '''
    apply_operation_expresion : 
    '''
    try:
        quadrupleManager.applyOperation(['||', '&&'], funcDir)
    except:
        exit()

def p_relacional(p):
    '''
    relacional : aritmetica apply_operation_relational relacionalp
    '''
    p[0] = (p[1], p[3])

def p_relacionalp(p):
    '''
    relacionalp : EQUALS operation_seen relacional
                | NOT_EQUAL operation_seen relacional
                | LESS_THAN operation_seen relacional
                | LESS_THAN_EQUAL operation_seen relacional
                | GREATER_THAN operation_seen relacional
                | GREATER_THAN_EQUAL operation_seen relacional
                | empty
    '''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

# regla intermedia que se encarga de realizar los quadruplos de operiones relacionales
def p_apply_operation_relational(p):
    '''
    apply_operation_relational : 
    '''
    try:
        quadrupleManager.applyOperation(['>', '>=', '<', '<=', '==', '!='], funcDir)
    except:
        exit()

def p_aritmetica(p):
    '''
    aritmetica : factor apply_operation_aritmetica aritmeticap
    '''
    p[0] = (p[1], p[2])

def p_aritmeticap(p):
    '''
    aritmeticap : SUM operation_seen aritmetica
                | SUBTRACT operation_seen aritmetica
                | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

# regla intermedia que se encarga de realizar los quadruplos de operiones aritemticas
def p_apply_operation_aritmetica(p):
    '''
    apply_operation_aritmetica : 
    '''
    try:
        quadrupleManager.applyOperation(['+', '-'], funcDir)
    except:
        exit()

def p_factor(p):
    '''
    factor : matriz apply_operation_factor factorp
    '''
    p[0] = (p[1], p[3])

def p_factorp(p):
    '''
    factorp : MULTIPLY operation_seen factor 
            | DIVIDE operation_seen factor 
            | empty
    '''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

# regla intermedia que se encarga de realizar los quadruplos de multiplicar y dividir
def p_apply_operation_factor(p):
    '''
    apply_operation_factor : 
    '''
    try:
        quadrupleManager.applyOperation(['*', '/'], funcDir)
    except:
        exit()

# regla intermedia que se encarga de agregar el operador a la pila de operadores
def p_operation_seen(p):
    '''
    operation_seen : 
    '''
    if p[-1] == ')':
        quadrupleManager.operationStack.pop()
    else:
        quadrupleManager.operationStack.append(p[-1])


def p_matriz(p):
    '''
    matriz : cte matrizp 
           | NOT operation_seen cte apply_not 
    '''
    p[0] = (p[1], p[2])

def p_apply_not(p):
    '''
    apply_not :
    '''
    quadrupleManager.applyUnary(['!'], funcDir)

def p_matrizp(p):
    '''
    matrizp : DETERMINANT operation_seen apply_mat
            | TRANSPOSED operation_seen apply_mat
            | INVERSE operation_seen apply_mat
            | empty
    '''
    p[0] = p[1]

def p_apply_mat(p):
    '''
    apply_mat :
    '''
    quadrupleManager.applyUnary(['?', '¡', '$'], funcDir)

def p_cte(p): 
    '''
    cte : CTE_INT
        | CTE_FLOAT
        | CTE_CHAR
        | llamadaFuncion
        | ID operand_seen dimId
        | L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen
    '''
    if len(p) == 6:
        p[0] = (p[1], p[3], p[4])

    # Para cuando se recibe una variable
    elif len(p) == 4:
        p[0] = (p[1], p[3])
 
    elif not type(p[1]) is float and not type(p[1]) is int and not type(p[1]) is str:
        pass
    else:
        if type(p[1]) is int:
            if not funcDir.constantExists(p[1]):
                funcDir.addConstant(p[1], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
            quadrupleManager.typeStack.append('int')
        elif type(p[1]) is float:
            if not funcDir.constantExists(p[1]):
                funcDir.addConstant(p[1], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'float') ,'float')
            quadrupleManager.typeStack.append('float')
        else:
            if not funcDir.constantExists(p[1]):
                funcDir.addConstant(p[1], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'char') ,'char')
            quadrupleManager.typeStack.append('char')
        
        quadrupleManager.operandStack.append(funcDir.getVirtualAddressOfVariable(p[1]))

        p[0] = p[1]

# Indica una llamada a una funcion, agrega los cuadruplos del ERA, GOSUB y RETURN
def p_llamadaFuncion(p):
    '''
    llamadaFuncion : ID set_func_scope L_PARENTHESIS operation_seen llamadaFuncionp R_PARENTHESIS operation_seen
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

    if not funcDir.isVoid(funcDir.functionCalled):
        quadrupleManager.generateERA(funcDir)
        quadrupleManager.generateGoSub(funcDir.functionCalled, funcDir)
        quadrupleManager.generateReturnAssignment(funcDir)
        funcDir.functionCalled = None
        funcDir.parameterCounter = 0
    else:
        print('Error: no se puede llamar una funcion con tipo de retorno void en una expresion')
        exit()

def p_llamadaFuncionp(p):
    '''
    llamadaFuncionp : expresion verify_parameter llamadaFuncionpp
                    | empty
    '''
    if len(p) == 3:
        p[0] = p[1]
    else: 
        p[0] = p[1]
    

def p_llamadaFuncionpp(p):
    '''
    llamadaFuncionpp : COMMA llamadaFuncionp
                    | empty
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2])
    else: 
        p[0] = p[1]

# Verifica si los parametros son los debidos en tipos y cuenta de parametros
def p_verify_parameter(p):
    '''
    verify_parameter :
    '''
    funcDir.verifyParameter(quadrupleManager)

def p_funcionVacia(p):
    '''
    funcionVacia : ID set_func_scope L_PARENTHESIS llamadaFuncionp R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[3], p[4], p[5], p[6])
    if funcDir.isVoid(funcDir.functionCalled):
        quadrupleManager.generateERA(funcDir)
        quadrupleManager.generateGoSub(funcDir.functionCalled, funcDir)
        funcDir.functionCalled = None
        funcDir.parameterCounter = 0
    else:
        print('Error: no se puede llamar una funcion con tipo de retorno diferente a void afuera de una expresion')
        exit()

def p_set_func_scope(p):
    '''
    set_func_scope :
    '''
    try: 
        funcDir.scopeExists(p[-1])
    except:
        print(f'Error: funcion {p[-1]} no existe')
        exit()
    else:
        funcDir.functionCalled = p[-1]



def p_regresa(p):
    '''
    regresa : REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])
    funcDir.callFromReturn += 1
    funcDir.verifyFunctionCompatibility(quadrupleManager)
    quadrupleManager.generateReturn(funcDir.callFromReturn, funcDir)
    

def p_lectura(p):
    '''
    lectura : LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_lecturap(p):
    '''
    lecturap : ID operand_seen dimId gen_input lecturapp
    '''
    p[0] = (p[1], p[2], p[3])

def p_gen_input(p):
    '''
    gen_input :
    '''
    funcDir.currentId = p[-2]
    if funcDir.isVariableArray():
        print('Lee no es compatible con matrices')
        exit()

    quadrupleManager.generateInput(p[-2], funcDir)
    funcDir.currentId = None

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
    escriturap : LETRERO gen_print escriturapp
               | expresion gen_print escriturapp
    '''
    p[0] = (p[1], p[2])

def p_gen_print(p):
    '''
    gen_print :
    '''
    if type(p[-1]) is str :
        quadrupleManager.generatePrint(p[-1])
    else:
        quadrupleManager.generatePrint(False)

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
    decision : SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[6], p[7], p[8])

def p_jump_false(p):
    '''
    jump_false : 
    '''
    quadrupleManager.generateJump('false')

def p_update_jump(p):
    '''
    update_jump :
    '''
    quadrupleManager.updateJump('normal')

def p_decisionp(p):
    '''
    decisionp : SINO jump_else bloque update_jump
              | empty update_jump
    '''
    if len(p) == 5:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_jump_else(p):
    '''
    jump_else :
    '''
    quadrupleManager.generateJump('jump_else')

def p_cicloCondicional(p):
    '''
    cicloCondicional : MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle
    '''
    p[0] = (p[1], p[3], p[4], p[5], p[7], p[8])

def p_jump_cycle(p):
    '''
    jump_cycle : 
    '''
    quadrupleManager.generateJump('jump_cycle')

def p_update_jump_cycle(p):
    '''
    update_jump_cycle : 
    '''
    quadrupleManager.updateJump('cycle')

def p_cicloNoCondicional(p):
    '''
    cicloNoCondicional : DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_add_gt(p):
    '''
    add_gt :
    '''
    quadrupleManager.typeStack.append(quadrupleManager.typeStack[-1])
    quadrupleManager.typeStack.append(quadrupleManager.typeStack[-1])
    quadrupleManager.operandStack.append(p[-10])
    quadrupleManager.typeStack.append(funcDir.getTypeOfVariable(p[-10]))
    quadrupleManager.operationStack.append('>')

def p_add_one(p):
    '''
    add_one : 
    '''
    aux = quadrupleManager.jumpStack[-2]
    temp = quadrupleManager.quadruplesList[aux][2]
    quadrupleManager.operandStack.append(temp)
    quadrupleManager.typeStack.append('int')
    if not funcDir.constantExists(1):
        funcDir.addConstant(1, quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
    quadrupleManager.operandStack.append(1)
    quadrupleManager.operationStack.append('+')
    quadrupleManager.applyOperation(['+'], funcDir)

    aux = quadrupleManager.operandStack.pop()
    quadrupleManager.operandStack.append(temp)
    quadrupleManager.operandStack.append(aux)
    quadrupleManager.operationStack.append('=')
    quadrupleManager.applyOperation(['='], funcDir)

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
