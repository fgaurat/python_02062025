from pydantic import BaseModel


class TodoPydantic(BaseModel):
    id:int=0
    user_id:int=0
    title:str=""
    completed:bool=False