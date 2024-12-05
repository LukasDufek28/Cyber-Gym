from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PridajClanokFormular(FlaskForm):
    meno = StringField("Meno", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    recenzia = TextAreaField("Recenzia")
    odoslat = SubmitField("Pridaj clanok")