
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR COLON COMMA CTE_CHAR CTE_FLOAT CTE_INT DESDE DETERMINANT DIVIDE EQUALS ESCRIBE FLOAT FUNCION GREATER_THAN GREATER_THAN_EQUAL HACER HASTA HAZ ID INT INVERSE LECTURA LESS_THAN LESS_THAN_EQUAL LETRERO LPARENTHESIS L_CURLY_BRACKET L_SQUARE_BRACKET MIENTRAS MULTIPLY NOT NOT_EQUAL OR PRINCIPAL PROGRAMA REGRESA RPARENTHESIS R_CURLY_BRACKET R_SQUARE_BRACKET SEMICOLON SI SINO SUBTRACT SUM TRANSPOSED VAR VOID\n    start : programa\n    \n    programa : PROGRAMA ID SEMICOLON var\n    \n    var : VAR varp\n        | empty\n    \n    varp : tipo COLON ID varppp varpp SEMICOLON varpppp\n    \n    varpp : COMMA ID varppp varpp\n          | empty\n    \n    varppp : dimDeclare\n           | dimDeclare dimDeclare\n           | empty\n    \n    varpppp : varp\n            | empty\n    \n    dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET\n    \n    tipo : INT\n         | FLOAT\n         | CHAR\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAMA':([0,],[3,]),'$end':([1,2,5,6,8,9,25,28,29,30,],[0,-1,-17,-2,-4,-3,-17,-5,-11,-12,]),'ID':([3,14,21,],[4,15,26,]),'SEMICOLON':([4,15,16,17,18,20,22,23,26,27,31,32,],[5,-17,-17,-8,-10,25,-7,-9,-17,-13,-17,-6,]),'VAR':([5,],[7,]),'INT':([7,25,],[11,11,]),'FLOAT':([7,25,],[12,12,]),'CHAR':([7,25,],[13,13,]),'COLON':([10,11,12,13,],[14,-14,-15,-16,]),'L_SQUARE_BRACKET':([15,17,26,27,],[19,19,19,-13,]),'COMMA':([15,16,17,18,23,26,27,31,],[-17,21,-8,-10,-9,-17,-13,21,]),'CTE_INT':([19,],[24,]),'R_SQUARE_BRACKET':([24,],[27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'programa':([0,],[2,]),'var':([5,],[6,]),'empty':([5,15,16,25,26,31,],[8,18,22,30,18,22,]),'varp':([7,25,],[9,29,]),'tipo':([7,25,],[10,10,]),'varppp':([15,26,],[16,31,]),'dimDeclare':([15,17,26,],[17,23,17,]),'varpp':([16,31,],[20,32,]),'varpppp':([25,],[28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> programa','start',1,'p_start','patito.py',121),
  ('programa -> PROGRAMA ID SEMICOLON var','programa',4,'p_programa','patito.py',127),
  ('var -> VAR varp','var',2,'p_variables','patito.py',133),
  ('var -> empty','var',1,'p_variables','patito.py',134),
  ('varp -> tipo COLON ID varppp varpp SEMICOLON varpppp','varp',7,'p_variablesp','patito.py',140),
  ('varpp -> COMMA ID varppp varpp','varpp',4,'p_variablespp','patito.py',146),
  ('varpp -> empty','varpp',1,'p_variablespp','patito.py',147),
  ('varppp -> dimDeclare','varppp',1,'p_variablesppp','patito.py',153),
  ('varppp -> dimDeclare dimDeclare','varppp',2,'p_variablesppp','patito.py',154),
  ('varppp -> empty','varppp',1,'p_variablesppp','patito.py',155),
  ('varpppp -> varp','varpppp',1,'p_variablespppp','patito.py',164),
  ('varpppp -> empty','varpppp',1,'p_variablespppp','patito.py',165),
  ('dimDeclare -> L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET','dimDeclare',3,'p_dimDeclare','patito.py',171),
  ('tipo -> INT','tipo',1,'p_tipo','patito.py',177),
  ('tipo -> FLOAT','tipo',1,'p_tipo','patito.py',178),
  ('tipo -> CHAR','tipo',1,'p_tipo','patito.py',179),
  ('empty -> <empty>','empty',0,'p_empty','patito.py',185),
]
