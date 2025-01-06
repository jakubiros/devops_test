from flask import Flask
from datetime import datetime

app = Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, %s!' % name

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def server_time():
    now = datetime.now()
    return f"Current server time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

@app.route('/about')
def about():
    return "This is a simple Flask app for learning DevOps practices."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)