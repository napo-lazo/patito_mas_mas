from re import search
from sys import exit
from numpy import add, array, subtract, dot, linalg

class VirtualMachine(object):
    def __init__(self, data, ctes, eras):
        self.quadruplesList = data[0]
        self.initialEra = data[1]
        self.eras = eras
        
        self.globalInts = 1000
        self.globalFloats = 3500
        self.globalChars = 6000
        self.localInts = 8500
        self.localFloats = 11000
        self.localChars = 13500
        self.cteInts = 16000
        self.cteFloats = 18500
        self.cteChars = 21000
        self.tempInts = 23500
        self.tempFloats = 26000
        self.tempBools = 28500
        self.pointers = 31000

        self.GlobalIntsSize = data[1][0][0]
        self.GlobalFloatsSize = data[1][0][1]
        self.GlobalCharsSize = data[1][0][2]
        self.LocalIntsSize = [data[1][1][0]]
        self.LocalFloatsSize = [data[1][1][1]]
        self.LocalCharsSize = [data[1][1][2]]
        self.CteIntsSize = data[1][2][0]
        self.CteFloatsSize = data[1][2][1]
        self.CteCharsSize = data[1][2][2]
        self.TempIntsSize = [data[1][3][0]]
        self.TempFloatsSize = [data[1][3][1]]
        self.TempBoolsSize = [data[1][3][2]]

        GlobalSize = self.GlobalIntsSize + self.GlobalFloatsSize + self.GlobalCharsSize
        LocalSize = self.LocalIntsSize[-1] + self.LocalFloatsSize[-1] + self.LocalCharsSize[-1]
        CteSize = self.CteIntsSize + self.CteFloatsSize + self.CteCharsSize
        TempSize = self.TempIntsSize[-1] + self.TempFloatsSize[-1] + self.TempBoolsSize[-1]


        LocalAux = [None] * LocalSize
        TempAux = [None] * TempSize

        self.Globals = [None] * GlobalSize
        self.Locals = [LocalAux]
        self.Ctes = [x[0] for x in ctes] 
        self.Temps = [TempAux]
        self.Pointers = [None] * data[1][4][0]
        print(ctes)

    def allocateMemoryForFunction(self, era, parameterList):
        intParams = 0
        floatParams = 0
        charParams = 0
        eraValues = self.eras[era]
        LocalIntsSize = eraValues[0][0]
        self.LocalIntsSize.append(LocalIntsSize)
        LocalFloatsSize = eraValues[0][1]
        self.LocalFloatsSize.append(LocalFloatsSize)
        LocalCharsSize = eraValues[0][2]
        self.LocalCharsSize.append(LocalCharsSize)
        LocalSize = LocalIntsSize + LocalFloatsSize + LocalCharsSize
        LocalAux = [None] * LocalSize
        for i in range(0, len(parameterList)):
            if type(parameterList[i]) is str:
                LocalAux[LocalIntsSize + LocalFloatsSize + charParams] = parameterList[i]
                charParams += 1
            elif type(parameterList[i]) is float:
                LocalAux[LocalIntsSize + floatParams] = parameterList[i]
                floatParams += 1
            else:
                LocalAux[intParams] = parameterList[i]
                intParams += 1

        TempIntsSize = eraValues[1][0]
        self.TempIntsSize.append(TempIntsSize)
        TempFloatsSize = eraValues[1][1]
        self.TempFloatsSize.append(TempFloatsSize)
        TempBoolsSize = eraValues[1][2]
        self.TempBoolsSize.append(TempBoolsSize)
        TempSize = TempIntsSize + TempFloatsSize + TempBoolsSize
        TempAux = [None] * TempSize

        self.Locals.append(LocalAux)
        self.Temps.append((TempAux))

    def getTypeOfInput(self, value):
        if value[0] == "'" and value[-1] == "'":
            if len(value) == 3:
                return 'char'
            else:
                print('Error: valor de tipo char tiene que ir entre comillas sencillas y ser un solo caracter')
                exit()
        elif search(r'\-?[0-9]+\.[0-9]+', value):
            return 'float'
        elif search(r'\-?[0-9]+', value):
            return 'int'
        else:
            print('Error: valor de tipo char tiene que ir entre comillas sencillas y ser un solo caracter')
            exit()


    def verifyInputCompatibility(self, address, typeOfValue):
        if address >= 1000 and address < 3500 and typeOfValue == 'int':
            return True
        elif address >= 3500 and address < 6000 and typeOfValue == 'float':
            return True
        elif address >= 6000 and address < 8500 and typeOfValue == 'char':
            return True
        elif address >= 8500 and address < 11000 and typeOfValue == 'int':
            return True
        elif address >= 11000 and address < 13500 and typeOfValue == 'float':
            return True
        elif address >= 13500 and address < 16000 and typeOfValue == 'char':
            return True
        return False

    def getValueFromAddress(self, address):
        if address >= self.pointers:
            # print(f'dir: {self.Pointers[address - self.pointers]}')
            return self.getValueFromAddress(self.Pointers[address - self.pointers])
        if address < self.localInts and address >= self.globalInts:
            if address < self.globalFloats:
                aux = address - self.globalInts
            elif address < self.globalChars:
                aux = address - self.globalFloats
                aux += self.GlobalIntsSize
            else:
                aux = address - self.globalChars
                aux += self.GlobalIntsSize + self.GlobalFloatsSize
            return self.Globals[int(aux)]
        elif address < self.cteInts and address >= self.localInts:
            if address < self.localFloats:
                aux = address - self.localInts
            elif address < self.localChars:
                aux = address - self.localFloats
                aux += self.LocalIntsSize[-1]
            else:
                aux = address - self.localChars
                aux += self.LocalIntsSize[-1] + self.LocalFloatsSize[-1]
            return self.Locals[-1][aux]
        elif address < self.tempInts and address >= self.cteInts:
            if address < self.cteFloats:
                aux = address - self.cteInts
            elif address < self.cteChars:
                aux = address - self.cteFloats
                aux += self.CteIntsSize
            else:
                aux = address - self.cteChars
                aux += self.CteIntsSize + self.CteFloatsSize
            return self.Ctes[aux]
        elif address < 31000 and address >= self.tempInts:
            if address < self.tempFloats:
                aux = address - self.tempInts
            elif address < self.tempBools:
                aux = address - self.tempFloats + self.TempIntsSize[-1]
            else:
                aux = address - self.tempBools + self.TempIntsSize[-1] + self.TempFloatsSize[-1]
            return self.Temps[-1][aux]


    def setAddressToValue(self, address, value):
        if address >= self.pointers:
            self.setAddressToValue(self.Pointers[address - self.pointers], value)
        if address < self.localInts and address >= self.globalInts:
            if address < self.globalFloats:
                self.Globals[address - self.globalInts] = value
            elif address < self.globalChars:
                self.Globals[int(address - self.globalFloats + self.GlobalIntsSize) ] = value
            else:
                self.Globals[int(address - self.globalChars + self.GlobalIntsSize + self.GlobalFloatsSize)] = value
        elif address < self.cteInts and address >= self.localInts:
            if address < self.localFloats:
                self.Locals[-1][address - self.localInts] = value
            elif address < self.localChars:
                self.Locals[-1][address - self.localFloats + self.LocalIntsSize[-1]] = value
            else:
                self.Locals[-1][address - self.localChars + self.LocalIntsSize[-1] + self.LocalFloatsSize[-1]] = value
        elif address < 31000 and address >= self.tempInts:
            if address < self.tempFloats:
                self.Temps[-1][address - self.tempInts] = value
            elif address < self.tempBools:
                self.Temps[-1][address - self.tempFloats + self.TempIntsSize[-1]] = value
            else:
                self.Temps[-1][address - self.tempBools + self.TempIntsSize[-1] + self.TempFloatsSize[-1]] = value

    def convertToMatrix(self, initialAddress, dimensions):

        matrixValues = []
        rowValues = []

        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                aux = initialAddress + i * dimensions[1] + j
                rowValues.append(self.getValueFromAddress(aux))
            matrixValues.append(rowValues.copy())
            rowValues.clear()

        return matrixValues

    def setMatrixValuesToAddresses(self, matrixValues, initialAddress, dimensions):
        
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                self.setAddressToValue(initialAddress + i * dimensions[1] + j, matrixValues[i][j])

    def executeProgram(self):
        parameterList = []
        indexStack = []
        i = 0
        n = len(self.quadruplesList)
        while i < n:
            current = self.quadruplesList[i]
            # print(current[0])
            if(current[0] == 'GOTO'):
                i = int(current[3]) - 1
            elif(current[0] == '='):
                self.setAddressToValue(current[3], self.getValueFromAddress(current[1]))
            elif(current[0] in ['+', '-', '*', '/', '>', '>=', '<', '<=', '==', '!=', '&&', '||']):
                leftOperand = self.getValueFromAddress(current[1])
                rightOperand = self.getValueFromAddress(current[2])
                if current[0] == '+' and current[3] >= self.pointers:
                    self.Pointers[current[3] - self.pointers] = eval(f'{leftOperand} + {rightOperand}')
                else:
                    if current[0] == '&&':
                        result = eval(f'{leftOperand} and {rightOperand}')
                    elif current[0] == '||':
                        result = eval(f'{leftOperand} or {rightOperand}')
                    else:
                        result = eval(f'{leftOperand} {current[0]} {rightOperand}')
                    self.setAddressToValue(current[3], result)
            elif(current[0] in ['+Mat', '-Mat', '*Mat']):
                leftOperand = self.convertToMatrix(current[1][0], current[1][1])
                rightOperand = self.convertToMatrix(current[2][0], current[2][1])
                if current[0] == '+Mat':
                    self.setMatrixValuesToAddresses(add(array(leftOperand), array(rightOperand)), current[3][0], current[3][1])
                elif current[0] == '-Mat':
                    self.setMatrixValuesToAddresses(subtract(array(leftOperand), array(rightOperand)), current[3][0], current[3][1])
                elif current[0] == '*Mat':
                    self.setMatrixValuesToAddresses(dot(array(leftOperand), array(rightOperand)), current[3][0], current[3][1])
            elif(current[0] in ['=Mat']):
                self.setMatrixValuesToAddresses(self.convertToMatrix(current[1][0], current[1][1]) ,current[3][0], current[3][1])
            elif(current[0] in ['!']):
                operand = self.getValueFromAddress(current[1])
                if current[0] == '!':
                    result = eval(f'not {operand}')
                self.setAddressToValue(current[3], result)
                print(self.Temps)
            elif(current[0] == '?'):
                operand = self.convertToMatrix(current[1][0], current[1][1])
                self.setMatrixValuesToAddresses(linalg.inv(array(operand)), current[3][0], current[3][1])
            elif(current[0] == '¡'):
                operand = self.convertToMatrix(current[1][0], current[1][1])
                self.setMatrixValuesToAddresses((array(operand)).transpose(), current[3][0], current[3][1])
            elif(current[0] == '$'):
                operand = self.convertToMatrix(current[1][0], current[1][1])
                result = linalg.det(array(operand))
                self.setAddressToValue(current[3], result)
            elif(current[0] == 'GOTOF'):
                if not self.getValueFromAddress(current[1]):
                    i = int(current[3]) - 1
            elif(current[0] == 'ESCRIBE'):
                # print(self.Pointers)
                if type(current[1]) is str:
                    print(current[1])
                else:
                    aux = self.getValueFromAddress(current[1])
                    if aux == None:
                        print('Error: Escribir necesita tener un valor para poder imprimirlo')
                        exit()
                    if type(aux) is str:
                        print(aux[1])
                    else:
                        print(aux)
            elif(current[0] == 'LEE'):
                aux = input(f'Escribe el valor que desea guardar: ')
                if self.verifyInputCompatibility(current[3], self.getTypeOfInput(aux)):
                    self.setAddressToValue(current[3], aux)
                else:
                    print('Error: Los tipos no son compatibles')
                    exit()
            elif(current[0] == 'VERIFY'):
                if self.getValueFromAddress(current[1]) >= self.getValueFromAddress(current[3]):
                    print('Error: indice es mayor que el tama;o del arreglo')
                    exit()
            elif(current[0] == 'GOSUB'):
                indexStack.append(i)
                i = current[3] - 1
            elif(current[0] == 'ENDFUNC'):
                print('Locals: ', self.Locals[-1])
                i = indexStack.pop()
                self.Locals.pop()
                self.Temps.pop()
                self.LocalIntsSize.pop()
                self.LocalFloatsSize.pop()
                self.LocalCharsSize.pop()
                self.TempIntsSize.pop()
                self.TempFloatsSize.pop()
                self.TempBoolsSize.pop()
            elif(current[0] == 'ERA'):
                self.allocateMemoryForFunction(current[3], parameterList)
                parameterList.clear()
            elif(current[0] == 'RETURN'):
                self.setAddressToValue(current[3], self.getValueFromAddress(current[1]))
                i = indexStack.pop()
                self.Locals.pop()
                self.Temps.pop()
                self.LocalIntsSize.pop()
                self.LocalFloatsSize.pop()
                self.LocalCharsSize.pop()
                self.TempIntsSize.pop()
                self.TempFloatsSize.pop()
                self.TempBoolsSize.pop()
            elif(current[0] == 'PARAMETER'):
                parameterList.append(self.getValueFromAddress(current[1]))
            
            i += 1
        print(self.Globals)