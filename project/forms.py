from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
import email_validator
from wtforms import validators
from project.models import User



class RegistrationForm(FlaskForm):
    id = IntegerField('Id')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()],id="pwd")
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')],id="pwd2")
    phone = IntegerField('Phone')
    address = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    option = RadioField('option', choices=[('admin','Admin'),('user','User')])
    submit = SubmitField('Register')
        #login 
    email_login = StringField('Email',
                        validators=[DataRequired(), Email()])
    password_login = PasswordField('Password', validators=[DataRequired()],id="pwd1")
    remember = BooleanField('Remember Me')
    option1 = RadioField('Label', choices=[('admin','Admin'),('user','User')])
    remember = BooleanField('Remember Me')
    submit_login = SubmitField('Login')


    def validate_username(self,username):
        user = User.query.filter_by(name = username).first()
        if user:
            raise ValidationError('Username already taken.')

    
    def validate_email(self,email):
        user = User.query.filter_by(email = email).first()
        if user:
            raise ValidationError('Email already taken.')

"""
class LoginForm(FlaskForm):

    

  """