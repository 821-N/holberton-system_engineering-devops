#!/usr/bin/env python3
"""
    0. Gather data from an API
"""
import requests
from sys import argv
from json import loads


def get(path):
    response = requests.get("https://jsonplaceholder.typicode.com/"+path)
    return loads(response.text)

user = get("users/"+argv[1])
todos = get("users/"+argv[1]+"/todos")
done = sum(item['completed'] for item in todos)

p = print
p("Employee %s is done with tasks(%d/%d)" % (user['name'], done, len(todos)))
for item in todos:
    if item['completed']:
        print("\t"+item['title'])
