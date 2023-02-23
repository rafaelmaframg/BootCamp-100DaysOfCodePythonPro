from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<name>")
def guess(name):
    genderize = requests.get("https://api.genderize.io", params={'name': name})
    agify = requests.get('https://api.agify.io', params={'name': name})
    agify = agify.json()
    genderize = genderize.json()
    return f"<h1> Hello {name}, <br> I Think you are {genderize['gender']}, <br> and maybe {agify['age']} years old</h1>"


@app.route("/blog/<int:num>")
def get_blog(num):
    response = requests.get('https://api.npoint.io/1a8e655d4e52acbc0420')
    response = response.json()
    return render_template('blog.html', posts=response, num=num)

if __name__ == "__main__":
    app.run(debug=True)