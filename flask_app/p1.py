# from flask import Flask,jsonify , request


# app = Flask(__name__)


# @app.route("/test",methods=['GET', 'POST'])
# def test():
#     if request.method== "GET":
#         return jsonify ({"response": "Get request called"})
#     elif request.method == "POSt":
#         req_json = request.json
#         name = req_json['name']
#         return jsonify ({"response": "Hey" + name})


# if __name__ == '__main__':
#     app.run(debug=True,port=9000)


# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route("/test", methods=['GET', 'POST'])
# def test():
#     if request.method == "GET":
#         return jsonify({"response": "Get request called"})
#     elif request.method == "POST":
#         req_json = request.json
#         name = req_json.get('name')  # Use get to avoid KeyError
#         if name:
#             return jsonify({"response": "Hey " + name})
#         else:
#             return jsonify({"error": "Name not provided"}), 400  # Return an error response with status code 400

# if __name__ == '__main__':
#     app.run(debug=True, port=9000)



from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

if __name__ == "__main__":
    app.run(debug=True)
