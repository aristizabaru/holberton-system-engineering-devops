#!/usr/bin/python3
"""0-gather_data_from_an_API

Gather data from employee API"""

import requests
import sys


# Process functions
def make_request(id):
    """make request to end points"""
    user_r = "https://jsonplaceholder.typicode.com/users/" + id
    todo_r = "https://jsonplaceholder.typicode.com/todos/?userId=" + id
    data = [requests.get(user_r).json(), requests.get(todo_r).json()]
    return(data)


def print_data(data):
    """print json data"""
    user_name = data[0]["name"]
    completed_task = task = 0

    for item in data[1]:
        task += 1
        if item['completed']:
            completed_task += 1

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          completed_task,
                                                          task))

    for item in data[1]:
        if item['completed'] is True:
            print('\t {}'.format(item['title']))


def main():
    """handles http request to API and send to print response"""
    if len(sys.argv) == 2:
        data = make_request(sys.argv[1])
        print_data(data)


if __name__ == "__main__":
    main()
