from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/SayHello/<username>')
def say_hello(username):
    return "Hello" + username

if __name__ == '__main__':
    app.run()
