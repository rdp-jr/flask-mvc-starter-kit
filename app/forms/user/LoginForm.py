from flask_wtf.form import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), 
    Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), 
    Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")


   