import email
from re import template
from sqlite3 import connect
from flask import Flask,request,render_template,redirect,session
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from flask import Blueprint
import MySQLdb

login_app = Blueprint("loginup",__name__)


def connect():
    con = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd =  "ryo",
        db = "mw",
        use_unicode=True,
        charset = "utf8")
    return con

@login_app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        session.clear()
        return render_template("login.html")
    elif request.method=="POST":
        email = request.form["email"]
        passwd = request.form["passwd"]
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT passwd,id,age,height,admin
                    FROM user
                    WHERE id=%(email)s
                    """,{"email":email})
        data = []
        print(data)
        for row in cur:
            print(row)
            data.append([row[0],row[1],row[2],row[3],row[4]])
        if len(data)==0:
            con.close()
            return render_template("login.html", msg="そのメールアドレスは登録されていません")
        if cph(data[0][0], passwd):
            print(data)
            session["age"] = data[0][2]
            session["email"] = data[0][1]
            session["height"] = data[0][3]
            session["admin"] = 0 if data[0][4] is None else data[0][4]
            con.close()
            return redirect("home")
        else:
            con.close()
            return render_template("login.html",msg="パスワードが間違っています")
