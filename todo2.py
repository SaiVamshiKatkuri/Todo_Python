from flask import Flask
from flask_cors import CORS
import sqlite3
import json


app = Flask(__name__)
CORS(app)



@app.route('/')
def hello():
    return "Hello From Server!"

@app.route('/addtodo/<todo>')
def addtodo(todo):
    conn = sqlite3.connect('mytodos1.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos1 VALUES ('"+todo+"')")
    conn.commit()
    conn.close()
    return "SUCCESS"

@app.route('/gettodos/')
def gettodos():
    conn = sqlite3.connect('mytodos1.db')
    c = conn.cursor()
    c.execute("SELECT rowid, todo FROM todos1")
    todos = c.fetchall()
    todo_array = []
    for t in todos:
        todo_array.append(t)
    return json.dumps(todo_array)
@app.route('/newtodos/')
def newtodos():
     conn = sqlite3.connect('mytodos1.db')
     c = conn.cursor()
     c.execute("DELETE FROM todos1 WHERE rowid>0")
     conn.commit()
     conn.close()

@app.route('/deletetodos/<id>')
def deletetodos(id):
     i=id
     conn = sqlite3.connect('mytodos1.db')
     c = conn.cursor()
     c.execute("DELETE FROM todos1 WHERE rowid="+i)
     conn.commit()
     conn.close()
     return "ok"



app.run(port="3000")