from fastapi import FastAPI, Query
from pydantic import BaseModel
import json
from utils import *


app= FastAPI()

class Task(BaseModel):
    id: int | None = None
    name: str
    description: str
    status: int
    priority: int
    created_at: str
    completed_date: str | None = None
    user_id:str

@app.get("/login")
async def login_route():
    pass

@app.get("/home/")
async def get_task():
   return get_tasks()

@app.post("/home/")
async def create_list(task:Task):
    inserts_tasks(task.model_dump())
    return task 

@app.delete("/home/{id}")
async def delete_list(id:int):
    tasks=exclude_tasks(id)
    return tasks