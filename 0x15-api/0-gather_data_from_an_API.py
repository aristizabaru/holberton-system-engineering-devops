#!/usr/bin/python3
"""0-gather_data_from_an_API

Gather data from employee API"""

import requests
import sys


# Process functions
def make_request(id):
    """make request to end points"""
    user_r = "https://jsonplaceholder.typicode.com/users/" + id
    todo_r = "https://jsonplaceholder.typicode.com/todos/"+"?userId=" + id
    data = [requests.get(user_r).json(), requests.get(todo_r).json()]
    return(data)


def print_data(data):
    """print json data"""
    if len(data[0]) != 0:
        # Print results
        if len(data) > 1:
            completed_task = list(filter(completed, data[1]))
            print("Employee {} is done "
                  "with tasks ({}/{}):".format(data[0]['name'],
                                               len(completed_task),
                                               len(data[1])))
            for task in completed_task:
                print('\t {}'.format(task['title']))
        else:
            print("Employee {} is done "
                  "with tasks (0/{0):".format(data[0]['name']))


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
