import ply.lex as lex

tokens = [
    'TEST'
]

t_TEST = r'test'
    

class ProxyLexer:

    def __init__(self, originalLex):
        self.lexer = originalLex

  

originalLex = lex.lex()
lexer = ProxyLexer(originalLex)

lexer.lexer.curlyBalance = 0
lexer.lexer.curlyBalance = 2
print(lexer.lexer.curlyBalance)