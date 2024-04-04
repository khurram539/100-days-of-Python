from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!<h1>' \
           '<p>This is a smooch time!</p>' \
           '<iframe src="https://giphy.com/embed/9G0AdBbVrkV3O" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'

@app.route('/bye')
def bye():
    return "<b>Bye!</b>"

# Creating variable path and converting the path to a specific data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
    
    
    
    