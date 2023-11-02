import pymysql
from flask import Flask
from werkzeug.exceptions import abort


def get_db_connection():
    connection = pymysql.connect(host="cmpe-272.cy4wjmr5qidh.us-east-2.rds.amazonaws.com",
                             database='blog', user='root', password='root_123')
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'

@app.route('/<int:id>/delete', methods=('DELETE',))
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    post = cursor.execute(f'SELECT * FROM posts WHERE id = {id};')
    if(post == 0):
        conn.close()
        return "Post not found", 404
    else:

        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM posts WHERE id = {id};')
        conn.commit()
        conn.close()
        return "Post deleted successfully", 200
