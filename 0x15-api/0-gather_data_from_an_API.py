#!/usr/bin/python3
"""
    0. Gather data from an API
"""
import requests
from sys import argv
from json import loads


if __name__ == "__main__":
    def get(path):
        response = requests.get("https://jsonplaceholder.typicode.com/"+path)
        return loads(response.text)

    user = get("users/"+argv[1])
    todos = get("todos?userId="+argv[1])
    done = sum(item['completed'] for item in todos)

    print(
        "Employee %s is done with tasks(%d/%d)" %
        (user['name'], done, len(todos))
    )
    for item in todos:
        if item['completed']:
            print("\t "+item['title'])
