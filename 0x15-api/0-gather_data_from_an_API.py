#!/usr/bin/python3
"""module to get requests"""

import requests
import sys


def getTodos():
    """retrieve employer to do task status"""

    id = sys.argv[1]
    response = requests.get("https://jsonplaceholder.typicode.com/users/"+id)
    response = response.json()
    name = response.get('name')

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    if response.status_code == 200:
        results = (response).json()
        task_completed = []

        for item in results:
            if item.get('userId') == int(id):
                if item.get('completed'):
                    task_completed.append(item['title'])

        print(f'Employee {name} is done with tasks({len(task_completed)}/\
            {len(results)}):')

        for item in task_completed:
            print(item)

    else:
        print(f'incorect response')


if __name__ == "__main__":
    getTodos()
