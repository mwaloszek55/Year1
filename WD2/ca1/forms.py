from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from wtforms.fields.html5 import DateField







class LoginForm(FlaskForm):
    user_id = StringField("User ID:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    user_id = StringField("User ID:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password:", validators=[InputRequired()])
    submit = SubmitField("Register")