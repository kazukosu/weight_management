import email
from sqlite3 import connect
from flask import Flask,request,render_template,url_for,redirect
from werkzeug.security import generate_password_hash as gph
from flask import Blueprint
import MySQLdb

signup_app = Blueprint("signup",__name__)

def connect():
    con = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd =  "ryo",
        db = "mw",
        use_unicode=True,
        charset = "utf8")
    return con

@signup_app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signUp.html")
    elif request.method=="POST":
        print("hello signup")
        id = request.form["id"]
        passwd=request.form["passwd"]
        height = request.form["height"]
        age = request.form["age"]
        sex = request.form["sex"]
        hashpass = gph(passwd)
        con =connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT * FROM user WHERE id=%(id)s
                    """,{"id":id})
        
        data = []
        for row in cur:
            print(row)
            data.append(row)
        if len(data) != 0:
            return render_template("signUp.html",msg="既に存在するIDです")
        con.commit()
        con.close()
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    INSERT INTO user
                    (id,sex,age,height,passwd)
                    VALUES (%(id)s,%(sex)s,%(age)s,%(height)s,%(hashpass)s)
                    """,{"id":id,"sex":sex,"age":age,"height":height,"hashpass":hashpass})
        con.commit()
        con.close()
        return render_template("info.html", id=id,sex=sex,age=age,height=height,passwd=passwd)

    name = "ログインページ"
    return render_template("login.html", name=name)