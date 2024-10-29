from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import BaseModel, Field
from utils import *
from login import Login


app= FastAPI()

class Task(BaseModel):
    name: str
    description: str = Field(title= "A Decrição da task")
    status: int = Field(ge=0, lt=2)
    priority: int = Field(ge= 0 , le=2)
    created_at: str
    completed_date: str | None = None
    user_id:str
    
class LoginData(BaseModel):
    username:str
    password: str

@app.post("/login/") #mudar rotas(?)
async def login_route(login:LoginData):
    p1=Login(login.username, login.password)
    return p1.login_user()

@app.post("/create_login/")
async def create_login(login:LoginData):
    p1=Login(login.username, login.password)
    return p1.create_user()

@app.get("/home/")
async def get_task():
   return get_tasks()

@app.post("/home/")
async def create_list(task:Task):
    inserts_tasks(task.model_dump())
    return task 

@app.delete("/home/{id}")
async def delete_list(id:Annotated[int, Path(title="Deletar Tarefa", description="Id para deletar tarefa específica")]):
    tasks=exclude_tasks(id)
    return tasks