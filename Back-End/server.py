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
    if (cwd.__contains__("Front-End")):
        cwd = cwd.removesuffix("/Front-End")
        cwd += "/Back-End"
    elif cwd.__contains__("Back-End"):
        cwd = cwd.removesuffix("/Back-End")
    else:
        cwd += "/Back-End"
    os.chdir(cwd)

    with open('test.py', 'w') as f:
        f.write(decoded_code)
    subprocess.run(['python3', 'main.py'])
    with open('ast.json', 'r') as f:
        ast_json_data = f.read()
    return jsonify(ast_json_data)

if __name__ == '__main__':
    app.run(debug=True) 
