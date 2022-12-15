import requests
import json

"""
{
  1 : 11
  2 : 8
  3 : 15

  10: 
}

"""

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def caunt_task_frequency(tasks):
    completedTaskByUser = {}
    for element in tasks:
        if element["completed"] == True:
            try:
                completedTaskByUser[element["userId"]]  += 1
            except KeyError:
                completedTaskByUser[element["userId"]]  = 1

    return completedTaskByUser

def get_users_with_top_completed_tasks(completedTaskByUser):
    userIdWithMaxCompletedTasks = []
    maxAmountOfTasks = max(completedTaskByUser.values())
    for userId, numberOfCompletedTasks in completedTaskByUser.items():
        if numberOfCompletedTasks == maxAmountOfTasks:
            userIdWithMaxCompletedTasks.append(userId)

    return userIdWithMaxCompletedTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskByUser = caunt_task_frequency(tasks)
    print(get_users_with_top_completed_tasks(completedTaskByUser))