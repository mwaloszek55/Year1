from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/identify", methods=["GET", "POST"])
def identify():
    if request.method == "GET":
        return render_template("form.html")
    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("response.html", family_name=family_name, given_name=given_name)


@app.route("/form")
def send_form():
    return render_template("form.html")

@app.route("/response", methods=["POST"])
def get_response():
    given_name = request.form["given_name"]
    family_name = request.form["family_name"]
    return render_template("response.html", family_name=family_name, given_name=given_name)



