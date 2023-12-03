from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/message')
def send_message():
    return 'This is a message from the server.'

if __name__ == '__main__':
    app.run(debug=True)

