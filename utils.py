import json


def get_data()->list:
    with open("ToDoList.json", "r") as file:
        data=json.load(file)
        return data
    
def get_tasks(user_id:str):
    tasks=get_data()
    new_tasks=[]
    for task in tasks:
        if task["user_id"] == user_id:
            new_tasks.append(task)
    return new_tasks
    

def find_task(id:int):
    tasks=get_data()
    for index, task in enumerate(tasks):
        if task["id"]==(id):

            return index, tasks
    

def inserts_tasks(task:dict):  
    tasks=get_data()
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
    
def sort_list(q:str,order,value):
    data=get_data()

    if order:
        print(type(order))
        if "reverse" in order:
            print("entrou no reverse")
            data.sort(key=lambda x: x[q].lower())
            data.reverse()
            return data
    if value:

        data.sort(key=lambda x: abs(x[q]-value))
        return data
    
    try :
        data.sort(key=lambda x: x[q].lower())       
    except: data.sort(key=lambda x: x[q])
    return data

def filter_task():
    tasks=get_data()
    for task in tasks:
        print(task)
        
print(get_tasks("Hienes"))