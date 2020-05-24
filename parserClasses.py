# variablesTable guarda las variables globales y de las funciones
class FunctionDirectory(object):

    def __init__(self):
        #variablesTable tiene el formato de {nombreScope : {returnType : valor, parameters: [type1, type2, etc] variables : {nombreVar1 : {type : valor, value : valor}}}} 
        self.variablesTable = {}
        self.ctesTable = {}
        self.currentScope = None
        self.currentType = None
        self.currentId = None
        self.functionCalled = None
        self.parameterCounter = 0
        self.callFromReturn = 0
        #########################
        self.localVariableCount = 0
        self.tempVariableCount = 0

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

    def constantExists(self, constant):
        try:
            self.ctesTable[constant]
            return True
        except:
            return False

    def addConstant(self, constant, virtualAddress, typeOfConstant):
        self.ctesTable[constant] = {'virtualAddress': virtualAddress, 'type' : typeOfConstant}

    def scopeExists(self, scopeName):
        return self.variablesTable[scopeName]

    def createScope(self, scopeName, returnType):
        if scopeName == 'global':
            self.variablesTable[scopeName] = {'returnType': returnType, 'variables' : {}}
        else:
            self.variablesTable[scopeName] = {'returnType': returnType, 'parameters' : [], 'variables' : {}}

    def createVariable(self, variableName, virtualAddress):
        if self.currentScope:
            self.variablesTable[self.currentScope]['variables'][variableName] = {'type' : self.currentType, 'virtualAddress' : virtualAddress, 'isArray' : False}
        else:
            self.variablesTable['global']['variables'][variableName] = {'type' : self.currentType, 'virtualAddress' : virtualAddress, 'isArray' : False}
    
    def variableExists(self, variableName):
        return self.variablesTable[self.currentScope]['variables'][variableName]
    
    def isVariableArray(self):
        if self.currentScope == None:
            return self.variablesTable['global']['variables'][self.currentId]['isArray']
        else:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['isArray']
    
    def setVariableAsArray(self):
        self.variablesTable[self.currentScope]['variables'][self.currentId]['isArray'] = True
        self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'] = []

    def addArrayDimensionSize(self, size):
        self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'].append(size)

    def getArrayDimensions(self, variable):
        if self.currentScope == None:
            return self.variablesTable['global']['variables'][variable]['arrayDimensions']
        else:
            return self.variablesTable[self.currentScope]['variables'][variable]['arrayDimensions']

    def getArrayDimensionsSize(self):
        if len(self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions']) == 2:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][0] * self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][1]
        else:
            return self.variablesTable[self.currentScope]['variables'][self.currentId]['arrayDimensions'][0]

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

    def addFunctionStart(self, quadrupleManager):
        self.variablesTable[self.currentScope]['startsAt'] = quadrupleManager.quadrupleCounter

    def getFunctionStart(self):
        return self.variablesTable[self.functionCalled]['startsAt']

    def addParameterToList(self, paramName, paramType):
            self.variablesTable[self.currentScope]['parameters'].append(paramType)
            self.variablesTable[self.currentScope]['variables'][paramName] = {'type' : paramType}

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
    
    def areParametersFinished(self):
        return self.parameterCounter == len(self.variablesTable[self.functionCalled]['parameters'])

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
        
    def isVoid(self):
        return self.variablesTable[self.functionCalled]['returnType'] == 'void'

    def getReturnType(self, functionName):
        return self.variablesTable[functionName]['returnType']

    def releaseVars(self):
        # release vartable, end function, update temporal var count
        self.functionDirectory['varTable'].clear()
    
    #TODO: count parameters and give parameters virutal addresses
    def createEra(self, virtualDirectory):
        # [ints, floats, chars]
        locales = [virtualDirectory.localIntsCounter - virtualDirectory.CharRanges[0], virtualDirectory.localFloatsCounter - virtualDirectory.IntRanges[1], virtualDirectory.localCharsCounter - virtualDirectory.FloatRanges[1]]
        # [ints, floats, bools]
        temporales = [virtualDirectory.tempIntsCounter - virtualDirectory.CharRanges[2], virtualDirectory.tempFloatsCounter - virtualDirectory.IntRanges[3], virtualDirectory.tempBoolsCounter - virtualDirectory.FloatRanges[3]]
        self.variablesTable[self.currentScope]['era'] = [locales, temporales]
    
    def getEra(self):
        return self.variablesTable[self.functionCalled]['era']

    def turnCtesIntoList(self):
        aux = self.ctesTable.items()
        ctes = []
        addresses = []
        for x in aux:
            ctes.append(x[0])
            addresses.append(x[1]['virtualAddress'])
        return  sorted(list(zip(ctes, addresses)), key=lambda tup: tup[1])


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