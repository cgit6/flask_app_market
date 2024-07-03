from flask import Flask
# SQL Alchemy 的優勢 => ORM
from flask_sqlalchemy import SQLAlchemy
# import os
# 因為這裡產生 circular import

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "fa9920a030e1403f913ee1f7"
# print(app.config["SQLALCHEMY_DATABASE_URI"])
db = SQLAlchemy(app) # 初始化 SQLAlchemy




from market import routes