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


@app.route("/game")
def game():
    if g.user is not None:
        return render_template("game.html")
    return redirect( url_for("index") )


@app.route("/store_score", methods=["POST"])
def store_score():
    db = get_db()
    score = int(request.form["score"])
    db.execute("""INSERT INTO scores (score, user_id) VALUES (?, ?)""", (score, g.user))
    db.commit()
    return "success"





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
            return redirect( url_for("index") )
    return render_template("login.html", form=form)




@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )

@app.route("/leaderboard")
def leaderboard():
    db = get_db()
    scores = db.execute("""SELECT * FROM scores
                            ORDER BY score DESC
                            LIMIT 10""").fetchall()
    return render_template("leaderboard.html", scores=scores)