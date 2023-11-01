import pymysql
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    connection = pymysql.connect(host="cmpe-272.cy4wjmr5qidh.us-east-2.rds.amazonaws.com",
                             database='blog', user='root', password='root_123')
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title:
            abort(400, 'Title is required.')
        else:
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(f"INSERT INTO posts (title, content) VALUES ('{title}', '{content}');")
                conn.commit()
                conn.close()
                return "Post created successfully"
            except Exception as e:
                return str(e), 401

