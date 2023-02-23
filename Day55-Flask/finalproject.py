from flask import Flask
import random

app = Flask(__name__)

def generate_number():
    return random.randint(0,9)

@app.route("/<int:guess>")
def number(guess):
    if num < guess:
        return f"<h1>High</h1><br>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num == guess:
        return f"<h1>You Rock!</h1><br>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    else:
        return f"<h1>Low</h1><br>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

@app.route("/")
def home():
    global num
    num = generate_number()
    return f"<h1>Guess a number between 0 annd 9</h1><br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"




if __name__ == "__main__":
    app.run(debug=True)