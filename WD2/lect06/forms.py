from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class BMIForm(FlaskForm):
    w = DecimalField("Weight (kg)", validators=[InputRequired(), NumberRange(10, 300)])
    h = DecimalField("Height (m)", validators=[InputRequired(), NumberRange(0.5, 2.5)])
    bmi = DecimalField("BMI")
    submit = SubmitField("Submit")