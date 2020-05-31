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
    def getVirtualAddressOfVariable(self, variable):
        try:
            # print(self.variablesTable[self.currentScope]['variables'][variable]['virtualAddress'])
            return self.variablesTable[self.currentScope]['variables'][variable]['virtualAddress']
        except:
            try:
                # print(self.variablesTable['global']['variables'][variable]['virtualAddress'])
                return self.variablesTable['global']['variables'][variable]['virtualAddress']
            except:
                try: 
                    # print(self.ctesTable[variable]['virtualAddress'])
                    return self.ctesTable[variable]['virtualAddress']
                except:
                    # TODO: add proper logic
                    return variable

    def getMatrixStart(self, variable):
        try:
            # print(self.variablesTable[self.currentScope]['variables'][variable]['virtualAddress'])
            return self.variablesTable[self.currentScope]['variables'][variable]['virtualAddress']
        except:
            try:
                # print(self.variablesTable['global']['variables'][variable]['virtualAddress'])
                return self.variablesTable['global']['variables'][variable]['virtualAddress']
            except:
                # TODO: add proper logic
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
    # . 
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
                return self.variablesTable[self.currentScope]['variables'][self.currentId]['isArray']
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
            return self.variablesTable[self.currentScope]['variables'][variable]['arrayDimensions'].copy()

    # Regresa los valores que se encuentran en la lista de dimensiones, para verificar
    def getArrayDimensionsSize(self):
        if len(self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions']) == 2:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][0] * self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][1]
        else:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][0]

    # dado un id de variable regresa su tipo de dato
    def getTypeOfVariable(self, variableName):
        if self.currentScope is None:
            print(f'{variableName} del scope global') 
            return self.variablesTable['global']['variables'][variableName]['type']
        else:
            try: 
                print(f'Intento de {variableName} del scope {self.currentScope}')
                return self.variablesTable[self.currentScope]['variables'][variableName]['type']
            except:
                print(f'{variableName} del scope global') 
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
        #TODO: Throw error if parameters are missing
        if self.parameterCounter < len(self.variablesTable[self.functionCalled]['parameters']):
            if quadrupleManager.typeStack.pop() != self.variablesTable[self.functionCalled]['parameters'][self.parameterCounter]:
                print(f'Error: El tipo del parametro {self.parameterCounter} no es del tipo {self.variablesTable[self.functionCalled]["parameters"][self.parameterCounter]}')
            else:
                quadrupleManager.generateParameter(quadrupleManager.operandStack.pop(), self.parameterCounter)
                self.parameterCounter += 1
        elif self.parameterCounter >= len(self.variablesTable[self.functionCalled]['parameters']):
            print('Error: Parametros de mas')
    
    # Determina si el contador de parametros es igual al numero de parametros de la funcion 
    def areParametersFinished(self):
        return self.parameterCounter == len(self.variablesTable[self.functionCalled]['parameters'])

    # Verifica si la funcion regresa el mismo tipo de valor que su definicion, en caso de void, marca error si regresa un valor
    def verifyFunctionCompatibility(self, quadrupleManager):

        if self.callFromReturn == 0 and self.variablesTable[self.currentScope]['returnType'] != 'void':
            print('Falta que la funcion regrese un valor')
            return

        if self.callFromReturn >= 1 and self.variablesTable[self.currentScope]['returnType'] == 'void':
            print('Funcion void no puede regresar valores')
            return

        if self.callFromReturn >= 1:
            aux = quadrupleManager.typeStack[-1]
        else:
            return

        if aux == self.variablesTable[self.currentScope]['returnType']:
            print('tipos son validos')
        else:
            print('Los tipos no son validos')
    
    # Determina si la funcion es tipo void
    def isVoid(self):
        return self.variablesTable[self.functionCalled]['returnType'] == 'void'

    # Obtiene el tipo de variable de retorno de la funcion 
    def getReturnType(self, functionName):
        return self.variablesTable[functionName]['returnType']

    # Borra el contenido de la tabla de variables
    def releaseVars(self):
        self.functionDirectory['varTable'].clear()
    
    # Calcula la cantidad de memoria que se necesita por las variables locales y temporales
    #TODO: count parameters and give parameters virutal addresses
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
        print(aux)
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

    def addCteVirtualAddress(self, constant, virtualAddress, typeOfConstant):
        self.ctesTable['virtualAddresses'][constant] = {'virtualAddress': virtualAddress, 'type' : typeOfConstant}
    
    def constantVirtualAddressExists(self, constant):
        try:
            self.ctesTable['virtualAddresses'][constant]
            return True
        except:
            return False

    def getCteVirtualAddress(self, constant):
        return self.ctesTable['virtualAddresses'][constant]['virtualAddress']


# class FunctionDirectory(object):
#     # funcDir = {'nameid': {'returnType': <datatype> , 'parameters': [],'varTable': <table>}, 'size': <ERA>}
#     def __init__(self):
#         self.functionDirectory={}
#         self.parameterCount = 0
#         self.localVariableCount = 0
#         self.tempVariableCount = 0
#         # Con este defines en donde empieza la funcion
#         self.quadrupleCounter = 0

#     def createFunction(self, functionName, returnType, parameters):
#         self.functionDirectory[functionName] = {'returnType': returnType, 'parameters': [], 'varTable': VariablesTable()}
    
#     def releaseVars(self):
#         # release vartable, end function, update temporal var count
#         self.functionDirectory['varTable'].clear()
