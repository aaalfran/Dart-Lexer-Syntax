
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CADENA COMA CONST CORCHETE_DER CORCHETE_IZQ DIVISION DOSPUNTOS DOUBLE ELSE ES_IGUAL FALSE FINAL FLOAT FOR FUNCION IF IGUAL IN INCREMENTADOR INT INTEGER LIST LLAVEL LLAVER LPARENT MAIN MAS MAYOR_O_IGUAL MAYOR_QUE MENOR_O_IGUAL MENOR_QUE MULTIPL NEGACION NO_IGUAL OR PARSE PRINT PUNTO PUNTOCOMA READLINESYNC RESTA RETURN RPARENT SALTO_LINEA STDIN STDOUT STRING TABULACION TODOUBLE TOINT TOSTRING TRUE VAR VARIABLE VOID WRITEsentencias : asignacion\n                  | comparacion\n                  | operacion\n                  | impresion\n                  | for\n                  | if\n                  | if-else\n                  | write\n                   sentencias2 : funcion\n                   | estructurassentenciasVarias : sentencias2\n                      | sentencias2 sentenciasVariasasignacion : declaradores VARIABLE IGUAL tipodato PUNTOCOMA\n                  | declaradores VARIABLE IGUAL negativo PUNTOCOMA\n                  | BOOL VARIABLE IGUAL valoresverdad PUNTOCOMAdeclaradores : INT\n                  | CONST\n                  | VAR\n                  | BOOL\n                  | FINAL\n                  | STRINGtipodato : INTEGER\n              | CADENA\n              | FLOAT\n              | VARIABLE\n              | valoresverdad\n              | negativo\n            \n    negativo : RESTA INTEGER\n              | RESTA FLOAT\n    valoresverdad : TRUE\n                   | FALSEcomparacion : VARIABLE comparadores VARIABLE PUNTOCOMAcomparadores : ES_IGUAL\n                  | NO_IGUAL\n                  | MENOR_QUE\n                  | MAYOR_QUE\n                  | MENOR_O_IGUAL\n                  | MAYOR_O_IGUALoperacion : datonumerico operador datonumerico PUNTOCOMAdatonumerico : INTEGER\n                    | FLOAT\n                    | negativooperador : MAS\n                | RESTA\n                | MULTIPL\n                | DIVISIONimpresion : PRINT LPARENT tipodato RPARENT PUNTOCOMAfuncion : VOID VARIABLE LPARENT declaracionfunciones VARIABLE RPARENT LLAVEL LLAVER\n               | VOID VARIABLE LPARENT  VARIABLE RPARENT LLAVEL LLAVER\n               | VOID VARIABLE LPARENT RPARENT LLAVEL LLAVER\n               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN VARIABLE PUNTOCOMA LLAVER\n               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN tipodato PUNTOCOMA LLAVERdeclaracionfunciones : INT\n                          | DOUBLE\n                          | STRING\n                          | BOOLestructuras : declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ elementos CORCHETE_DER PUNTOCOMA\n                 | declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ CORCHETE_DER PUNTOCOMA\n                 | declaradoresestruras VARIABLE IGUAL LLAVEL elementosdiccionario LLAVER PUNTOCOMA\n                 | declaradoresestruras VARIABLE IGUAL MENOR_QUE declaracionfunciones MAYOR_QUE LLAVEL elementos LLAVER PUNTOCOMAdeclaradoresestruras : CONST\n                           | VAR\n                           | FINALelementos : tipodatoestructura\n               | tipodatoestructura COMA elementostipodatoestructura : INTEGER\n                        | CADENA\n                        | DOUBLEelementosdiccionario : tipodatoestructura DOSPUNTOS tipodatoestructura\n                          | tipodatoestructura DOSPUNTOS tipodatoestructura COMA elementosdiccionario for : FOR LPARENT declaracionesfor VARIABLE IN VARIABLE RPARENT LLAVEL LLAVER\n          | FOR LPARENT declaracionesfor VARIABLE IGUAL INTEGER PUNTOCOMA VARIABLE comparadores INTEGER PUNTOCOMA VARIABLE operador operador RPARENT LLAVEL LLAVERdeclaracionesfor : VAR\n                      | INT\n                      | VARIABLEif : IF LPARENT VARIABLE RPARENT LLAVEL LLAVER\n        | IF LPARENT TRUE RPARENT LLAVEL LLAVER\n        | IF LPARENT FALSE RPARENT LLAVEL LLAVER\n        | IF LPARENT VARIABLE comparadores VARIABLE RPARENT LLAVEL LLAVER\n        | IF LPARENT datonumerico comparadores datonumerico RPARENT LLAVEL LLAVERif-else : if ELSE LLAVEL LLAVERwrite : STDOUT PUNTO WRITE LPARENT tipodato RPARENT PUNTOCOMA'
    
_lr_action_items = {'BOOL':([0,],[13,]),'VARIABLE':([0,10,13,20,21,22,23,24,29,30,31,32,33,34,35,42,43,44,49,62,63,64,65,80,84,89,106,117,],[11,28,36,-16,-17,-18,-20,-21,50,-33,-34,-35,-36,-37,-38,57,63,66,57,78,-75,-73,-74,92,57,97,111,118,]),'PRINT':([0,],[15,]),'FOR':([0,],[16,]),'IF':([0,],[18,]),'STDOUT':([0,],[19,]),'INT':([0,43,],[20,65,]),'CONST':([0,],[21,]),'VAR':([0,43,],[22,64,]),'FINAL':([0,],[23,]),'STRING':([0,],[24,]),'INTEGER':([0,26,30,31,32,33,34,35,37,38,39,40,41,42,44,49,83,84,90,115,],[17,46,-33,-34,-35,-36,-37,-38,17,-43,-44,-45,-46,54,17,54,17,54,98,116,]),'FLOAT':([0,26,30,31,32,33,34,35,37,38,39,40,41,42,44,49,83,84,],[25,47,-33,-34,-35,-36,-37,-38,25,-43,-44,-45,-46,56,25,56,25,56,]),'RESTA':([0,12,14,17,25,30,31,32,33,34,35,37,38,39,40,41,42,44,46,47,49,83,84,118,119,],[26,-42,39,-40,-41,-33,-34,-35,-36,-37,-38,26,-43,-44,-45,-46,26,26,-28,-29,26,26,26,39,39,]),'$end':([1,2,3,4,5,6,7,8,9,71,74,76,85,86,87,88,99,101,102,109,112,113,114,123,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-81,-32,-39,-13,-14,-15,-47,-76,-77,-78,-82,-79,-80,-71,-72,]),'ELSE':([7,99,101,102,112,113,],[27,-76,-77,-78,-79,-80,]),'ES_IGUAL':([11,12,17,25,46,47,66,69,111,],[30,-42,-40,-41,-28,-29,30,30,30,]),'NO_IGUAL':([11,12,17,25,46,47,66,69,111,],[31,-42,-40,-41,-28,-29,31,31,31,]),'MENOR_QUE':([11,12,17,25,46,47,66,69,111,],[32,-42,-40,-41,-28,-29,32,32,32,]),'MAYOR_QUE':([11,12,17,25,46,47,66,69,111,],[33,-42,-40,-41,-28,-29,33,33,33,]),'MENOR_O_IGUAL':([11,12,17,25,46,47,66,69,111,],[34,-42,-40,-41,-28,-29,34,34,34,]),'MAYOR_O_IGUAL':([11,12,17,25,46,47,66,69,111,],[35,-42,-40,-41,-28,-29,35,35,35,]),'MAS':([12,14,17,25,38,39,40,41,46,47,118,119,],[-42,38,-40,-41,-43,-44,-45,-46,-28,-29,38,38,]),'MULTIPL':([12,14,17,25,38,39,40,41,46,47,118,119,],[-42,40,-40,-41,-43,-44,-45,-46,-28,-29,40,40,]),'DIVISION':([12,14,17,25,38,39,40,41,46,47,118,119,],[-42,41,-40,-41,-43,-44,-45,-46,-28,-29,41,41,]),'PUNTOCOMA':([12,17,25,46,47,50,52,54,55,56,57,58,60,61,72,73,75,77,98,104,116,],[-42,-40,-41,-28,-29,74,76,-22,-23,-24,-25,-26,-30,-31,85,86,87,88,106,109,117,]),'RPARENT':([12,17,25,38,39,40,41,46,47,53,54,55,56,57,58,59,60,61,66,67,68,92,95,96,97,120,],[-42,-40,-41,-43,-44,-45,-46,-28,-29,77,-22,-23,-24,-25,-26,-27,-30,-31,79,81,82,100,103,104,105,121,]),'LPARENT':([15,16,18,70,],[42,43,44,84,]),'PUNTO':([19,],[45,]),'LLAVEL':([27,79,81,82,100,103,105,121,],[48,91,93,94,107,108,110,122,]),'IGUAL':([28,36,78,],[49,51,90,]),'CADENA':([42,49,84,],[55,55,55,]),'TRUE':([42,44,49,51,84,],[60,67,60,60,60,]),'FALSE':([42,44,49,51,84,],[61,68,61,61,61,]),'WRITE':([45,],[70,]),'LLAVER':([48,91,93,94,107,108,110,122,],[71,99,101,102,112,113,114,123,]),'IN':([78,],[89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'asignacion':([0,],[2,]),'comparacion':([0,],[3,]),'operacion':([0,],[4,]),'impresion':([0,],[5,]),'for':([0,],[6,]),'if':([0,],[7,]),'if-else':([0,],[8,]),'write':([0,],[9,]),'declaradores':([0,],[10,]),'negativo':([0,37,42,44,49,83,84,],[12,12,59,12,73,12,59,]),'datonumerico':([0,37,44,83,],[14,52,69,95,]),'comparadores':([11,66,69,111,],[29,80,83,115,]),'operador':([14,118,119,],[37,119,120,]),'tipodato':([42,49,84,],[53,72,96,]),'valoresverdad':([42,49,51,84,],[58,58,75,58,]),'declaracionesfor':([43,],[62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','sintaxis.py',6),
  ('sentencias -> comparacion','sentencias',1,'p_sentencias','sintaxis.py',7),
  ('sentencias -> operacion','sentencias',1,'p_sentencias','sintaxis.py',8),
  ('sentencias -> impresion','sentencias',1,'p_sentencias','sintaxis.py',9),
  ('sentencias -> for','sentencias',1,'p_sentencias','sintaxis.py',10),
  ('sentencias -> if','sentencias',1,'p_sentencias','sintaxis.py',11),
  ('sentencias -> if-else','sentencias',1,'p_sentencias','sintaxis.py',12),
  ('sentencias -> write','sentencias',1,'p_sentencias','sintaxis.py',13),
  ('sentencias2 -> funcion','sentencias2',1,'p_sentencias2','sintaxis.py',16),
  ('sentencias2 -> estructuras','sentencias2',1,'p_sentencias2','sintaxis.py',17),
  ('sentenciasVarias -> sentencias2','sentenciasVarias',1,'p_sentenciasVarias','sintaxis.py',19),
  ('sentenciasVarias -> sentencias2 sentenciasVarias','sentenciasVarias',2,'p_sentenciasVarias','sintaxis.py',20),
  ('asignacion -> declaradores VARIABLE IGUAL tipodato PUNTOCOMA','asignacion',5,'p_asignacion','sintaxis.py',24),
  ('asignacion -> declaradores VARIABLE IGUAL negativo PUNTOCOMA','asignacion',5,'p_asignacion','sintaxis.py',25),
  ('asignacion -> BOOL VARIABLE IGUAL valoresverdad PUNTOCOMA','asignacion',5,'p_asignacion','sintaxis.py',26),
  ('declaradores -> INT','declaradores',1,'p_declaradores','sintaxis.py',28),
  ('declaradores -> CONST','declaradores',1,'p_declaradores','sintaxis.py',29),
  ('declaradores -> VAR','declaradores',1,'p_declaradores','sintaxis.py',30),
  ('declaradores -> BOOL','declaradores',1,'p_declaradores','sintaxis.py',31),
  ('declaradores -> FINAL','declaradores',1,'p_declaradores','sintaxis.py',32),
  ('declaradores -> STRING','declaradores',1,'p_declaradores','sintaxis.py',33),
  ('tipodato -> INTEGER','tipodato',1,'p_tipodato','sintaxis.py',35),
  ('tipodato -> CADENA','tipodato',1,'p_tipodato','sintaxis.py',36),
  ('tipodato -> FLOAT','tipodato',1,'p_tipodato','sintaxis.py',37),
  ('tipodato -> VARIABLE','tipodato',1,'p_tipodato','sintaxis.py',38),
  ('tipodato -> valoresverdad','tipodato',1,'p_tipodato','sintaxis.py',39),
  ('tipodato -> negativo','tipodato',1,'p_tipodato','sintaxis.py',40),
  ('negativo -> RESTA INTEGER','negativo',2,'p_negativo','sintaxis.py',44),
  ('negativo -> RESTA FLOAT','negativo',2,'p_negativo','sintaxis.py',45),
  ('valoresverdad -> TRUE','valoresverdad',1,'p_valoresverdad','sintaxis.py',48),
  ('valoresverdad -> FALSE','valoresverdad',1,'p_valoresverdad','sintaxis.py',49),
  ('comparacion -> VARIABLE comparadores VARIABLE PUNTOCOMA','comparacion',4,'p_comparacion','sintaxis.py',51),
  ('comparadores -> ES_IGUAL','comparadores',1,'p_comparadores','sintaxis.py',53),
  ('comparadores -> NO_IGUAL','comparadores',1,'p_comparadores','sintaxis.py',54),
  ('comparadores -> MENOR_QUE','comparadores',1,'p_comparadores','sintaxis.py',55),
  ('comparadores -> MAYOR_QUE','comparadores',1,'p_comparadores','sintaxis.py',56),
  ('comparadores -> MENOR_O_IGUAL','comparadores',1,'p_comparadores','sintaxis.py',57),
  ('comparadores -> MAYOR_O_IGUAL','comparadores',1,'p_comparadores','sintaxis.py',58),
  ('operacion -> datonumerico operador datonumerico PUNTOCOMA','operacion',4,'p_operacion','sintaxis.py',62),
  ('datonumerico -> INTEGER','datonumerico',1,'p_datonumerico','sintaxis.py',64),
  ('datonumerico -> FLOAT','datonumerico',1,'p_datonumerico','sintaxis.py',65),
  ('datonumerico -> negativo','datonumerico',1,'p_datonumerico','sintaxis.py',66),
  ('operador -> MAS','operador',1,'p_operador','sintaxis.py',68),
  ('operador -> RESTA','operador',1,'p_operador','sintaxis.py',69),
  ('operador -> MULTIPL','operador',1,'p_operador','sintaxis.py',70),
  ('operador -> DIVISION','operador',1,'p_operador','sintaxis.py',71),
  ('impresion -> PRINT LPARENT tipodato RPARENT PUNTOCOMA','impresion',5,'p_impresion','sintaxis.py',73),
  ('funcion -> VOID VARIABLE LPARENT declaracionfunciones VARIABLE RPARENT LLAVEL LLAVER','funcion',8,'p_funcion','sintaxis.py',76),
  ('funcion -> VOID VARIABLE LPARENT VARIABLE RPARENT LLAVEL LLAVER','funcion',7,'p_funcion','sintaxis.py',77),
  ('funcion -> VOID VARIABLE LPARENT RPARENT LLAVEL LLAVER','funcion',6,'p_funcion','sintaxis.py',78),
  ('funcion -> declaracionfunciones VARIABLE LPARENT RPARENT LLAVEL RETURN VARIABLE PUNTOCOMA LLAVER','funcion',9,'p_funcion','sintaxis.py',79),
  ('funcion -> declaracionfunciones VARIABLE LPARENT RPARENT LLAVEL RETURN tipodato PUNTOCOMA LLAVER','funcion',9,'p_funcion','sintaxis.py',80),
  ('declaracionfunciones -> INT','declaracionfunciones',1,'p_declaracionfunciones','sintaxis.py',82),
  ('declaracionfunciones -> DOUBLE','declaracionfunciones',1,'p_declaracionfunciones','sintaxis.py',83),
  ('declaracionfunciones -> STRING','declaracionfunciones',1,'p_declaracionfunciones','sintaxis.py',84),
  ('declaracionfunciones -> BOOL','declaracionfunciones',1,'p_declaracionfunciones','sintaxis.py',85),
  ('estructuras -> declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ elementos CORCHETE_DER PUNTOCOMA','estructuras',7,'p_estructuras','sintaxis.py',87),
  ('estructuras -> declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ CORCHETE_DER PUNTOCOMA','estructuras',6,'p_estructuras','sintaxis.py',88),
  ('estructuras -> declaradoresestruras VARIABLE IGUAL LLAVEL elementosdiccionario LLAVER PUNTOCOMA','estructuras',7,'p_estructuras','sintaxis.py',89),
  ('estructuras -> declaradoresestruras VARIABLE IGUAL MENOR_QUE declaracionfunciones MAYOR_QUE LLAVEL elementos LLAVER PUNTOCOMA','estructuras',10,'p_estructuras','sintaxis.py',90),
  ('declaradoresestruras -> CONST','declaradoresestruras',1,'p_declaracionestructura','sintaxis.py',92),
  ('declaradoresestruras -> VAR','declaradoresestruras',1,'p_declaracionestructura','sintaxis.py',93),
  ('declaradoresestruras -> FINAL','declaradoresestruras',1,'p_declaracionestructura','sintaxis.py',94),
  ('elementos -> tipodatoestructura','elementos',1,'p_elementos','sintaxis.py',96),
  ('elementos -> tipodatoestructura COMA elementos','elementos',3,'p_elementos','sintaxis.py',97),
  ('tipodatoestructura -> INTEGER','tipodatoestructura',1,'p_tipodatoestructura','sintaxis.py',99),
  ('tipodatoestructura -> CADENA','tipodatoestructura',1,'p_tipodatoestructura','sintaxis.py',100),
  ('tipodatoestructura -> DOUBLE','tipodatoestructura',1,'p_tipodatoestructura','sintaxis.py',101),
  ('elementosdiccionario -> tipodatoestructura DOSPUNTOS tipodatoestructura','elementosdiccionario',3,'p_elementosdiccionario','sintaxis.py',103),
  ('elementosdiccionario -> tipodatoestructura DOSPUNTOS tipodatoestructura COMA elementosdiccionario','elementosdiccionario',5,'p_elementosdiccionario','sintaxis.py',104),
  ('for -> FOR LPARENT declaracionesfor VARIABLE IN VARIABLE RPARENT LLAVEL LLAVER','for',9,'p_estructura_for','sintaxis.py',106),
  ('for -> FOR LPARENT declaracionesfor VARIABLE IGUAL INTEGER PUNTOCOMA VARIABLE comparadores INTEGER PUNTOCOMA VARIABLE operador operador RPARENT LLAVEL LLAVER','for',17,'p_estructura_for','sintaxis.py',107),
  ('declaracionesfor -> VAR','declaracionesfor',1,'p_declaracionesfor','sintaxis.py',109),
  ('declaracionesfor -> INT','declaracionesfor',1,'p_declaracionesfor','sintaxis.py',110),
  ('declaracionesfor -> VARIABLE','declaracionesfor',1,'p_declaracionesfor','sintaxis.py',111),
  ('if -> IF LPARENT VARIABLE RPARENT LLAVEL LLAVER','if',6,'p_if','sintaxis.py',113),
  ('if -> IF LPARENT TRUE RPARENT LLAVEL LLAVER','if',6,'p_if','sintaxis.py',114),
  ('if -> IF LPARENT FALSE RPARENT LLAVEL LLAVER','if',6,'p_if','sintaxis.py',115),
  ('if -> IF LPARENT VARIABLE comparadores VARIABLE RPARENT LLAVEL LLAVER','if',8,'p_if','sintaxis.py',116),
  ('if -> IF LPARENT datonumerico comparadores datonumerico RPARENT LLAVEL LLAVER','if',8,'p_if','sintaxis.py',117),
  ('if-else -> if ELSE LLAVEL LLAVER','if-else',4,'p_if_else','sintaxis.py',119),
  ('write -> STDOUT PUNTO WRITE LPARENT tipodato RPARENT PUNTOCOMA','write',7,'p_write','sintaxis.py',121),
]
