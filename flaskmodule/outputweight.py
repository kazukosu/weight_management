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
    