from market import app 
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User # 匯入
from market.forms import RegisterForm
from market import db

@app.route("/") # decorator in python
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

# 註冊表單
@app.route("/register", methods=["GET","POST"])
def register_page():
    form = RegisterForm()

    # form.validate_on_submit() 具體在做什麼?
    # 這邊進行驗證作業
    if form.validate_on_submit():
        # 將使用者填寫的訊息存進資料庫
        username = form.username.data
        email_address = form.email_address.data
        password = form.pwd1.data
        # confirm_password = form.pwd2.data
        # 這裡的名稱要對應到資料庫的名稱
        user_to_create = User(username=username, email_address=email_address, password_hash=password) 
        # 加到資料庫
        db.session.add(user_to_create)
        # 更新數據庫
        db.session.commit()
        # 送出表單之後(重新定向)跳轉到 market 頁面
        return redirect(url_for("market_page"))
    
    # 如果驗證有出現錯誤訊息
    if form.errors != {}:
        # 列出所有錯誤訊息
        # 🤔 (錯誤訊息)這個東西可以存到一個 log 檔案
        for err_msg in form.errors.values():
            # 將錯誤訊息傳到前端(client)
            # category 為變數
            flash(f"建立使用者時出錯: {err_msg}", category="danger")

    return render_template("register.html",form=form)

# # 動態路徑
# @app.route("/about/<string:name>")
# def abiut_page(name):
#     print(name)
