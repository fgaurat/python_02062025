import requests
import sqlite3



def main():
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = r.json()

    # print(data[0]['title'])

    with sqlite3.connect("todos_db.db") as con:
        sql = "INSERT INTO todos(user_id,title,completed) VALUES(?,?,?)"
        cur = con.cursor()

        for todo in data:
            del todo['id']
            the_todo = list(todo.values())
            cur.execute(sql,the_todo)
            # print(todo.values())
        


if __name__=='__main__':
    main()
