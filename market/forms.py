from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

# 🤔 現在做的這些跟用 schema 有什麼不一樣?
# Length: 用於驗證字串的長度(最短幾個字或最長幾個字)
# EqualTo: 驗證兩者是否相等?
# Email: 
# DataRequired: 有沒有填寫?
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="使用者名稱:", validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label="電子信箱:",validators=[Email(), DataRequired()])
    # 創建密碼
    pwd1 = PasswordField(label="密碼:", validators=[Length(min=6), DataRequired()])
    # 確認密碼
    pwd2 = PasswordField(label="確認密碼:", validators=[EqualTo("pwd1"), DataRequired()])
    # 送出鈕
    submit = SubmitField(label="創建帳號")
