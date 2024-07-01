from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # decorator in python
@app.route("/home")
def home_page():
    return render_template("home.html")

# # 動態路徑
# @app.route("/about/<string:name>")
# def abiut_page(name):
#     print(name)


