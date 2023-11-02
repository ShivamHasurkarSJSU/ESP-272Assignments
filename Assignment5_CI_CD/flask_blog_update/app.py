import pymysql
from flask import Flask, request
from werkzeug.exceptions import abort


def get_db_connection():
    connection = pymysql.connect(host="cmpe-272.cy4wjmr5qidh.us-east-2.rds.amazonaws.com",
                             database='blog', user='root', password='root_123')
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'

@app.route('/<int:id>/edit', methods=('PUT',))
def edit(id):
    title = request.form.get('title')
    content = request.form.get('content')

    if not title:
        abort(400)
    else:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM posts WHERE id = {id};')
        post = cursor.fetchone()
        if(cursor.rowcount == 0):
            return 'Post not found', 404
        else:
            cursor.execute(f"UPDATE posts SET title = '{title}', content = '{content}' WHERE id = {id};")
            conn.commit()
            conn.close()
            return 'Post updated successfully', 200
