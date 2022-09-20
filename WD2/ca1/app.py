from flask import Flask, render_template, redirect, url_for, session, request, make_response, g
from database import get_db, close_db
from forms import RegistrationForm, LoginForm
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps




app = Flask(__name__)
app.config["SECRET_KEY"] = "babooey"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)





@app.teardown_appcontext
def close_db_at_end_of_request(e=None):
    close_db(e)





@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)





@app.route("/")
def index():
    return render_template("index.html")





@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        digits = 0
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        for i in password:
            if i.isdigit():
                digits+=1
        db = get_db()
        if db.execute("""SELECT * FROM users
                      WHERE user_id =?;""", (user_id,)).fetchone() is not None:
            form.user_id.errors.append("User ID already taken!")
        elif password != password2:
            form.password.errors.append("Passwords must be the same. ")
        elif not (len(password)>=8 and len(password)<=16):
            form.password.errors.append("Your password password must be between 8 and 16 characters. ")
        elif digits < 3:
            form.password.errors.append("Your password has less than 3 digits. ")
        else:
            db.execute("""INSERT INTO users (user_id, password)
                          Values (?, ?)""", (user_id, generate_password_hash(password)))
            db.commit()
            return redirect( url_for("login") )
    return render_template("register.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        user = db.execute(""" SELECT * FROM users
                            Where user_id = ?;""", (user_id,)).fetchone()
        if user is None:
            form.user_id.errors.append("Unknown user ID")
        elif not check_password_hash(user["password"], password):
            form.password.errors.append("Wrong Password")
        else:
            session.clear()
            session["user_id"] = user_id
            items = db.execute("""SELECT item FROM cart
                                  WHERE user= ?""", (user_id,)).fetchall()
            quants = db.execute("""SELECT quant FROM cart
                                  WHERE user= ?""", (user_id,)).fetchall()
            if "cart" not in session:
                session["cart"] = {}
                for i in range(len(items)):
                    session["cart"][items[i]["item"]] = quants[i]["quant"]


            return redirect( url_for("index") )
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )



@app.route("/shop")
def shop():
    db = get_db()
    bikes = db.execute("""SELECT * FROM bikes;""").fetchall()
    return render_template("shop.html", bikes=bikes)



@app.route("/bikes/<int:bike_id>")
def bike(bike_id):
    db = get_db()
    bike = db.execute("""SELECT * FROM bikes
                         WHERE bike_id = ?;""", (bike_id,)).fetchone()
    return render_template("bike.html", bike=bike)



@app.route("/cart")
def cart():
    db = get_db()
    if "cart" not in session:
        session["cart"] = {}
    names = {}
    for bike_id in session["cart"]:
        name = db.execute("""SELECT * FROM bikes
                             WHERE bike_id = ?;""", (bike_id,)).fetchone()["name"]
        names[bike_id] = name     
    return render_template("cart.html", cart=session["cart"], names=names)



@app.route("/add_to_cart/<int:bike_id>")
def add_to_cart(bike_id):
    if "cart" not in session:
        session["cart"] = {}
    if bike_id not in session["cart"]:
        session["cart"][bike_id] = 0
    session["cart"][bike_id] = session["cart"][bike_id] + 1
    if g.user is not None:
        db = get_db()
        quant = session["cart"][bike_id]
        if db.execute("""SELECT * FROM cart
                        WHERE item = ? AND user = ?""", (bike_id, g.user)).fetchone() is not None:
            db.execute("""UPDATE cart SET quant = ? WHERE item = ? AND user = ?""", (quant, bike_id, g.user))
            db.commit()
        else:
            db.execute("""INSERT INTO cart (item, user, quant) VALUES (?, ?, ?)""", (bike_id, g.user, quant))
            db.commit()
    return redirect( url_for("cart"))


@app.route("/remove_from_cart/<int:bike_id>")
def remove_from_cart(bike_id):
    db = get_db()
    if "cart" not in session:
        session["cart"] = {}
    if bike_id not in session["cart"]:
        session["cart"][bike_id] = 0
    session["cart"][bike_id] = session["cart"][bike_id] - 1
    if g.user is not None:
        db = get_db()
        quant = session["cart"][bike_id]
        if db.execute("""SELECT * FROM cart
                        WHERE item = ? AND user = ?""", (bike_id, g.user)).fetchone() is not None:
            db.execute("""UPDATE cart SET quant = ? WHERE item = ? AND user = ?""", (quant, bike_id, g.user))
            db.commit()
        else:
            db.execute("""INSERT INTO cart (item, user, quant) VALUES (?, ?, ?)""", (bike_id, g.user, quant))
            db.commit()
    if session["cart"][bike_id] <= 0:
        session["cart"].pop(bike_id)
    return redirect( url_for("cart") )

