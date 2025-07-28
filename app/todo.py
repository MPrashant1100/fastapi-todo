from typing import List
from pydantic import BaseModel

# Temporary in-memory storage List
todo_List = []

# Todo Model or Schema 
class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False   # here default value is false and this is not required 

    