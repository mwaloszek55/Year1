from flask import Flask
from datetime import datetime
from random import choice


app = Flask(__name__)


@app.route("/")
def send_greeting():
    return "Hello, world!"


@app.route("/bro")
def send_poggers():
    return "poggers"

@app.route("/datetime")
def datetimehehe():
    return datetime.now().strftime("%H-%M-%S %d-%m-%y")

@app.route("/greetme")
def randomgreeting():
    phrases = ["my friend", "ya big eejit", "big boi"]
    return "Hello, " + choice(phrases)

@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return "Hello, " + name

@app.route("/adios/<name>")
@app.route("/au_revoir/<name>")
@app.route("/parting_by_name/<name>")
def send_parting_by_name(name):
    return "So long, " + name


@app.errorhandler(404)
def page_not_found(error):
    return "oopsie", 404













