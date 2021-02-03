from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/beproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from project import routes
