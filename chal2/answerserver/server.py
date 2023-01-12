from flask import Flask
from flask import request
from flask import render_template, make_response, redirect
import random
import string

app = Flask(__name__)

admin_pwd = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

@app.route("/")
def index():
    resp = make_response(render_template("index.html"))
    resp.set_cookie('admin', b"0")
    return resp


@app.route("/login", methods = ['POST'])
def login():
    if "user" not in request.form or "password" not in request.form:
        return redirect("/")
    user = request.form['user']
    password = request.form['password']
    resp = make_response(render_template("index.html"))
    if user == "admin" and password == admin_pwd:
        resp.set_cookie('admin', b"1")
    return resp


@app.route("/admin")
def admin():
    admin = request.cookies.get('admin')
    if admin:
        return render_template("flag.html")
    return redirect("/")

