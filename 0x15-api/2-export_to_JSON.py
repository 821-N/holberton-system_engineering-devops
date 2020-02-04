#!/usr/bin/python3
"""
    1. Export to CSV
"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    def get(path):
        response = requests.get("https://jsonplaceholder.typicode.com/"+path)
        return json.loads(response.text)

    id = argv[1]
    with open(id+".json", 'w') as file:
        user = get("users/"+id)
        todos = get("todos?userId="+id)
        obj = {}
        obj[id] = [{
            'task': item['title'],
            'completed': item['completed'],
            'username': user['username'],
        } for item in todos]
        file.write(json.dumps(obj))
