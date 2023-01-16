#!/usr/bin/python3
import requests
import sys

def getTodos():
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/"

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    print(response.status_code)
    if response.status_code == 200:
        results = (response).json()
        task_completed = []

        for item in results:
            if item.get('userId') == int(id):
                if item.get('completed'):
                    task_completed.append(item['title'])

        print("Employee EMPLOYEE_NAME is done with tasks("
            +str(len(task_completed))+"/"
            +str(len(results))+"):")

        for item in task_completed:
            print(item)

    else:
        print(f'incorect response')

if __name__ == "__main__":
    getTodos()
