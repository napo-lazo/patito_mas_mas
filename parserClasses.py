# variablesTable guarda las variables globales y de las funciones
class VariablesTable(object):

    def __init__(self):
        #variablesTable tiene el formato de {nombreScope : {returnType : valor, variables : {nombreVar1 : {type : valor, value : valor}, nombreVar2 : {type : valor, value : valor}, etc}}} 
        self.variablesTable = {}
        self.currentScope = None
        self.currentType = None
        self.currentId = None

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

    def addParameterToList(self, paramName, paramType):
            self.variablesTable[self.currentScope]['parameters'].append(paramType)
            self.variablesTable[self.currentScope]['variables'][paramName] = {'type' : paramType}

class FunctionDirectory(object):
    # funcDir = {'nameid': {'returnType': <datatype> , 'parameters': [],'varTable': <table>}, 'size': <ERA>}
    def __init__(self):
        self.functionDirectory={}
        self.parameterCount = 0
        self.localVariableCount = 0
        self.tempVariableCount = 0
        # Con este defines en donde empieza la funcion
        self.quadrupleCounter = 0

    def createFunction(self, functionName, returnType, parameters):
        self.functionDirectory[functionName] = {'returnType': returnType, 'parameters': [], 'varTable': VariablesTable()}
        # activation record , crea un espacio en memoria 
        # se puede leer la funcion, identificar y contar variables para reservar espacios de ese tamano 
        # con la ayuda de varTable asignandoles direcciones a cada variable
    
    #def variableCount(self, vartype):
        # count number of ints, floats, chars or booleans
    
    def releaseVars(self):
        # release vartable, end function, update temporal var count
        self.functionDirectory['varTable'].clear()
