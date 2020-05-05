#!/usr/bin/python3
"""Python script that, using a REST API
"""
import json
from collections import OrderedDict
import requests
from sys import argv

if __name__ == "__main__":

    user_id = requests.get(
        "https://jsonplaceholder.typicode.com/users?id=" + argv[1])
    todo_id = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])

    json_user = user_id.json()
    json_todo = todo_id.json()
    titles = []
    name = json_user[0]['name']
    n_id = OrderedDict()
    file_id = argv[1] + ".json"

    with open(file_id, 'w') as f:
        for pointer in json_todo:
            n = OrderedDict()
            n['task'] = pointer['title']
            n['completed'] = pointer['completed']
            n['username'] = name
            titles.append(n)
        n_id[argv[1]] = titles
        json.dump(n_id, f)
