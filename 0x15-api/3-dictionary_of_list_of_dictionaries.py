#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import json
import requests


todo_endpoint = "https://jsonplaceholder.typicode.com/todos"
user_endpoint = "https://jsonplaceholder.typicode.com/users"


def get_all_todos():
    """Get TODO lists for all users identified by `user_id`"""
    todos = requests.get(todo_endpoint)
    try:
        return todos.json()
    except:
        exit(1)


def get_all_users():
    """Get all users"""
    users = requests.get(user_endpoint)
    try:
        return users.json()
    except:
        exit(1)


def export_json_user_todos():
    """Export employee TODO lists to a json file"""
    todos = get_all_todos()
    users = get_all_users()
    data = {
        u['id']: [dict(task=todo.get('title'),
                       completed=todo.get('completed'),
                       username=u.get('username'))
                  for todo in filter(
                          lambda t: t.get('userId') == u.get('id'), todos
                  )] for u in users
    }
    with open("todo_all_employees.json", 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    export_json_user_todos()
