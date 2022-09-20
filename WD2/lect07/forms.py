from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField
from wtforms.validators import InputRequired

class WombatForm(FlaskForm):
    wombat = BooleanField("Check the box if you think Derek likes wombats:")
    submit = SubmitField("Submit")


class ToppingForm(FlaskForm):
    topping = SelectField("fave pizza topping", validators=[InputRequired()], choices=[("anchovies", "Anchovies"), ("chocolate", "Chocolate"), ("painapple", "Painapple")])
    submit = SubmitField("Submit")


class ColourForm(FlaskForm):
    colour = RadioField("fave colour", choices=[("red", "Red:"), ("green", "Green:"), ("blue", "Blue:")], default="red")
    submit = SubmitField("Submit")