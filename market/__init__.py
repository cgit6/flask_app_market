from flask import Flask
# SQL Alchemy 的優勢 => ORM
from flask_sqlalchemy import SQLAlchemy
# import os
# 因為這裡產生 circular import

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
print(app.config["SQLALCHEMY_DATABASE_URI"])
db = SQLAlchemy(app)

db.init_app(app) 
with app.app_context():
    db.create_all()

from market import routes