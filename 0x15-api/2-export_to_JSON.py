#!/usr/bin/python3

"""This module gets employer todo list from

https://jsonplaceholder.typicode.com/todos/

"""

import csv

import json

import requests

import sys

def get_user_todo_list():

    employee_id = sys.argv[1]

    url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id

    url2 = '%s/todos' % url1

    todo_list = requests.get(url2).json()

    user = requests.get(url1).json()

    path = "{}.json".format(employee_id)

    complete = []

    for todo in todo_list:

        task = {}

        task['task'] = todo.get('title')

        task['completed'] = todo.get('completed')

        task['username'] = user.get('username')

        complete.append(task)

    json_task = {}

    json_task[employee_id] = complete

    with open(path, 'w') as f:

        json.dump(json_task, f)

if __name__ == '__main__':

    get_user_todo_list()
