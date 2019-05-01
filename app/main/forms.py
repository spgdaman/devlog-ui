from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

class SignupForm(FlaskForm):
    firstname = StringField('Firstname',validators=[Required()])
    lastname = StringField('Lastname', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required])
    password = PasswordField('Password',validators=[Required()])
    confirmpass = PasswordField('Confirm password', validators=[Required(),EqualTo('Password',message="Your passwords do not match!")])
    submit = SubmitField('Submit', validators=[Required()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me?')
    submit = SubmitField('Submit')
