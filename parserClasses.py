# variablesTable guarda las variables globales y de las funciones
class FunctionDirectory(object):

    def __init__(self):
        #variablesTable tiene el formato de {nombreScope : {returnType : valor, variables : {nombreVar1 : {type : valor, value : valor}, nombreVar2 : {type : valor, value : valor}, etc}}} 
        self.variablesTable = {}
        self.currentScope = None
        self.currentType = None
        self.currentId = None
        self.functionCalled = None
        self.parameterCounter = 0
        self.callFromReturn = 0
        #########################
        self.localVariableCount = 0
        self.tempVariableCount = 0

    def scopeExists(self, scopeName):
        return self.variablesTable[scopeName]

    def createScope(self, scopeName, returnType):
        if scopeName == 'global':
            self.variablesTable[scopeName] = {'returnType': returnType, 'variables' : {}}
        else:
            self.variablesTable[scopeName] = {'returnType': returnType, 'parameters' : [], 'variables' : {}}

    def createVariable(self, variableName):
        self.variablesTable[self.currentScope]['variables'][variableName] = {'type' : self.currentType}
    
    def variableExists(self, variableName):
        return self.variablesTable[self.currentScope]['variables'][variableName]
    
    def currentVariableValue(self):
        return self.variablesTable[self.currentScope]['variables'][self.currentId]['value']
    
    def assignValueToCurrentVariable(self, value):
        self.variablesTable[self.currentScope]['variables'][self.currentId]['value'] = value

    def getTypeOfVariable(self, variableName):
        print(f'{variableName} del scope {self.currentScope}')
        if self.currentScope is None: 
            return self.variablesTable['global']['variables'][variableName]['type']
        else:
            try: 
                return self.variablesTable[self.currentScope]['variables'][variableName]['type']
            except:
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

    def releaseVars(self):
        # release vartable, end function, update temporal var count
        self.functionDirectory['varTable'].clear()

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