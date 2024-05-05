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

    with open('/home/kvsb/Documents/VSCode/Project Ideas/ASTVisualizer/Back-End/test.py', 'w') as f:
        f.write(decoded_code)
    subprocess.run(['python3', 'main.py'])
    with open('/home/kvsb/Documents/VSCode/Project Ideas/ASTVisualizer/Back-End/ast.json', 'r') as f:
        ast_json_data = f.read()
    # with open('/home/kvsb/Documents/VSCode/Project Ideas/ASTVisualizer/Front-End/src/App.jsx', 'r') as f:
    #     print("hello")
    return jsonify(ast_json_data)

@app.route('/astjson')
def send_json():
    with open ('/home/kvsb/Documents/VSCode/Project Ideas/ASTVisualizer/Back-End/ast.json', 'r') as f:
        return jsonify(f.read())


if __name__ == '__main__':
    app.run(debug=True) 
