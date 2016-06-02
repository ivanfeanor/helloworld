try:
    from flask import Flask
except ImportError:
    raise Exception('Sorry, please install flask')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

print('Hello, World!')
