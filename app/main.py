# Add a new todo item
# View all todos
# Get todo by ID
# Delete a todo
# Update a todo

from fastapi import FastAPI, HTTPException
from app.todo import todo_List, Todo

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to the TODO app"
    }

# add a todo
@app.post("/todos/")
def create_todo(todo: Todo):
    todo_List.append(todo)
    return {
        "message" : "Todo added", "todo": todo
    }

# get all todos 
@app.get("/todos/")
def get_all_todos():
    return todo_List

# get a todo by id 
@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    for todo in todo_List:
        if todo.id == todo_id:
            return todo
    raise HTTPException (
        status_code=404, 
        detail= "Todo not found"
    )    

# delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todo_List):
        if todo.id == todo_id:
            del todo_List[i]
            return {"message": "Todo deleted"}
    raise HTTPException (
        status_code=404, 
        detail="Todo not found"
        ) 

# update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todo_List):
        if todo.id == todo_id:
            todo_List[i] = updated_todo
            return { 
                "message": "Todo updated", 
                "todo": updated_todo
                }  
    raise HTTPException (
        status_code=404, 
        detail="Todo not found"
        )       
