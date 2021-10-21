from flask_wtf.form import FlaskForm
from wtforms.fields.simple import PasswordField
from app.models.user import User

from wtforms import StringField, SubmitField
from wtforms.validators import EqualTo, InputRequired, Length, ValidationError

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), 
    Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), 
    Length(min=4, max=20), EqualTo('confirm_password', message='Passwords must match')], render_kw={"placeholder": "Password"})

    confirm_password = PasswordField(validators=[InputRequired(), 
    Length(min=4, max=20)], render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField("Register")


    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists")