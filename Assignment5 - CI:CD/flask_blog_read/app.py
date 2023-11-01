import pymysql
from flask import Flask
from werkzeug.exceptions import abort
import json

def get_db_connection():
    connection = pymysql.connect(host="cmpe-272.cy4wjmr5qidh.us-east-2.rds.amazonaws.com",
                             database='blog', user='root', password='root_123')
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'

@app.route('/', methods=('GET',))
def readByAll():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM posts;')
    posts = cursor.fetchall()
    if(cursor.rowcount == 0):
        conn.close()
        return "Post not found", 404
    else:
        result = []
        for row in posts:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
            result.append(d)
        return json.dumps(result, default=str), 200

@app.route('/<int:id>', methods=('GET',))
def readById(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM posts WHERE id = {id};')
    posts = cursor.fetchall()
    if(cursor.rowcount == 0):
        conn.close()
        return "Post not found", 404
    else:
        result = []
        for row in posts:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
            result.append(d)
        return json.dumps(result, default=str), 200
