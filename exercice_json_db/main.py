from TodoDAO import TodoDAO


def main():
    dao = TodoDAO("todos_db.db")
    all_todos = list(dao.findAll())


    print(all_todos)
    # t = next(all_todos)
    # print(t)
    # t = next(all_todos)
    # print(t)
    # for todo in dao.findAll():
    #     print(todo) # 

if __name__=='__main__':
    main()
