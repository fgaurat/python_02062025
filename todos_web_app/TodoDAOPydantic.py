import sqlite3
from TodoPydantic import TodoPydantic
from typing import List

class TodoDAOPydantic:

    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)

    def findAll(self)->List[TodoPydantic]:
        data = []
        cur = self.__con.cursor()
        rs = cur.execute('SELECT id,user_id,title,completed FROM todos')
        
        for row in rs.fetchall():
            
            a,b = 0,1


            id,user_id,title,completed = (*row,) # (1,10,"toto",True)
            id,user_id,title,completed = *row, # (1,10,"toto",True)
            id,user_id,title,completed = [*row] # [1,10,"toto",True]
            todo = TodoPydantic(id=id,user_id=user_id,title=title,completed=completed)
            data.append(todo)
        
        return data

    def __del__(self):
        self.__con.close()
        

