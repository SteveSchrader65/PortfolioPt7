from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return f'Hello, Stranger'


if __name__ == '__main__':
    app.run()
