import requests

def create_task():
    url = "http://127.0.0.1:8000/api/create-task"
    data = {
        "user_id": "1",
        "dev_ref": "1",
        "task": "another create tasks",
        "due_date": "2022-11-11"
    }

    task = requests.post(url=url, json=data)
    print(task)