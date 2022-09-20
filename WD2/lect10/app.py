from flask import Flask, render_template, redirect, url_for
from database import get_db, close_db
from flask import session
from flask_session import Session


app = Flask(__name__)
app.config["SECRET_KEY"] = "babooey"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.teardown_appcontext
def close_db_at_end_of_request(e=None):
    close_db(e)

@app.route("/wines")
def wines():
    db = get_db()
    wines = db.execute("""SELECT * FROM WINES;""").fetchall()
    return render_template("wines.html", wines=wines)

@app.route("/wine/<int:wine_id>")
def wine(wine_id):
    db = get_db()
    wine = db.execute("""SELECT * FROM wines
                         WHERE wine_id = ?;""", (wine_id,)).fetchone()
    return render_template("wine.html", wine=wine)

@app.route("/cart")
def cart():
    if "cart" not in session:
        session["cart"] = {}
    names = {}
    db = get_db()
    for wine_id in session["cart"]:
        name = db.execute("""SELECT * FROM wines
                             WHERE wine_id = ?;""", (wine_id,)).fetchone()["name"]
        names[wine_id] = name
    return render_template("cart.html", cart=session["cart"], names=names)


@app.route("/add_to_cart/<int:wine_id>")
def add_to_cart(wine_id):
    if "cart" not in session:
        session["cart"] = {}
    if wine_id not in session["cart"]:
        session["cart"][wine_id] = 0
    session["cart"][wine_id] = session["cart"][wine_id] + 1
    return redirect( url_for("cart") )







