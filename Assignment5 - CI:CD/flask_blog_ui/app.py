import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'


@app.route('/')
def index():
    posts = requests.get("http://127.0.0.1:5002/", data={}, verify=False)
    print(posts)
    posts = posts.json()
    return render_template('index.html', posts=posts)


@app.route('/<int:id>')
def post(id):
    post = requests.get(f"http://127.0.0.1:5002/{id}", data={}, verify=False)
    print(post)
    post = post.json()[0]
    return render_template('post.html', post=post)


@app.route('/create', methods=('POST', 'GET'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            response = requests.post(f"http://127.0.0.1:5000/create", data={'title': title, 'content': content}, verify=False)
            print("create response ", response)
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST', 'PUT'))
def edit(id):
    post = requests.get(f"http://127.0.0.1:5002/{id}", data={}, verify=False).json()[0]

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            response = requests.put(f"http://127.0.0.1:5003/{id}/edit", data={'title': title, 'content': content}, verify=False)
            print("update response ", response)
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    requests.delete(f"http://127.0.0.1:5001/{id}/delete", verify=False)
    return redirect(url_for('index'))
