from flask import Flask
app = Flask(__name__)


@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/SayHello2/<username>')
def say_hello(username):
    return "Hello " + username

if __name__ == '__main__':
    app.run()
