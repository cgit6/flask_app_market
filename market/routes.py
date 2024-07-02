from market import app 
from flask import render_template
from market.models import ItemModel # 
# from db import db
# import models # 處理數據的


@app.route("/") # decorator in python
@app.route("/home")
def home_page():
    return render_template("home.html")

# # 動態路徑
# @app.route("/about/<string:name>")
# def abiut_page(name):
#     print(name)

@app.route('/market')
def market_page():
    items = ItemModel.query.all()
    return render_template('market.html', items=items)
