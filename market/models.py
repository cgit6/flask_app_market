from market import db

# 使用者
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    # 密碼要經過加密
    password_hash = db.Column(db.String(length=60), nullable=False)
    # default 就是在註冊完帳戶後的初始值
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # 首先它不是一個 Column() 是一個 relationship()
    # 一個使用者可以與多個物品產生連結
    items = db.relationship("Item", backref="owned_user", lazy=True)
    # 

    def __repr__(self):
        return f"User {self.username}"


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
        
# 其他範例
# class ItemModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     barcode = db.Column(db.String(80), unique=True, nullable=False)
#     description = db.Column(db.String(200), nullable=False)