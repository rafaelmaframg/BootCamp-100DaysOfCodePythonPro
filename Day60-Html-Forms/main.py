from flask import Flask, render_template, request
import requests
import smtplib
import os
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c3264bccdcaa99509994").json()

app = Flask(__name__)
OWN_EMAIL = YOUR OWN EMAIL ADDRESS
OWN_PASSWORD = YOUR EMAIL ADDRESS PASSWORD

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/form-entry', methods=['POST'])
def receive_data():
    data = request.form
    send_email(to_mail=OWN_EMAIL, email=data['email'], name=data['name'], phone=data['phone'], message=data['message'])
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"


def send_email(message, to_mail, email, name, phone):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("user"), password=os.getenv("pass"))
        connection.sendmail(from_addr=os.getenv('user'), to_addrs=to_mail, msg=email_message")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
