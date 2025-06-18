from flask import Flask,render_template
from TodoDAO import TodoDAO

app = Flask(__name__)

# flask run

@app.route("/hello")
def hello_world():
    return "<p>Bonjour, World!</p>"

@app.route("/moche")
def index_moche():
    dao = TodoDAO('todos_db.db')    
    
    html = "<table>"
    for todo in dao.findAll():
        html+=f"""<tr>
            <td>{todo.id}</td>  
            <td>{todo.title}</td>  
            <td>{todo.completed}</td>  
        </tr>
"""

    html+= "</table>"
    return html


@app.route("/")
def index():
    dao = TodoDAO('todos_db.db')    
    
    return render_template("todos.html",todos=dao.findAll())