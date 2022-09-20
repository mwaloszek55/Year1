from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from wtforms.fields.html5 import DateField

class BandForm(FlaskForm):
    band = StringField("Band:", validators=[InputRequired()])
    submit = SubmitField("Submit")


class GigForm(FlaskForm):
    band = StringField("Band:", validators=[InputRequired()])
    gig_date = DateField("Gig Date:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
    user_id = StringField("User ID:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password:", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit")









