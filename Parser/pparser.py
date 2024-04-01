import ply.yacc as yacc
from lexer import tokens

class Node:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.value = value
        if children:
            self.children = children
        else:
            self.children = []

    def to_json(self):
        return {
            'type': self.type,
            'value': self.value,
            'children': [child.to_json() for child in self.children] 
        }

def p_program(p):
    '''program : statements'''
    p[0] = Node('Program', p[1])  

def p_statements(p):
    '''statements : statement
                  | statements statement '''
    if len(p) == 2:  # Single statement
        p[0] = [p[1]]
    else:  # Multiple statements
        p[0] = p[1] + [p[2]] 

def p_statement_assign(p):
    '''statement : IDENTIFIER ASSIGN expression'''
    p[0] = Node('Assignment', [Node('Identifier', [], p[1]), p[3]], '=')

def p_statement_expr(p):
    '''statement : expression''' 
    p[0] = Node('ExpressionStatement', [p[1]])  

def p_term_number(p): 
    '''term : NUMBER''' 
    p[0] = Node('Number', [], p[1]) 

def p_term_identifier(p):  
    '''term : IDENTIFIER'''
    p[0] = Node('Identifier', [], p[1])

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    # ... (same as before)

def p_statement_loop(p):
    '''statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN block
                 | WHILE LPAREN expression RPAREN block'''
    # Define the AST structure for loops
    if p[1] == 'FOR':
        loop_type = 'ForLoop'
        init_expr = p[3]
        cond_expr = p[5]
        incr_expr = p[7]
    else:
        loop_type = 'WhileLoop'
        cond_expr = p[3]
    body = p[9]
    p[0] = Node(loop_type, [cond_expr, body])

def p_statement_if(p):
  '''statement : IF LPAREN expression RPAREN block ELSE block
                 | IF LPAREN expression RPAREN block'''  # This line is commented out
  # Define the AST structure for if-else statements
  if len(p) == 7:  # if-else block
    cond_expr = p[3]
    then_body = p[5]
    else_body = p[7]
    p[0] = Node('IfElse', [cond_expr, then_body, else_body])
  else:  # if block (commented out)
    cond_expr = p[3]
    then_body = p[5]
    p[0] = Node('If', [cond_expr, then_body])


def p_block(p):
    '''block : INDENT statements DEDENT'''
    # Represents a code block within a loop or conditional statement
    p[0] = p[2]

# Add grammar rules for expressions involving comparison operators
def p_expression_comparison(p):
    '''expression : expression EQ expression
                 | expression NE expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE expression'''
    p[0] = Node('Comparison', [p[1], p[3]], p[2])

def p_expression(p):
  '''expression : expression TIMES term
                | expression DIVIDE term
                | expression PLUS term
                | expression MINUS term
                | term'''

  # Operator precedence enforced through rule ordering
  if len(p) == 4:  # Multiplication or division
    if p[2] == '*':
      p[0] = Node('Operator', [p[1], p[3]], '*')
    else:
      p[0] = Node('Operator', [p[1], p[3]], '/')
  else:  # Addition or subtraction (lower precedence) or term
    if len(p) == 3:
      if p[2] == '+':
        p[0] = Node('Operator', [p[1], p[3]], '+')
      else:
        p[0] = Node('Operator', [p[1], p[3]], '-')
    else:
      p[0] = p[1]  # Term

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type, "Value:", p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc() 
