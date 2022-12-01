# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,redirect,session,Blueprint,jsonify
from sqlite3 import connect
import MySQLdb
import html
from datetime import timedelta



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
def users():
    if "age" in session:
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
            print(type(row[3]))
            
        con.close()
        return jsonify(res)
    else:
        return "Session is invalid"

@api_app.route("/api/users_weight")
def weights():
    if "age" in session:
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT user_id,date,weight
                    FROM weight
                    """)
        res = {"users_weight":[]}
        for row in cur:
            weight = {"id":row[0],
                    "date":row[1],
                    "weight":row[2],
                    }
            res["users_weight"].append(weight)
        con.close()

        return jsonify(res)
    else:
        return "Session is invalid"

@api_app.route("/api/users_data")
def users_data():
    if "age" in session:
        res = {"users":[]}

        con = connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT age,id,height,sex
                    FROM user
                    """)
        for row in cur:
            print(row)
            user = {}
            user["id"] = row[1]
            user["age"] = row[0]
            user["height"] = row[2]
            user["sex"] = row[3]
            user["weight"] = []
            res["users"].append(user)

        cur.execute("""
                    SELECT user_id,date,weight
                    FROM weight
                    """)
        #userリストを作る
        users = []
        for user in res["users"]:
            users.append(user["id"])
        
        for row in cur:
            i = users.index(row[0])
            weight = {"date":row[1],
                    "weight":row[2]}
            res["users"][i]["weight"].append(weight)

        return res
    else:
        return "Session is invalid"

