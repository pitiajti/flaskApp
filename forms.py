from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm()):
    username = StringField('username', 
                            validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), ])