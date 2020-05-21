from re import search
from sys import exit

class VirtualMachine(object):
    def __init__(self, data, ctes):
        self.quadruplesList = data[0]
        self.initialEra = data[1]
        
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

        self.GlobalIntsSize = data[1][0][0]
        self.GlobalFloatsSize = data[1][0][1]
        self.GlobalCharsSize = data[1][0][2]
        self.CteIntsSize = data[1][2][0]
        self.CteFloatsSize = data[1][2][1]
        self.CteCharsSize = data[1][2][2]
        self.TempIntsSize = data[1][3][0]
        self.TempFloatsSize = data[1][3][1]
        self.TempBoolsSize = data[1][3][2]

        GlobalSize = self.GlobalIntsSize + self.GlobalFloatsSize + self.GlobalCharsSize
        LocalSize = data[1][1][0] + data[1][1][1] + data[1][1][2]
        CteSize = self.CteIntsSize + self.CteFloatsSize + self.CteCharsSize
        TempSize = self.TempIntsSize + self.TempFloatsSize + self.TempBoolsSize


        LocalAux = [None] * LocalSize
        TempAux = [None] * TempSize

        self.Globals = [None] * GlobalSize
        self.Locals = [LocalAux]
        self.Ctes = [x[0] for x in ctes] 
        self.Temps = [TempAux]
        print(ctes)

    def getTypeOfInput(self, value):
        if search(r'\-?[0-9]+\.[0-9]+', value):
            return 'float'
        elif search(r'\-?[0-9]+', value):
            return 'int'
        else:
            #TODO: add size verification
            return 'char'

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
        if address < self.localInts and address >= self.globalInts:
            if address < self.globalFloats:
                aux = address - self.globalInts
            elif address < self.globalChars:
                aux = address - self.globalFloats
                aux += self.GlobalIntsSize
            else:
                aux = address - self.globalChars
                aux += self.GlobalIntsSize + self.GlobalFloatsSize
            return self.Globals[aux]
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
                aux = address - self.tempFloats + self.TempIntsSize
            else:
                aux = address - self.tempBools + self.TempIntsSize + self.TempFloatsSize
            return self.Temps[-1][aux]


    def setAddressToValue(self, address, value):
        if address < self.localInts and address >= self.globalInts:
            if address < self.globalFloats:
                self.Globals[address - self.globalInts] = value
            elif address < self.globalChars:
                self.Globals[address - self.globalFloats + self.GlobalIntsSize] = value
            else:
                self.Globals[address - self.globalChars + self.GlobalIntsSize + self.GlobalFloatsSize] = value
                
        elif address < 31000 and address >= self.tempInts:
            if address < self.tempFloats:
                self.Temps[-1][address - self.tempInts] = value
            elif address < self.tempBools:
                self.Temps[-1][address - self.tempFloats + self.TempIntsSize] = value
            else:
                self.Temps[-1][address - self.tempBools + self.TempIntsSize + self.TempFloatsSize] = value

    def executeProgram(self):
        i = 0
        n = len(self.quadruplesList)
        while i < n:
            current = self.quadruplesList[i]
            if(current[0] == 'GOTO'):
                i = int(current[3]) - 1
            elif(current[0] == '='):
                self.setAddressToValue(current[3], self.getValueFromAddress(current[1]))
            elif(current[0] in ['+', '-', '*', '/', '>', '>=', '<', '<=', '==', '!=']):
                leftOperand = self.getValueFromAddress(current[1])
                rightOperand = self.getValueFromAddress(current[2])
                result = eval(f'{leftOperand} {current[0]} {rightOperand}')
                self.setAddressToValue(current[3], result)
            elif(current[0] == 'GOTOF'):
                if not self.getValueFromAddress(current[1]):
                    i = int(current[3]) - 1
            elif(current[0] == 'ESCRIBE'):
                if type(current[1]) is str:
                    print(current[1])
                else:
                    aux = self.getValueFromAddress(current[1])
                    if type(aux) is str:
                        print(aux[1])
                    else:
                        print(aux)
            elif(current[0] == 'LEE'):
                aux = input(f'Escribe el valor que desea guardar: ')
                if self.verifyInputCompatibility(current[3], self.getTypeOfInput(aux)):
                    self.setAddressToValue(current[3], aux)
                else:
                    #TODO: end program on error
                    print('Types are not compatible')
            elif(current[0] == 'VERIFY'):
                index = self.getValueFromAddress(current[1])
                if index >= current[3]:
                    print('Error: indice es mayor que el tama;o del arreglo')
                    exit()
            # elif(current[0] == 'DISPLACE'):
            #     leftOperand = current[1]
            #     rightOperand = self.getValueFromAddress(current[2]) 
            #     self.setAddressToValue(current[3], leftOperand + rightOperand)
            #     tempIndex = 1
            #     while True:
            #         try:
            #             temp = list(self.quadruplesList[i + tempIndex])
            #             indexToReplace = temp.index(current[3])
            #             temp[indexToReplace] = self.getValueFromAddress(current[3])
            #             self.quadruplesList[i + tempIndex] = temp
            #             break
            #         except:
            #             tempIndex += 1
            # elif(current[0] == 'DISPLACEMAT'):
            #     leftOperand = self.getValueFromAddress(current[1])
            #     rightOperand = self.getValueFromAddress(current[2]) 
            #     self.setAddressToValue(current[3], leftOperand + rightOperand)
            #     print(leftOperand * rightOperand + 1)


            i += 1