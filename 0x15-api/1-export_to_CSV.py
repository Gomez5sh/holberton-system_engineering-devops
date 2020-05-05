#!/usr/bin/python3
"""Python script that, using a REST API
"""
import csv
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
    file_id = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    name = json_user[0]['name']
    file_id = argv[1] + ".csv"

    with open(file_id, 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL, quotechar='"')
        for pointer in json_todo:
            if pointer['userId'] == int(argv[1]):
                pointer['name'] = name
                write.writerow([pointer['userId'], pointer['name'],
                                pointer['completed'], pointer['title']])
