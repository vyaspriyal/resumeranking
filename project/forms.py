from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
import email_validator
from wtforms import validators
from project.models import User,Admin
from flask import redirect
from wtforms.fields.html5 import TelField
import regex as Regexp


class RegistrationForm(FlaskForm):
    id = IntegerField('Id')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()],id="pwd")
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired()],id="pwd2")
    phone =  StringField('Phone', [validators.DataRequired(),validators.Length(min = 10,max = 10),validators.Regexp(regex='\+?\d[\d -]{8,12}\d')])
    address = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    option = RadioField('option', choices=[('admin','Admin'),('user','User')])
    submit = SubmitField('Register')
  

    
    def validate_email(self, email):
        if self.option.data == "user":
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Please use a different email address.')
        else:
            user = Admin.query.filter_by(email=email.data).first()
            print(self.option,flush = True)
            if user is not None:
                raise ValidationError('Please use a different email address.')
            
    def validate_phone(self,phone):
        
        if  (self.phone.data).isalpha():
            raise ValidationError('Phone number Contains letter or symbol')
    
       
            


class LoginForm(FlaskForm):
          #login 
    email_login = StringField('Email',
                        validators=[DataRequired(), Email()])
    password_login = PasswordField('Password', validators=[DataRequired()],id="pwd1")
    remember = BooleanField('Remember Me')
    option1 = RadioField('Label', choices=[('admin','Admin'),('user','User')])
    remember = BooleanField('Remember Me')
    submit_login = SubmitField('Login')



    

