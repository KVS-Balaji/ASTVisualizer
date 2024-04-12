from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/process-code', methods=['POST'])
def process_code():
    code = request.get_data().decode('utf-8')  

    with open('test.py', 'w') as f:
        f.write(code)

    subprocess.run(['python', 'main.py'])  

    with open('ast.json', 'r') as f:
        ast_json_data = f.read()

    return jsonify(ast_json_data) 

if __name__ == '__main__':
    app.run(debug=True) 
