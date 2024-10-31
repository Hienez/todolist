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
    new_task={"id":(id_create(tasks))}
    new_task.update(task)    
    tasks.append(new_task)
    with open("ToDoList.json", "w") as file:
        json.dump(tasks, file)
    return 1


def exclude_tasks(id:int):
    index, tasks=find_task(id)
    tasks.pop(index)
    with open("ToDoList.json","w") as file:
        json.dump(tasks, file)
    return file

def id_create(data:list)->int:
    id_list=[]
    for tasks in data:
        id_list.append(tasks.get("id"))
    id_list.sort(reverse=True)
    if  id_list:
        return id_list[0]+1
    else: return 1
    
def sort_list(q:str,reverse:int):
    data=get_tasks()
    data.sort(key=lambda x: x[q].lower())
    if reverse:
        data.reverse()
        return data
    return data
        
