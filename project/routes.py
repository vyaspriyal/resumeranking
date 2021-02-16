from flask import  render_template, url_for, flash, redirect,request,send_from_directory
from project import app,db,bcrypt
from project.forms import RegistrationForm,LoginForm
from project.models import User,Admin
from flask_login import login_user,current_user,logout_user,login_required
from wtforms import validators
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
import email_validator
from flask_wtf import FlaskForm

from sqlalchemy.exc import SQLAlchemyError



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/user")
def user():
    return render_template('user/mainpageuser.html')
@app.route("/admin")
def admin():
    return render_template('admin/mainpageadmin.html')


@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        if current_user.type == "user":
            return redirect(url_for('user'))
        if current_user.type == "admin":
            return redirect(url_for('admin'))
  

    form = RegistrationForm()
    option = request.form.get("option")
    
    
    if   request.form.get('submit',False) == "Register":
        if form.validate_on_submit():
    
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            name = request.form['username']
            phone = request.form['phone']
            email = request.form['email']
            password = request.form['password']
            address = request.form['address']

            if option == "user":
                print("impl",flush=True)
                my_data = User(name,email,hashed_password,phone,address)
                
            
                db.session.add(my_data)
                db.session.commit()
            
            elif option == "admin":
                my_data = Admin(name,email,hashed_password,phone,address)
                try:
                    db.session.add(my_data)
                    db.session.commit()
                except:
                    if form.validate_on_submit():
                        pass
            else:
                pass

    else:
        pass

    return render_template('register.html', title='Register',form = form)
    



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated :
        if current_user.type == "user":
            return redirect(url_for('user'))
        if current_user.type == "admin":
            return redirect(url_for('admin'))
  
    form = LoginForm()

    if form.validate_on_submit():
        email_login = request.form['email_login']
        password_login = request.form['password_login']
        option1 = request.form.get("option1")
        if option1 == "user":
            user = User.query.filter_by(email = email_login).first()
            if user and bcrypt.check_password_hash(user.password,password_login):
            
                login_user(user,remember=form.remember.data)
                return redirect(url_for('user'))
            else:
                flash('Login Unsuccessfull')
        elif option1 == "admin":
            admin = Admin.query.filter_by(email = email_login).first()
            if admin and bcrypt.check_password_hash(admin.password,password_login):
                login_user(admin,remember=form.remember.data)
                return redirect(url_for('admin'))
            else:
                flash('Login Unsuccessfull')
        else:
            flash('Pls select one option')

      

    return render_template('login.html', title='Login', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('user/mainpageuser.html', title='About')

