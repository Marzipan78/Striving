from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
    username = StringField("Username",
                            validators=[ DataRequired(), Length(min = 2, max = 20)] )
    email = StringField("Email",
                        validators= [DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Password", validators=[DataRequired()])