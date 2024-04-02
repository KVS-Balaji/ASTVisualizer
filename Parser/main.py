from lexer import lexer
from pparser import parser
import json

with open(r'test.py', 'r') as f:
    data = f.read()

lexer.input(data)

for tok in lexer:
    print(tok)
    if tok.type == 'INDENT':
        print("Indent level:", len(lexer.indents), "- Column:", tok.lexer.column)

result = parser.parse(data, lexer=lexer) 

def print_ast(node, indent=0):
    print(' ' * indent + node.type)
    for child in node.children:
        print_ast(child, indent + 2)

print_ast(result)
ast_json = json.dumps(result.to_json(), indent=2)

with open('./ast.json', 'w') as jsonf:
    jsonf.write(ast_json)

print(ast_json)


#TRY THIS CODE (SUGGESTED BY CHATGPT) But i have no idea what it does
# from lexer import lexer
# from pparser import parser
# import json

# with open(r'test.py', 'r') as f:
#     data = f.read()

# lexer.input(data)

# # Initialize indentation tracking
# indent_stack = [0]

# for tok in lexer:
#     if tok.type == 'INDENT':
#         current_indent = len(tok.value)
#         if current_indent > indent_stack[-1]:
#             indent_stack.append(current_indent)
#             lexer.token(type='INDENT')
#         elif current_indent < indent_stack[-1]:
#             while current_indent < indent_stack[-1]:
#                 indent_stack.pop()
#                 lexer.token(type='DEDENT')
#         else:
#             lexer.token(type='NEWLINE')
#     elif tok.type == 'DEDENT':
#         indent_stack.pop()

# # Parse the input
# result = parser.parse(data, lexer=lexer)

# # Print the AST
# def print_ast(node, indent=0):
#     if node:
#         print(' ' * indent + node.type)
#         for child in node.children:
#             print_ast(child, indent + 2)

# print_ast(result)

# # Convert AST to JSON
# ast_json = json.dumps(result.to_json(), indent=2)

# with open('./ast.json', 'w') as jsonf:
#     jsonf.write(ast_json)

# print(ast_json)