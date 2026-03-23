from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/about")
def about():
    return "Mikolaj"

@app.route("/contact")
def contact():
    return "Dane komorkowe"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"

@app.route("/square/<int:n>")
def square(n):
    return f"{n} to {n**2}"

from datetime import datetime
@app.route("/datatime")
def datatime():
    return f"{datatime.now()}"

from flask import render_template

@app.route("/h_template/<nickname>")
def h_template(nickname):
    return render_template("index.html", name = nickname)

@app.route("/age/<int:age>")
def age(age):
    return render_template("age.html", age = age)

@app.route("/loop")
def loop():
    data = ["Python", "Flask", "HTML"]
    return render_template("loop.html", items = data)


@app.route("/users")
def users():
    data = [{'status':"active",
            "nickname": "dzordzo_automatovic",
            "age": "41"},
            {'status':"active",
            "nickname": "maniek",
            "age": "21"},
            {'status':"active",
            "nickname": "dzordzo",
            "age": "34"}]
    return render_template("users.html", users = data)


app.run(debug=True)