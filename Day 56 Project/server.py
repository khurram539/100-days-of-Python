from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Khurram.html")

if __name__ == "__main__":
    app.run(debug=True)


# export FLASK_APP=server.py
# flask run 