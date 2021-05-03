#!/usr/bin/python3
"""1-export_to_CSV

Gather data from employee API"""

import csv
import requests
import sys


def make_request(id):
    """make request to end points"""
    # Config
    user_r = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo_r = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(id)
    # Requests
    response_user = requests.get(user_r)
    response_todo = requests.get(todo_r)
    data = [response_user.json(), response_todo.json()]
    return(data)


def export_csv(data):
    """Export data to csv file"""
    # prepare info
    username = data[0]['username']
    csv_data = list()
    for dict_ in data[1]:
        dict_.update({'username': username})
        dict_.pop('id')
        csv_data.append(dict_)
    for item in csv_data:
        for key, value in item.items():
            item[key] = "'{}'".format(value)
    print(csv_data)
    with open(str(data[0]['id']) + '.csv', 'w', newline='') as fd:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(fd, fieldnames=fieldnames)
        # writer.writeheader()
        for item in csv_data:
            writer.writerow(item)


def main():
    """handles http request to API and export response"""
    if len(sys.argv) == 2:
        data = make_request(sys.argv[1])
        export_csv(data)


if __name__ == "__main__":
    main()
