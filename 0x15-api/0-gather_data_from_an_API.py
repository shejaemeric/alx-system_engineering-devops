import requests
import sys
import json

id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/todos/"

response = requests.get('https://jsonplaceholder.typicode.com/todos')
if response.status_code == 200:
    results = (response).json()
    task_completed = []

    for item in results:
        if item['userId'] == int(id):
            if item['completed']:
                task_completed.append(item['title'])

    print("Employee EMPLOYEE_NAME is done with tasks("
        +str(len(task_completed))+"/"
        +str(len(results))+"):")

    for item in task_completed:
        print(item)

else:
    print(f'incorect response')
