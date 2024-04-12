import ast
import sys
import json

def ast_to_json(ast_node):
  if isinstance(ast_node, ast.Module):
    return {
      'name': 'Program',
      'children': [ast_to_json(child) for child in ast_node.body] 
    }

  elif isinstance(ast_node, ast.Assign):
    return {
      'name': '=',
      'children': [ast_to_json(ast_node.targets[0]), ast_to_json(ast_node.value)] 
    }

  elif isinstance(ast_node, ast.If):
    return {
      'name': 'If',
      'children': [ast_to_json(ast_node.test), 
                   {'name': 'If Body', 'children': [ast_to_json(child) for child in ast_node.body]},
                   {'name': 'Else Body', 'children': [ast_to_json(child) for child in ast_node.orelse]}]
    }

  elif isinstance(ast_node, ast.Expr):
    return ast_to_json(ast_node.value)  # Assume only Call nodes are within Expr

  elif isinstance(ast_node, ast.Call):
    return {
      'name': ast_node.func.id,  
      'children': [ast_to_json(arg) for arg in ast_node.args] 
    }

  elif isinstance(ast_node, ast.Name):
    return {'name': str(ast_node.id)}  # Keep this for ast.Name

  elif isinstance(ast_node, ast.Constant):
    return {'name': str(ast_node.value)}  # Modified line

  elif isinstance(ast_node, ast.Compare):
    operator_symbols = {
        ast.Eq: "==",
        ast.NotEq: "!=",
        ast.Lt: "<",
        ast.LtE: "<=",
        ast.Gt: ">",
        ast.GtE: ">=",
    }
    return {
        'name': [operator_symbols.get(op.__class__, str(op.__class__.__name__)) for op in ast_node.ops], 
        'children': [
            ast_to_json(ast_node.left)
        ] + [ast_to_json(comp) for comp in ast_node.comparators]
    }

  elif isinstance(ast_node, ast.For):
    return {
        'name': 'For',
        'children': [
            {'name': ast_node.target.id},
            {'name': 'Iterable', 'children': [ast_to_json(ast_node.iter)]},
            {'name': 'Loop Body', 'children': [ast_to_json(child) for child in ast_node.body]}
        ]
    }

  elif isinstance(ast_node, ast.While):
    return {
        'name': 'While',
        'children': [
            {'name': 'Condition', 'children': [ast_to_json(ast_node.test)]},
            {'name': 'Loop Body', 'children': [ast_to_json(child) for child in ast_node.body]}
        ]
    }
  
  elif isinstance(ast_node, ast.List):
    return {
        'name': 'List',
        'children': [ast_to_json(elt) for elt in ast_node.elts] 
    }
  
  elif isinstance(ast_node, ast.BinOp):
    operator_symbol = {
        ast.Add: "+",
        ast.Sub: "-",
        ast.Mult: "*",
        ast.Div: "/",
        ast.FloorDiv: "//",
        ast.Mod: "%",
        ast.Pow: "**"
    }.get(ast_node.op.__class__, str(ast_node.op.__class__.__name__))

    return {
        'name': operator_symbol,
        'children': [
            ast_to_json(ast_node.left),
            ast_to_json(ast_node.right)
        ]
    }

  elif isinstance(ast_node, ast.AugAssign):
    op_symbol = {
        ast.Add: "+=",
        ast.Sub: "-=",
        ast.Mult: "*=",
        ast.Div: "/=",
        ast.FloorDiv: "//=",
        ast.Mod: "%=",
        ast.Pow: "**=",
    }.get(ast_node.op.__class__, str(ast_node.op.__class__.__name__))

    return {
        'name': op_symbol,
        'children': [
            ast_to_json(ast_node.target),
            ast_to_json(ast_node.value) 
        ]
    }
  
  elif isinstance(ast_node, ast.Try):
    return {
        "name": "Try",
        "children": [
            {"name": "Try Body", "children": [ast_to_json(child) for child in ast_node.body]},
            {
                "name": "Except",
                "children": [
                    { 
                        "name": "Exception Type", 
                        "children": [ast_to_json(ex.type) for ex in ast_node.handlers] 
                    },
                    {
                        "name": "Except Body", 
                        "children": [ast_to_json(child) for ex in ast_node.handlers for child in ex.body] 
                    }
                ] 
            },
            {
                "name": "Else",
                "children": [ast_to_json(child) for child in ast_node.orelse]
            },
            {
                "name": "Finally",
                "children": [ast_to_json(child) for child in ast_node.finalbody] 
            }
        ]
    }
  # ... other parts ...

  elif isinstance(ast_node, ast.FunctionDef):
    return {
        "name": "Function", 
        "children": [
            {"name": "Name", "children": [{"name": ast_node.name}]}, # Access 'id' directly
            {"name": "Arguments", "children": [{"name": arg.arg} for arg in ast_node.args.args]},  # Access 'arg' attribute
            {"name": "Body", "children": [ast_to_json(child) for child in ast_node.body]}
        ]
    }

  elif isinstance(ast_node, ast.Return): 
    return {
        "name": "Return", 
        "children": [ast_to_json(ast_node.value)] 
    } 

  else:
    return {'name': type(ast_node).__name__} # Fallback for unknown types 

try:
  filename = sys.argv[1]
  with open(f'./TestFiles/{filename}.py', 'r') as f:
    data = f.read()
except:
  print('No file input given')
  exit(0)

ast_tree = ast.parse(data)
ast_json = ast_to_json(ast_tree)

with open('./ast.json', 'w') as f:
  json.dump(ast_json, f, indent=2)