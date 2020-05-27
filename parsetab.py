
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR COLON COMMA CTE_CHAR CTE_FLOAT CTE_INT DESDE DETERMINANT DIVIDE EOF EQUALS ESCRIBE FLOAT FUNCION GREATER_THAN GREATER_THAN_EQUAL HACER HASTA HAZ ID INT INVERSE LECTURA LESS_THAN LESS_THAN_EQUAL LETRERO L_CURLY_BRACKET L_PARENTHESIS L_SQUARE_BRACKET MIENTRAS MULTIPLY NOT NOT_EQUAL OR PRINCIPAL PROGRAMA REGRESA R_CURLY_BRACKET R_PARENTHESIS R_SQUARE_BRACKET SEMICOLON SI SINO SUBTRACT SUM TRANSPOSED VAR VOID\n    start : programa\n    \n    programa : PROGRAMA ID SEMICOLON jump var funcion clear_scope PRINCIPAL update_jump L_PARENTHESIS R_PARENTHESIS bloque EOF\n    \n    jump :\n    \n    clear_scope :\n    \n    var : VAR var_seen varp\n        | empty\n     \n    var_seen :\n    \n    varp : tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp\n         | tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp\n    \n    tipo_seen :\n    \n    variable_seen : \n    \n    delete_type :\n    \n    varpp : COMMA ID variable_seen varppp varpp\n          | empty\n    \n    varppp : dimDeclare\n           | dimDeclare dimDeclare\n           | empty\n    \n    varpppp : varp\n            | empty\n    \n    dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET\n    \n    tipo : INT\n         | FLOAT\n         | CHAR\n    \n    funcion : FUNCION funcionp\n            | FUNCION error\n            | empty\n    \n    funcionp : tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque end_func funcion\n    \n    create_func_scope : \n    \n    end_func :\n    \n    parametro : tipo ID save_param parametrop\n              | empty\n    \n    save_param :\n    \n    parametrop : COMMA tipo ID save_param parametrop\n               | empty\n    \n    tipoRetorno : tipo\n                | VOID\n    \n    bloque : L_CURLY_BRACKET bloquep R_CURLY_BRACKET\n    \n    bloquep : estatuto bloquep\n            | empty\n    \n    estatuto : asignacion\n             | funcionVacia\n             | regresa\n             | lectura\n             | escritura\n             | decision\n             | cicloCondicional\n             | cicloNoCondicional\n    \n    asignacion : ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON\n    \n    operand_seen :\n    \n    dimId : is_array create_dim dim pop_array\n          | is_array create_dim dim dim pop_array\n          | empty\n    \n    pop_array :\n    \n    is_array :  \n    \n    dim : L_SQUARE_BRACKET bracket_seen expresion R_SQUARE_BRACKET bracket_seen\n    \n    create_dim :\n    \n    bracket_seen :\n    \n    apply_operation_assign : \n    \n    expresion : relacional apply_operation_expresion expresionp\n              | NOT relacional expresionp\n    \n    expresionp : AND operation_seen expresion\n               | OR operation_seen expresion\n               | empty\n    \n    apply_operation_expresion : \n    \n    relacional : aritmetica apply_operation_relational relacionalp\n    \n    relacionalp : EQUALS operation_seen relacional\n                | NOT_EQUAL operation_seen relacional\n                | LESS_THAN operation_seen relacional\n                | LESS_THAN_EQUAL operation_seen relacional\n                | GREATER_THAN operation_seen relacional\n                | GREATER_THAN_EQUAL operation_seen relacional\n                | empty\n    \n    apply_operation_relational : \n    \n    aritmetica : factor apply_operation_aritmetica aritmeticap\n    \n    aritmeticap : SUM operation_seen aritmetica\n                | SUBTRACT operation_seen aritmetica\n                | empty\n    \n    apply_operation_aritmetica : \n    \n    factor : matriz apply_operation_factor factorp\n    \n    factorp : MULTIPLY operation_seen factor \n            | DIVIDE operation_seen factor \n            | empty\n    \n    apply_operation_factor : \n    \n    operation_seen : \n    \n    matriz : cte matrizp\n    \n    matrizp : DETERMINANT\n            | TRANSPOSED\n            | INVERSE\n            | empty\n    \n    cte : CTE_INT\n        | CTE_FLOAT\n        | CTE_CHAR\n        | llamadaFuncion\n        | ID operand_seen dimId\n        | L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen\n    \n    llamadaFuncion : ID set_func_scope L_PARENTHESIS operation_seen llamadaFuncionp R_PARENTHESIS operation_seen\n    \n    llamadaFuncionp : expresion verify_parameter llamadaFuncionpp\n                    | empty\n    \n    llamadaFuncionpp : COMMA llamadaFuncionp\n                    | empty\n    \n    verify_parameter :\n    \n    funcionVacia : ID set_func_scope L_PARENTHESIS llamadaFuncionp R_PARENTHESIS SEMICOLON\n    \n    set_func_scope :\n    \n    regresa : REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON\n    \n    lectura : LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON\n    \n    lecturap : ID dimId gen_input lecturapp\n    \n    gen_input :\n    \n    lecturapp : COMMA lecturap\n              | empty\n    \n    escritura : ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON\n    \n    escriturap : LETRERO gen_print escriturapp\n               | expresion gen_print escriturapp\n    \n    gen_print :\n    \n    escriturapp : COMMA escriturap\n                | empty\n    \n    decision : SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp\n    \n    jump_false : \n    \n    update_jump :\n    \n    decisionp : SINO jump_else bloque update_jump\n              | empty update_jump\n    \n    jump_else :\n    \n    cicloCondicional : MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle\n    \n    jump_cycle : \n    \n    update_jump_cycle : \n    \n    cicloNoCondicional : DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle\n    \n    add_gt :\n    \n    add_one : \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAMA':([0,],[3,]),'$end':([1,2,49,],[0,-1,-2,]),'ID':([3,17,18,19,20,21,22,30,36,41,51,53,54,55,56,57,58,59,60,67,71,76,80,81,82,83,97,98,101,117,120,124,129,158,160,164,166,167,171,172,173,174,175,176,179,180,183,184,187,188,190,192,197,203,204,206,209,210,211,212,213,214,215,216,217,218,219,220,221,223,228,249,252,255,257,258,263,264,265,266,268,274,275,276,],[4,26,-35,-36,-21,-22,-23,33,43,61,61,-40,-41,-42,-43,-44,-45,-46,-47,85,91,-37,110,112,110,110,110,-84,110,110,152,-84,110,110,-57,-104,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-105,-110,110,-84,110,-102,110,110,110,110,110,110,110,110,110,110,110,110,110,110,112,110,-128,-48,-116,-118,-124,-120,-122,110,-118,-119,-127,-124,-125,]),'SEMICOLON':([4,33,38,39,44,45,46,48,70,72,73,75,90,91,92,93,96,100,102,103,104,105,106,107,108,109,110,122,130,131,132,133,134,135,136,137,138,139,140,141,143,145,156,159,161,165,168,169,170,177,178,181,182,185,186,199,200,201,202,208,230,231,234,235,236,237,238,239,240,241,242,243,244,245,246,253,254,260,261,],[5,-11,-128,-128,-128,-15,-17,-128,-12,-14,-16,-12,121,-11,-20,123,-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,-128,164,-128,-128,-128,-128,-128,-85,-86,-87,-88,-89,-128,188,190,-128,-53,204,-59,-63,-60,-65,-72,-74,-77,-79,-82,-94,-13,-58,-53,-50,-84,252,-51,-95,-61,-62,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-57,-84,-55,-96,]),'VAR':([5,6,42,],[-3,8,8,]),'FUNCION':([5,6,7,9,23,76,86,119,121,123,153,154,155,157,],[-3,-128,11,-6,-5,-37,-29,11,-128,-128,-8,-18,-19,-9,]),'PRINCIPAL':([5,6,7,9,10,12,14,15,16,23,76,86,119,121,123,151,153,154,155,157,],[-3,-128,-128,-6,-4,-26,25,-24,-25,-5,-37,-29,-128,-128,-128,-27,-8,-18,-19,-9,]),'INT':([8,11,13,32,88,121,123,],[-7,20,20,20,20,20,20,]),'FLOAT':([8,11,13,32,88,121,123,],[-7,21,21,21,21,21,21,]),'CHAR':([8,11,13,32,88,121,123,],[-7,22,22,22,22,22,22,]),'L_CURLY_BRACKET':([9,23,34,42,68,121,123,153,154,155,157,226,250,256,262,273,],[-6,-5,41,-128,41,-128,-128,-8,-18,-19,-9,41,41,-121,41,41,]),'error':([11,33,],[16,39,]),'VOID':([11,],[19,]),'COLON':([20,21,22,24,27,],[-21,-22,-23,-10,30,]),'L_PARENTHESIS':([25,26,28,29,61,62,63,64,65,66,79,80,82,83,84,97,98,101,110,117,124,129,142,158,160,166,167,171,172,173,174,175,176,179,180,183,184,187,192,197,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[-118,-28,31,32,-103,80,81,82,83,-123,97,98,98,98,117,98,-84,98,-103,98,-84,98,187,98,-57,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,98,-84,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'R_PARENTHESIS':([31,32,35,37,43,69,87,89,96,97,99,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,126,127,128,131,132,133,134,135,136,137,138,139,140,141,144,146,147,149,152,159,162,163,165,168,169,170,177,178,181,182,185,186,187,189,191,193,194,198,201,202,205,206,207,208,221,222,224,225,229,231,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,253,254,260,261,],[34,-128,42,-31,-32,-128,-30,-34,-52,-128,130,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,143,-128,145,-113,-113,148,161,-101,-98,-128,-128,-128,-128,-128,-85,-86,-87,-88,-89,-128,-107,-128,-128,196,-32,-53,-128,208,-59,-63,-60,-65,-72,-74,-77,-79,-82,-94,-84,-128,-111,-115,-112,-128,-53,-50,-97,-128,-100,-84,-128,-106,-109,-114,-33,-51,-99,-95,-61,-62,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,254,-108,-57,-84,-55,-96,]),'L_SQUARE_BRACKET':([33,38,39,45,61,78,85,91,92,95,110,112,118,122,125,141,159,253,260,],[-11,47,47,47,-49,-54,-49,-11,-20,-56,-49,-54,-54,47,160,-54,160,-57,-55,]),'COMMA':([33,38,39,43,44,45,46,48,69,73,91,92,96,100,102,103,104,105,106,107,108,109,110,112,114,115,122,127,131,132,133,134,135,136,137,138,139,140,141,144,146,147,152,156,159,162,165,168,169,170,177,178,181,182,185,186,189,198,201,202,208,231,234,235,236,237,238,239,240,241,242,243,244,245,246,253,254,260,261,],[-11,-128,-128,-32,71,-15,-17,71,88,-16,-11,-20,-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,-128,-113,-113,-128,-101,-128,-128,-128,-128,-128,-85,-86,-87,-88,-89,-128,-107,192,192,-32,71,-53,206,-59,-63,-60,-65,-72,-74,-77,-79,-82,-94,223,88,-53,-50,-84,-51,-95,-61,-62,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-57,-84,-55,-96,]),'EOF':([40,76,],[49,-37,]),'R_CURLY_BRACKET':([41,50,51,52,53,54,55,56,57,58,59,60,76,77,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[-128,76,-128,-39,-40,-41,-42,-43,-44,-45,-46,-47,-37,-38,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'REGRESA':([41,51,53,54,55,56,57,58,59,60,76,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[62,62,-40,-41,-42,-43,-44,-45,-46,-47,-37,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'LECTURA':([41,51,53,54,55,56,57,58,59,60,76,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[63,63,-40,-41,-42,-43,-44,-45,-46,-47,-37,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'ESCRIBE':([41,51,53,54,55,56,57,58,59,60,76,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[64,64,-40,-41,-42,-43,-44,-45,-46,-47,-37,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'SI':([41,51,53,54,55,56,57,58,59,60,76,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[65,65,-40,-41,-42,-43,-44,-45,-46,-47,-37,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'MIENTRAS':([41,51,53,54,55,56,57,58,59,60,76,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[66,66,-40,-41,-42,-43,-44,-45,-46,-47,-37,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'DESDE':([41,51,53,54,55,56,57,58,59,60,76,164,188,190,204,249,252,255,257,258,263,264,266,268,274,275,276,],[67,67,-40,-41,-42,-43,-44,-45,-46,-47,-37,-104,-105,-110,-102,-128,-48,-116,-118,-124,-120,-122,-118,-119,-127,-124,-125,]),'CTE_INT':([47,80,82,83,97,98,101,117,124,129,158,160,166,167,171,172,173,174,175,176,179,180,183,184,187,192,197,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[74,106,106,106,106,-84,106,106,-84,106,106,-57,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,106,-84,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'ASSIGN':([61,78,85,94,96,118,150,159,201,202,231,253,260,],[-49,-128,-49,124,-52,-128,197,-53,-53,-50,-51,-57,-55,]),'R_SQUARE_BRACKET':([74,96,100,102,103,104,105,106,107,108,109,110,131,132,133,134,135,136,137,138,139,140,141,159,165,168,169,170,177,178,181,182,185,186,201,202,208,231,232,234,235,236,237,238,239,240,241,242,243,244,245,246,253,254,260,261,],[92,-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,-128,-128,-128,-128,-128,-85,-86,-87,-88,-89,-128,-53,-59,-63,-60,-65,-72,-74,-77,-79,-82,-94,-53,-50,-84,-51,253,-95,-61,-62,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-57,-84,-55,-96,]),'SINO':([76,249,],[-37,256,]),'NOT':([80,82,83,97,98,117,124,129,158,160,166,167,187,192,197,203,206,209,210,221,228,265,],[101,101,101,101,-84,101,-84,101,101,-57,-84,-84,-84,101,-84,101,101,101,101,101,101,101,]),'CTE_FLOAT':([80,82,83,97,98,101,117,124,129,158,160,166,167,171,172,173,174,175,176,179,180,183,184,187,192,197,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[107,107,107,107,-84,107,107,-84,107,107,-57,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,107,-84,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'CTE_CHAR':([80,82,83,97,98,101,117,124,129,158,160,166,167,171,172,173,174,175,176,179,180,183,184,187,192,197,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[108,108,108,108,-84,108,108,-84,108,108,-57,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,108,-84,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'LETRERO':([82,192,],[114,114,]),'DETERMINANT':([96,105,106,107,108,109,110,141,159,186,201,202,208,231,234,253,254,260,261,],[-52,137,-90,-91,-92,-93,-49,-128,-53,-94,-53,-50,-84,-51,-95,-57,-84,-55,-96,]),'TRANSPOSED':([96,105,106,107,108,109,110,141,159,186,201,202,208,231,234,253,254,260,261,],[-52,138,-90,-91,-92,-93,-49,-128,-53,-94,-53,-50,-84,-51,-95,-57,-84,-55,-96,]),'INVERSE':([96,105,106,107,108,109,110,141,159,186,201,202,208,231,234,253,254,260,261,],[-52,139,-90,-91,-92,-93,-49,-128,-53,-94,-53,-50,-84,-51,-95,-57,-84,-55,-96,]),'MULTIPLY':([96,104,105,106,107,108,109,110,135,136,137,138,139,140,141,159,186,201,202,208,231,234,253,254,260,261,],[-52,-83,-128,-90,-91,-92,-93,-49,183,-85,-86,-87,-88,-89,-128,-53,-94,-53,-50,-84,-51,-95,-57,-84,-55,-96,]),'DIVIDE':([96,104,105,106,107,108,109,110,135,136,137,138,139,140,141,159,186,201,202,208,231,234,253,254,260,261,],[-52,-83,-128,-90,-91,-92,-93,-49,184,-85,-86,-87,-88,-89,-128,-53,-94,-53,-50,-84,-51,-95,-57,-84,-55,-96,]),'SUM':([96,103,104,105,106,107,108,109,110,134,135,136,137,138,139,140,141,159,182,185,186,201,202,208,231,234,245,246,253,254,260,261,],[-52,-78,-83,-128,-90,-91,-92,-93,-49,179,-128,-85,-86,-87,-88,-89,-128,-53,-79,-82,-94,-53,-50,-84,-51,-95,-80,-81,-57,-84,-55,-96,]),'SUBTRACT':([96,103,104,105,106,107,108,109,110,134,135,136,137,138,139,140,141,159,182,185,186,201,202,208,231,234,245,246,253,254,260,261,],[-52,-78,-83,-128,-90,-91,-92,-93,-49,180,-128,-85,-86,-87,-88,-89,-128,-53,-79,-82,-94,-53,-50,-84,-51,-95,-80,-81,-57,-84,-55,-96,]),'EQUALS':([96,102,103,104,105,106,107,108,109,110,133,134,135,136,137,138,139,140,141,159,178,181,182,185,186,201,202,208,231,234,243,244,245,246,253,254,260,261,],[-52,-73,-78,-83,-128,-90,-91,-92,-93,-49,171,-128,-128,-85,-86,-87,-88,-89,-128,-53,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-75,-76,-80,-81,-57,-84,-55,-96,]),'NOT_EQUAL':([96,102,103,104,105,106,107,108,109,110,133,134,135,136,137,138,139,140,141,159,178,181,182,185,186,201,202,208,231,234,243,244,245,246,253,254,260,261,],[-52,-73,-78,-83,-128,-90,-91,-92,-93,-49,172,-128,-128,-85,-86,-87,-88,-89,-128,-53,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-75,-76,-80,-81,-57,-84,-55,-96,]),'LESS_THAN':([96,102,103,104,105,106,107,108,109,110,133,134,135,136,137,138,139,140,141,159,178,181,182,185,186,201,202,208,231,234,243,244,245,246,253,254,260,261,],[-52,-73,-78,-83,-128,-90,-91,-92,-93,-49,173,-128,-128,-85,-86,-87,-88,-89,-128,-53,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-75,-76,-80,-81,-57,-84,-55,-96,]),'LESS_THAN_EQUAL':([96,102,103,104,105,106,107,108,109,110,133,134,135,136,137,138,139,140,141,159,178,181,182,185,186,201,202,208,231,234,243,244,245,246,253,254,260,261,],[-52,-73,-78,-83,-128,-90,-91,-92,-93,-49,174,-128,-128,-85,-86,-87,-88,-89,-128,-53,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-75,-76,-80,-81,-57,-84,-55,-96,]),'GREATER_THAN':([96,102,103,104,105,106,107,108,109,110,133,134,135,136,137,138,139,140,141,159,178,181,182,185,186,201,202,208,231,234,243,244,245,246,253,254,260,261,],[-52,-73,-78,-83,-128,-90,-91,-92,-93,-49,175,-128,-128,-85,-86,-87,-88,-89,-128,-53,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-75,-76,-80,-81,-57,-84,-55,-96,]),'GREATER_THAN_EQUAL':([96,102,103,104,105,106,107,108,109,110,133,134,135,136,137,138,139,140,141,159,178,181,182,185,186,201,202,208,231,234,243,244,245,246,253,254,260,261,],[-52,-73,-78,-83,-128,-90,-91,-92,-93,-49,176,-128,-128,-85,-86,-87,-88,-89,-128,-53,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-75,-76,-80,-81,-57,-84,-55,-96,]),'AND':([96,100,102,103,104,105,106,107,108,109,110,131,132,133,134,135,136,137,138,139,140,141,159,170,177,178,181,182,185,186,201,202,208,231,234,237,238,239,240,241,242,243,244,245,246,253,254,260,261,],[-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,166,166,-128,-128,-128,-85,-86,-87,-88,-89,-128,-53,-65,-72,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-57,-84,-55,-96,]),'OR':([96,100,102,103,104,105,106,107,108,109,110,131,132,133,134,135,136,137,138,139,140,141,159,170,177,178,181,182,185,186,201,202,208,231,234,237,238,239,240,241,242,243,244,245,246,253,254,260,261,],[-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,167,167,-128,-128,-128,-85,-86,-87,-88,-89,-128,-53,-65,-72,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-57,-84,-55,-96,]),'HASTA':([96,100,102,103,104,105,106,107,108,109,110,131,132,133,134,135,136,137,138,139,140,141,159,165,168,169,170,177,178,181,182,185,186,201,202,208,231,234,235,236,237,238,239,240,241,242,243,244,245,246,251,253,254,259,260,261,],[-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,-128,-128,-128,-128,-128,-85,-86,-87,-88,-89,-128,-53,-59,-63,-60,-65,-72,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-61,-62,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-58,-57,-84,265,-55,-96,]),'HACER':([96,100,102,103,104,105,106,107,108,109,110,131,132,133,134,135,136,137,138,139,140,141,159,165,168,169,170,177,178,181,182,185,186,201,202,208,231,234,235,236,237,238,239,240,241,242,243,244,245,246,253,254,260,261,267,269,270,271,272,],[-52,-64,-73,-78,-83,-128,-90,-91,-92,-93,-49,-128,-128,-128,-128,-128,-85,-86,-87,-88,-89,-128,-53,-59,-63,-60,-65,-72,-74,-77,-79,-82,-94,-53,-50,-84,-51,-95,-61,-62,-66,-67,-68,-69,-70,-71,-75,-76,-80,-81,-57,-84,-55,-96,-123,-126,-73,-117,273,]),'HAZ':([148,195,196,227,],[-117,226,-117,250,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'programa':([0,],[2,]),'jump':([5,],[6,]),'var':([6,42,],[7,68,]),'empty':([6,7,32,38,39,41,42,44,48,51,69,78,97,105,112,118,119,121,122,123,131,132,133,134,135,141,146,147,156,162,189,198,206,221,249,],[9,12,37,46,46,52,9,72,72,52,89,96,128,140,96,96,12,155,46,155,168,168,177,181,185,96,193,193,72,207,224,89,128,128,257,]),'funcion':([7,119,],[10,151,]),'var_seen':([8,],[13,]),'clear_scope':([10,],[14,]),'funcionp':([11,],[15,]),'tipoRetorno':([11,],[17,]),'tipo':([11,13,32,88,121,123,],[18,24,36,120,24,24,]),'varp':([13,121,123,],[23,154,154,]),'tipo_seen':([24,],[27,]),'update_jump':([25,257,266,],[28,263,268,]),'create_func_scope':([26,],[29,]),'parametro':([32,],[35,]),'variable_seen':([33,91,],[38,122,]),'bloque':([34,68,226,250,262,273,],[40,86,249,258,266,274,]),'varppp':([38,39,122,],[44,48,156,]),'dimDeclare':([38,39,45,122,],[45,45,73,45,]),'bloquep':([41,51,],[50,77,]),'estatuto':([41,51,],[51,51,]),'asignacion':([41,51,],[53,53,]),'funcionVacia':([41,51,],[54,54,]),'regresa':([41,51,],[55,55,]),'lectura':([41,51,],[56,56,]),'escritura':([41,51,],[57,57,]),'decision':([41,51,],[58,58,]),'cicloCondicional':([41,51,],[59,59,]),'cicloNoCondicional':([41,51,],[60,60,]),'save_param':([43,152,],[69,198,]),'varpp':([44,48,156,],[70,75,199,]),'operand_seen':([61,85,110,],[78,118,141,]),'set_func_scope':([61,110,],[79,142,]),'jump_cycle':([66,267,],[84,269,]),'parametrop':([69,198,],[87,229,]),'delete_type':([70,75,],[90,93,]),'dimId':([78,112,118,141,],[94,144,150,186,]),'is_array':([78,112,118,141,],[95,95,95,95,]),'expresion':([80,82,83,97,117,129,158,192,203,206,209,210,221,228,265,],[99,115,116,127,149,163,200,115,232,127,235,236,127,251,267,]),'relacional':([80,82,83,97,101,117,129,158,192,203,206,209,210,211,212,213,214,215,216,221,228,265,],[100,100,100,100,132,100,100,100,100,100,100,100,100,237,238,239,240,241,242,100,100,100,]),'aritmetica':([80,82,83,97,101,117,129,158,192,203,206,209,210,211,212,213,214,215,216,217,218,221,228,265,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,243,244,102,102,102,]),'factor':([80,82,83,97,101,117,129,158,192,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,245,246,103,103,103,]),'matriz':([80,82,83,97,101,117,129,158,192,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'cte':([80,82,83,97,101,117,129,158,192,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'llamadaFuncion':([80,82,83,97,101,117,129,158,192,203,206,209,210,211,212,213,214,215,216,217,218,219,220,221,228,265,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'lecturap':([81,223,],[111,248,]),'escriturap':([82,192,],[113,225,]),'end_func':([86,],[119,]),'create_dim':([95,],[125,]),'llamadaFuncionp':([97,206,221,],[126,233,247,]),'operation_seen':([98,124,166,167,171,172,173,174,175,176,179,180,183,184,187,197,208,254,],[129,158,209,210,211,212,213,214,215,216,217,218,219,220,221,228,234,261,]),'apply_operation_expresion':([100,],[131,]),'apply_operation_relational':([102,270,],[133,271,]),'apply_operation_aritmetica':([103,],[134,]),'apply_operation_factor':([104,],[135,]),'matrizp':([105,],[136,]),'gen_print':([114,115,],[146,147,]),'varpppp':([121,123,],[153,157,]),'dim':([125,159,],[159,201,]),'verify_parameter':([127,],[162,]),'expresionp':([131,132,],[165,169,]),'relacionalp':([133,],[170,]),'aritmeticap':([134,],[178,]),'factorp':([135,],[182,]),'gen_input':([144,],[189,]),'escriturapp':([146,147,],[191,194,]),'jump_false':([148,196,271,],[195,227,272,]),'pop_array':([159,201,],[202,231,]),'bracket_seen':([160,253,],[203,260,]),'llamadaFuncionpp':([162,],[205,]),'lecturapp':([189,],[222,]),'apply_operation_assign':([200,251,],[230,259,]),'decisionp':([249,],[255,]),'jump_else':([256,],[262,]),'update_jump_cycle':([258,275,],[264,276,]),'add_gt':([269,],[270,]),'add_one':([274,],[275,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> programa','start',1,'p_start','patitoParser.py',317),
  ('programa -> PROGRAMA ID SEMICOLON jump var funcion clear_scope PRINCIPAL update_jump L_PARENTHESIS R_PARENTHESIS bloque EOF','programa',13,'p_programa','patitoParser.py',347),
  ('jump -> <empty>','jump',0,'p_jump','patitoParser.py',353),
  ('clear_scope -> <empty>','clear_scope',0,'p_clear_scope','patitoParser.py',359),
  ('var -> VAR var_seen varp','var',3,'p_variables','patitoParser.py',368),
  ('var -> empty','var',1,'p_variables','patitoParser.py',369),
  ('var_seen -> <empty>','var_seen',0,'p_var_seen','patitoParser.py',386),
  ('varp -> tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp','varp',10,'p_variablesp','patitoParser.py',396),
  ('varp -> tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp','varp',10,'p_variablesp','patitoParser.py',397),
  ('tipo_seen -> <empty>','tipo_seen',0,'p_tipo_seen','patitoParser.py',405),
  ('variable_seen -> <empty>','variable_seen',0,'p_variable_seen','patitoParser.py',413),
  ('delete_type -> <empty>','delete_type',0,'p_delete_type','patitoParser.py',439),
  ('varpp -> COMMA ID variable_seen varppp varpp','varpp',5,'p_variablespp','patitoParser.py',448),
  ('varpp -> empty','varpp',1,'p_variablespp','patitoParser.py',449),
  ('varppp -> dimDeclare','varppp',1,'p_variablesppp','patitoParser.py',459),
  ('varppp -> dimDeclare dimDeclare','varppp',2,'p_variablesppp','patitoParser.py',460),
  ('varppp -> empty','varppp',1,'p_variablesppp','patitoParser.py',461),
  ('varpppp -> varp','varpppp',1,'p_variablespppp','patitoParser.py',479),
  ('varpppp -> empty','varpppp',1,'p_variablespppp','patitoParser.py',480),
  ('dimDeclare -> L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET','dimDeclare',3,'p_dimDeclare','patitoParser.py',487),
  ('tipo -> INT','tipo',1,'p_tipo','patitoParser.py',508),
  ('tipo -> FLOAT','tipo',1,'p_tipo','patitoParser.py',509),
  ('tipo -> CHAR','tipo',1,'p_tipo','patitoParser.py',510),
  ('funcion -> FUNCION funcionp','funcion',2,'p_funcion','patitoParser.py',516),
  ('funcion -> FUNCION error','funcion',2,'p_funcion','patitoParser.py',517),
  ('funcion -> empty','funcion',1,'p_funcion','patitoParser.py',518),
  ('funcionp -> tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque end_func funcion','funcionp',10,'p_funcionp','patitoParser.py',527),
  ('create_func_scope -> <empty>','create_func_scope',0,'p_create_func_scope','patitoParser.py',536),
  ('end_func -> <empty>','end_func',0,'p_end_func','patitoParser.py',568),
  ('parametro -> tipo ID save_param parametrop','parametro',4,'p_parametro','patitoParser.py',578),
  ('parametro -> empty','parametro',1,'p_parametro','patitoParser.py',579),
  ('save_param -> <empty>','save_param',0,'p_save_param','patitoParser.py',588),
  ('parametrop -> COMMA tipo ID save_param parametrop','parametrop',5,'p_parametrop','patitoParser.py',595),
  ('parametrop -> empty','parametrop',1,'p_parametrop','patitoParser.py',596),
  ('tipoRetorno -> tipo','tipoRetorno',1,'p_tipoRetorno','patitoParser.py',605),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','patitoParser.py',606),
  ('bloque -> L_CURLY_BRACKET bloquep R_CURLY_BRACKET','bloque',3,'p_bloque','patitoParser.py',612),
  ('bloquep -> estatuto bloquep','bloquep',2,'p_bloquep','patitoParser.py',618),
  ('bloquep -> empty','bloquep',1,'p_bloquep','patitoParser.py',619),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','patitoParser.py',628),
  ('estatuto -> funcionVacia','estatuto',1,'p_estatuto','patitoParser.py',629),
  ('estatuto -> regresa','estatuto',1,'p_estatuto','patitoParser.py',630),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','patitoParser.py',631),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','patitoParser.py',632),
  ('estatuto -> decision','estatuto',1,'p_estatuto','patitoParser.py',633),
  ('estatuto -> cicloCondicional','estatuto',1,'p_estatuto','patitoParser.py',634),
  ('estatuto -> cicloNoCondicional','estatuto',1,'p_estatuto','patitoParser.py',635),
  ('asignacion -> ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON','asignacion',8,'p_asignacion','patitoParser.py',641),
  ('operand_seen -> <empty>','operand_seen',0,'p_operand_seen','patitoParser.py',647),
  ('dimId -> is_array create_dim dim pop_array','dimId',4,'p_dimId','patitoParser.py',661),
  ('dimId -> is_array create_dim dim dim pop_array','dimId',5,'p_dimId','patitoParser.py',662),
  ('dimId -> empty','dimId',1,'p_dimId','patitoParser.py',663),
  ('pop_array -> <empty>','pop_array',0,'p_pop_array','patitoParser.py',697),
  ('is_array -> <empty>','is_array',0,'p_is_array','patitoParser.py',703),
  ('dim -> L_SQUARE_BRACKET bracket_seen expresion R_SQUARE_BRACKET bracket_seen','dim',5,'p_dim','patitoParser.py',711),
  ('create_dim -> <empty>','create_dim',0,'p_create_dim','patitoParser.py',717),
  ('bracket_seen -> <empty>','bracket_seen',0,'p_bracket_seen','patitoParser.py',724),
  ('apply_operation_assign -> <empty>','apply_operation_assign',0,'p_apply_operation_assign','patitoParser.py',783),
  ('expresion -> relacional apply_operation_expresion expresionp','expresion',3,'p_expresion','patitoParser.py',793),
  ('expresion -> NOT relacional expresionp','expresion',3,'p_expresion','patitoParser.py',794),
  ('expresionp -> AND operation_seen expresion','expresionp',3,'p_expresionp','patitoParser.py',803),
  ('expresionp -> OR operation_seen expresion','expresionp',3,'p_expresionp','patitoParser.py',804),
  ('expresionp -> empty','expresionp',1,'p_expresionp','patitoParser.py',805),
  ('apply_operation_expresion -> <empty>','apply_operation_expresion',0,'p_apply_operation_expresion','patitoParser.py',815),
  ('relacional -> aritmetica apply_operation_relational relacionalp','relacional',3,'p_relacional','patitoParser.py',824),
  ('relacionalp -> EQUALS operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',830),
  ('relacionalp -> NOT_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',831),
  ('relacionalp -> LESS_THAN operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',832),
  ('relacionalp -> LESS_THAN_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',833),
  ('relacionalp -> GREATER_THAN operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',834),
  ('relacionalp -> GREATER_THAN_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',835),
  ('relacionalp -> empty','relacionalp',1,'p_relacionalp','patitoParser.py',836),
  ('apply_operation_relational -> <empty>','apply_operation_relational',0,'p_apply_operation_relational','patitoParser.py',846),
  ('aritmetica -> factor apply_operation_aritmetica aritmeticap','aritmetica',3,'p_aritmetica','patitoParser.py',855),
  ('aritmeticap -> SUM operation_seen aritmetica','aritmeticap',3,'p_aritmeticap','patitoParser.py',861),
  ('aritmeticap -> SUBTRACT operation_seen aritmetica','aritmeticap',3,'p_aritmeticap','patitoParser.py',862),
  ('aritmeticap -> empty','aritmeticap',1,'p_aritmeticap','patitoParser.py',863),
  ('apply_operation_aritmetica -> <empty>','apply_operation_aritmetica',0,'p_apply_operation_aritmetica','patitoParser.py',873),
  ('factor -> matriz apply_operation_factor factorp','factor',3,'p_factor','patitoParser.py',882),
  ('factorp -> MULTIPLY operation_seen factor','factorp',3,'p_factorp','patitoParser.py',888),
  ('factorp -> DIVIDE operation_seen factor','factorp',3,'p_factorp','patitoParser.py',889),
  ('factorp -> empty','factorp',1,'p_factorp','patitoParser.py',890),
  ('apply_operation_factor -> <empty>','apply_operation_factor',0,'p_apply_operation_factor','patitoParser.py',900),
  ('operation_seen -> <empty>','operation_seen',0,'p_operation_seen','patitoParser.py',910),
  ('matriz -> cte matrizp','matriz',2,'p_matriz','patitoParser.py',922),
  ('matrizp -> DETERMINANT','matrizp',1,'p_matrizp','patitoParser.py',928),
  ('matrizp -> TRANSPOSED','matrizp',1,'p_matrizp','patitoParser.py',929),
  ('matrizp -> INVERSE','matrizp',1,'p_matrizp','patitoParser.py',930),
  ('matrizp -> empty','matrizp',1,'p_matrizp','patitoParser.py',931),
  ('cte -> CTE_INT','cte',1,'p_cte','patitoParser.py',937),
  ('cte -> CTE_FLOAT','cte',1,'p_cte','patitoParser.py',938),
  ('cte -> CTE_CHAR','cte',1,'p_cte','patitoParser.py',939),
  ('cte -> llamadaFuncion','cte',1,'p_cte','patitoParser.py',940),
  ('cte -> ID operand_seen dimId','cte',3,'p_cte','patitoParser.py',941),
  ('cte -> L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen','cte',5,'p_cte','patitoParser.py',942),
  ('llamadaFuncion -> ID set_func_scope L_PARENTHESIS operation_seen llamadaFuncionp R_PARENTHESIS operation_seen','llamadaFuncion',7,'p_llamadaFuncion','patitoParser.py',987),
  ('llamadaFuncionp -> expresion verify_parameter llamadaFuncionpp','llamadaFuncionp',3,'p_llamadaFuncionp','patitoParser.py',1004),
  ('llamadaFuncionp -> empty','llamadaFuncionp',1,'p_llamadaFuncionp','patitoParser.py',1005),
  ('llamadaFuncionpp -> COMMA llamadaFuncionp','llamadaFuncionpp',2,'p_llamadaFuncionpp','patitoParser.py',1015),
  ('llamadaFuncionpp -> empty','llamadaFuncionpp',1,'p_llamadaFuncionpp','patitoParser.py',1016),
  ('verify_parameter -> <empty>','verify_parameter',0,'p_verify_parameter','patitoParser.py',1025),
  ('funcionVacia -> ID set_func_scope L_PARENTHESIS llamadaFuncionp R_PARENTHESIS SEMICOLON','funcionVacia',6,'p_funcionVacia','patitoParser.py',1031),
  ('set_func_scope -> <empty>','set_func_scope',0,'p_set_func_scope','patitoParser.py',1045),
  ('regresa -> REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON','regresa',5,'p_regresa','patitoParser.py',1059),
  ('lectura -> LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON','lectura',5,'p_lectura','patitoParser.py',1069),
  ('lecturap -> ID dimId gen_input lecturapp','lecturap',4,'p_lecturap','patitoParser.py',1075),
  ('gen_input -> <empty>','gen_input',0,'p_gen_input','patitoParser.py',1081),
  ('lecturapp -> COMMA lecturap','lecturapp',2,'p_lecturapp','patitoParser.py',1088),
  ('lecturapp -> empty','lecturapp',1,'p_lecturapp','patitoParser.py',1089),
  ('escritura -> ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON','escritura',5,'p_escritura','patitoParser.py',1098),
  ('escriturap -> LETRERO gen_print escriturapp','escriturap',3,'p_escriturap','patitoParser.py',1105),
  ('escriturap -> expresion gen_print escriturapp','escriturap',3,'p_escriturap','patitoParser.py',1106),
  ('gen_print -> <empty>','gen_print',0,'p_gen_print','patitoParser.py',1112),
  ('escriturapp -> COMMA escriturap','escriturapp',2,'p_escriturapp','patitoParser.py',1121),
  ('escriturapp -> empty','escriturapp',1,'p_escriturapp','patitoParser.py',1122),
  ('decision -> SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp','decision',8,'p_decision','patitoParser.py',1131),
  ('jump_false -> <empty>','jump_false',0,'p_jump_false','patitoParser.py',1137),
  ('update_jump -> <empty>','update_jump',0,'p_update_jump','patitoParser.py',1143),
  ('decisionp -> SINO jump_else bloque update_jump','decisionp',4,'p_decisionp','patitoParser.py',1149),
  ('decisionp -> empty update_jump','decisionp',2,'p_decisionp','patitoParser.py',1150),
  ('jump_else -> <empty>','jump_else',0,'p_jump_else','patitoParser.py',1159),
  ('cicloCondicional -> MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle','cicloCondicional',9,'p_cicloCondicional','patitoParser.py',1165),
  ('jump_cycle -> <empty>','jump_cycle',0,'p_jump_cycle','patitoParser.py',1171),
  ('update_jump_cycle -> <empty>','update_jump_cycle',0,'p_update_jump_cycle','patitoParser.py',1177),
  ('cicloNoCondicional -> DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle','cicloNoCondicional',18,'p_cicloNoCondicional','patitoParser.py',1183),
  ('add_gt -> <empty>','add_gt',0,'p_add_gt','patitoParser.py',1189),
  ('add_one -> <empty>','add_one',0,'p_add_one','patitoParser.py',1199),
  ('empty -> <empty>','empty',0,'p_empty','patitoParser.py',1217),
]
