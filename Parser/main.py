from lexer import lexer
from pparser import parser
import json

with open('./test.py', 'r') as f:
    data = f.read()

result = parser.parse(data, lexer=lexer) 

def print_ast(node, indent=0):
    print(' ' * indent + node.type)
    for child in node.children:
        print_ast(child, indent + 2)

print_ast(result)
ast_json = json.dumps(result.to_json(), indent=2)

print(ast_json)