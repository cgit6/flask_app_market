from market import app

if __name__ == "__main__":
    # 初始化 Flask SQLAlchemy

    app.run()


# from app import create_app, db
# import models

# if __name__ == "__main__":
#     with app.app_context():
#         # 添加數據到數據庫
#         item1 = models.ItemModel(name="IPhone 12", price=502, barcode='846154104832', description='desc2')
#         db.session.add(item1)
#         db.session.commit()
    
#         # 查詢數據庫中的所有項目
#         items = models.ItemModel.query.all()
#         for item in items:
#             print(f"ID: {item.id}, Name: {item.name}, Price: {item.price}, Barcode: {item.barcode}, Description: {item.description}")
    
#     app.run()
