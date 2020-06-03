# variablesTable guarda las variables globales y de las funciones
class FunctionDirectory(object):

    def __init__(self):
        #variablesTable tiene el formato de {nombreScope : {returnType : valor, parameters: [type1, type2, etc] variables : {nombreVar1 : {type : valor, value : valor}}}} 
        self.variablesTable = {}
        self.ctesTable = {'virtualAddresses' : {}}
        self.eras = {}
        self.currentScope = None
        self.currentType = None
        self.currentId = None
        self.functionCalled = None
        self.parameterCounter = 0
        self.callFromReturn = 0
        #########################
        self.localVariableCount = 0
        self.tempVariableCount = 0

    # Esta funcion recibe como parametro una variable que se encuentre en la tabla de variables y regresa su direccion virtual
    # si ya es una direccion virtual se regresa a si misma
    def getVirtualAddressOfVariable(self, variable):
        try:
            return self.variablesTable[self.currentScope]['variables'][variable]['virtualAddress']
        except:
            try:
                return self.variablesTable['global']['variables'][variable]['virtualAddress']
            except:
                try: 
                    return self.ctesTable[variable]['virtualAddress']
                except:
                    return variable

    #lo mismo que la funcion anterior pero para la direccion inicial de una matriz
    def getMatrixStart(self, variable):
        try:
            return self.variablesTable[self.currentScope]['variables'][variable]['virtualAddress']
        except:
            try:
                return self.variablesTable['global']['variables'][variable]['virtualAddress']
            except:
                return variable

    # Esta funcion determina si una constante existe en la tabla de constantes
    def constantExists(self, constant):
        try:
            self.ctesTable[constant]
            return True
        except:
            return False

    # Agrega una constante a la tabla de constantes, recibe el valor, direccion y tipo de dato
    def addConstant(self, constant, virtualAddress, typeOfConstant):
        self.ctesTable[constant] = {'virtualAddress': virtualAddress, 'type' : typeOfConstant}

    # Regresa el scopename si es que existe en la tabla
    def scopeExists(self, scopeName):
        return self.variablesTable[scopeName]

    # Crea en la tabla de variables el scope
    def createScope(self, scopeName, returnType):
        if scopeName == 'global':
            self.variablesTable[scopeName] = {'returnType': returnType, 'variables' : {}}
        else:
            self.eras[scopeName] = []
            self.variablesTable[scopeName] = {'returnType': returnType, 'parameters' : [], 'variables' : {}, 'era' : scopeName}

    # Agrega una variable a la tabla de variables con su nombre y direccion virtual
    def createVariable(self, variableName, virtualAddress):
        if self.currentScope:
            self.variablesTable[self.currentScope]['variables'][variableName] = {'type' : self.currentType, 'virtualAddress' : virtualAddress, 'isArray' : False}
        else:
            self.variablesTable['global']['variables'][variableName] = {'type' : self.currentType, 'virtualAddress' : virtualAddress, 'isArray' : False}
    
    # Determina si la variable con el nombre que se manda como parametro existe en la tabla de variables
    def variableExists(self, variableName):
        return self.variablesTable[self.currentScope]['variables'][variableName]
    
    # Nos sirve para determinar si una variable es un arreglo a partir del id de la variable
    def isVariableArray(self):
        try: 
            if self.currentScope == None:
                return self.variablesTable['global']['variables'][self.currentId]['isArray']
            else:
                try:
                    return self.variablesTable[self.currentScope]['variables'][self.currentId]['isArray']
                except:
                    return self.variablesTable['global']['variables'][self.currentId]['isArray']
        except:
            return False    
    # Ayuda a marcar una variable como arreglo y prepara el espacio para las dimensiones
    def setVariableAsArray(self):
        self.variablesTable[self.currentScope]['variables'][self.currentId]['isArray'] = True
        self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'] = []

    # Agrega una dimension del arreglo como parametro a la lista de dimensiones 
    def addArrayDimensionSize(self, size):
        self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'].append(size)

    # ?? Regresa las dimensiones de una variable arreglo como parametro
    def getArrayDimensions(self, variable):
        if self.currentScope == None:
            return self.variablesTable['global']['variables'][variable]['arrayDimensions'].copy()
        else:
            try:
                return self.variablesTable[self.currentScope]['variables'][variable]['arrayDimensions'].copy()
            except:
                return self.variablesTable['global']['variables'][variable]['arrayDimensions'].copy()

    # Regresa los valores que se encuentran en la lista de dimensiones, para verificar
    def getArrayDimensionsSize(self):
        if len(self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions']) == 2:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][0] * self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][1]
        else:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][0]

    # dado un id de variable regresa su tipo de dato
    def getTypeOfVariable(self, variableName):
        if self.currentScope is None:
            return self.variablesTable['global']['variables'][variableName]['type']
        else:
            try: 
                return self.variablesTable[self.currentScope]['variables'][variableName]['type']
            except:
                return self.variablesTable['global']['variables'][variableName]['type']

    # Marca la direccion en la que empieza una funcion
    def addFunctionStart(self, quadrupleManager):
        self.variablesTable[self.currentScope]['startsAt'] = quadrupleManager.quadrupleCounter

    # Regresa la direccion en la que empieza una funcion
    def getFunctionStart(self):
        return self.variablesTable[self.functionCalled]['startsAt']

    # Agrega un parametro al diccionario de parametros dado sus atributos: nombre, tipo y direccion 
    def addParameterToList(self, paramName, paramType, virtualAddress):
            self.variablesTable[self.currentScope]['parameters'].append(paramType)
            self.variablesTable[self.currentScope]['variables'][paramName] = {'type' : paramType, 'virtualAddress' : virtualAddress}

    # Verifica si el parametro que se mando a la funcion hace match con la definicion de la funcion 
    def verifyParameter(self, quadrupleManager):
        if self.parameterCounter < len(self.variablesTable[self.functionCalled]['parameters']):
            if quadrupleManager.typeStack.pop() != self.variablesTable[self.functionCalled]['parameters'][self.parameterCounter]:
                print(f'Error: El tipo del parametro {self.parameterCounter} en la funcion {self.functionCalled} no es del tipo {self.variablesTable[self.functionCalled]["parameters"][self.parameterCounter]}')
                exit()
            else:
                quadrupleManager.generateParameter(quadrupleManager.operandStack.pop(), self.parameterCounter)
                self.parameterCounter += 1
        elif self.parameterCounter >= len(self.variablesTable[self.functionCalled]['parameters']):
            print(f'Error: Parametros de mas en la funcion {self.functionCalled}')
            exit()
    
    # Determina si el contador de parametros es igual al numero de parametros de la funcion 
    def areParametersFinished(self):
        return self.parameterCounter == len(self.variablesTable[self.functionCalled]['parameters'])

    # Verifica si la funcion regresa el mismo tipo de valor que su definicion, en caso de void, marca error si regresa un valor
    def verifyFunctionCompatibility(self, quadrupleManager):

        if self.currentScope == None:
            print('Error: No se puede usar el estatuto de regresa afuera de una funcion')
            exit()

        if self.callFromReturn >= 1 and self.variablesTable[self.currentScope]['returnType'] == 'void':
            print('Error: Funcion void no puede regresar valores')
            exit()
            return

        if self.callFromReturn >= 1:
            aux = quadrupleManager.typeStack[-1]
        else:
            return

        if aux != self.variablesTable[self.currentScope]['returnType']:
            print(f'Error: La funcion {self.currentScope} no regresa un valor de tipo {self.getReturnType(self.currentScope)}')
            exit()
    
    # Determina si la funcion es tipo void
    def isVoid(self, scope):
        return self.variablesTable[scope]['returnType'] == 'void'

    # Obtiene el tipo de variable de retorno de la funcion 
    def getReturnType(self, functionName):
        return self.variablesTable[functionName]['returnType']
    
    # Calcula la cantidad de memoria que se necesita por las variables locales y temporales
    def createEra(self, virtualDirectory):
        # [ints, floats, chars]
        locales = [virtualDirectory.localIntsCounter - virtualDirectory.CharRanges[0], virtualDirectory.localFloatsCounter - virtualDirectory.IntRanges[1], virtualDirectory.localCharsCounter - virtualDirectory.FloatRanges[1]]
        # [ints, floats, bools]
        temporales = [virtualDirectory.tempIntsCounter - virtualDirectory.CharRanges[2], virtualDirectory.tempFloatsCounter - virtualDirectory.IntRanges[3], virtualDirectory.tempBoolsCounter - virtualDirectory.FloatRanges[3]]
        self.eras[self.currentScope] = [locales, temporales]
    
    # Regresa el tamano del ERA 
    def getEra(self):
        return self.variablesTable[self.functionCalled]['era']

    # Crea la lista de constantes para la maquina virtual 
    def turnCtesIntoList(self):
        aux = self.ctesTable.items()
        virtualAddresses = self.ctesTable['virtualAddresses'].items()
        first = True
        ctes = []
        addresses = []
        for x in aux:
            if first:
                for y in virtualAddresses:
                    ctes.append(y[0])
                    addresses.append(y[1]['virtualAddress'])
                first = not first
            else:
                ctes.append(x[0])
                addresses.append(x[1]['virtualAddress'])
        return  sorted(list(zip(ctes, addresses)), key=lambda tup: tup[1])

    #crea una direccion virutal en las constantes
    def addCteVirtualAddress(self, constant, virtualAddress, typeOfConstant):
        self.ctesTable['virtualAddresses'][constant] = {'virtualAddress': virtualAddress, 'type' : typeOfConstant}
    
    #revisa si existe una direccion de memoria en la tabla de constantes
    def constantVirtualAddressExists(self, constant):
        try:
            self.ctesTable['virtualAddresses'][constant]
            return True
        except:
            return False

    #consigue una direccion de memoria de la tabla de constantes
    def getCteVirtualAddress(self, constant):
        return self.ctesTable['virtualAddresses'][constant]['virtualAddress']


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
        elif scope == 'temp':
            if type == 'int':
                self.tempIntsCounter += size
                return self.globalIntsCounter - 1
            elif type == 'float':
                self.tempFloatsCounter += size
                return self.globalFloatsCounter - 1
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
                             '==':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool', ('char', 'char'): 'bool', ('bool', 'bool'): 'bool'},
                             '!=':{('int', 'int'): 'bool', ('int', 'float'): 'bool', ('float', 'int'): 'bool', ('float', 'float'): 'bool', ('char', 'char'): 'char', ('bool', 'bool'): 'bool'},
                             '&&':{('bool', 'bool'): 'bool'},
                             '||':{('bool', 'bool'): 'bool'},
                             '!':{('bool'):'bool'},
                             '?':{('int'): 'float', ('float'): 'float'},
                             '$':{('int'): 'int', ('float'): 'float'},
                             '¡':{('int'): 'int', ('float'): 'float'}}
        # stack para guardar y manejar la logica de los saltos
        self.jumpStack = []
        # stack donde se guardan las operaciones que se quieren realizar (+, *, -, escribe, &&, etc)
        self.operationStack = []
        # stack donde se guardan los tipos de los operandos para realizar validanciones de tipo
        self.typeStack = []
        # stack donde se guardan los operandos que se van a usar para los saltos y las operaciones
        self.operandStack = []
        #stack para guardar los valores de retorno
        self.returnValuesStack = []
        #stack para guardar los tipos de los valores de retorno
        self.returnTypeStack = []
        #guarda las dimensiones de matrices
        self.dimStack = []
        #guarda las dimensiones de matrices que se usan en operaciones
        self.matDimStack = []
        #guarda el tipo de matrices que se usan en operaciones
        self.matTypeStack = []
        # stack que guarda los quadruplos generados que despues se pasaran a la maquina virtual
        self.quadruplesList = []
        # un contador para llevar el total de los quadruplos generados, funciona como el tama;o de un arreglo 
        self.quadrupleCounter = 0

    # metodo privado que se encarga de ver si dos tipos son compatibles con una operacion, si lo son se regresa el tipo resultante de lo contrario se regresa un None
    def __verifyTypeCompatibility(self, operation):
        if operation in ['!', '?', '¡', '$']:
            try:
                return self.semanticCube[operation][(self.typeStack.pop())]
            except:
                return None
        else:
            try:
                return self.semanticCube[operation][(self.typeStack.pop(), self.typeStack.pop())]
            except:
                return None
    
    # metodo publico que se encarga de aplicar la operacion que esta hasta arriba del stack, se le tiene que pasar una lista con los posibles operadores para que se respete la precedencia
    def applyOperation(self, operatorsList, funcDir):

        if len(self.operationStack) != 0 and self.operationStack[-1] in operatorsList:
            if self.operationStack[-1] == '(':
                return 

            operation = self.operationStack.pop()
            rightOperand = self.operandStack.pop()
            leftOperand = self.operandStack.pop()
            
            resultType = self.__verifyTypeCompatibility(operation)
            if not resultType:
                print(f'Los tipos de {leftOperand} y {rightOperand} no son compatibles con esta operacion: {operation}')
                exit()
            
            if operation in ['=']:
                #aplica la operacion con matrices
                if len(self.matDimStack):
                    try: 
                        rightMat = self.matDimStack.pop()
                        leftMat = self.matDimStack.pop()
                    except:
                        print('Se necesitan dos matrices para esta operacion "="')
                        exit()
                    if not (rightOperand == rightMat[0] or rightOperand == rightMat[1]):
                        print('Operador derecho no es una matriz')
                        exit()
                    if not (leftOperand == leftMat[0] or leftOperand == leftMat[1]):
                        print('Operador izquierdo no es una matriz')
                        exit
                    if leftMat[2] == rightMat[2]:
                        left = (funcDir.getMatrixStart(leftOperand), leftMat[2])
                        right = (funcDir.getMatrixStart(rightOperand), rightMat[2])
                        self.quadruplesList.append((operation + 'Mat', right, -1, left))
                    else:
                        print('Error: matrices no son de tama;os compatibles')
                        exit()
                else:
                    self.quadruplesList.append((operation, funcDir.getVirtualAddressOfVariable(rightOperand), -1, funcDir.getVirtualAddressOfVariable(leftOperand)))
            else:
                #aplica la operacion con matrices
                if len(self.matDimStack):
                    try :
                        rightMat = self.matDimStack.pop()
                        leftMat = self.matDimStack.pop()
                    except:
                        print('Se necesitan que estos operadores sean matrices')
                        exit()
                    if not (rightOperand == rightMat[0] or rightOperand == rightMat[1]):
                        print('Operador derecho no es una matriz')
                        exit()
                    if not(leftOperand == leftMat[0] or leftOperand == leftMat[1]):
                        print('Operador izquierdo no es una matriz')
                        exit()
                    if (operation in ['+', '-'] and leftMat[2] == rightMat[2]) or (operation == '*' and leftMat[2][1] == rightMat[2][0]):
                        resultAddress = self.virutalDirectory.generateAddressForVariable('temp', resultType)
                        left = (funcDir.getMatrixStart(leftOperand), leftMat[2])
                        right = (funcDir.getMatrixStart(rightOperand), rightMat[2])
                        if operation == '*':
                            result = (resultAddress, [leftMat[2][0], rightMat[2][1]])
                            self.matDimStack.append((resultAddress, resultAddress, [leftMat[2][0], rightMat[2][1]]))
                        else:
                            result = (resultAddress, leftMat[2])
                            self.matDimStack.append((resultAddress, resultAddress, leftMat[2]))
                        self.virutalDirectory.setSpaceForArray('temp', resultType, leftMat[2][0] * leftMat[2][1] - 1)
                        self.operandStack.append(resultAddress)
                        self.typeStack.append(resultType)
                        self.quadruplesList.append((operation + 'Mat', left, right, result))
                    elif not operation in ['+', '-', '*']:
                        print('Error: esa no es una operacion valida para matrices')
                        exit()
                    else:
                        print('Error: matrices no son de tama;os compatibles')
                        exit()

                else:
                    resultAddress = self.virutalDirectory.generateAddressForVariable('temp', resultType)
                    self.quadruplesList.append((operation, funcDir.getVirtualAddressOfVariable(leftOperand), funcDir.getVirtualAddressOfVariable(rightOperand), resultAddress))
                    self.operandStack.append(resultAddress)
                    self.typeStack.append(resultType)
                    self.virutalDirectory.genericCounter += 1
            self.quadrupleCounter += 1
            
    #aplica los operadores unarios
    def applyUnary(self, operatorsList, funcDir):
        if len(self.operationStack) != 0 and self.operationStack[-1] in operatorsList:
            if self.operationStack[-1] == '(':
                return 

            operation = self.operationStack.pop()
            operand = self.operandStack.pop()
            
            resultType = self.__verifyTypeCompatibility(operation)
            if not resultType:
                print(f'El tipo de {operand} no es compatible con esta operacion: {operation}')
                exit()
            
            #aplica la operacion con matrices
            if len(self.matDimStack) != 0:
                mat = self.matDimStack.pop()
                if not(operand == mat[0] or operand == mat[1]):
                    print('Operando no es una matriz')
                    exit()
                
                resultAddress = self.virutalDirectory.generateAddressForVariable('temp', resultType)
                left = (funcDir.getMatrixStart(operand), mat[2])
                if operation == '$':
                    if mat[2][0] != mat[2][1]:
                        print("Error: se necesita una matriz cuadrada para calcular la determinante")
                        exit()
                    result = resultAddress
                else:
                    if operation == '¡':
                        result = (resultAddress, [mat[2][1], mat[2][0]])
                        self.matDimStack.append((resultAddress, resultAddress, [mat[2][1], mat[2][0]]))
                    else:
                        result = (resultAddress, mat[2])
                        self.matDimStack.append((resultAddress, resultAddress, mat[2]))
                    self.virutalDirectory.setSpaceForArray('temp', resultType, mat[2][0] * mat[2][1] - 1)
                
                self.operandStack.append(resultAddress)
                self.typeStack.append(resultType)
                self.quadruplesList.append((operation, left, -1, result))

            else:
                resultAddress = self.virutalDirectory.generateAddressForVariable('temp', resultType)
                self.quadruplesList.append((operation, funcDir.getVirtualAddressOfVariable(operand), -1, resultAddress))
                self.operandStack.append(resultAddress)
                self.typeStack.append(resultType)
            self.quadrupleCounter += 1

    # Agrega el parametro PARAM a la lista de cuadruplos
    def generateParameter(self, parameter, parameterPosition):
        self.quadruplesList.append(('PARAMETER', parameter, -1, parameterPosition))
        self.quadrupleCounter += 1

    # Agrega el GOSUB a la lista de cuadruplos
    def generateGoSub(self, funcName, funcDir):
        if funcDir.areParametersFinished():
            self.quadruplesList.append(('GOSUB', funcName, -1, funcDir.getFunctionStart()))
            self.quadrupleCounter += 1

        else:
            print(f'Error: faltan parametros en la funcion {funcDir.functionCalled}')
            exit()
    
    # Agrega el ENDFUNC a la lista de cuadruplos
    def generateEndFunc(self):
        self.quadruplesList.append(('ENDFUNC', -1, -1, -1))
        self.quadrupleCounter += 1

    # Agrega un ESCRIBE a la lista de cuadruplos, puede recibir una string o un operando 
    def generatePrint(self, string):
        if len(self.matDimStack) != 0:
            print('Escribe no es compatible con matrices')
            exit()
        if string:
            self.quadruplesList.append(('ESCRIBE', string , -1, -1))
        else:
            self.quadruplesList.append(('ESCRIBE', self.operandStack.pop(), -1, -1))
            self.typeStack.pop()
        self.quadrupleCounter += 1

    # Agrega un LEE a la lista de cuadruplos
    def generateInput(self, variable, funcDir):

        self.quadruplesList.append(('LEE', -1, -1, funcDir.getVirtualAddressOfVariable(self.operandStack.pop())))
        self.typeStack.pop()
        self.quadrupleCounter += 1

    # Agrega un RETURN a la lista de cuadruplos 
    def generateReturn(self, returnCounter, funcDir):

        if returnCounter > 0:
            returnAddress = funcDir.getVirtualAddressOfVariable(funcDir.currentScope)
            self.quadruplesList.append(('RETURN', self.operandStack.pop(), -1, returnAddress))
            self.returnValuesStack.append(returnAddress)
            self.returnTypeStack.append(self.typeStack.pop())
            self.quadrupleCounter += 1
    
    # Agrega un RETURN a la lista de cuadruplos
    # Ademas almacena en el stack de operandos el valor de retorno de la funcion y agrega su dir como cuadruplo 
    def generateReturnAssignment(self, funcDir):

        if len(self.matDimStack) != 0:
            print('Regresa no es compatible con matrices')
            exit()

        resultAddress = self.virutalDirectory.generateAddressForVariable('temp', funcDir.getReturnType(funcDir.functionCalled))
        self.quadruplesList.append(('=', funcDir.getVirtualAddressOfVariable(funcDir.functionCalled), -1, resultAddress))
        self.operandStack.append(resultAddress)
        self.typeStack.append(funcDir.getReturnType(funcDir.functionCalled))
        self.quadrupleCounter += 1

    # Agrega un ERA  a la lista de cuadruplos
    def generateERA(self, funcDir):
        self.quadruplesList.append(('ERA', -1, -1, funcDir.getEra()))
        self.quadrupleCounter += 1
    
    # Agrega un ENDPROG a la lista de cuadruplos
    def generateEndProg(self, funcDir):
        if funcDir.areFunctionsFinished():
            self.quadruplesList.append(('ENDPROG', -1, -1, -1))

    # Metodo publico que se encarga de generar un salto inicial
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
                exit()
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