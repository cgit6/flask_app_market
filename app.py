from flask import Flask, render_template
from db import db
import models # 處理數據的



def create_app(db_url =None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"

    # 初始化 Flask SQLAlchemy
    db.init_app(app) 

    with app.app_context():
        db.create_all()


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
        items = [
            {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
            {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
            {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
        ]
        return render_template('market.html', items=items)

    return app