
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIVIDE IDENTIFIER LPAREN MINUS NUMBER PLUS RPAREN TIMESprogram : statementsstatements : statement\n                  | statements statement statement : IDENTIFIER ASSIGN expressionstatement : expressionexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : NUMBERterm : IDENTIFIER'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,],[4,4,-2,-10,-5,-8,-9,-3,12,12,12,-10,-4,-6,-7,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,],[7,7,-2,-10,-5,-8,-9,-3,7,7,7,-10,-4,-6,-7,]),'$end':([1,2,3,4,5,6,7,8,12,13,14,15,],[0,-1,-2,-10,-5,-8,-9,-3,-10,-4,-6,-7,]),'ASSIGN':([4,],[9,]),'PLUS':([4,5,6,7,12,13,14,15,],[-10,10,-8,-9,-10,10,-6,-7,]),'MINUS':([4,5,6,7,12,13,14,15,],[-10,11,-8,-9,-10,11,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,],[3,8,]),'expression':([0,2,9,],[5,5,13,]),'term':([0,2,9,10,11,],[6,6,6,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','pparser.py',17),
  ('statements -> statement','statements',1,'p_statements','pparser.py',21),
  ('statements -> statements statement','statements',2,'p_statements','pparser.py',22),
  ('statement -> IDENTIFIER ASSIGN expression','statement',3,'p_statement_assign','pparser.py',29),
  ('statement -> expression','statement',1,'p_statement_expr','pparser.py',33),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','pparser.py',37),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','pparser.py',41),
  ('expression -> term','expression',1,'p_expression_term','pparser.py',45),
  ('term -> NUMBER','term',1,'p_term_number','pparser.py',49),
  ('term -> IDENTIFIER','term',1,'p_term_identifier','pparser.py',53),
]
