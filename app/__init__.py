# Alexandru Cimpoiesu (PM), Shafin Kazi, Mustafa Abdullah, Jalen Chen
# koalas
# SoftDev pd4
# p05
# 2026-06-01


from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
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
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT id, course_code, name, subject, difficulty, workload_hours, content FROM Reviews ORDER BY id DESC")
    cols = [d[0] for d in c.description]
    posts = [dict(zip(cols, row)) for row in c.fetchall()]
    db.close()
    return render_template("forum.html", posts=posts)
 

@app.route("/review", methods=["GET", "POST"])
def disp_review():
    if request.method == 'POST':
        course = request.form.get("course", "")
        subject = request.form.get("subject", "")
        difficulty = request.form.get("difficulty", 1)
        hours = request.form.get("hours", 0)
        desc = request.form.get("desc", "").strip()
        # print("course: " + course)
        # print("diff: " + str(difficulty))
        # print("hours: " + str(hours))
        # print("desc: " + desc)
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()

        c.execute("INSERT INTO Reviews (course_code, name, subject, difficulty, workload_hours, content) VALUES(?, ?, ?, ?, ?, ?)",
                                        (course, session['username'], subject, difficulty, hours, desc,))
        db.commit()
        db.close()
        flash('Review posted!', 'success')
    return render_template("review.html")
    

@app.route("/api/courses", methods=["GET"])
def get_courses():
    try:
        courses = db.select_query("SELECT * FROM Courses")
        return jsonify(courses)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    build_db.populate_database()
    app.debug = False
    app.run()
