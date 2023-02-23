from flask import Flask

app = Flask(__name__)




def bold(function):
    def make_bold():
        return f"<b>{function()}</b>"
    return make_bold

def emphasis(function):
    def make_emphasis():
        return f"<em> {function()}</em>"
    return make_emphasis

def underline(function):
    def make_underline():
        return f"<u>{function()}</u>"
    return make_underline

@app.route("/")
def home():
    return "hello world"

@app.route("/<name>")
def get_user(name):
    return f"hello {name}"

@app.route("/bye")
@bold
@emphasis
@underline
def bye():
    return "bye"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)