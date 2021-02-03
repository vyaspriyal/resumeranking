from flask import Flask, render_template, url_for, flash, redirect,request

from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()
from flask_bcrypt import Bcrypt
from forms import RegistrationForm
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/beproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


#database creation for user
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
    address = db.Column(db.String(100))
    image_file = db.Column(db.String(20), nullable=False,default = 'default.jpg')
    def __init__(self,name,email,password,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
# database creation for admin
class Admin(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
    address = db.Column(db.String(100))
    image_file = db.Column(db.String(20), nullable=False,default = 'default.jpg')
    def __init__(self,name,email,password,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address

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
    if request.method == 'POST':
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
            flash('Thank you for registering')
        elif option == "admin":
            my_data = Admin(name,email,hashed_password,phone,address)
            db.session.add(my_data)
            db.session.commit()
        
        else:
            pass
    
    
        
        
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
