from flask import Flask, request
import json


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        "id": 2,
        "name": "task2",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "task3",
        "description": "This is task 3"
    }
]

tasksJSON = json.dumps(tasks)


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return tasksJSON

@app.route('/api/task', methods=['POST'])
def create_task():
    request_data = request.get_json()
    tasksData = json.loads(tasksJSON)
    tasksData.append(request_data['task'])
    return json.dumps(tasksData);

if __name__ == '__main__':
    app.run()