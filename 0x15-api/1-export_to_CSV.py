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

    name = json_user[0]['name']

    with open(str(argv[1])+'.csv', 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for pointer in json_todo:
            write.writerow([str(argv[1]), str(name),
                            pointer['completed'], pointer['title']])
