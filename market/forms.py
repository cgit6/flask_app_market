from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

# 🤔 現在做的這些跟用 schema 有什麼不一樣?
# Length: 用於驗證字串的長度(最短幾個字或最長幾個字)
# EqualTo: 驗證兩者是否相等?
# Email: 
# DataRequired: 有沒有填寫?
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
# 註冊表單
class RegisterForm(FlaskForm):
    # 檢查資料是否合格，比如說使用者有沒有重複
    def validate_username(self, username_to_check):
        # 搜尋當前使用者名稱是否已經存在
        user = User.query.filter_by(username=username_to_check.data).first()
        # 如果有一樣的名稱
        if user:
            raise ValidationError("使用者名稱已經存在(換個名稱)")

    # 檢查 email 有沒有重複
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        # 如果有找到
        if email_address:
            raise ValidationError("電子郵箱已經存在(換電子郵箱)")





    username = StringField(label="使用者名稱:", validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label="電子信箱:",validators=[Email(), DataRequired()])
    # 創建密碼
    pwd1 = PasswordField(label="密碼:", validators=[Length(min=6), DataRequired()])
    # 確認密碼
    pwd2 = PasswordField(label="確認密碼:", validators=[EqualTo("pwd1"), DataRequired()])
    # 送出鈕
    submit = SubmitField(label="創建帳號")

# 用於登入
class LoginForm(FlaskForm):
    username = StringField(label="使用者名稱", validators=[DataRequired()])
    password = PasswordField(label="密碼", validators=[DataRequired()])
    submit = SubmitField(label="登入")

# 交易請求
class PurchaseItmeForm(FlaskForm):
    submit = SubmitField(label="購買物品")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="賣出物品")
