from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()

#in memory database
todos=[]

#model for todo item
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool=False

#create a new task
@app.post("/todos/",response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

#get all tasks
@app.get("/todos/",response_model=List[Todo])
def get_todos():
    return todos

#get task by id
@app.get("/todos/{todo_id}",response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    raise HTTPException(status_code=404,detail="To-Do not found")

#update task by id
@app.put("/todos/{todo_id}",response_model=Todo)
def update_todo(todo_id: int,updated_todo: Todo):
    for i,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[i]=updated_todo
            return updated_todo
    raise HTTPException(status_code=404,detail="To-Do not found")

#delete task by id
@app.delete("/todos/{todo_id}",response_model=dict)
def delete_todo(todo_id: int):
    for i,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(i)
            return {"message":"To-Do deleted successfully"}
    raise HTTPException(status_code=404,detail="To-Do not found")

@app.get("/")
def read_root():
    return {"message":"welcome to FastAPI!"}