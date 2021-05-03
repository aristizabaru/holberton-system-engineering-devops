#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries

Gather data from employee API"""

import json
import requests
import sys


def make_request():
    """make request to end points"""
    # Config
    user_r = "https://jsonplaceholder.typicode.com/users/"
    todo_r = "https://jsonplaceholder.typicode.com/todos/"
    # Requests
    response_user = requests.get(user_r)
    response_todo = requests.get(todo_r)
    data = [response_user.json(), response_todo.json()]
    return(data)


def export_json(data):
    """Export data to json file"""
    # prepare info
    json_data = dict()
    for user in data[0]:
        json_data.update({str(user['id']): list()})

    for key, value in json_data.items():
        for dict_ in data[1]:
            if dict_['userId'] == int(key):
                value.append({"username": data[0][int(key) - 1]["username"],
                              "task": dict_["title"],
                              "completed": dict_["completed"]})
            elif dict_['userId'] > int(key):
                break

    with open('todo_all_employees.json', 'w', encoding="utf8") as fd:
        json.dump(json_data, fd)


def main():
    """handles http request to API and export response"""
    data = make_request()
    export_json(data)


if __name__ == "__main__":
    main()
