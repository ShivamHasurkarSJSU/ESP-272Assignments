from flask import Flask, render_template
import gc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gc_stats')
def gc_stats():
    return str(gc.get_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)