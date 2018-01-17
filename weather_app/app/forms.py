from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class WeatherForm(FlaskForm):
    """Class, renders different input and submit properties to
    check_weather.html
    """
    station = StringField("City", validators=[DataRequired()])
    submit = SubmitField("Check Weather")
