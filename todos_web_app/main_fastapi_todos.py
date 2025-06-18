from fastapi import FastAPI
from TodoDAOPydantic import TodoDAOPydantic
from TodoPydantic import TodoPydantic
from typing import List

app = FastAPI()


@app.get('/todos',response_model=List[TodoPydantic])
def get_todo():
    dao = TodoDAOPydantic('todos_db.db')
    todos = dao.findAll()
    return todos
