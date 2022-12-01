from flask import Flask,request,render_template,redirect,session,Blueprint
from sqlite3 import connect
import MySQLdb
import html



api_app = Blueprint("api",__name__)


def connect():
    con = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd =  "ryo",
        db = "mw",
        use_unicode=True,
        charset = "utf8")
    return con

@api_app.route("/api/users", methods=["GET"])
def inputweight():
    con = connect()
    cur = con.cursor()
    cur.execute("""
                SELECT age,id,height,sex
                FROM user
                """)
    res = {"users":[]}
    for row in cur:
        user = {"id":row[1],
                "age":row[0],
                "height":row[2],
                "sex":row[3]}
        res["users"].append(user)
        
    con.close()
    return res