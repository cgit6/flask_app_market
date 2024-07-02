from market import db


class ItemModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30),nullable=False, unique=True)
    price = db.Column(db.Integer,nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f"Item {self.name}"
        
# 其他範例
# class ItemModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     barcode = db.Column(db.String(80), unique=True, nullable=False)
#     description = db.Column(db.String(200), nullable=False)