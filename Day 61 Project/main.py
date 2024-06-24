from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

app = Flask(__name__)
app.secret_key = "BlankMisticalBEAST@1324"


class LoginForm(FlaskForm):
    email = StringField(label='email')
    password = PasswordField(label='password')
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    
# export FLASK_APP=main.py
# flask run