import sqlite3
from Todo import Todo

class TodoDAO:

    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)

    def findAll(self):
        cur = self.__con.cursor()
        rs = cur.execute('SELECT id,user_id,title,completed FROM todos')

        # todos = []
        # for row in rs.fetchall():
        #     todo = Todo(*row)
        #     todos.append(todo)
        # return todos
        # return [Todo(*row) for row in rs.fetchall()]
        
        for row in rs.fetchall():
            todo = Todo(*row)
            yield todo

    def __del__(self):
        self.__con.close()
        

