from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'No mandaste info en el body'}),400
    if 'done' not in body:
        return jsonify({'msg': 'El Campo done es obligatorio'}),400
    if 'label' not in body:
        return jsonify({'msg': 'El Campo label es obligatorio'}),400
    new_todo = {}
    new_todo['done'] = body['done']
    new_todo['label'] = body['label']
    todos.append(new_todo)  
    return jsonify({'msg': 'new todo created'}) ,201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify({'msg': 'todo borrado con exito' }),200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245)