from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.sqlite3'

app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)
app.app_context().push()


# 'postgresql://postgres:Tr4der2404@localhost/login'