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