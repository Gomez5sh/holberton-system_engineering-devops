#!/usr/bin/python3
"""Python script that, using a REST API
"""
import json
import requests
import sys

if __name__ == "__main__":

    user_id = requests.get("https://jsonplaceholder.typicode.com/users?id="
                           + sys.argv[1])
    todo_id = requests.get("https://jsonplaceholder.typicode.com/todos?userId="
                           + sys.argv[1])

    json_user = user_id.json()
    json_todo = todo_id.json()
    complete_task = 0
    total_task = 0
    titles = []

    for pointer in json_todo:
        if pointer['completed'] is True:
            complete_task += 1
            titles.append(pointer['title'])
        total_task += 1

    name_id = json_user[0]['name']

    print("Employee {} s done with tasks({}/{}):"
          .format(name_id, complete_task, total_task))

    for task in titles:
        print('\t' + task)
