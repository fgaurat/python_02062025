from dataclasses import dataclass

@dataclass
class Todo:
    id:int=0
    user_id:int=0
    title:str=""
    completed:bool=False