from datetime import date
from re import template
from sqlite3 import connect
from flask import Flask,request,render_template,redirect,session
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from flask import Blueprint
import MySQLdb



outputweight_app = Blueprint("outputweight",__name__)


def connect():
    con = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd =  "ryo",
        db = "mw",
        use_unicode=True,
        charset = "utf8")
    return con

@outputweight_app.route("/outputweight", methods=["GET","POST"])
def outputweight():
    if request.method=='GET':
        user_id = session['email']
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT date, weight
                    FROM weight
                    WHERE user_id=%(user_id)s
                    """,{"user_id":user_id})
        data=[]
        for row in cur:
            print(row[0])
            data.append([row[0],row[1]])

        return render_template('outputweight.html',
                                user_id=user_id,
                                data=data)
    