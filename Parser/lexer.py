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
}

tokens = [
    'NUMBER', 
    'FLOAT',  
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'IDENTIFIER', 'ASSIGN',
    'EQUALS', 'NOTEQUAL', 'LESSTHAN', 'GREATERTHAN', 
    'LESSTHANEQUAL', 'GREATERTHANEQUAL',
    'AND', 'OR', 'NOT',
    'STRING',
    'COMMA', 'COLON', 
    'INDENT', 'DEDENT', 
] + list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS          = r'=='
t_NOTEQUAL        = r'!='
t_LESSTHAN        = r'<'
t_GREATERTHAN     = r'>'
t_LESSTHANEQUAL   = r'<='
t_GREATERTHANEQUAL = r'>='
t_AND             = r'and'
t_OR              = r'or'
t_NOT             = r'not'
t_COMMA           = r'\,'
t_COLON       = r':'
t_ignore = r' '

def t_FLOAT(t):
    r'\d+\.\d+' 
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\'([^"\\]|\\[\s\S])*\'' 
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

def t_ASSIGN(t):
    r'='
    return t

def t_INDENT(t):
   r'\t'
   pass

def t_DEDENT(t):
   r'CHANGE_IN_DEDENTATION'
   pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
