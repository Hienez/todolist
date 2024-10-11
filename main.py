import json
import get_create

class ToDoList :
    def __init__(self) -> None:
        with open("ToDoList.json", 'r') as file:
            self.todolist= json.load(file)

    def createTask(): 
        pass

    def changeTask():
        pass


todolist_instance= ToDoList()

