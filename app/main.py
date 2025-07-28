from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from app.database import engine, create_db_and_tables
from app.models.todo_model import Todo

app = FastAPI()

# Create DB tables at app startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return {
        "message": "Welcome to the TODO app"
    }

# add a todo
@app.post("/todos/")
def create_todo(todo: Todo):
    with Session(engine) as session:
     session.add(todo)
     session.commit()
     session.refresh(todo)
    return {
        "message" : "Todo added", "todo": todo
    }

# get all todos 
@app.get("/todos/")
def get_all_todos():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        return todos

# get a todo by id 
@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    with Session(engine) as session:
        todo =  session.get(Todo, todo_id)
        if not todo:
            raise HTTPException (
            status_code=404, 
            detail= "Todo not found"
            )    

# delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    with Session(engine) as session: 
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException (
                status_code=404, 
                detail="Not found"
                )
        session.delete(todo)
        session.commit()
        return {
            "message" : "Todo deleted"
        }

# update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: Todo):
    with Session(engine) as session:
      todo = session.get(Todo, todo_id)
      if not todo:
          raise HTTPException (
          status_code=404, 
         detail="Todo not found"
         )  
      todo.task = updated.task 
      todo.completed = updated.completed
      session.add(todo)
      session.commit()
      session.refresh(todo)
      return { 
          "message": "Todo updated", 
          "todo": todo
          } 
