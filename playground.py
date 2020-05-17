import re

char = 'c'
entero = 12
flotante = 37.877

if re.search(r'\-?[0-9]+\.[0-9]+', str(char)):
    print('float')
elif re.search(r'\-?[0-9]+', str(char)):
    print('int')
else:
    print('char')