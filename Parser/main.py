from lexer import lexer
from pparser import parser
import json

with open('./test.py', 'r') as f:
    data = f.read()

lexer.input(data)

for tok in lexer:
    print(tok)
    if tok.type == 'INDENT':
        print("Indent level:", len(lexer.indents), "- Column:", tok.lexer.column)

# result = parser.parse(data, lexer=lexer) 

# def print_ast(node, indent=0):
#     print(' ' * indent + node.type)
#     for child in node.children:
#         print_ast(child, indent + 2)

# print_ast(result)
# ast_json = json.dumps(result.to_json(), indent=2)

# with open('./ast.json', 'w') as jsonf:
#     jsonf.write(ast_json)

# print(ast_json)