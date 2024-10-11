import json


def get_tasks()->list:
    with open("ToDoList.json", "r") as file:
        data=json.load(file)
        return data

def find_task(id:int):
    tasks=get_tasks()
    for index, task in enumerate(tasks):
        if task["id"]==(id):

            return index, tasks
    

def inserts_tasks(task:dict):
    tasks=get_tasks()
    tasks.append(task)
    with open("ToDoList.json", "w") as file:
        json.dump(tasks, file)
    return


def exclude_tasks(id:int):
    index, tasks=find_task(id)
    tasks.pop(index)
    with open("ToDoList.json","w") as file:
        json.dump(tasks, file)
    return file
