# Alexandru Cimpoiesu (PM), Shafin Kazi, Mustafa Abdullah, Jalen Chen
# koalas
# SoftDev pd4
# p05
# 2026-06-01


from flask import Flask, render_template, request, session, redirect, url_for, flash
from auth import bp as auth_bp
import sqlite3, os, build_db, db

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.secret_key = "secretkey"
DB_FILE = "koalas.db"


@app.route("/")
def disp_homepage():
    session['username'] = 's'
    return render_template('home.html')

@app.route("/forum")
def disp_forum():
    return render_template("forum.html")

@app.route("/review")
def disp_review():
    return render_template("review.html")

if __name__ == "__main__":
    app.debug = False
    app.run()
