from flask import Flask, jsonify, request

app = Flask(__name__)




@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    return jsonify({'tasks': tasks})

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = {}
    return jsonify({'task': task})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()
    new_task = {}
    return jsonify({'task': new_task})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_data = request.get_json()
    updated_task = {}
    return jsonify({'task': updated_task})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return jsonify({'message': 'Task deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True)
