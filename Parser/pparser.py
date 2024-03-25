import ply.yacc as yacc
from lexer import tokens

# AST Node class
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

# Grammar Rules with AST Generation

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

def p_expression_plus(p): 
    '''expression : expression PLUS term'''
    p[0] = Node('Operator', [p[1], p[3]], '+')

def p_expression_minus(p): 
    '''expression : expression MINUS term'''
    p[0] = Node('Operator', [p[1], p[3]], '-')

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_number(p): 
    '''term : NUMBER''' 
    p[0] = Node('Number', [], p[1]) 

def p_term_identifier(p):  
    '''term : IDENTIFIER'''
    p[0] = Node('Identifier', [], p[1])

# ... Add more grammar rules for multiplication, division, parentheses, etc.

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc() 
