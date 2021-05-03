#!/usr/bin/python3
"""2-export_to_JSON

Gather data from employee API"""

import json
import requests
import sys


def make_request(id):
    """make request to end points"""
    # Config
    user_r = "https://jsonplaceholder.typicode.com/users/" + id
    todo_r = "https://jsonplaceholder.typicode.com/todos/?userId=" + id
    # Requests
    response_user = requests.get(user_r)
    response_todo = requests.get(todo_r)
    data = [response_user.json(), response_todo.json()]
    return(data)


def export_json(data):
    """Export data to json file"""
    # prepare info
    json_data = {str(data[0]['id']): list()}

    for dict_ in data[1]:
        json_data[str(data[0]['id'])].append(
            {"task": dict_["title"],
             "completed": dict_["completed"],
             "username": data[0]["username"]})

    with open(str(data[0]['id']) + '.json', 'w', encoding="utf8") as fd:
        json.dump(json_data, fd)


def main():
    """handles http request to API and export response"""
    if len(sys.argv) == 2:
        data = make_request(sys.argv[1])
        export_json(data)


if __name__ == "__main__":
    main()
