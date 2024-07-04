from market import app 
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User # 匯入
from market.forms import RegisterForm, LoginForm, PurchaseItmeForm, SellItemForm
from market import db
# login_required 是用來做
from flask_login import login_user, logout_user, login_required, current_user



@app.route("/") # decorator in python
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route('/market', methods=["GET","POST"])
@login_required
def market_page():
    # 交易訊息
    purchase_form = PurchaseItmeForm()
    # 在後端顯示交易紀錄，這邊其實可以做成記錄在後端的交易紀錄
    # if purchase_form.validate_on_submit():
    #     # print(purchase_form.__dict__) # 是一個物件所以可以用下面key value 的方式
    #     # print(purchase_form["submit"])
    #     # print(purchase_form["purchase_item"]) # 使用者查看的訊息
    #     print(request.form.get("purchase_item"))
    selling_form = SellItemForm()

    # 換一種寫法
    if request.method =="POST":
        # 購買商品的邏輯: 當使用者送出購買請求
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first() # 購買的物品的obj
        if p_item_object:
            # 檢查使用者有沒有足夠的餘額可以購買該物品
            if current_user.can_purchase(p_item_object):
                # # 如果可以，更新數據
                # p_item_object.owner = current_user.id
                # current_user.budget -= p_item_object.price # 更新剩餘金額
                # print("????:",current_user.budget)
                # db.session.commit() # 更新數據庫
                p_item_object.buy(current_user) # 把上面三行打包成一個function
                # 顯示
                flash(f"購買{p_item_object.name}/{p_item_object.price}$成功",category="success")
            else:
                flash(f"餘額不足，無法購買 {p_item_object.name}",category="danger")
        
        # 賣出商品的邏輯

        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            # 檢查能不能賣
            if current_user.can_sell(s_item_object):
                # 執行賣出，更新資料庫
                s_item_object.sell(current_user)
                flash(f"{s_item_object.name},賣出成功",category="success")
            else:
                flash(f"{s_item_object.name},賣出失敗，返回市場",category="danger")
                
        
        return redirect(url_for("market_page"))


    if request.method =="GET":

        items = Item.query.filter_by(owner=None)
        # owner:標記物品屬於誰的
        # 利用當前使用者的id 查詢屬於他的物品有哪些
        owned_items = Item.query.filter_by(owner=current_user.id) 

        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)

    # # 資料庫中的所有物品
    # items = Item.query.all()
    # 改成過濾 owner=none
    items = Item.query.filter_by(owner=None)

    # 🤔他會重新刷新一次頁面有辦法不要重新刷新嗎?
    return render_template('market.html', items=items, purchase_form=purchase_form)

# 註冊表單
@app.route("/register", methods=["GET","POST"])
def register_page():
    form = RegisterForm() # 使用者輸入的註冊資料

    # form.validate_on_submit() 具體在做什麼?
    # 這邊進行驗證作業
    if form.validate_on_submit():
        # 將使用者填寫的訊息存進資料庫
        username = form.username.data
        email_address = form.email_address.data
        password = form.pwd1.data
        # confirm_password = form.pwd2.data
        # 這裡的名稱要對應到資料庫的名稱
        user_to_create = User(username=username, email_address=email_address, password=password) 
        # 加到資料庫
        db.session.add(user_to_create)
        # 更新數據庫
        db.session.commit()
        # 註冊成功之後直接登入
        login_user(user_to_create)
        # 顯示訊息
        flash(f"註冊成功，已登入 {user_to_create.username}", category="success")
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



# 登入
@app.route("/login", methods=["GET","POST"])
def login_page():
    form = LoginForm() # 使用者輸入的登入資料
    # 
    if form.validate_on_submit():
        # 查找資料庫中有沒有相同的使用者名稱
        attempted_user = User.query.filter_by(username=form.username.data).first()
        # 如果使用者存在而且密碼正確
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"{attempted_user.username} 登入成功", category="success")
            # 跳轉到 market_page
            return redirect(url_for("market_page"))
        else:
            flash("使用者名稱和密碼不符！請再試一次", category="danger")


    
    # 
    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user() # 登出
    flash("已經登出",category="success")
    return redirect(url_for("home_page"))


# # 動態路徑
# @app.route("/about/<string:name>")
# def abiut_page(name):
#     print(name)
