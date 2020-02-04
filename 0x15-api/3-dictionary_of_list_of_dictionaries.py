#!/usr/bin/python3
"""
    1. Export to CSV
"""
import requests
import json


if __name__ == "__main__":
    def get(path):
        response = requests.get("https://jsonplaceholder.typicode.com/"+path)
        return response.json()

    users = get("users")
    with open("todo_all_employees.json", 'w') as file:
        obj = {}
        for user in users:
            id = user['id']
            todos = get("todos?userId="+str(id))
            obj[str(id)] = [{
                'task': item['title'],
                'completed': item['completed'],
                'username': user['username'],
            } for item in todos]
        file.write(json.dumps(obj))
