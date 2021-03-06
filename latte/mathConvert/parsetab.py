
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDSUB_OP CLOSE_INVIS_PAREN CLOSE_PAREN CONTROL_ID DIV_OP ENTITY EQUALS MATHEMATICAL_ID MULT_OP NUMBER OPEN_INVIS_PAREN OPEN_PAREN POWER SUBSCRIPT SYMBOL TEXT_FUNCexpression : expression ENTITY expressionexpression : expression EQUALS expressionexpression : expression ADDSUB_OP termexpression : termterm : term MULT_OP factorterm : term DIV_OP factorterm : factorfactor : ADDSUB_OP termfactor : factor POWER factorfactor : factor SUBSCRIPT factorfactor : NUMBERfactor : SYMBOLfactor : MATHEMATICAL_ID OPEN_PAREN expression CLOSE_PARENfactor : TEXT_FUNCfactor : OPEN_PAREN expression CLOSE_PARENfactor : OPEN_INVIS_PAREN expression CLOSE_INVIS_PAREN'
    
_lr_action_items = {'ADDSUB_OP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,],[2,13,2,-4,-7,-11,-12,2,-14,2,2,2,2,-8,2,2,2,2,2,13,13,13,13,-3,-5,-6,-9,-10,13,-15,-16,-13,]),'NUMBER':([0,2,8,10,11,12,13,15,16,17,18,19,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'SYMBOL':([0,2,8,10,11,12,13,15,16,17,18,19,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'MATHEMATICAL_ID':([0,2,8,10,11,12,13,15,16,17,18,19,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'TEXT_FUNC':([0,2,8,10,11,12,13,15,16,17,18,19,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'OPEN_PAREN':([0,2,7,8,10,11,12,13,15,16,17,18,19,],[8,8,19,8,8,8,8,8,8,8,8,8,8,]),'OPEN_INVIS_PAREN':([0,2,8,10,11,12,13,15,16,17,18,19,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,3,4,5,6,9,14,22,23,24,25,26,27,28,30,31,32,],[0,-4,-7,-11,-12,-14,-8,-1,-2,-3,-5,-6,-9,-10,-15,-16,-13,]),'ENTITY':([1,3,4,5,6,9,14,20,21,22,23,24,25,26,27,28,29,30,31,32,],[11,-4,-7,-11,-12,-14,-8,11,11,11,11,-3,-5,-6,-9,-10,11,-15,-16,-13,]),'EQUALS':([1,3,4,5,6,9,14,20,21,22,23,24,25,26,27,28,29,30,31,32,],[12,-4,-7,-11,-12,-14,-8,12,12,12,12,-3,-5,-6,-9,-10,12,-15,-16,-13,]),'CLOSE_PAREN':([3,4,5,6,9,14,20,22,23,24,25,26,27,28,29,30,31,32,],[-4,-7,-11,-12,-14,-8,30,-1,-2,-3,-5,-6,-9,-10,32,-15,-16,-13,]),'CLOSE_INVIS_PAREN':([3,4,5,6,9,14,21,22,23,24,25,26,27,28,30,31,32,],[-4,-7,-11,-12,-14,-8,31,-1,-2,-3,-5,-6,-9,-10,-15,-16,-13,]),'MULT_OP':([3,4,5,6,9,14,24,25,26,27,28,30,31,32,],[15,-7,-11,-12,-14,15,15,-5,-6,-9,-10,-15,-16,-13,]),'DIV_OP':([3,4,5,6,9,14,24,25,26,27,28,30,31,32,],[16,-7,-11,-12,-14,16,16,-5,-6,-9,-10,-15,-16,-13,]),'POWER':([4,5,6,9,14,25,26,27,28,30,31,32,],[17,-11,-12,-14,-8,17,17,17,17,-15,-16,-13,]),'SUBSCRIPT':([4,5,6,9,14,25,26,27,28,30,31,32,],[18,-11,-12,-14,-8,18,18,18,18,-15,-16,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,8,10,11,12,19,],[1,20,21,22,23,29,]),'term':([0,2,8,10,11,12,13,19,],[3,14,3,3,3,3,24,3,]),'factor':([0,2,8,10,11,12,13,15,16,17,18,19,],[4,4,4,4,4,4,4,25,26,27,28,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression ENTITY expression','expression',3,'p_expression_entity','parser.py',15),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_equals','parser.py',20),
  ('expression -> expression ADDSUB_OP term','expression',3,'p_expression_addsub_op','parser.py',25),
  ('expression -> term','expression',1,'p_expression_term','parser.py',30),
  ('term -> term MULT_OP factor','term',3,'p_term_multiply','parser.py',35),
  ('term -> term DIV_OP factor','term',3,'p_expression_fraction','parser.py',40),
  ('term -> factor','term',1,'p_term_factor','parser.py',45),
  ('factor -> ADDSUB_OP term','factor',2,'p_negative','parser.py',50),
  ('factor -> factor POWER factor','factor',3,'p_term_power','parser.py',55),
  ('factor -> factor SUBSCRIPT factor','factor',3,'p_term_subscript','parser.py',60),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',65),
  ('factor -> SYMBOL','factor',1,'p_factor_symbol','parser.py',70),
  ('factor -> MATHEMATICAL_ID OPEN_PAREN expression CLOSE_PAREN','factor',4,'p_factor_func','parser.py',75),
  ('factor -> TEXT_FUNC','factor',1,'p_expression_textfunc','parser.py',88),
  ('factor -> OPEN_PAREN expression CLOSE_PAREN','factor',3,'p_factor_parenthetical','parser.py',93),
  ('factor -> OPEN_INVIS_PAREN expression CLOSE_INVIS_PAREN','factor',3,'p_factor_invis_paren','parser.py',98),
]
