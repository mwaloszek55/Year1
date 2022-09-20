from flask import Flask, render_template


app = Flask(__name__)


@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return render_template("greet1.html", name=name)



@app.route("/greet_across_the_world/<language>")
def send_greeting_by_language(language):
    hello_dict = {"en": "hello", "fr": "bonjour", "es": "hola"}
    if language in hello_dict:
        greeting = hello_dict[language]
    else:
        greeting = "Hi"
    return render_template("greet2.html", greeting=greeting)








