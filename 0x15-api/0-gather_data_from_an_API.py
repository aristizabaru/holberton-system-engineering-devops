#!/usr/bin/python3
"""0-gather_data_from_an_API

Gather data from employee API"""

import requests
import sys


# Process functions
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


def print_data(data):
    """print json data"""
    if len(data[0]) != 0:
        # Print results
        completed_task = list(filter(completed, data[1]))
        print("Employee {} is done "
              "with tasks ({}/{}):".format(data[0]['name'],
                                           len(completed_task),
                                           len(data[1])))
        if len(completed_task) != 0.
        for task in completed_task:
            print('\t {}'.format(task['title']))


def completed(element):
    """Filter completed todos"""
    return element['completed']


def main():
    """handles http request to API and send to print response"""
    if len(sys.argv) == 2:
        data = make_request(sys.argv[1])
        print_data(data)


if __name__ == "__main__":
    main()
