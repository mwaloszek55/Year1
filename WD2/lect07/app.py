from flask import Flask, render_template
from forms import WombatForm, ToppingForm, ColourForm





app = Flask(__name__)
app.config["SECRET_KEY"] = "babooey"


@app.route("/wombat", methods=["GET", "POST"])
def wombats():
    form = WombatForm()
    answer = ""
    if form.validate_on_submit():
        wombat = form.wombat.data
        if wombat == True:
            answer = "You're wrong. Derek does not like wombats"
        else:
            answer = "You're correct! Derek does not like wombats"
    return render_template("wombat_form.html", form=form, title="Wombat Preferences!", answer=answer)

@app.route("/topping", methods=["GET", "POST"])
def pizza_topping():
    form = ToppingForm()
    answer = ""
    if form.validate_on_submit():
        topping = form.topping.data
        if topping == "anchovies":
            answer = "You're correct"
        else:
            answer = "You're wrong"
    return render_template("topping_form.html", form=form, title="Topping Preferences!", answer=answer)


@app.route("/colour", methods=["GET", "POST"])
def colour():
    form = ColourForm()
    answer = ""
    if form.validate_on_submit():
        colour = form.colour.data
        if colour == "green":
            answer = "You're correct"
        else:
            answer = "You're wrong"
    return render_template("colour_form.html", form=form, title="Colour Preferences!", answer=answer)





