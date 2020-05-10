
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR COLON COMMA CTE_CHAR CTE_FLOAT CTE_INT DESDE DETERMINANT DIVIDE EOF EQUALS ESCRIBE FLOAT FUNCION GREATER_THAN GREATER_THAN_EQUAL HACER HASTA HAZ ID INT INVERSE LECTURA LESS_THAN LESS_THAN_EQUAL LETRERO L_CURLY_BRACKET L_PARENTHESIS L_SQUARE_BRACKET MIENTRAS MULTIPLY NOT NOT_EQUAL OR PRINCIPAL PROGRAMA REGRESA R_CURLY_BRACKET R_PARENTHESIS R_SQUARE_BRACKET SEMICOLON SI SINO SUBTRACT SUM TRANSPOSED VAR VOID\n    start : programa\n    \n    programa : PROGRAMA ID SEMICOLON var funcion clear_scope PRINCIPAL L_PARENTHESIS R_PARENTHESIS bloque EOF\n    \n    clear_scope :\n    \n    var : VAR var_seen varp\n        | empty\n     \n    var_seen :\n    \n    varp : tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp\n         | tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp\n    \n    tipo_seen :\n    \n    variable_seen : \n    \n    delete_type :\n    \n    varpp : COMMA ID variable_seen varppp varpp\n          | empty\n    \n    varppp : dimDeclare\n           | dimDeclare dimDeclare\n           | empty\n    \n    varpppp : varp\n            | empty\n    \n    dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET\n    \n    tipo : INT\n         | FLOAT\n         | CHAR\n    \n    funcion : FUNCION funcionp\n            | FUNCION error\n            | empty\n    \n    funcionp : tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque funcion\n    \n    create_func_scope : \n    \n    parametro : tipo ID save_param parametrop\n              | empty\n    \n    save_param :\n    \n    parametrop : COMMA tipo ID save_param parametrop\n               | empty\n    \n    tipoRetorno : tipo\n                | VOID\n    \n    bloque : L_CURLY_BRACKET bloquep R_CURLY_BRACKET\n    \n    bloquep : estatuto bloquep\n            | empty\n    \n    estatuto : asignacion\n             | funcionVacia\n             | regresa\n             | lectura\n             | escritura\n             | decision\n             | cicloCondicional\n             | cicloNoCondicional\n    \n    asignacion : ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON\n    \n    operand_seen :\n    \n    apply_operation_assign : \n    \n    dimId : dim\n                | dim dim\n                | empty\n    \n    dim : L_SQUARE_BRACKET expresion R_SQUARE_BRACKET\n    \n    expresion : relacional apply_operation_expresion expresionp\n              | NOT relacional expresionp\n    \n    expresionp : AND operation_seen expresion\n               | OR operation_seen expresion\n               | empty\n    \n    apply_operation_expresion : \n    \n    relacional : aritmetica apply_operation_relational relacionalp\n    \n    relacionalp : EQUALS operation_seen relacional\n                | NOT_EQUAL operation_seen relacional\n                | LESS_THAN operation_seen relacional\n                | LESS_THAN_EQUAL operation_seen relacional\n                | GREATER_THAN operation_seen relacional\n                | GREATER_THAN_EQUAL operation_seen relacional\n                | empty\n    \n    apply_operation_relational : \n    \n    aritmetica : factor apply_operation_aritmetica aritmeticap\n    \n    aritmeticap : SUM operation_seen aritmetica\n                | SUBTRACT operation_seen aritmetica\n                | empty\n    \n    apply_operation_aritmetica : \n    \n    factor : matriz apply_operation_factor factorp\n    \n    factorp : MULTIPLY operation_seen factor \n            | DIVIDE operation_seen factor \n            | empty\n    \n    apply_operation_factor : \n    \n    operation_seen : \n    \n    matriz : cte matrizp\n    \n    matrizp : DETERMINANT\n            | TRANSPOSED\n            | INVERSE\n            | empty\n    \n    cte : CTE_INT\n        | CTE_FLOAT\n        | CTE_CHAR\n        | llamadaFuncion\n        | ID operand_seen dimId\n        | L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen\n    \n    llamadaFuncion : ID L_PARENTHESIS expresion llamadaFuncionp R_PARENTHESIS\n    \n    llamadaFuncionp : COMMA expresion\n                    | empty\n    \n    funcionVacia : ID L_PARENTHESIS expresion llamadaFuncionp R_PARENTHESIS SEMICOLON\n    \n    regresa : REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON\n    \n    lectura : LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON\n    \n    lecturap : ID dimId lecturapp\n    \n    lecturapp : COMMA lecturap\n              | empty\n    \n    escritura : ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON\n    \n    escriturap : LETRERO escriturapp\n               | expresion escriturapp\n    \n    escriturapp : COMMA escriturap\n                | empty\n    \n    decision : SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp\n    \n    jump_false : \n    \n    update_jump :\n    \n    decisionp : SINO jump_else bloque update_jump\n              | empty update_jump\n    \n    jump_else :\n    \n    cicloCondicional : MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle\n    \n    jump_cycle : \n    \n    update_jump_cycle : \n    \n    cicloNoCondicional : DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle\n    \n    add_gt :\n    \n    add_one : \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAMA':([0,],[3,]),'$end':([1,2,40,],[0,-1,-2,]),'ID':([3,16,17,18,19,20,21,29,34,36,42,44,45,46,47,48,49,50,51,58,66,69,70,71,72,73,79,87,89,92,108,118,122,123,125,142,149,153,161,162,166,167,168,169,170,171,174,175,178,179,181,182,184,186,190,200,201,202,203,204,205,206,207,208,209,210,211,212,216,234,238,239,241,242,245,246,247,248,250,256,257,258,],[4,25,-33,-34,-20,-21,-22,32,52,60,52,-38,-39,-40,-41,-42,-43,-44,-45,75,-35,88,88,103,88,88,115,88,-78,88,88,-78,88,88,88,88,191,88,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-94,-95,103,-99,-78,-93,88,88,88,88,88,88,88,88,88,88,88,88,88,-116,-46,-104,-106,-112,-108,-110,88,-106,-107,-115,-112,-113,]),'SEMICOLON':([4,32,38,39,61,62,63,65,78,80,81,83,85,86,88,91,93,94,95,96,97,98,99,100,114,115,116,117,119,121,127,128,129,130,131,132,133,134,135,136,137,138,140,151,154,155,158,160,163,164,165,172,173,176,177,180,195,197,199,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,],[5,-10,-116,-116,-116,-14,-16,-116,-11,-13,-15,-11,-49,-51,-47,-58,-67,-72,-77,-116,-84,-85,-86,-87,150,-10,-19,152,-50,-116,-116,-116,-116,-116,-116,-79,-80,-81,-82,-83,181,182,186,-116,-52,-88,200,-53,-57,-54,-59,-66,-68,-71,-73,-76,-116,-48,-78,-12,238,-90,-89,-55,-56,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,]),'VAR':([5,59,],[7,7,]),'FUNCION':([5,6,8,22,66,110,150,152,192,193,194,196,],[-116,10,-5,-4,-35,10,-116,-116,-7,-17,-18,-8,]),'PRINCIPAL':([5,6,8,9,11,13,14,15,22,66,110,148,150,152,192,193,194,196,],[-116,-116,-5,-3,-25,24,-23,-24,-4,-35,-116,-26,-116,-116,-7,-17,-18,-8,]),'INT':([7,10,12,31,112,150,152,],[-6,19,19,19,19,19,19,]),'FLOAT':([7,10,12,31,112,150,152,],[-6,20,20,20,20,20,20,]),'CHAR':([7,10,12,31,112,150,152,],[-6,21,21,21,21,21,21,]),'L_CURLY_BRACKET':([8,22,30,59,76,150,152,192,193,194,196,214,235,240,244,255,],[-5,-4,34,-116,34,-116,-116,-7,-17,-18,-8,34,34,-109,34,34,]),'error':([10,32,],[15,39,]),'VOID':([10,],[18,]),'COLON':([19,20,21,23,26,],[-20,-21,-22,-9,29,]),'L_PARENTHESIS':([24,25,28,52,53,54,55,56,57,69,70,72,73,74,87,88,89,92,108,118,122,123,125,142,153,161,162,166,167,168,169,170,171,174,175,178,179,190,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[27,-27,31,69,70,71,72,73,-111,89,89,89,89,108,89,122,-78,89,89,-78,89,89,89,89,89,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'R_PARENTHESIS':([27,31,35,37,60,77,85,86,88,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,113,119,121,124,126,127,128,129,130,131,132,133,134,135,136,139,141,143,144,146,154,155,156,157,159,160,163,164,165,172,173,176,177,180,183,185,187,191,198,199,213,217,220,221,222,223,224,225,226,227,228,229,230,231,232,233,237,],[30,-116,59,-29,-30,-116,-49,-51,-47,-116,-58,-67,-72,-77,-116,-84,-85,-86,-87,137,138,-116,140,-116,-116,145,-28,-32,-50,-116,158,-92,-116,-116,-116,-116,-116,-79,-80,-81,-82,-83,-116,-100,-103,-101,189,-52,-88,-116,199,-91,-53,-57,-54,-59,-66,-68,-71,-73,-76,-96,-98,-102,-30,220,-78,-97,-116,-90,-89,-55,-56,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,-31,]),'L_SQUARE_BRACKET':([32,38,39,52,62,68,75,85,88,103,109,115,116,121,151,154,],[-10,64,64,-47,64,87,-47,87,-47,87,87,-10,-19,87,64,-52,]),'COMMA':([32,38,39,60,61,62,63,65,77,81,85,86,88,90,91,93,94,95,96,97,98,99,100,103,105,106,115,116,119,121,127,128,129,130,131,132,133,134,135,136,139,151,154,155,156,160,163,164,165,172,173,176,177,180,191,195,199,217,220,221,222,223,224,225,226,227,228,229,230,231,232,233,],[-10,-116,-116,-30,79,-14,-16,79,112,-15,-49,-51,-47,125,-58,-67,-72,-77,-116,-84,-85,-86,-87,-116,142,142,-10,-19,-50,-116,-116,-116,-116,-116,-116,-79,-80,-81,-82,-83,184,-116,-52,-88,125,-53,-57,-54,-59,-66,-68,-71,-73,-76,-30,79,-78,112,-90,-89,-55,-56,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,]),'EOF':([33,66,],[40,-35,]),'R_CURLY_BRACKET':([34,41,42,43,44,45,46,47,48,49,50,51,66,67,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[-116,66,-116,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-36,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'REGRESA':([34,42,44,45,46,47,48,49,50,51,66,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[53,53,-38,-39,-40,-41,-42,-43,-44,-45,-35,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'LECTURA':([34,42,44,45,46,47,48,49,50,51,66,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[54,54,-38,-39,-40,-41,-42,-43,-44,-45,-35,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'ESCRIBE':([34,42,44,45,46,47,48,49,50,51,66,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[55,55,-38,-39,-40,-41,-42,-43,-44,-45,-35,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'SI':([34,42,44,45,46,47,48,49,50,51,66,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[56,56,-38,-39,-40,-41,-42,-43,-44,-45,-35,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'MIENTRAS':([34,42,44,45,46,47,48,49,50,51,66,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[57,57,-38,-39,-40,-41,-42,-43,-44,-45,-35,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'DESDE':([34,42,44,45,46,47,48,49,50,51,66,181,182,186,200,234,238,239,241,242,245,246,248,250,256,257,258,],[58,58,-38,-39,-40,-41,-42,-43,-44,-45,-35,-94,-95,-99,-93,-116,-46,-104,-106,-112,-108,-110,-106,-107,-115,-112,-113,]),'ASSIGN':([52,68,75,84,85,86,109,119,147,154,],[-47,-116,-47,118,-49,-51,-116,-50,190,-52,]),'CTE_INT':([64,69,70,72,73,87,89,92,108,118,122,123,125,142,153,161,162,166,167,168,169,170,171,174,175,178,179,190,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[82,97,97,97,97,97,-78,97,97,-78,97,97,97,97,97,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'SINO':([66,234,],[-35,240,]),'NOT':([69,70,72,73,87,89,108,118,122,123,125,142,153,161,162,190,201,202,216,247,],[92,92,92,92,92,-78,92,-78,92,92,92,92,92,-78,-78,-78,92,92,92,92,]),'CTE_FLOAT':([69,70,72,73,87,89,92,108,118,122,123,125,142,153,161,162,166,167,168,169,170,171,174,175,178,179,190,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[98,98,98,98,98,-78,98,98,-78,98,98,98,98,98,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'CTE_CHAR':([69,70,72,73,87,89,92,108,118,122,123,125,142,153,161,162,166,167,168,169,170,171,174,175,178,179,190,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[99,99,99,99,99,-78,99,99,-78,99,99,99,99,99,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'LETRERO':([72,142,],[105,105,]),'R_SQUARE_BRACKET':([82,85,86,88,91,93,94,95,96,97,98,99,100,119,120,121,127,128,129,130,131,132,133,134,135,136,154,155,160,163,164,165,172,173,176,177,180,199,220,221,222,223,224,225,226,227,228,229,230,231,232,233,],[116,-49,-51,-47,-58,-67,-72,-77,-116,-84,-85,-86,-87,-50,154,-116,-116,-116,-116,-116,-116,-79,-80,-81,-82,-83,-52,-88,-53,-57,-54,-59,-66,-68,-71,-73,-76,-78,-90,-89,-55,-56,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,]),'DETERMINANT':([85,86,88,96,97,98,99,100,119,121,154,155,199,220,221,],[-49,-51,-47,133,-84,-85,-86,-87,-50,-116,-52,-88,-78,-90,-89,]),'TRANSPOSED':([85,86,88,96,97,98,99,100,119,121,154,155,199,220,221,],[-49,-51,-47,134,-84,-85,-86,-87,-50,-116,-52,-88,-78,-90,-89,]),'INVERSE':([85,86,88,96,97,98,99,100,119,121,154,155,199,220,221,],[-49,-51,-47,135,-84,-85,-86,-87,-50,-116,-52,-88,-78,-90,-89,]),'MULTIPLY':([85,86,88,95,96,97,98,99,100,119,121,131,132,133,134,135,136,154,155,199,220,221,],[-49,-51,-47,-77,-116,-84,-85,-86,-87,-50,-116,178,-79,-80,-81,-82,-83,-52,-88,-78,-90,-89,]),'DIVIDE':([85,86,88,95,96,97,98,99,100,119,121,131,132,133,134,135,136,154,155,199,220,221,],[-49,-51,-47,-77,-116,-84,-85,-86,-87,-50,-116,179,-79,-80,-81,-82,-83,-52,-88,-78,-90,-89,]),'SUM':([85,86,88,94,95,96,97,98,99,100,119,121,130,131,132,133,134,135,136,154,155,177,180,199,220,221,232,233,],[-49,-51,-47,-72,-77,-116,-84,-85,-86,-87,-50,-116,174,-116,-79,-80,-81,-82,-83,-52,-88,-73,-76,-78,-90,-89,-74,-75,]),'SUBTRACT':([85,86,88,94,95,96,97,98,99,100,119,121,130,131,132,133,134,135,136,154,155,177,180,199,220,221,232,233,],[-49,-51,-47,-72,-77,-116,-84,-85,-86,-87,-50,-116,175,-116,-79,-80,-81,-82,-83,-52,-88,-73,-76,-78,-90,-89,-74,-75,]),'EQUALS':([85,86,88,93,94,95,96,97,98,99,100,119,121,129,130,131,132,133,134,135,136,154,155,173,176,177,180,199,220,221,230,231,232,233,],[-49,-51,-47,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,166,-116,-116,-79,-80,-81,-82,-83,-52,-88,-68,-71,-73,-76,-78,-90,-89,-69,-70,-74,-75,]),'NOT_EQUAL':([85,86,88,93,94,95,96,97,98,99,100,119,121,129,130,131,132,133,134,135,136,154,155,173,176,177,180,199,220,221,230,231,232,233,],[-49,-51,-47,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,167,-116,-116,-79,-80,-81,-82,-83,-52,-88,-68,-71,-73,-76,-78,-90,-89,-69,-70,-74,-75,]),'LESS_THAN':([85,86,88,93,94,95,96,97,98,99,100,119,121,129,130,131,132,133,134,135,136,154,155,173,176,177,180,199,220,221,230,231,232,233,],[-49,-51,-47,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,168,-116,-116,-79,-80,-81,-82,-83,-52,-88,-68,-71,-73,-76,-78,-90,-89,-69,-70,-74,-75,]),'LESS_THAN_EQUAL':([85,86,88,93,94,95,96,97,98,99,100,119,121,129,130,131,132,133,134,135,136,154,155,173,176,177,180,199,220,221,230,231,232,233,],[-49,-51,-47,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,169,-116,-116,-79,-80,-81,-82,-83,-52,-88,-68,-71,-73,-76,-78,-90,-89,-69,-70,-74,-75,]),'GREATER_THAN':([85,86,88,93,94,95,96,97,98,99,100,119,121,129,130,131,132,133,134,135,136,154,155,173,176,177,180,199,220,221,230,231,232,233,],[-49,-51,-47,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,170,-116,-116,-79,-80,-81,-82,-83,-52,-88,-68,-71,-73,-76,-78,-90,-89,-69,-70,-74,-75,]),'GREATER_THAN_EQUAL':([85,86,88,93,94,95,96,97,98,99,100,119,121,129,130,131,132,133,134,135,136,154,155,173,176,177,180,199,220,221,230,231,232,233,],[-49,-51,-47,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,171,-116,-116,-79,-80,-81,-82,-83,-52,-88,-68,-71,-73,-76,-78,-90,-89,-69,-70,-74,-75,]),'AND':([85,86,88,91,93,94,95,96,97,98,99,100,119,121,127,128,129,130,131,132,133,134,135,136,154,155,165,172,173,176,177,180,199,220,221,224,225,226,227,228,229,230,231,232,233,],[-49,-51,-47,-58,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,161,161,-116,-116,-116,-79,-80,-81,-82,-83,-52,-88,-59,-66,-68,-71,-73,-76,-78,-90,-89,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,]),'OR':([85,86,88,91,93,94,95,96,97,98,99,100,119,121,127,128,129,130,131,132,133,134,135,136,154,155,165,172,173,176,177,180,199,220,221,224,225,226,227,228,229,230,231,232,233,],[-49,-51,-47,-58,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,162,162,-116,-116,-116,-79,-80,-81,-82,-83,-52,-88,-59,-66,-68,-71,-73,-76,-78,-90,-89,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,]),'HASTA':([85,86,88,91,93,94,95,96,97,98,99,100,119,121,127,128,129,130,131,132,133,134,135,136,154,155,160,163,164,165,172,173,176,177,180,199,220,221,222,223,224,225,226,227,228,229,230,231,232,233,236,243,],[-49,-51,-47,-58,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,-116,-116,-116,-116,-116,-79,-80,-81,-82,-83,-52,-88,-53,-57,-54,-59,-66,-68,-71,-73,-76,-78,-90,-89,-55,-56,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,-48,247,]),'HACER':([85,86,88,91,93,94,95,96,97,98,99,100,119,121,127,128,129,130,131,132,133,134,135,136,154,155,160,163,164,165,172,173,176,177,180,199,220,221,222,223,224,225,226,227,228,229,230,231,232,233,249,251,252,253,254,],[-49,-51,-47,-58,-67,-72,-77,-116,-84,-85,-86,-87,-50,-116,-116,-116,-116,-116,-116,-79,-80,-81,-82,-83,-52,-88,-53,-57,-54,-59,-66,-68,-71,-73,-76,-78,-90,-89,-55,-56,-60,-61,-62,-63,-64,-65,-69,-70,-74,-75,-111,-114,-67,-105,255,]),'HAZ':([145,188,189,215,],[-105,214,-105,235,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'programa':([0,],[2,]),'var':([5,59,],[6,76,]),'empty':([5,6,31,34,38,39,42,59,61,65,68,77,90,96,103,105,106,109,110,121,127,128,129,130,131,139,150,151,152,156,195,217,234,],[8,11,37,43,63,63,43,8,80,80,86,113,126,136,86,143,143,86,11,86,163,163,172,176,180,185,194,63,194,126,80,113,241,]),'funcion':([6,110,],[9,148,]),'var_seen':([7,],[12,]),'clear_scope':([9,],[13,]),'funcionp':([10,],[14,]),'tipoRetorno':([10,],[16,]),'tipo':([10,12,31,112,150,152,],[17,23,36,149,23,23,]),'varp':([12,150,152,],[22,193,193,]),'tipo_seen':([23,],[26,]),'create_func_scope':([25,],[28,]),'bloque':([30,76,214,235,244,255,],[33,110,234,242,248,256,]),'parametro':([31,],[35,]),'variable_seen':([32,115,],[38,151,]),'bloquep':([34,42,],[41,67,]),'estatuto':([34,42,],[42,42,]),'asignacion':([34,42,],[44,44,]),'funcionVacia':([34,42,],[45,45,]),'regresa':([34,42,],[46,46,]),'lectura':([34,42,],[47,47,]),'escritura':([34,42,],[48,48,]),'decision':([34,42,],[49,49,]),'cicloCondicional':([34,42,],[50,50,]),'cicloNoCondicional':([34,42,],[51,51,]),'varppp':([38,39,151,],[61,65,195,]),'dimDeclare':([38,39,62,151,],[62,62,81,62,]),'operand_seen':([52,75,88,],[68,109,121,]),'jump_cycle':([57,249,],[74,251,]),'save_param':([60,191,],[77,217,]),'varpp':([61,65,195,],[78,83,218,]),'dimId':([68,103,109,121,],[84,139,147,155,]),'dim':([68,85,103,109,121,],[85,119,85,85,85,]),'expresion':([69,70,72,73,87,108,122,123,125,142,153,201,202,216,247,],[90,101,106,107,120,146,156,157,159,106,197,222,223,236,249,]),'relacional':([69,70,72,73,87,92,108,122,123,125,142,153,201,202,203,204,205,206,207,208,216,247,],[91,91,91,91,91,128,91,91,91,91,91,91,91,91,224,225,226,227,228,229,91,91,]),'aritmetica':([69,70,72,73,87,92,108,122,123,125,142,153,201,202,203,204,205,206,207,208,209,210,216,247,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,230,231,93,93,]),'factor':([69,70,72,73,87,92,108,122,123,125,142,153,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,232,233,94,94,]),'matriz':([69,70,72,73,87,92,108,122,123,125,142,153,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'cte':([69,70,72,73,87,92,108,122,123,125,142,153,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'llamadaFuncion':([69,70,72,73,87,92,108,122,123,125,142,153,201,202,203,204,205,206,207,208,209,210,211,212,216,247,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'lecturap':([71,184,],[102,213,]),'escriturap':([72,142,],[104,187,]),'parametrop':([77,217,],[111,237,]),'delete_type':([78,83,],[114,117,]),'operation_seen':([89,118,161,162,166,167,168,169,170,171,174,175,178,179,190,199,],[123,153,201,202,203,204,205,206,207,208,209,210,211,212,216,221,]),'llamadaFuncionp':([90,156,],[124,198,]),'apply_operation_expresion':([91,],[127,]),'apply_operation_relational':([93,252,],[129,253,]),'apply_operation_aritmetica':([94,],[130,]),'apply_operation_factor':([95,],[131,]),'matrizp':([96,],[132,]),'escriturapp':([105,106,],[141,144,]),'expresionp':([127,128,],[160,164,]),'relacionalp':([129,],[165,]),'aritmeticap':([130,],[173,]),'factorp':([131,],[177,]),'lecturapp':([139,],[183,]),'jump_false':([145,189,253,],[188,215,254,]),'varpppp':([150,152,],[192,196,]),'apply_operation_assign':([197,236,],[219,243,]),'decisionp':([234,],[239,]),'jump_else':([240,],[244,]),'update_jump':([241,248,],[245,250,]),'update_jump_cycle':([242,257,],[246,258,]),'add_gt':([251,],[252,]),'add_one':([256,],[257,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> programa','start',1,'p_start','patitoParser.py',143),
  ('programa -> PROGRAMA ID SEMICOLON var funcion clear_scope PRINCIPAL L_PARENTHESIS R_PARENTHESIS bloque EOF','programa',11,'p_programa','patitoParser.py',161),
  ('clear_scope -> <empty>','clear_scope',0,'p_clear_scope','patitoParser.py',167),
  ('var -> VAR var_seen varp','var',3,'p_variables','patitoParser.py',176),
  ('var -> empty','var',1,'p_variables','patitoParser.py',177),
  ('var_seen -> <empty>','var_seen',0,'p_var_seen','patitoParser.py',194),
  ('varp -> tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp','varp',10,'p_variablesp','patitoParser.py',204),
  ('varp -> tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp','varp',10,'p_variablesp','patitoParser.py',205),
  ('tipo_seen -> <empty>','tipo_seen',0,'p_tipo_seen','patitoParser.py',214),
  ('variable_seen -> <empty>','variable_seen',0,'p_variable_seen','patitoParser.py',222),
  ('delete_type -> <empty>','delete_type',0,'p_delete_type','patitoParser.py',247),
  ('varpp -> COMMA ID variable_seen varppp varpp','varpp',5,'p_variablespp','patitoParser.py',256),
  ('varpp -> empty','varpp',1,'p_variablespp','patitoParser.py',257),
  ('varppp -> dimDeclare','varppp',1,'p_variablesppp','patitoParser.py',267),
  ('varppp -> dimDeclare dimDeclare','varppp',2,'p_variablesppp','patitoParser.py',268),
  ('varppp -> empty','varppp',1,'p_variablesppp','patitoParser.py',269),
  ('varpppp -> varp','varpppp',1,'p_variablespppp','patitoParser.py',285),
  ('varpppp -> empty','varpppp',1,'p_variablespppp','patitoParser.py',286),
  ('dimDeclare -> L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET','dimDeclare',3,'p_dimDeclare','patitoParser.py',293),
  ('tipo -> INT','tipo',1,'p_tipo','patitoParser.py',328),
  ('tipo -> FLOAT','tipo',1,'p_tipo','patitoParser.py',329),
  ('tipo -> CHAR','tipo',1,'p_tipo','patitoParser.py',330),
  ('funcion -> FUNCION funcionp','funcion',2,'p_funcion','patitoParser.py',336),
  ('funcion -> FUNCION error','funcion',2,'p_funcion','patitoParser.py',337),
  ('funcion -> empty','funcion',1,'p_funcion','patitoParser.py',338),
  ('funcionp -> tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque funcion','funcionp',9,'p_funcionp','patitoParser.py',347),
  ('create_func_scope -> <empty>','create_func_scope',0,'p_create_func_scope','patitoParser.py',355),
  ('parametro -> tipo ID save_param parametrop','parametro',4,'p_parametro','patitoParser.py',373),
  ('parametro -> empty','parametro',1,'p_parametro','patitoParser.py',374),
  ('save_param -> <empty>','save_param',0,'p_save_param','patitoParser.py',383),
  ('parametrop -> COMMA tipo ID save_param parametrop','parametrop',5,'p_parametrop','patitoParser.py',390),
  ('parametrop -> empty','parametrop',1,'p_parametrop','patitoParser.py',391),
  ('tipoRetorno -> tipo','tipoRetorno',1,'p_tipoRetorno','patitoParser.py',400),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','patitoParser.py',401),
  ('bloque -> L_CURLY_BRACKET bloquep R_CURLY_BRACKET','bloque',3,'p_bloque','patitoParser.py',407),
  ('bloquep -> estatuto bloquep','bloquep',2,'p_bloquep','patitoParser.py',413),
  ('bloquep -> empty','bloquep',1,'p_bloquep','patitoParser.py',414),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','patitoParser.py',423),
  ('estatuto -> funcionVacia','estatuto',1,'p_estatuto','patitoParser.py',424),
  ('estatuto -> regresa','estatuto',1,'p_estatuto','patitoParser.py',425),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','patitoParser.py',426),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','patitoParser.py',427),
  ('estatuto -> decision','estatuto',1,'p_estatuto','patitoParser.py',428),
  ('estatuto -> cicloCondicional','estatuto',1,'p_estatuto','patitoParser.py',429),
  ('estatuto -> cicloNoCondicional','estatuto',1,'p_estatuto','patitoParser.py',430),
  ('asignacion -> ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON','asignacion',8,'p_asignacion','patitoParser.py',436),
  ('operand_seen -> <empty>','operand_seen',0,'p_operand_seen','patitoParser.py',442),
  ('apply_operation_assign -> <empty>','apply_operation_assign',0,'p_apply_operation_assign','patitoParser.py',456),
  ('dimId -> dim','dimId',1,'p_dimId','patitoParser.py',465),
  ('dimId -> dim dim','dimId',2,'p_dimId','patitoParser.py',466),
  ('dimId -> empty','dimId',1,'p_dimId','patitoParser.py',467),
  ('dim -> L_SQUARE_BRACKET expresion R_SQUARE_BRACKET','dim',3,'p_dim','patitoParser.py',476),
  ('expresion -> relacional apply_operation_expresion expresionp','expresion',3,'p_expresion','patitoParser.py',483),
  ('expresion -> NOT relacional expresionp','expresion',3,'p_expresion','patitoParser.py',484),
  ('expresionp -> AND operation_seen expresion','expresionp',3,'p_expresionp','patitoParser.py',493),
  ('expresionp -> OR operation_seen expresion','expresionp',3,'p_expresionp','patitoParser.py',494),
  ('expresionp -> empty','expresionp',1,'p_expresionp','patitoParser.py',495),
  ('apply_operation_expresion -> <empty>','apply_operation_expresion',0,'p_apply_operation_expresion','patitoParser.py',505),
  ('relacional -> aritmetica apply_operation_relational relacionalp','relacional',3,'p_relacional','patitoParser.py',514),
  ('relacionalp -> EQUALS operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',520),
  ('relacionalp -> NOT_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',521),
  ('relacionalp -> LESS_THAN operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',522),
  ('relacionalp -> LESS_THAN_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',523),
  ('relacionalp -> GREATER_THAN operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',524),
  ('relacionalp -> GREATER_THAN_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',525),
  ('relacionalp -> empty','relacionalp',1,'p_relacionalp','patitoParser.py',526),
  ('apply_operation_relational -> <empty>','apply_operation_relational',0,'p_apply_operation_relational','patitoParser.py',536),
  ('aritmetica -> factor apply_operation_aritmetica aritmeticap','aritmetica',3,'p_aritmetica','patitoParser.py',545),
  ('aritmeticap -> SUM operation_seen aritmetica','aritmeticap',3,'p_aritmeticap','patitoParser.py',551),
  ('aritmeticap -> SUBTRACT operation_seen aritmetica','aritmeticap',3,'p_aritmeticap','patitoParser.py',552),
  ('aritmeticap -> empty','aritmeticap',1,'p_aritmeticap','patitoParser.py',553),
  ('apply_operation_aritmetica -> <empty>','apply_operation_aritmetica',0,'p_apply_operation_aritmetica','patitoParser.py',563),
  ('factor -> matriz apply_operation_factor factorp','factor',3,'p_factor','patitoParser.py',572),
  ('factorp -> MULTIPLY operation_seen factor','factorp',3,'p_factorp','patitoParser.py',578),
  ('factorp -> DIVIDE operation_seen factor','factorp',3,'p_factorp','patitoParser.py',579),
  ('factorp -> empty','factorp',1,'p_factorp','patitoParser.py',580),
  ('apply_operation_factor -> <empty>','apply_operation_factor',0,'p_apply_operation_factor','patitoParser.py',590),
  ('operation_seen -> <empty>','operation_seen',0,'p_operation_seen','patitoParser.py',600),
  ('matriz -> cte matrizp','matriz',2,'p_matriz','patitoParser.py',612),
  ('matrizp -> DETERMINANT','matrizp',1,'p_matrizp','patitoParser.py',618),
  ('matrizp -> TRANSPOSED','matrizp',1,'p_matrizp','patitoParser.py',619),
  ('matrizp -> INVERSE','matrizp',1,'p_matrizp','patitoParser.py',620),
  ('matrizp -> empty','matrizp',1,'p_matrizp','patitoParser.py',621),
  ('cte -> CTE_INT','cte',1,'p_cte','patitoParser.py',627),
  ('cte -> CTE_FLOAT','cte',1,'p_cte','patitoParser.py',628),
  ('cte -> CTE_CHAR','cte',1,'p_cte','patitoParser.py',629),
  ('cte -> llamadaFuncion','cte',1,'p_cte','patitoParser.py',630),
  ('cte -> ID operand_seen dimId','cte',3,'p_cte','patitoParser.py',631),
  ('cte -> L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen','cte',5,'p_cte','patitoParser.py',632),
  ('llamadaFuncion -> ID L_PARENTHESIS expresion llamadaFuncionp R_PARENTHESIS','llamadaFuncion',5,'p_llamadaFuncion','patitoParser.py',665),
  ('llamadaFuncionp -> COMMA expresion','llamadaFuncionp',2,'p_llamadaFuncionp','patitoParser.py',671),
  ('llamadaFuncionp -> empty','llamadaFuncionp',1,'p_llamadaFuncionp','patitoParser.py',672),
  ('funcionVacia -> ID L_PARENTHESIS expresion llamadaFuncionp R_PARENTHESIS SEMICOLON','funcionVacia',6,'p_funcionVacia','patitoParser.py',681),
  ('regresa -> REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON','regresa',5,'p_regresa','patitoParser.py',687),
  ('lectura -> LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON','lectura',5,'p_lectura','patitoParser.py',693),
  ('lecturap -> ID dimId lecturapp','lecturap',3,'p_lecturap','patitoParser.py',699),
  ('lecturapp -> COMMA lecturap','lecturapp',2,'p_lecturapp','patitoParser.py',705),
  ('lecturapp -> empty','lecturapp',1,'p_lecturapp','patitoParser.py',706),
  ('escritura -> ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON','escritura',5,'p_escritura','patitoParser.py',715),
  ('escriturap -> LETRERO escriturapp','escriturap',2,'p_escriturap','patitoParser.py',721),
  ('escriturap -> expresion escriturapp','escriturap',2,'p_escriturap','patitoParser.py',722),
  ('escriturapp -> COMMA escriturap','escriturapp',2,'p_escriturapp','patitoParser.py',728),
  ('escriturapp -> empty','escriturapp',1,'p_escriturapp','patitoParser.py',729),
  ('decision -> SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp','decision',8,'p_decision','patitoParser.py',738),
  ('jump_false -> <empty>','jump_false',0,'p_jump_false','patitoParser.py',744),
  ('update_jump -> <empty>','update_jump',0,'p_update_jump','patitoParser.py',750),
  ('decisionp -> SINO jump_else bloque update_jump','decisionp',4,'p_decisionp','patitoParser.py',756),
  ('decisionp -> empty update_jump','decisionp',2,'p_decisionp','patitoParser.py',757),
  ('jump_else -> <empty>','jump_else',0,'p_jump_else','patitoParser.py',766),
  ('cicloCondicional -> MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle','cicloCondicional',9,'p_cicloCondicional','patitoParser.py',772),
  ('jump_cycle -> <empty>','jump_cycle',0,'p_jump_cycle','patitoParser.py',778),
  ('update_jump_cycle -> <empty>','update_jump_cycle',0,'p_update_jump_cycle','patitoParser.py',784),
  ('cicloNoCondicional -> DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle','cicloNoCondicional',18,'p_cicloNoCondicional','patitoParser.py',790),
  ('add_gt -> <empty>','add_gt',0,'p_add_gt','patitoParser.py',796),
  ('add_one -> <empty>','add_one',0,'p_add_one','patitoParser.py',806),
  ('empty -> <empty>','empty',0,'p_empty','patitoParser.py',825),
]
