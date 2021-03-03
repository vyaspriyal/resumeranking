from project import db,login_manager,session
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    if session.get('type') == "user":

        return User.query.get(int(user_id))
    elif session.get('type') == "admin":
        return Admin.query.get(int(user_id))
    else:
        return None
  
#database creation for user
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
    address = db.Column(db.String(100))
    image_file = db.Column(db.String(20), nullable=False,default = 'default.jpg')
    type = db.Column(db.String(20),default = 'user')
    No_of_year_experience = db.Column(db.Integer,default = 0)
    about = db.Column(db.String(500))
    tagline = db.Column(db.String(20))
    current_workplace =  db.Column(db.String(60))
    def __init__(self,name,email,password,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
        
    def get_id(self):
        return str(self.id)
  


# database creation for admin
class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
    address = db.Column(db.String(100))
    image_file = db.Column(db.String(20), nullable=False,default = 'default.jpg')
    type = db.Column(db.String(20),default = 'admin')
    def __init__(self,name,email,password,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
    def get_id(self):
        return str(self.id)

