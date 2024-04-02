import ply.lex as lex

reserved = {
    'if' : 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT', 
    'True': 'TRUE',
    'False': 'FALSE',
    'None': 'NONE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

tokens = [
    'NUMBER', 
    'FLOAT',  
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'IDENTIFIER', 'ASSIGN',
    'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', 'EXCLAMATION',
    'STRING',
    'COMMA', 'COLON', 'SEMICOLON', 
    'INDENT', 'DEDENT', 
] + list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_AND             = r'and'
t_OR              = r'or'
t_NOT             = r'not'
t_COMMA           = r'\,'
t_COLON       = r':'
t_SEMICOLON = r';'
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EXCLAMATION = r'\!'

def t_FLOAT(t):
    r'\d+\.\d+' 
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"([^"]*)"'
    t.value = t.value[1:-1] 
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
  r'\n+' 
  t.lexer.lineno += len(t.value)
  t.lexer.column = 0 


def t_ASSIGN(t):
    r'='
    return t

def t_INDENT(t):
  r'[ \t]+'
  t.lexer.column += len(t.value)
  print("INDENT DETECTED")
  t.lexer.last_indent = t.lexer.column  # Update last indent position
  return None 

def t_COMMENT(t):
    r'\#.*'  
    t.lexer.lineno += 1  
    pass  

def initialize_lexer_state(lexer):
    lexer.column = 0            
    lexer.last_indent = 0        
    lexer.indents = []  

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
initialize_lexer_state(lexer)