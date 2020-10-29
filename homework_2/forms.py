from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email

# DataRequired == Making sure teh field is filled in
# EqualTo == Making sure the field(s) are the same (I.E Password and Config Password)
# Email == Making Sure the field has a proper email given to it. 

class UserInfoForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()