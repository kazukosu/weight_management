from re import template
from sqlite3 import connect
from flask import Flask,request,render_template,redirect,session
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from flask import Blueprint
import MySQLdb
import datetime


inputweight_app = Blueprint("inputweight",__name__)


def connect():
    con = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd =  "ryo",
        db = "mw",
        use_unicode=True,
        charset = "utf8")
    return con

@inputweight_app.route("/inputweight", methods=["GET","POST"])
def inputweight():
    if request.method=="GET":
        print(session.keys())
        return render_template("inputweight.html")
    else:
        nowdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(nowdate)
        con = connect()
        cur = con.cursor()
        #datetimeの型がおかしい　要修正
        #print(type(session['email']))
        cur.execute(
            """
            INSERT INTO weight
            (user_id,date,weight)
            VALUES
            (%(user_id)s,%(date)s,%(weight)s)
            """,{"user_id":session['email'], "date": nowdate,"weight":request.form['weight']}
        )
        con.commit()
        con.close()
    return render_template("inputweightsuccess.html",
                           date=nowdate,
                           weight = request.form['weight']
                          )