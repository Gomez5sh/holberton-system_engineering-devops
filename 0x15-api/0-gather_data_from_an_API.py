#!/usr/bin/python3
"""Python script that, using a REST API
"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    user_id = requests.get(
        "https://jsonplaceholder.typicode.com/users?id=" + argv[1])
    todo_id = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])

    json_user = user_id.json()
    json_todo = todo_id.json()
    complete_task = 0
    total_task = 0
    titles = []

    name = json_user[0]['name']

    for task in json_todo:
        if task['userId'] == int(argv[1]):
            if task['completed'] is True:
                complete_task += 1
                titles.append(task['title'])
            total_task += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete_task, total_task))
    for title in titles:
        print('\t ', end="")
        print(title)
