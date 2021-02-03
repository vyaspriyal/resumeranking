from project import db


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

