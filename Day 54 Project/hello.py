from flask import Flask
# import random   

app = Flask(__name__)

# print(random.__name__)
# print(__name__)

@app.route('/')
def hello_word():
    return "<p>Hello World!</p>"

# export FLASK_APP=hello.py
# flask run

if __name__ == '__main__':
    app.run()   # python hello.py
    