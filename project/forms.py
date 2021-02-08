from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
import email_validator
from wtforms import validators
from project.models import User,Admin
from flask import redirect



class RegistrationForm(FlaskForm):
    id = IntegerField('Id')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()],id="pwd")
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired()],id="pwd2")
    phone = IntegerField('Phone',validators=[DataRequired()])
    address = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    option = RadioField('option', choices=[('admin','Admin'),('user','User')])
    submit = SubmitField('Register')
        #login 
    email_login = StringField('Email',
                        validators=[ Email()],default='abc@gmail.com')
    password_login = PasswordField('Password', validators=[],id="pwd1")
    remember = BooleanField('Remember Me')
    option1 = RadioField('Label', choices=[('admin','Admin'),('user','User')], default='user')
    remember = BooleanField('Remember Me')
    submit_login = SubmitField('Login')

    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
   
       
            

"""
class LoginForm(FlaskForm):

    

  """