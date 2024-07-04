from market import db, login_manager
from market import bcrypt
# 這是什麼東西??
from flask_login import UserMixin
# 這是幹嘛的?
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 使用者
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    # 密碼要經過hash加密
    password_hash = db.Column(db.String(length=60), nullable=False)
    # 當前餘額，default 就是在註冊完帳戶後的初始值
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # 首先它不是一個 Column() 是一個 relationship()
    # 一個使用者可以與多個物品產生連結
    items = db.relationship("Item", backref="owned_user", lazy=True)
    # 改變顯示的內容
    def __repr__(self):
        return f"User {self.username}"

    # 1.註冊時使用的
    @property
    def password(self):
        return self.password

    # 把密碼轉換成 hash 密碼
    # 🤔這是什麼時候會執行??
    @password.setter
    def password(self, plain_text_password):
        # 把收到的密碼轉換成hash過的
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    # 2.登入時使用的
    # 檢查密碼，attempted_password 是登入的時候使用者輸入的密碼，self.password_hash 是資料庫中儲存的 hash 密碼
    def check_password_correction(self, attempted_password):
        # 返回一個布林值
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
        
    # 這是登入後的餘額顯示用的，每三位數就加一個逗號
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            # 🤔可是這樣就只會有一個逗號不是?如果超過百萬就錯了
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"    

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    


# 物品
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30),nullable=False, unique=True)
    price = db.Column(db.Integer,nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    # 一種連結，這裡的 foreign key 與 user table 的 id(primary key) 產生連結
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item {self.name}"

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()


        
# 其他範例
# class ItemModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     barcode = db.Column(db.String(80), unique=True, nullable=False)
#     description = db.Column(db.String(200), nullable=False)