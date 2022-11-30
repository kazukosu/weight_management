# from weight_management.flaskmodule.login import login
from sqlite3 import connect
from flask import Flask, redirect, render_template,session
from flaskmodule.signup import signup_app
from flaskmodule.login import login_app
from flaskmodule.inputweight import inputweight_app
from flaskmodule.outputweight import outputweight_app
import html
import secrets
import MySQLdb
from datetime import timedelta

print("hello main.py!")
# Flaskとrender_template（HTMLを表示させるための関数）をインポート

# Flaskオブジェクトの生成
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
app.permanent_session_lifetime = timedelta(minutes=60)
app.register_blueprint(signup_app)
app.register_blueprint(login_app)
app.register_blueprint(inputweight_app)
app.register_blueprint(outputweight_app)

def connect():
    con = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd =  "ryo",
        db = "mw",
        use_unicode=True,
        charset = "utf8")
    return con


# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/hello")
def hello():
    return "Hello World"

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    print(session.keys())
    return render_template("index.html")

@app.route("/home")
def home():
    if "age" in session:
        if session["admin"] == 1:
            #html.escapeは文字列に対してのみ利用可能intの場合はエラー吐く
            return render_template("success.html",
                                    age=html.escape(str(session["age"])),
                                    email=html.escape(session["email"]),
                                    height=html.escape(str(session["height"])),
                                    admin="<a href=\"admin\">ユーザ情報一覧</a>")
        else:
            print(session.keys())
            return render_template("success.html",
                                    age=html.escape(str(session["age"])),
                                    email=html.escape(session["email"]),
                                    height=html.escape(str(session["height"])))
    else:
        return redirect("login")

@app.route("/admin")
def admin():
    if "admin" in session:
        if session["admin"] == 1:
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        SELECT age,id,height,sex
                        FROM user
                        """)
            res = ""
            for row in cur:
                res = res + "<table border=\"1\" align=\"center\">\n"
                res = res + "\t<tr><td align=\"right\">年齢</td><td>" + html.escape(str(row[0])) + "</td></tr>\n"
                res = res + "\t<tr><td align=\"right\">メールアドレス</td><td>" + html.escape(str(row[1])) + "</td></tr>\n"
                res = res + "\t<tr><td align=\"right\">身長</td><td>" + html.escape(str(row[2])) + "</td></tr>\n"
                res = res + "\t<a href=\"home\">ホーム</a>"
            con.close()
            return res
        else:
            return redirect("home")
    else:
        return redirect("home")


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
