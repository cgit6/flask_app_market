from flask import Flask
# SQL Alchemy 的優勢 => ORM
from flask_sqlalchemy import SQLAlchemy
# import os
# 因為這裡產生 circular import，所以對整個檔案進行重構
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "fa9920a030e1403f913ee1f7"
# print(app.config["SQLALCHEMY_DATABASE_URI"])
db = SQLAlchemy(app) # 初始化 SQLAlchemy
# 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# 🤔這是什麼?? 如果沒登入就跳畫面?
login_manager.login_view = "login_page"
login_manager.login_message = "請登入帳號"
login_manager.login_message_category = "info" # 顯示藍色



from market import routes