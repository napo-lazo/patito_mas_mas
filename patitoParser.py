import patitoLexer
from parserClasses import FunctionDirectory
from patitoLogger import logs
from patitoLexer import tokens
import ply.yacc as yacc
from virutalMachine import VirtualMachine
from sys import exit

class VirutalDirectory(object):
    def __init__(self):

        self.genericCounter = 50000
        # Lista de las direcciones de memoria de cada tipo de variable 
        # [globales, locales, constantes, temporales]
        self.IntRanges = [3500, 11000, 18500, 26000]
        self.FloatRanges = [6000, 13500, 21000, 28500]
        self.CharRanges = [8500, 16000, 23500, -1]
        self.BoolRanges = [-1, -1, -1, 31000]
        # Contadores que apuntan a cada inicio de los rangos 
        self.globalIntsCounter = 1000
        self.globalFloatsCounter = 3500
        self.globalCharsCounter = 6000
        self.localIntsCounter = 8500
        self.localFloatsCounter = 11000
        self.localCharsCounter = 13500
        self.cteIntsCounter = 16000
        self.cteFloatsCounter = 18500
        self.cteCharsCounter = 21000
        self.tempIntsCounter = 23500
        self.tempFloatsCounter = 26000
        self.tempBoolsCounter = 28500
        self.pointersCounter = 31000

    # Regresa todos los contadores 
    # help
    def exportCounters(self):
        return [
                [self.globalIntsCounter - 1000, 
                self.globalFloatsCounter - self.IntRanges[0], 
                self.globalCharsCounter - self.FloatRanges[0]],
                [self.localIntsCounter - self.CharRanges[0], 
                self.localFloatsCounter - self.IntRanges[1], 
                self.localCharsCounter - self.FloatRanges[1]],
                [self.cteIntsCounter - self.CharRanges[1],
                self.cteFloatsCounter - self.IntRanges[2],
                self.cteCharsCounter - self.FloatRanges[2]],
                [self.tempIntsCounter - self.CharRanges[2], 
                self.tempFloatsCounter - self.IntRanges[3], 
                self.tempBoolsCounter - self.FloatRanges[3]],
                [self.pointersCounter - 31000]
               ]

    # Cuando se llama a crear una variable se utiliza esta funcion para crear su direccion virtual
    # Recibe su scope y tipo, mueve el contador de variables en el scope y regresa su direccion virtual 
    def generateAddressForVariable(self, scope, type):
        print(scope)
        if scope == 'global':
            if type == 'int':
                self.globalIntsCounter += 1
                return self.globalIntsCounter - 1
            elif type == 'float':
                self.globalFloatsCounter += 1
                return self.globalFloatsCounter - 1
            else:
                self.globalCharsCounter += 1
                return self.globalCharsCounter - 1
        elif scope == 'cte':
            if type == 'int':
                self.cteIntsCounter += 1
                return self.cteIntsCounter - 1
            elif type == 'float':
                self.cteFloatsCounter += 1
                return self.cteFloatsCounter - 1
            else:
                self.cteCharsCounter += 1
                return self.cteCharsCounter - 1
        elif scope == 'temp':
            if type == 'int':
                self.tempIntsCounter += 1
                return self.tempIntsCounter - 1
            elif type == 'float':
                self.tempFloatsCounter += 1
                return self.tempFloatsCounter - 1
            else:
                self.tempBoolsCounter += 1
                return self.tempBoolsCounter - 1
        elif scope == 'pointer':
            self.pointersCounter += 1
            return self.pointersCounter - 1
        else:
            if type == 'int':
                self.localIntsCounter += 1
                return self.localIntsCounter - 1
            elif type == 'float':
                self.localFloatsCounter += 1
                return self.localFloatsCounter - 1
            else:
                self.localCharsCounter += 1
                return self.localCharsCounter - 1
    
    # Genera el espacio necesario para un arreglo 
    # Regresa el contador en la direccion del ultimo elemento del arreglo
    def setSpaceForArray(self, scope, type, size):
        if scope == 'global':
            if type == 'int':
                self.globalIntsCounter += size
                return self.globalIntsCounter - 1
            elif type == 'float':
                self.globalFloatsCounter += size
                return self.globalFloatsCounter - 1
            else:
                self.globalCharsCounter += size
                return self.globalCharsCounter - 1
        else:
            if type == 'int':
                self.localIntsCounter += size
                return self.localIntsCounter - 1
            elif type == 'float':
                self.localFloatsCounter += size
                return self.localFloatsCounter - 1
            else:
                self.localCharsCounter += size
                return self.localCharsCounter - 1

    # Regresa los contadores locales a su posicion original
    # Se llama cada vez que se acabe una funcion 
    def resetLocalAddresses(self):
        self.localIntsCounter = 8500
        self.localFloatsCounter = 11000
        self.localCharsCounter = 13500
        self.tempIntsCounter = 23500
        self.tempFloatsCounter = 26000
        self.tempBoolsCounter = 28500


class QuadrupleManager(object):
    def __init__(self):
        self.virutalDirectory = VirutalDirectory()
        #Falta ver que rollo con las matrices y operaciones unarias, por el momento solo operaciones binarias, revisar comparasiones entre enteros y flotantes
        self.semanticCube = {'=':{('int', 'int'): 'int', ('float', 'float'): 'float', ('char', 'char'): 'char'},
                             '+':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'}, 
                             '-':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'}, 
                             '*':{('int', 'int'): 'int', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'}, 
                             '/':{('int', 'int'): 'float', ('int', 'float'): 'float', ('float', 'int'): 'float', ('float', 'float'): 'float'},
                             '>':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '>=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '<':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '<=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool'},
                             '==':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool', ('char', 'char'): 'char', ('bool', 'bool'): 'bool'},
                             '!=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool', ('char', 'char'): 'char', ('bool', 'bool'): 'bool'},
                             '&&':{('bool', 'bool'): 'bool'},
                             '||':{('bool', 'bool'): 'bool'}}
        # stack para guardar y manejar la logica de los saltos
        self.jumpStack = []
        # stack donde se guardan las operaciones que se quieren realizar (+, *, -, escribe, &&, etc)
        self.operationStack = []
        # stack donde se guardan los tipos de los operandos para realizar validanciones de tipo
        self.typeStack = []
        # stack donde se guardan los operandos que se van a usar para los saltos y las operaciones
        self.operandStack = []
        self.returnValuesStack = []
        self.returnTypeStack = []
        self.dimStack = []
        # stack que guarda los quadruplos generados que despues se pasaran a la maquina virtual
        self.quadruplesList = []
        # un contador para llevar el total de los quadruplos generados, funciona como el tama;o de un arreglo 
        self.quadrupleCounter = 0

    # metodo privado que se encarga de ver si dos tipos son compatibles con una operacion, si lo son se regresa el tipo resultante de lo contrario se regresa un None
    def __verifyTypeCompatibility(self, operation):
        try:
            return self.semanticCube[operation][(self.typeStack.pop(), self.typeStack.pop())]
        except:
            return None
    
    # Cuando se llame esta funcion se debe de llamar adentro de un try/except con un 'raise SyntaxError' dentro del except para poder propagar el error al parser
    # metodo publico que se encarga de aplicar la operacion que esta hasta arriba del stack, se le tiene que pasar una lista con los posibles operadores para que se respete la precedencia
    def applyOperation(self, operatorsList):

        if len(self.operationStack) != 0 and self.operationStack[-1] in operatorsList:
            if self.operationStack[-1] == '(':
                logs.append('Se agrego un "(" al operationStack\n')
                return 

            operation = self.operationStack.pop()
            rightOperand = self.operandStack.pop()
            leftOperand = self.operandStack.pop()
            
            resultType = self.__verifyTypeCompatibility(operation)
            if not resultType:
                print(f'Los tipos de {leftOperand} y {rightOperand} no son compatibles con esta operacion: {operation}')
                raise SyntaxError
            
            if operation in ['=']:
                self.quadruplesList.append((operation, funcDir.getVirtualAddressOfVariable(rightOperand), -1, funcDir.getVirtualAddressOfVariable(leftOperand)))
                logs.append(f'Se realizo {leftOperand} {operation} {rightOperand}\n')
            else:
                # self.quadruplesList.append((operation, leftOperand, rightOperand, self.virutalDirectory.genericCounter))
                resultAddress = self.virutalDirectory.generateAddressForVariable('temp', resultType)
                self.quadruplesList.append((operation, funcDir.getVirtualAddressOfVariable(leftOperand), funcDir.getVirtualAddressOfVariable(rightOperand), resultAddress))
                logs.append(f'Se realizo {leftOperand} {operation} {rightOperand} y se gurado el resultado en "{self.virutalDirectory.genericCounter}"\n')
                self.operandStack.append(resultAddress)
                logs.append(f'Se agrego el valor temporal "{resultAddress}" al operandStack\n')
                self.typeStack.append(resultType)
                logs.append(f'Se agrego "{resultType}" al typeStack\n')
                self.virutalDirectory.genericCounter += 1
            self.quadrupleCounter += 1
            
    # Agrega el parametro PARAM a la lista de cuadruplos
    def generateParameter(self, parameter, parameterPosition):
        self.quadruplesList.append(('PARAMETER', parameter, -1, parameterPosition))
        self.quadrupleCounter += 1

    # Agrega el GOSUB a la lista de cuadruplos
    def generateGoSub(self, funcName):
        #TODO: tirar error
        if funcDir.areParametersFinished():
            self.quadruplesList.append(('GOSUB', funcName, -1, funcDir.getFunctionStart()))
            self.quadrupleCounter += 1

        else:
            print('Error: faltan parametros')
    
    # Agrega el ENDFUNC a la lista de cuadruplos
    def generateEndFunc(self):
        self.quadruplesList.append(('ENDFUNC', -1, -1, -1))
        self.quadrupleCounter += 1

    # Agrega un ESCRIBE a la lista de cuadruplos, puede recibir una string o un operando 
    def generatePrint(self, string):
        if string:
            self.quadruplesList.append(('ESCRIBE', string, -1, -1))
        else:
            self.quadruplesList.append(('ESCRIBE', self.operandStack.pop(), -1, -1))
            self.typeStack.pop()
        self.quadrupleCounter += 1

    # Agrega un LEE a la lista de cuadruplos
    def generateInput(self, variable):
        self.quadruplesList.append(('LEE', -1, -1, funcDir.getVirtualAddressOfVariable(variable)))
        self.quadrupleCounter += 1

    # Agrega un RETURN a la lista de cuadruplos 
    def generateReturn(self, returnCounter):
        if returnCounter > 0:
            returnAddress = funcDir.getVirtualAddressOfVariable(funcDir.currentScope)
            self.quadruplesList.append(('RETURN', self.operandStack.pop(), -1, returnAddress))
            self.returnValuesStack.append(returnAddress)
            self.returnTypeStack.append(self.typeStack.pop())
            self.quadrupleCounter += 1
    
    # Agrega un RETURN a la lista de cuadruplos
    # Ademas almacena en el stack de operandos el valor de retorno de la funcion y agrega su dir como cuadruplo 
    def generateReturnAssignment(self):
        resultAddress = self.virutalDirectory.generateAddressForVariable('temp', funcDir.getReturnType(funcDir.functionCalled))
        self.quadruplesList.append(('=', funcDir.getVirtualAddressOfVariable(funcDir.functionCalled), -1, resultAddress))
        self.operandStack.append(resultAddress)
        self.typeStack.append(funcDir.getReturnType(funcDir.functionCalled))
        self.quadrupleCounter += 1

    # Agrega un ERA  a la lista de cuadruplos
    def generateERA(self, funcDir):
        print(self.quadruplesList)
        self.quadruplesList.append(('ERA', -1, -1, funcDir.getEra()))
        self.quadrupleCounter += 1
    
    # Agrega un ENDPROG a la lista de cuadruplos
    def generateEndProg(self):
        if funcDir.areFunctionsFinished():
            self.quadruplesList.append(('ENDPROG', -1, -1, -1))

    # Metodo publico que se encarga de generar un salto inicial
    #TODO: Refactorizar funcion
    def generateJump(self, jumpType):
        if jumpType == 'false':
            self.jumpStack.append(self.quadrupleCounter)
            valueToTest = self.operandStack.pop()
            #TODO: consider adding to semantic cube
            if self.typeStack.pop() == 'bool':
                self.quadruplesList.append(('GOTOF', valueToTest, -1, '-'))
                self.quadrupleCounter += 1
            else:
                print(f'el valor de {valueToTest} no es un booleano')
                raise SyntaxError
        elif jumpType == 'jump_cycle':
            self.jumpStack.append(self.quadrupleCounter)
        elif jumpType == 'jump_else':
            aux = self.jumpStack.pop()
            self.jumpStack.append(self.quadrupleCounter)
            self.jumpStack.append(aux)
            self.quadruplesList.append(('GOTO', -1, -1, '-'))
            self.quadrupleCounter +=1
            self.updateJump('normal')
        elif jumpType == 'jump':
            self.jumpStack.append(self.quadrupleCounter)
            self.quadruplesList.append(('GOTO', -1, -1, '-'))
            self.quadrupleCounter += 1

    
    # Metodo publico que se encarga de actualizar un salto para llenar la ubicacion a la que saltara
    def updateJump(self, jumpType):
        if jumpType == 'normal':
            i = self.jumpStack.pop()
            jumpToUpdate = self.quadruplesList[i]
            self.quadruplesList[i] = (jumpToUpdate[0], jumpToUpdate[1], jumpToUpdate[2], self.quadrupleCounter)
        elif jumpType == 'cycle':
            aux = self.jumpStack.pop()
            self.quadruplesList.append(('GOTO', -1, -1, self.jumpStack.pop()))
            self.jumpStack.append(aux)
            self.quadrupleCounter += 1
            self.updateJump('normal')

    def exportData(self):
        return [self.quadruplesList, self.virutalDirectory.exportCounters()]

    # metodo publico para limpiar los stacks y reiniciar los contadores
    def clearData(self):
        self.virutalDirectory.genericCounter = 1000
        self.jumpStack.clear()
        self.operandStack.clear()
        self.typeStack.clear()
        self.operandStack.clear()
        self.quadruplesList.clear()
        self.quadrupleCounter = 0

funcDir = FunctionDirectory()
quadrupleManager = QuadrupleManager()

# Gramatica para el parser

def p_start(p):
    '''
    start : programa
    '''
    print(funcDir.eras)
    print()
    print(funcDir.variablesTable)
    print()
    print(funcDir.ctesTable)
    print()
    print(quadrupleManager.quadrupleCounter)
    print(quadrupleManager.jumpStack)
    print(quadrupleManager.operandStack)
    print(quadrupleManager.typeStack)
    print(quadrupleManager.quadruplesList)
    print(quadrupleManager.dimStack)
    myMachine = VirtualMachine(quadrupleManager.exportData(), funcDir.turnCtesIntoList(), funcDir.eras)
    print(myMachine.initialEra)

    myMachine.executeProgram()
    # print(myMachine.Globals)
    # print(myMachine.Locals)
    # print(myMachine.Ctes)
    # print(myMachine.Temps)


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
    logs.append(f'Se elimino {temp} como el scope actual\n')
    del(temp)

# Regla de variables
def p_variables(p):
    '''
    var : VAR var_seen varp
        | empty
    '''
    if len(p) != 2: 
        p[0] = (p[1], p[3])
        
        # borra el scope actual porque aqui ya se termina el procesamiento de las variables globales
        # temp = funcDir.currentScope
        # funcDir.currentScope = None
        # logs.append(f'Se elimino "{temp}" como el scope actual\n')
        # del(temp)
        
    else:
        p[0] = p[1]

# Regla intermedia para asignar el scope actual como global
def p_var_seen(p):
    ''' 
    var_seen :
    '''
    if funcDir.currentScope is None:
        funcDir.createScope('global', 'void')
        logs.append('Se creo la funcion global de retorno tipo void en el dirFunc\n')
        funcDir.currentScope = 'global'
        logs.append('global se asigno como el scope actual\n')

def p_variablesp(p):
    # this error raise doesn't stop the compilation
    '''
    varp : tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp
         | tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp
    '''
    p[0] = (p[1], p[3], p[4], p[6], p[7], p[9], p[10])

# regla intermedia para asignar el tipo actual de las variables que se estan declarando
def p_tipo_seen(p):
    '''
    tipo_seen :
    '''
    funcDir.currentType = p[-1]
    logs.append(f'Se asigno {p[-1]} como el tipo de variable actual\n')

# regla intermedia para crear una variable del tipo actual en la tabla de variables del scope actual
def p_variable_seen(p):
    '''
    variable_seen : 
    '''
    # '''
    # variable_seen : 
    #               | error error 
    # '''
    # primero se revisa si ya hay una variable con ese nombre
    try:
        funcDir.variableExists(p[-1])

    # si no la hay se crea una de manera normal
    except:
        print('crea variable')
        funcDir.createVariable(p[-1], quadrupleManager.virutalDirectory.generateAddressForVariable(funcDir.currentScope, funcDir.currentType))
        logs.append(f'Se agrego la variable "{p[-1]}" al scope de {funcDir.currentScope}\n')

    # de lo contrario se tira un error de variable duplicada
    else:
        print(f'ERROR: Variable "{p[-1]}" already exists')
        raise SyntaxError

    funcDir.currentId = p[-1]

# regla intermedia que solo se encarga de eliminar el tipo actual
def p_delete_type(p):
    '''
    delete_type :
    '''
    temp = funcDir.currentType
    funcDir.currentType = None   
    logs.append(f'Se elimino "{temp}" como el tipo actual\n')
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
    logs.append(f'Se elimino "{temp}" como la variable actual\n')
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
    # '''
    # dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET
    #            | L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET error error  
    # '''
    # revisa que el tama;o de las dimensiones sea mayor o igual a 1 de lo contrario tira un error
    if(p[2] <= 0):
        print('ERROR: Array size cant be less than 1')
        raise SyntaxError
    else:
        p[0] = (p[1], p[2], p[3])
    
    if not funcDir.isVariableArray():
        funcDir.setVariableAsArray()
           
    funcDir.addArrayDimensionSize(p[2])
    logs.append(f'Se le asigno a {funcDir.currentId} una dimension de tama;o {p[2]}\n')

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
            | FUNCION error
            | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_funcionp(p):
    # poner una regla de error aqui permite que el codigo termine de compilar y marca el error
    '''
    funcionp : tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque end_func funcion
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    #functionDirectory[p[2]] = {'returnType':p[1], 'varTable':{}}
    #functionDirectory[p[2]].localVariableCount = p[5].length()

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
        if p[-2] != 'void':
            #TODO: verificar que el usuario no declare variables con el nombre de alguna funcion
            funcDir.currentType = p[-2]
            try:
                funcDir.scopeExists('global')
            except:
                funcDir.createScope('global', 'void')
                funcDir.createVariable(p[-1], quadrupleManager.virutalDirectory.generateAddressForVariable('global', p[-2]))
            else:
                funcDir.createVariable(p[-1], quadrupleManager.virutalDirectory.generateAddressForVariable('global', p[-2]))
                print(f'scope: {funcDir.currentScope}')
            funcDir.currentType = None
        
        funcDir.createScope(p[-1], p[-2])
        logs.append(f'Se creo la funcion {p[-1]} de retorno tipo {p[-2]} en el dirFunc\n')
        funcDir.currentScope = p[-1]
        logs.append(f'{p[-1]} se asigno como el scope actual\n')
        funcDir.addFunctionStart(quadrupleManager)
    else:
        print(f'Error: {p[-1]} ya existe')
        exit()

def p_end_func(p):
    '''
    end_func :
    '''
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
    logs.append(f'Se agrego el parametro "{p[-1]}" de tipo "{p[-2]}" al scope de func1\n')

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

def p_operand_seen(p):
    '''
    operand_seen :
    '''
    funcDir.currentId = p[-1]
    quadrupleManager.operandStack.append(funcDir.getVirtualAddressOfVariable(p[-1]))
    logs.append(f'Se agrego "{p[-1]}" al operandStack\n')
    try:
        quadrupleManager.typeStack.append(funcDir.getTypeOfVariable(p[-1]))
        logs.append(f'Se agrego "{quadrupleManager.typeStack[-1]}" al typeStack\n')
    except:
        print(f'ERROR: la variable {p[-1]} no ha sido declarada')
        raise SyntaxError

def p_dimId(p):
    '''
    dimId : is_array create_dim dim pop_array
          | is_array create_dim dim dim pop_array
          | empty
    '''
    # if len(p) >= 4:
        # aux = quadrupleManager.dimStack.pop()
        # print(quadrupleManager.operandStack)
        # print(quadrupleManager.typeStack)
        # print(quadrupleManager.quadruplesList)
        # if aux[1] == 1:
        #     offset = quadrupleManager.operandStack.pop()
        #     baseAddress = quadrupleManager.operandStack.pop()
        #     typeOf = quadrupleManager.typeStack.pop()

        #     temp = quadrupleManager.virutalDirectory.tempIntsCounter
        #     quadrupleManager.virutalDirectory.tempIntsCounter += 1
        #     quadrupleManager.quadruplesList.append(('DISPLACE', baseAddress, offset, temp))
        #     quadrupleManager.operandStack.append(temp)
        #     quadrupleManager.quadrupleCounter += 1
        # else:
        #     offset = quadrupleManager.operandStack.pop()
        #     baseAddress = quadrupleManager.operandStack.pop()
        #     typeOf = quadrupleManager.typeStack.pop()
        #     if typeOf != 'int':
        #         print('Error: solo se puede indexar un arreglo con valores enteros')
        #         exit()
        #     temp = quadrupleManager.virutalDirectory.tempIntsCounter
        #     quadrupleManager.virutalDirectory.tempIntsCounter += 1
        #     quadrupleManager.quadruplesList.append(('DISPLACEMAT', baseAddress, offset, temp))
        #     quadrupleManager.operandStack.append(temp)
        #     quadrupleManager.quadrupleCounter += 1
    
    funcDir.currentId = None

def p_pop_array(p):
    '''
    pop_array :
    '''
    quadrupleManager.dimStack.pop()

def p_is_array(p):
    '''
    is_array :  
    '''
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

def p_bracket_seen(p):
    '''
    bracket_seen :
    '''
    if p[-1] == ']':
        dim = quadrupleManager.dimStack[-1][1][0]
        #TODO: convert to constant
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
            quadrupleManager.applyOperation('*')
            print(f'Primer valor de matriz indexing: {quadrupleManager.quadruplesList[-1]}')
        else:
            if quadrupleManager.typeStack[-1] != 'int':
                print('Error: solo se puede indexar un arreglo con valores enteros')
                exit()
            if len(quadrupleManager.dimStack[-1][1]) != quadrupleManager.dimStack[-1][2]:
                # if not funcDir.constantExists(quadrupleManager.operandStack[-2]):
                #     funcDir.addConstant(quadrupleManager.operandStack[-1], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
                quadrupleManager.operationStack.append('+')
                quadrupleManager.applyOperation('+')
                print(f'Segundo valor de matriz indexing: {quadrupleManager.quadruplesList[-1]}')

            if not funcDir.constantExists(quadrupleManager.operandStack[-2]):
                funcDir.addConstant(quadrupleManager.operandStack[-2], quadrupleManager.virutalDirectory.generateAddressForVariable('cte', 'int') ,'int')
            quadrupleManager.operationStack.append('+')
            quadrupleManager.applyOperation('+')
            pointerAddress = quadrupleManager.virutalDirectory.generateAddressForVariable('pointer', 'int')
            aux = quadrupleManager.quadruplesList.pop()
            quadrupleManager.quadruplesList.append((aux[0], aux[1], aux[2], pointerAddress))
            quadrupleManager.operandStack.pop()
            quadrupleManager.operandStack.append(pointerAddress)
            # quadrupleManager.quadruplesList.append(('OFFSET', quadrupleManager.operandStack[-1], -1, quadrupleManager.virutalDirectory.tempIntsCounter))
            # quadrupleManager.operandStack.append(quadrupleManager.virutalDirectory.tempIntsCounter)
            # quadrupleManager.virutalDirectory.tempIntsCounter += 1
            # quadrupleManager.quadrupleCounter += 1

        quadrupleManager.operationStack.pop()
    else:
        # aux = quadrupleManager.dimStack.pop()[1]
        # quadrupleManager.dimStack.append((funcDir.currentId, aux + 1))

        quadrupleManager.operationStack.append('(')

# regla intermedia que se encarga de realizar los quadruplos de operiones logicas
def p_apply_operation_assign(p):
    '''
    apply_operation_assign : 
    '''
    try:
        quadrupleManager.applyOperation(['='])
    except:
        raise SyntaxError

# falta ver que rollo con el not
def p_expresion(p):
    '''
    expresion : relacional apply_operation_expresion expresionp
              | NOT relacional expresionp
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
        quadrupleManager.applyOperation(['||', '&&'])
    except:
        raise SyntaxError

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
        quadrupleManager.applyOperation(['>', '>=', '<', '<=', '==', '!='])
    except:
        raise SyntaxError

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
        quadrupleManager.applyOperation(['+', '-'])
    except:
        raise SyntaxError

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
        quadrupleManager.applyOperation(['*', '/'])
    except:
        raise SyntaxError

# regla intermedia que se encarga de agregar el operador a la pila de operadores
def p_operation_seen(p):
    '''
    operation_seen : 
    '''
    if p[-1] == ')':
        quadrupleManager.operationStack.pop()
        logs.append('Se termino un parentesis\n')
    else:
        quadrupleManager.operationStack.append(p[-1])
        logs.append(f'Se agrego {p[-1]} al operantionStack\n')


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
        | ID operand_seen dimId
        | L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen
    '''
    if len(p) == 6:
        p[0] = (p[1], p[3], p[4])

    # Para cuando se recibe una variable
    # TODO: Falta para cuando el valor viene de un arreglo/matriz y despues convertirlo y ver si se puede reusar en regla gramatical
    elif len(p) == 4:
        p[0] = (p[1], p[3])

        # quadrupleManager.operandStack.append(p[1])
        # logs.append(f'Se agrego {p[1]} al operandStack')
        # try:
        #     quadrupleManager.typeStack.append(variablesTable.getTypeOfVariable(p[1]))
        # except:
        #     print(f'ERROR: la variable {p[1]} no ha sido declarada')
        #     raise SyntaxError

    #TODO: por el momento solo esta pensado para ctes y no funciones 
    elif not type(p[1]) is float and not type(p[1]) is int and not type(p[1]) is str:
        pass
    else:
        #TODO: add verification of char constants
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
        print(quadrupleManager.operandStack)
        logs.append(f'Se agrego la constante "{p[1]}" al operandStack\n')
        logs.append(f'Se agrego "{type(p[1])}" al typeStack\n')

        p[0] = p[1]

def p_llamadaFuncion(p):
    '''
    llamadaFuncion : ID set_func_scope L_PARENTHESIS operation_seen llamadaFuncionp R_PARENTHESIS operation_seen
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

    if not funcDir.isVoid():
        # print(funcDir.functionCalled)
        quadrupleManager.generateERA(funcDir)
        quadrupleManager.generateGoSub(funcDir.functionCalled)
        quadrupleManager.generateReturnAssignment()
        funcDir.functionCalled = None
        funcDir.parameterCounter = 0
    else:
        print('Error: no se puede llamar una funcion con tipo de retorno void en una expresion')
        raise SyntaxError

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
    if funcDir.isVoid():
        quadrupleManager.generateERA(funcDir)
        quadrupleManager.generateGoSub(funcDir.functionCalled)
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
        print('Error: funcion no existe')
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
    quadrupleManager.generateReturn(funcDir.callFromReturn)
    

def p_lectura(p):
    '''
    lectura : LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_lecturap(p):
    '''
    lecturap : ID dimId gen_input lecturapp
    '''
    p[0] = (p[1], p[2], p[3])

def p_gen_input(p):
    '''
    gen_input :
    '''
    #TODO: add array compatibility
    quadrupleManager.generateInput(p[-2])

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
    quadrupleManager.applyOperation(['+'])

    aux = quadrupleManager.operandStack.pop()
    quadrupleManager.operandStack.append(temp)
    quadrupleManager.operandStack.append(aux)
    quadrupleManager.operationStack.append('=')
    quadrupleManager.applyOperation(['='])

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
