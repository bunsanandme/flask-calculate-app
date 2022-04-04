from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    start_date = DateField(validators=[DataRequired()])
    end_date = DateField(validators=[DataRequired()])
    submit = SubmitField('Рассчитать')
