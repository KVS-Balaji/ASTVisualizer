from flask import Flask, request, jsonify
import subprocess
import base64
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/frontend', methods=['POST'])
def frontend():
    code = request.get_data().decode('utf-8')  
    decoded_code = base64.b64decode(code).decode('utf-8')
    
    cwd = os.getcwd()
    if (cwd.__contains__("ASTVisualizer") == False):
        cwd += "/ASTVisualizer"
    if (cwd.__contains__("Front-End")):
        cwd = cwd.removesuffix("/Front-End")
        cwd += "/Back-End"
    elif (cwd.__contains__("ASTVisualizer") and (cwd.__contains__("Back-End") == False)):
        cwd += "/Back-End"
    os.chdir(cwd)

    print(cwd)
    with open(f'{cwd}/test.py', 'w') as f:
        f.write(decoded_code)
    subprocess.run(['python3', 'main.py'])
    with open(f'{cwd}/ast.json', 'r') as f:
        ast_json_data = f.read()
    
    appjsx = open(f'{cwd.removesuffix("/Back-End")}/Front-End/src/App.jsx', 'w')
    s1 = open(f'{cwd}/s1.txt', 'r')
    s2 = open(f'{cwd}/s2.txt', 'r')
    appcode = s1.read() + ast_json_data + s2.read()
    appjsx.write(appcode)

    return "Done"


if __name__ == '__main__':
    app.run(debug=True) 
