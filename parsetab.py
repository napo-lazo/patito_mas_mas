
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR COLON COMMA CTE_CHAR CTE_FLOAT CTE_INT DESDE DETERMINANT DIVIDE EOF EQUALS ESCRIBE FLOAT FUNCION GREATER_THAN GREATER_THAN_EQUAL HACER HASTA HAZ ID INT INVERSE LECTURA LESS_THAN LESS_THAN_EQUAL LETRERO L_CURLY_BRACKET L_PARENTHESIS L_SQUARE_BRACKET MIENTRAS MULTIPLY NOT NOT_EQUAL OR PRINCIPAL PROGRAMA REGRESA R_CURLY_BRACKET R_PARENTHESIS R_SQUARE_BRACKET SEMICOLON SI SINO SUBTRACT SUM TRANSPOSED VAR VOID\n    start : programa\n    \n    programa : PROGRAMA ID SEMICOLON jump var funcion clear_scope PRINCIPAL update_jump L_PARENTHESIS R_PARENTHESIS bloque EOF\n    \n    jump :\n    \n    clear_scope :\n    \n    var : VAR var_seen varp\n        | empty\n     \n    var_seen :\n    \n    varp : tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp\n         | tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp\n    \n    tipo_seen :\n    \n    variable_seen : \n    \n    delete_type :\n    \n    varpp : COMMA ID variable_seen varppp varpp\n          | empty\n    \n    varppp : dimDeclare\n           | dimDeclare dimDeclare\n           | empty\n    \n    varpppp : varp\n            | empty\n    \n    dimDeclare : L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET\n    \n    tipo : INT\n         | FLOAT\n         | CHAR\n    \n    funcion : FUNCION funcionp\n            | FUNCION error\n            | empty\n    \n    funcionp : tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque end_func funcion\n    \n    create_func_scope : \n    \n    end_func :\n    \n    parametro : tipo ID save_param parametrop\n              | empty\n    \n    save_param :\n    \n    parametrop : COMMA tipo ID save_param parametrop\n               | empty\n    \n    tipoRetorno : tipo\n                | VOID\n    \n    bloque : L_CURLY_BRACKET bloquep R_CURLY_BRACKET\n    \n    bloquep : estatuto bloquep\n            | empty\n    \n    estatuto : asignacion\n             | funcionVacia\n             | regresa\n             | lectura\n             | escritura\n             | decision\n             | cicloCondicional\n             | cicloNoCondicional\n    \n    asignacion : ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON\n    \n    operand_seen :\n    \n    apply_operation_assign : \n    \n    dimId : dim\n                | dim dim\n                | empty\n    \n    dim : L_SQUARE_BRACKET expresion R_SQUARE_BRACKET\n    \n    expresion : relacional apply_operation_expresion expresionp\n              | NOT relacional expresionp\n    \n    expresionp : AND operation_seen expresion\n               | OR operation_seen expresion\n               | empty\n    \n    apply_operation_expresion : \n    \n    relacional : aritmetica apply_operation_relational relacionalp\n    \n    relacionalp : EQUALS operation_seen relacional\n                | NOT_EQUAL operation_seen relacional\n                | LESS_THAN operation_seen relacional\n                | LESS_THAN_EQUAL operation_seen relacional\n                | GREATER_THAN operation_seen relacional\n                | GREATER_THAN_EQUAL operation_seen relacional\n                | empty\n    \n    apply_operation_relational : \n    \n    aritmetica : factor apply_operation_aritmetica aritmeticap\n    \n    aritmeticap : SUM operation_seen aritmetica\n                | SUBTRACT operation_seen aritmetica\n                | empty\n    \n    apply_operation_aritmetica : \n    \n    factor : matriz apply_operation_factor factorp\n    \n    factorp : MULTIPLY operation_seen factor \n            | DIVIDE operation_seen factor \n            | empty\n    \n    apply_operation_factor : \n    \n    operation_seen : \n    \n    matriz : cte matrizp\n    \n    matrizp : DETERMINANT\n            | TRANSPOSED\n            | INVERSE\n            | empty\n    \n    cte : CTE_INT\n        | CTE_FLOAT\n        | CTE_CHAR\n        | llamadaFuncion\n        | ID operand_seen dimId\n        | L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen\n    \n    llamadaFuncion : ID set_func_scope L_PARENTHESIS operation_seen llamadaFuncionp R_PARENTHESIS operation_seen\n    \n    llamadaFuncionp : expresion verify_parameter llamadaFuncionpp\n                    | empty\n    \n    llamadaFuncionpp : COMMA llamadaFuncionp\n                    | empty\n    \n    verify_parameter :\n    \n    funcionVacia : ID set_func_scope L_PARENTHESIS llamadaFuncionp R_PARENTHESIS SEMICOLON\n    \n    set_func_scope :\n    \n    regresa : REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON\n    \n    lectura : LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON\n    \n    lecturap : ID dimId lecturapp\n    \n    lecturapp : COMMA lecturap\n              | empty\n    \n    escritura : ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON\n    \n    escriturap : LETRERO escriturapp\n               | expresion escriturapp\n    \n    escriturapp : COMMA escriturap\n                | empty\n    \n    decision : SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp\n    \n    jump_false : \n    \n    update_jump :\n    \n    decisionp : SINO jump_else bloque update_jump\n              | empty update_jump\n    \n    jump_else :\n    \n    cicloCondicional : MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle\n    \n    jump_cycle : \n    \n    update_jump_cycle : \n    \n    cicloNoCondicional : DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle\n    \n    add_gt :\n    \n    add_one : \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAMA':([0,],[3,]),'$end':([1,2,49,],[0,-1,-2,]),'ID':([3,17,18,19,20,21,22,30,36,41,51,53,54,55,56,57,58,59,60,67,71,76,80,81,82,83,97,98,99,102,118,121,125,131,149,162,167,169,170,174,175,176,177,178,179,182,183,186,187,190,191,193,195,199,203,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,242,245,247,249,250,254,255,256,257,259,265,266,267,],[4,26,-35,-36,-21,-22,-23,33,43,61,61,-40,-41,-42,-43,-44,-45,-46,-47,85,91,-37,111,113,111,111,111,111,-80,111,111,156,-80,111,111,111,-100,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-101,113,-105,-80,-98,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,-122,-48,-110,-112,-118,-114,-116,111,-112,-113,-121,-118,-119,]),'SEMICOLON':([4,33,38,39,44,45,46,48,70,72,73,75,90,91,92,93,95,96,101,103,104,105,106,107,108,109,110,111,123,126,132,133,134,135,136,137,138,139,140,141,142,143,145,147,160,163,164,168,171,172,173,180,181,184,185,188,189,201,202,207,226,228,229,230,231,232,233,234,235,236,237,238,239,240,246,252,],[5,-11,-122,-122,-122,-15,-17,-122,-12,-14,-16,-12,122,-11,-20,124,-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-122,-52,167,-122,-122,-122,-122,-122,-81,-82,-83,-84,-85,-122,191,195,-122,-54,203,-55,-59,-56,-61,-68,-70,-73,-75,-78,-90,-13,-50,-80,245,-91,-57,-58,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-80,-92,]),'VAR':([5,6,42,],[-3,8,8,]),'FUNCION':([5,6,7,9,23,76,86,120,122,124,157,158,159,161,],[-3,-122,11,-6,-5,-37,-29,11,-122,-122,-8,-18,-19,-9,]),'PRINCIPAL':([5,6,7,9,10,12,14,15,16,23,76,86,120,122,124,155,157,158,159,161,],[-3,-122,-122,-6,-4,-26,25,-24,-25,-5,-37,-29,-122,-122,-122,-27,-8,-18,-19,-9,]),'INT':([8,11,13,32,88,122,124,],[-7,20,20,20,20,20,20,]),'FLOAT':([8,11,13,32,88,122,124,],[-7,21,21,21,21,21,21,]),'CHAR':([8,11,13,32,88,122,124,],[-7,22,22,22,22,22,22,]),'L_CURLY_BRACKET':([9,23,34,42,68,122,124,157,158,159,161,222,243,248,253,264,],[-6,-5,41,-122,41,-122,-122,-8,-18,-19,-9,41,41,-115,41,41,]),'error':([11,33,],[16,39,]),'VOID':([11,],[19,]),'COLON':([20,21,22,24,27,],[-21,-22,-23,-10,30,]),'L_PARENTHESIS':([25,26,28,29,61,62,63,64,65,66,79,80,82,83,84,97,98,99,102,111,118,125,131,144,149,162,169,170,174,175,176,177,178,179,182,183,186,187,190,199,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[-112,-28,31,32,-99,80,81,82,83,-117,98,99,99,99,118,99,99,-80,99,-99,99,-80,99,190,99,99,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'R_PARENTHESIS':([31,32,35,37,43,69,87,89,95,96,98,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,126,128,129,130,133,134,135,136,137,138,139,140,141,142,143,146,148,150,151,153,156,163,165,166,168,171,172,173,180,181,184,185,188,189,190,192,194,196,200,204,205,206,207,220,221,225,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,246,252,],[34,-122,42,-31,-32,-122,-30,-34,-51,-53,-122,132,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,145,-122,147,-122,-122,152,-52,164,-97,-94,-122,-122,-122,-122,-122,-81,-82,-83,-84,-85,-122,-122,-106,-109,-107,198,-32,-54,-122,207,-55,-59,-56,-61,-68,-70,-73,-75,-78,-90,-80,-102,-104,-108,-122,-93,-122,-96,-80,-122,-103,-33,-95,-91,-57,-58,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,246,-80,-92,]),'L_SQUARE_BRACKET':([33,38,39,45,61,78,85,91,92,95,111,113,119,123,143,163,],[-11,47,47,47,-49,97,-49,-11,-20,97,-49,97,97,47,97,-54,]),'COMMA':([33,38,39,43,44,45,46,48,69,73,91,92,95,96,101,103,104,105,106,107,108,109,110,111,113,115,116,123,126,129,133,134,135,136,137,138,139,140,141,142,143,146,156,160,163,165,168,171,172,173,180,181,184,185,188,189,200,207,228,229,230,231,232,233,234,235,236,237,238,239,240,246,252,],[-11,-122,-122,-32,71,-15,-17,71,88,-16,-11,-20,-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-122,149,149,-122,-52,-97,-122,-122,-122,-122,-122,-81,-82,-83,-84,-85,-122,193,-32,71,-54,205,-55,-59,-56,-61,-68,-70,-73,-75,-78,-90,88,-80,-91,-57,-58,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-80,-92,]),'EOF':([40,76,],[49,-37,]),'R_CURLY_BRACKET':([41,50,51,52,53,54,55,56,57,58,59,60,76,77,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[-122,76,-122,-39,-40,-41,-42,-43,-44,-45,-46,-47,-37,-38,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'REGRESA':([41,51,53,54,55,56,57,58,59,60,76,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[62,62,-40,-41,-42,-43,-44,-45,-46,-47,-37,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'LECTURA':([41,51,53,54,55,56,57,58,59,60,76,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[63,63,-40,-41,-42,-43,-44,-45,-46,-47,-37,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'ESCRIBE':([41,51,53,54,55,56,57,58,59,60,76,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[64,64,-40,-41,-42,-43,-44,-45,-46,-47,-37,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'SI':([41,51,53,54,55,56,57,58,59,60,76,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[65,65,-40,-41,-42,-43,-44,-45,-46,-47,-37,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'MIENTRAS':([41,51,53,54,55,56,57,58,59,60,76,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[66,66,-40,-41,-42,-43,-44,-45,-46,-47,-37,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'DESDE':([41,51,53,54,55,56,57,58,59,60,76,167,191,195,203,242,245,247,249,250,254,255,257,259,265,266,267,],[67,67,-40,-41,-42,-43,-44,-45,-46,-47,-37,-100,-101,-105,-98,-122,-48,-110,-112,-118,-114,-116,-112,-113,-121,-118,-119,]),'CTE_INT':([47,80,82,83,97,98,99,102,118,125,131,149,162,169,170,174,175,176,177,178,179,182,183,186,187,190,199,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[74,107,107,107,107,107,-80,107,107,-80,107,107,107,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'ASSIGN':([61,78,85,94,95,96,119,126,154,163,],[-49,-122,-49,125,-51,-53,-122,-52,199,-54,]),'R_SQUARE_BRACKET':([74,95,96,101,103,104,105,106,107,108,109,110,111,126,127,133,134,135,136,137,138,139,140,141,142,143,163,168,171,172,173,180,181,184,185,188,189,207,228,229,230,231,232,233,234,235,236,237,238,239,240,246,252,],[92,-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,163,-122,-122,-122,-122,-122,-81,-82,-83,-84,-85,-122,-54,-55,-59,-56,-61,-68,-70,-73,-75,-78,-90,-80,-91,-57,-58,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-80,-92,]),'SINO':([76,242,],[-37,248,]),'NOT':([80,82,83,97,98,99,118,125,131,149,162,169,170,190,199,205,208,209,220,224,256,],[102,102,102,102,102,-80,102,-80,102,102,102,-80,-80,-80,-80,102,102,102,102,102,102,]),'CTE_FLOAT':([80,82,83,97,98,99,102,118,125,131,149,162,169,170,174,175,176,177,178,179,182,183,186,187,190,199,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[108,108,108,108,108,-80,108,108,-80,108,108,108,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'CTE_CHAR':([80,82,83,97,98,99,102,118,125,131,149,162,169,170,174,175,176,177,178,179,182,183,186,187,190,199,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[109,109,109,109,109,-80,109,109,-80,109,109,109,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,-80,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'LETRERO':([82,149,],[115,115,]),'DETERMINANT':([95,96,106,107,108,109,110,111,126,143,163,189,207,228,246,252,],[-51,-53,139,-86,-87,-88,-89,-49,-52,-122,-54,-90,-80,-91,-80,-92,]),'TRANSPOSED':([95,96,106,107,108,109,110,111,126,143,163,189,207,228,246,252,],[-51,-53,140,-86,-87,-88,-89,-49,-52,-122,-54,-90,-80,-91,-80,-92,]),'INVERSE':([95,96,106,107,108,109,110,111,126,143,163,189,207,228,246,252,],[-51,-53,141,-86,-87,-88,-89,-49,-52,-122,-54,-90,-80,-91,-80,-92,]),'MULTIPLY':([95,96,105,106,107,108,109,110,111,126,137,138,139,140,141,142,143,163,189,207,228,246,252,],[-51,-53,-79,-122,-86,-87,-88,-89,-49,-52,186,-81,-82,-83,-84,-85,-122,-54,-90,-80,-91,-80,-92,]),'DIVIDE':([95,96,105,106,107,108,109,110,111,126,137,138,139,140,141,142,143,163,189,207,228,246,252,],[-51,-53,-79,-122,-86,-87,-88,-89,-49,-52,187,-81,-82,-83,-84,-85,-122,-54,-90,-80,-91,-80,-92,]),'SUM':([95,96,104,105,106,107,108,109,110,111,126,136,137,138,139,140,141,142,143,163,185,188,189,207,228,239,240,246,252,],[-51,-53,-74,-79,-122,-86,-87,-88,-89,-49,-52,182,-122,-81,-82,-83,-84,-85,-122,-54,-75,-78,-90,-80,-91,-76,-77,-80,-92,]),'SUBTRACT':([95,96,104,105,106,107,108,109,110,111,126,136,137,138,139,140,141,142,143,163,185,188,189,207,228,239,240,246,252,],[-51,-53,-74,-79,-122,-86,-87,-88,-89,-49,-52,183,-122,-81,-82,-83,-84,-85,-122,-54,-75,-78,-90,-80,-91,-76,-77,-80,-92,]),'EQUALS':([95,96,103,104,105,106,107,108,109,110,111,126,135,136,137,138,139,140,141,142,143,163,181,184,185,188,189,207,228,237,238,239,240,246,252,],[-51,-53,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,174,-122,-122,-81,-82,-83,-84,-85,-122,-54,-70,-73,-75,-78,-90,-80,-91,-71,-72,-76,-77,-80,-92,]),'NOT_EQUAL':([95,96,103,104,105,106,107,108,109,110,111,126,135,136,137,138,139,140,141,142,143,163,181,184,185,188,189,207,228,237,238,239,240,246,252,],[-51,-53,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,175,-122,-122,-81,-82,-83,-84,-85,-122,-54,-70,-73,-75,-78,-90,-80,-91,-71,-72,-76,-77,-80,-92,]),'LESS_THAN':([95,96,103,104,105,106,107,108,109,110,111,126,135,136,137,138,139,140,141,142,143,163,181,184,185,188,189,207,228,237,238,239,240,246,252,],[-51,-53,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,176,-122,-122,-81,-82,-83,-84,-85,-122,-54,-70,-73,-75,-78,-90,-80,-91,-71,-72,-76,-77,-80,-92,]),'LESS_THAN_EQUAL':([95,96,103,104,105,106,107,108,109,110,111,126,135,136,137,138,139,140,141,142,143,163,181,184,185,188,189,207,228,237,238,239,240,246,252,],[-51,-53,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,177,-122,-122,-81,-82,-83,-84,-85,-122,-54,-70,-73,-75,-78,-90,-80,-91,-71,-72,-76,-77,-80,-92,]),'GREATER_THAN':([95,96,103,104,105,106,107,108,109,110,111,126,135,136,137,138,139,140,141,142,143,163,181,184,185,188,189,207,228,237,238,239,240,246,252,],[-51,-53,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,178,-122,-122,-81,-82,-83,-84,-85,-122,-54,-70,-73,-75,-78,-90,-80,-91,-71,-72,-76,-77,-80,-92,]),'GREATER_THAN_EQUAL':([95,96,103,104,105,106,107,108,109,110,111,126,135,136,137,138,139,140,141,142,143,163,181,184,185,188,189,207,228,237,238,239,240,246,252,],[-51,-53,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,179,-122,-122,-81,-82,-83,-84,-85,-122,-54,-70,-73,-75,-78,-90,-80,-91,-71,-72,-76,-77,-80,-92,]),'AND':([95,96,101,103,104,105,106,107,108,109,110,111,126,133,134,135,136,137,138,139,140,141,142,143,163,173,180,181,184,185,188,189,207,228,231,232,233,234,235,236,237,238,239,240,246,252,],[-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,169,169,-122,-122,-122,-81,-82,-83,-84,-85,-122,-54,-61,-68,-70,-73,-75,-78,-90,-80,-91,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-80,-92,]),'OR':([95,96,101,103,104,105,106,107,108,109,110,111,126,133,134,135,136,137,138,139,140,141,142,143,163,173,180,181,184,185,188,189,207,228,231,232,233,234,235,236,237,238,239,240,246,252,],[-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,170,170,-122,-122,-122,-81,-82,-83,-84,-85,-122,-54,-61,-68,-70,-73,-75,-78,-90,-80,-91,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-80,-92,]),'HASTA':([95,96,101,103,104,105,106,107,108,109,110,111,126,133,134,135,136,137,138,139,140,141,142,143,163,168,171,172,173,180,181,184,185,188,189,207,228,229,230,231,232,233,234,235,236,237,238,239,240,244,246,251,252,],[-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,-122,-122,-122,-122,-122,-81,-82,-83,-84,-85,-122,-54,-55,-59,-56,-61,-68,-70,-73,-75,-78,-90,-80,-91,-57,-58,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-50,-80,256,-92,]),'HACER':([95,96,101,103,104,105,106,107,108,109,110,111,126,133,134,135,136,137,138,139,140,141,142,143,163,168,171,172,173,180,181,184,185,188,189,207,228,229,230,231,232,233,234,235,236,237,238,239,240,246,252,258,260,261,262,263,],[-51,-53,-60,-69,-74,-79,-122,-86,-87,-88,-89,-49,-52,-122,-122,-122,-122,-122,-81,-82,-83,-84,-85,-122,-54,-55,-59,-56,-61,-68,-70,-73,-75,-78,-90,-80,-91,-57,-58,-62,-63,-64,-65,-66,-67,-71,-72,-76,-77,-80,-92,-117,-120,-69,-111,264,]),'HAZ':([152,197,198,223,],[-111,222,-111,243,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'programa':([0,],[2,]),'jump':([5,],[6,]),'var':([6,42,],[7,68,]),'empty':([6,7,32,38,39,41,42,44,48,51,69,78,98,106,113,115,116,119,120,122,123,124,133,134,135,136,137,143,146,160,165,200,205,220,242,],[9,12,37,46,46,52,9,72,72,52,89,96,130,142,96,150,150,96,12,159,46,159,171,171,180,184,188,96,194,72,206,89,130,130,249,]),'funcion':([7,120,],[10,155,]),'var_seen':([8,],[13,]),'clear_scope':([10,],[14,]),'funcionp':([11,],[15,]),'tipoRetorno':([11,],[17,]),'tipo':([11,13,32,88,122,124,],[18,24,36,121,24,24,]),'varp':([13,122,124,],[23,158,158,]),'tipo_seen':([24,],[27,]),'update_jump':([25,249,257,],[28,254,259,]),'create_func_scope':([26,],[29,]),'parametro':([32,],[35,]),'variable_seen':([33,91,],[38,123,]),'bloque':([34,68,222,243,253,264,],[40,86,242,250,257,265,]),'varppp':([38,39,123,],[44,48,160,]),'dimDeclare':([38,39,45,123,],[45,45,73,45,]),'bloquep':([41,51,],[50,77,]),'estatuto':([41,51,],[51,51,]),'asignacion':([41,51,],[53,53,]),'funcionVacia':([41,51,],[54,54,]),'regresa':([41,51,],[55,55,]),'lectura':([41,51,],[56,56,]),'escritura':([41,51,],[57,57,]),'decision':([41,51,],[58,58,]),'cicloCondicional':([41,51,],[59,59,]),'cicloNoCondicional':([41,51,],[60,60,]),'save_param':([43,156,],[69,200,]),'varpp':([44,48,160,],[70,75,201,]),'operand_seen':([61,85,111,],[78,119,143,]),'set_func_scope':([61,111,],[79,144,]),'jump_cycle':([66,258,],[84,260,]),'parametrop':([69,200,],[87,225,]),'delete_type':([70,75,],[90,93,]),'dimId':([78,113,119,143,],[94,146,154,189,]),'dim':([78,95,113,119,143,],[95,126,95,95,95,]),'expresion':([80,82,83,97,98,118,131,149,162,205,208,209,220,224,256,],[100,116,117,127,129,153,166,116,202,129,229,230,129,244,258,]),'relacional':([80,82,83,97,98,102,118,131,149,162,205,208,209,210,211,212,213,214,215,220,224,256,],[101,101,101,101,101,134,101,101,101,101,101,101,101,231,232,233,234,235,236,101,101,101,]),'aritmetica':([80,82,83,97,98,102,118,131,149,162,205,208,209,210,211,212,213,214,215,216,217,220,224,256,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,237,238,103,103,103,]),'factor':([80,82,83,97,98,102,118,131,149,162,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,239,240,104,104,104,]),'matriz':([80,82,83,97,98,102,118,131,149,162,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'cte':([80,82,83,97,98,102,118,131,149,162,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'llamadaFuncion':([80,82,83,97,98,102,118,131,149,162,205,208,209,210,211,212,213,214,215,216,217,218,219,220,224,256,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'lecturap':([81,193,],[112,221,]),'escriturap':([82,149,],[114,196,]),'end_func':([86,],[120,]),'llamadaFuncionp':([98,205,220,],[128,227,241,]),'operation_seen':([99,125,169,170,174,175,176,177,178,179,182,183,186,187,190,199,207,246,],[131,162,208,209,210,211,212,213,214,215,216,217,218,219,220,224,228,252,]),'apply_operation_expresion':([101,],[133,]),'apply_operation_relational':([103,261,],[135,262,]),'apply_operation_aritmetica':([104,],[136,]),'apply_operation_factor':([105,],[137,]),'matrizp':([106,],[138,]),'escriturapp':([115,116,],[148,151,]),'varpppp':([122,124,],[157,161,]),'verify_parameter':([129,],[165,]),'expresionp':([133,134,],[168,172,]),'relacionalp':([135,],[173,]),'aritmeticap':([136,],[181,]),'factorp':([137,],[185,]),'lecturapp':([146,],[192,]),'jump_false':([152,198,262,],[197,223,263,]),'llamadaFuncionpp':([165,],[204,]),'apply_operation_assign':([202,244,],[226,251,]),'decisionp':([242,],[247,]),'jump_else':([248,],[253,]),'update_jump_cycle':([250,266,],[255,267,]),'add_gt':([260,],[261,]),'add_one':([265,],[266,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> programa','start',1,'p_start','patitoParser.py',175),
  ('programa -> PROGRAMA ID SEMICOLON jump var funcion clear_scope PRINCIPAL update_jump L_PARENTHESIS R_PARENTHESIS bloque EOF','programa',13,'p_programa','patitoParser.py',193),
  ('jump -> <empty>','jump',0,'p_jump','patitoParser.py',199),
  ('clear_scope -> <empty>','clear_scope',0,'p_clear_scope','patitoParser.py',205),
  ('var -> VAR var_seen varp','var',3,'p_variables','patitoParser.py',214),
  ('var -> empty','var',1,'p_variables','patitoParser.py',215),
  ('var_seen -> <empty>','var_seen',0,'p_var_seen','patitoParser.py',232),
  ('varp -> tipo tipo_seen COLON ID variable_seen varppp varpp delete_type SEMICOLON varpppp','varp',10,'p_variablesp','patitoParser.py',242),
  ('varp -> tipo tipo_seen COLON ID error varppp varpp delete_type SEMICOLON varpppp','varp',10,'p_variablesp','patitoParser.py',243),
  ('tipo_seen -> <empty>','tipo_seen',0,'p_tipo_seen','patitoParser.py',252),
  ('variable_seen -> <empty>','variable_seen',0,'p_variable_seen','patitoParser.py',260),
  ('delete_type -> <empty>','delete_type',0,'p_delete_type','patitoParser.py',285),
  ('varpp -> COMMA ID variable_seen varppp varpp','varpp',5,'p_variablespp','patitoParser.py',294),
  ('varpp -> empty','varpp',1,'p_variablespp','patitoParser.py',295),
  ('varppp -> dimDeclare','varppp',1,'p_variablesppp','patitoParser.py',305),
  ('varppp -> dimDeclare dimDeclare','varppp',2,'p_variablesppp','patitoParser.py',306),
  ('varppp -> empty','varppp',1,'p_variablesppp','patitoParser.py',307),
  ('varpppp -> varp','varpppp',1,'p_variablespppp','patitoParser.py',323),
  ('varpppp -> empty','varpppp',1,'p_variablespppp','patitoParser.py',324),
  ('dimDeclare -> L_SQUARE_BRACKET CTE_INT R_SQUARE_BRACKET','dimDeclare',3,'p_dimDeclare','patitoParser.py',331),
  ('tipo -> INT','tipo',1,'p_tipo','patitoParser.py',366),
  ('tipo -> FLOAT','tipo',1,'p_tipo','patitoParser.py',367),
  ('tipo -> CHAR','tipo',1,'p_tipo','patitoParser.py',368),
  ('funcion -> FUNCION funcionp','funcion',2,'p_funcion','patitoParser.py',374),
  ('funcion -> FUNCION error','funcion',2,'p_funcion','patitoParser.py',375),
  ('funcion -> empty','funcion',1,'p_funcion','patitoParser.py',376),
  ('funcionp -> tipoRetorno ID create_func_scope L_PARENTHESIS parametro R_PARENTHESIS var bloque end_func funcion','funcionp',10,'p_funcionp','patitoParser.py',385),
  ('create_func_scope -> <empty>','create_func_scope',0,'p_create_func_scope','patitoParser.py',393),
  ('end_func -> <empty>','end_func',0,'p_end_func','patitoParser.py',412),
  ('parametro -> tipo ID save_param parametrop','parametro',4,'p_parametro','patitoParser.py',421),
  ('parametro -> empty','parametro',1,'p_parametro','patitoParser.py',422),
  ('save_param -> <empty>','save_param',0,'p_save_param','patitoParser.py',431),
  ('parametrop -> COMMA tipo ID save_param parametrop','parametrop',5,'p_parametrop','patitoParser.py',438),
  ('parametrop -> empty','parametrop',1,'p_parametrop','patitoParser.py',439),
  ('tipoRetorno -> tipo','tipoRetorno',1,'p_tipoRetorno','patitoParser.py',448),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','patitoParser.py',449),
  ('bloque -> L_CURLY_BRACKET bloquep R_CURLY_BRACKET','bloque',3,'p_bloque','patitoParser.py',455),
  ('bloquep -> estatuto bloquep','bloquep',2,'p_bloquep','patitoParser.py',461),
  ('bloquep -> empty','bloquep',1,'p_bloquep','patitoParser.py',462),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','patitoParser.py',471),
  ('estatuto -> funcionVacia','estatuto',1,'p_estatuto','patitoParser.py',472),
  ('estatuto -> regresa','estatuto',1,'p_estatuto','patitoParser.py',473),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','patitoParser.py',474),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','patitoParser.py',475),
  ('estatuto -> decision','estatuto',1,'p_estatuto','patitoParser.py',476),
  ('estatuto -> cicloCondicional','estatuto',1,'p_estatuto','patitoParser.py',477),
  ('estatuto -> cicloNoCondicional','estatuto',1,'p_estatuto','patitoParser.py',478),
  ('asignacion -> ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign SEMICOLON','asignacion',8,'p_asignacion','patitoParser.py',484),
  ('operand_seen -> <empty>','operand_seen',0,'p_operand_seen','patitoParser.py',490),
  ('apply_operation_assign -> <empty>','apply_operation_assign',0,'p_apply_operation_assign','patitoParser.py',504),
  ('dimId -> dim','dimId',1,'p_dimId','patitoParser.py',513),
  ('dimId -> dim dim','dimId',2,'p_dimId','patitoParser.py',514),
  ('dimId -> empty','dimId',1,'p_dimId','patitoParser.py',515),
  ('dim -> L_SQUARE_BRACKET expresion R_SQUARE_BRACKET','dim',3,'p_dim','patitoParser.py',524),
  ('expresion -> relacional apply_operation_expresion expresionp','expresion',3,'p_expresion','patitoParser.py',531),
  ('expresion -> NOT relacional expresionp','expresion',3,'p_expresion','patitoParser.py',532),
  ('expresionp -> AND operation_seen expresion','expresionp',3,'p_expresionp','patitoParser.py',541),
  ('expresionp -> OR operation_seen expresion','expresionp',3,'p_expresionp','patitoParser.py',542),
  ('expresionp -> empty','expresionp',1,'p_expresionp','patitoParser.py',543),
  ('apply_operation_expresion -> <empty>','apply_operation_expresion',0,'p_apply_operation_expresion','patitoParser.py',553),
  ('relacional -> aritmetica apply_operation_relational relacionalp','relacional',3,'p_relacional','patitoParser.py',562),
  ('relacionalp -> EQUALS operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',568),
  ('relacionalp -> NOT_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',569),
  ('relacionalp -> LESS_THAN operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',570),
  ('relacionalp -> LESS_THAN_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',571),
  ('relacionalp -> GREATER_THAN operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',572),
  ('relacionalp -> GREATER_THAN_EQUAL operation_seen relacional','relacionalp',3,'p_relacionalp','patitoParser.py',573),
  ('relacionalp -> empty','relacionalp',1,'p_relacionalp','patitoParser.py',574),
  ('apply_operation_relational -> <empty>','apply_operation_relational',0,'p_apply_operation_relational','patitoParser.py',584),
  ('aritmetica -> factor apply_operation_aritmetica aritmeticap','aritmetica',3,'p_aritmetica','patitoParser.py',593),
  ('aritmeticap -> SUM operation_seen aritmetica','aritmeticap',3,'p_aritmeticap','patitoParser.py',599),
  ('aritmeticap -> SUBTRACT operation_seen aritmetica','aritmeticap',3,'p_aritmeticap','patitoParser.py',600),
  ('aritmeticap -> empty','aritmeticap',1,'p_aritmeticap','patitoParser.py',601),
  ('apply_operation_aritmetica -> <empty>','apply_operation_aritmetica',0,'p_apply_operation_aritmetica','patitoParser.py',611),
  ('factor -> matriz apply_operation_factor factorp','factor',3,'p_factor','patitoParser.py',620),
  ('factorp -> MULTIPLY operation_seen factor','factorp',3,'p_factorp','patitoParser.py',626),
  ('factorp -> DIVIDE operation_seen factor','factorp',3,'p_factorp','patitoParser.py',627),
  ('factorp -> empty','factorp',1,'p_factorp','patitoParser.py',628),
  ('apply_operation_factor -> <empty>','apply_operation_factor',0,'p_apply_operation_factor','patitoParser.py',638),
  ('operation_seen -> <empty>','operation_seen',0,'p_operation_seen','patitoParser.py',648),
  ('matriz -> cte matrizp','matriz',2,'p_matriz','patitoParser.py',660),
  ('matrizp -> DETERMINANT','matrizp',1,'p_matrizp','patitoParser.py',666),
  ('matrizp -> TRANSPOSED','matrizp',1,'p_matrizp','patitoParser.py',667),
  ('matrizp -> INVERSE','matrizp',1,'p_matrizp','patitoParser.py',668),
  ('matrizp -> empty','matrizp',1,'p_matrizp','patitoParser.py',669),
  ('cte -> CTE_INT','cte',1,'p_cte','patitoParser.py',675),
  ('cte -> CTE_FLOAT','cte',1,'p_cte','patitoParser.py',676),
  ('cte -> CTE_CHAR','cte',1,'p_cte','patitoParser.py',677),
  ('cte -> llamadaFuncion','cte',1,'p_cte','patitoParser.py',678),
  ('cte -> ID operand_seen dimId','cte',3,'p_cte','patitoParser.py',679),
  ('cte -> L_PARENTHESIS operation_seen expresion R_PARENTHESIS operation_seen','cte',5,'p_cte','patitoParser.py',680),
  ('llamadaFuncion -> ID set_func_scope L_PARENTHESIS operation_seen llamadaFuncionp R_PARENTHESIS operation_seen','llamadaFuncion',7,'p_llamadaFuncion','patitoParser.py',715),
  ('llamadaFuncionp -> expresion verify_parameter llamadaFuncionpp','llamadaFuncionp',3,'p_llamadaFuncionp','patitoParser.py',734),
  ('llamadaFuncionp -> empty','llamadaFuncionp',1,'p_llamadaFuncionp','patitoParser.py',735),
  ('llamadaFuncionpp -> COMMA llamadaFuncionp','llamadaFuncionpp',2,'p_llamadaFuncionpp','patitoParser.py',745),
  ('llamadaFuncionpp -> empty','llamadaFuncionpp',1,'p_llamadaFuncionpp','patitoParser.py',746),
  ('verify_parameter -> <empty>','verify_parameter',0,'p_verify_parameter','patitoParser.py',755),
  ('funcionVacia -> ID set_func_scope L_PARENTHESIS llamadaFuncionp R_PARENTHESIS SEMICOLON','funcionVacia',6,'p_funcionVacia','patitoParser.py',761),
  ('set_func_scope -> <empty>','set_func_scope',0,'p_set_func_scope','patitoParser.py',774),
  ('regresa -> REGRESA L_PARENTHESIS expresion R_PARENTHESIS SEMICOLON','regresa',5,'p_regresa','patitoParser.py',787),
  ('lectura -> LECTURA L_PARENTHESIS lecturap R_PARENTHESIS SEMICOLON','lectura',5,'p_lectura','patitoParser.py',795),
  ('lecturap -> ID dimId lecturapp','lecturap',3,'p_lecturap','patitoParser.py',801),
  ('lecturapp -> COMMA lecturap','lecturapp',2,'p_lecturapp','patitoParser.py',807),
  ('lecturapp -> empty','lecturapp',1,'p_lecturapp','patitoParser.py',808),
  ('escritura -> ESCRIBE L_PARENTHESIS escriturap R_PARENTHESIS SEMICOLON','escritura',5,'p_escritura','patitoParser.py',817),
  ('escriturap -> LETRERO escriturapp','escriturap',2,'p_escriturap','patitoParser.py',823),
  ('escriturap -> expresion escriturapp','escriturap',2,'p_escriturap','patitoParser.py',824),
  ('escriturapp -> COMMA escriturap','escriturapp',2,'p_escriturapp','patitoParser.py',830),
  ('escriturapp -> empty','escriturapp',1,'p_escriturapp','patitoParser.py',831),
  ('decision -> SI L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque decisionp','decision',8,'p_decision','patitoParser.py',840),
  ('jump_false -> <empty>','jump_false',0,'p_jump_false','patitoParser.py',846),
  ('update_jump -> <empty>','update_jump',0,'p_update_jump','patitoParser.py',852),
  ('decisionp -> SINO jump_else bloque update_jump','decisionp',4,'p_decisionp','patitoParser.py',858),
  ('decisionp -> empty update_jump','decisionp',2,'p_decisionp','patitoParser.py',859),
  ('jump_else -> <empty>','jump_else',0,'p_jump_else','patitoParser.py',868),
  ('cicloCondicional -> MIENTRAS jump_cycle L_PARENTHESIS expresion R_PARENTHESIS jump_false HAZ bloque update_jump_cycle','cicloCondicional',9,'p_cicloCondicional','patitoParser.py',874),
  ('jump_cycle -> <empty>','jump_cycle',0,'p_jump_cycle','patitoParser.py',880),
  ('update_jump_cycle -> <empty>','update_jump_cycle',0,'p_update_jump_cycle','patitoParser.py',886),
  ('cicloNoCondicional -> DESDE ID operand_seen dimId ASSIGN operation_seen expresion apply_operation_assign HASTA expresion jump_cycle add_gt apply_operation_relational jump_false HACER bloque add_one update_jump_cycle','cicloNoCondicional',18,'p_cicloNoCondicional','patitoParser.py',892),
  ('add_gt -> <empty>','add_gt',0,'p_add_gt','patitoParser.py',898),
  ('add_one -> <empty>','add_one',0,'p_add_one','patitoParser.py',908),
  ('empty -> <empty>','empty',0,'p_empty','patitoParser.py',927),
]
