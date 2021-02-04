from flask import  render_template, url_for, flash, redirect,request
from project import app,db,bcrypt
from project.forms import RegistrationForm
from project.models import User,Admin
from flask_login import login_user



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('login.html', title='About')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
        #for login
    if form.validate_on_submit():
        email = request.form['email_login']
        password = request.form1['password_login']
        option1 = request.form.get("option1")
        user = User.query.filter_by(email = email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            pass




    return render_template('register.html', title='Register', form=form)
"""
    
    if  form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        name = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        option = request.form.get("option")

     
   
        
       
    
    
     
        if option == "user":
            my_data = User(name,email,hashed_password,phone,address)
            db.session.add(my_data)
            db.session.commit()
            
            return render_template('home.html', title='Register', form=form)
        elif option == "admin":
            my_data = Admin(name,email,hashed_password,phone,address)
            db.session.add(my_data)
            db.session.commit()
        
        else:
            pass
    
    
"""    



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form1.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

