from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1>Guess a between number 0 and 9!</h1>' \
           '<img src="https://media2.giphy.com/media/Kzbfaz4Bm27sCzZNDQ/giphy.gif?cid' \
           '=ecf05e4701wy2tzbvs0on5dp54usc4k3ez3dp5snvzp6dv58&rid=giphy.gif&ct=g alt="picture"> ' \
 \
 \



@app.route('/<int:y>')
def checker(y):
    x = random.randint(1, 11)
    if y < x:
        return '<h1 style="color: red"> Too low </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="pic">'
    elif y > x:
        return '<h1 style="color: purple"> Too High </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="pic">'
    else:
        return '<h1 style="color: green"> You Found Me!' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif alt="pic" >'


if __name__ == "__main__":
    app.run(debug=True)
