# Alexandru Cimpoiesu (PM), Shafin Kazi, Mustafa Abdullah, Jalen Chen
# koalas
# SoftDev pd4
# p05
# 2026-06-01


from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from auth import bp as auth_bp
import sqlite3, os, json, build_db, db

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.secret_key = "secretkey"
DB_FILE = "koalas.db"
SERVER_ERROR = 500


@app.route("/")
def disp_homepage():
    session['username'] = 's'
    return render_template('home.html')

@app.route("/forum")
def disp_forum():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT id, course_code, name, subject, difficulty, workload_hours, content FROM Reviews WHERE comment_for IS NULL ORDER BY id DESC")
    cols = [d[0] for d in c.description]
    posts = [dict(zip(cols, row)) for row in c.fetchall()]

    for post in posts:
        c.execute("SELECT id, name, content FROM Reviews WHERE comment_for = ? ORDER BY id DESC LIMIT 3", (post['id'],))
        comment_cols = [d[0] for d in c.description]
        post['top_comments'] = [dict(zip(comment_cols, row)) for row in c.fetchall()]

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

        c.execute("SELECT 1 FROM Courses WHERE course_code = ?", (course,))
        if not c.fetchone():
            c.close()
            flash('Please enter a valid course code.', 'error')
        else:
            c.execute("INSERT INTO Reviews (course_code, name, subject, difficulty, workload_hours, content) VALUES(?, ?, ?, ?, ?, ?)",
                                            (course, session['username'], subject, difficulty, hours, desc,))
            db.commit()
            db.close()
            flash('Review posted!', 'success')
    return render_template("review.html")

@app.route("/forum/<int:review_id>", methods=["GET", "POST"])
def disp_forum_detail(review_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT id, course_code, subject FROM Reviews WHERE id = ?", (review_id,))
    parent = c.fetchone()
    if not parent:
        db.close()
        flash('Post not found.', 'error')
        return redirect(url_for('disp_forum'))

    if request.method == 'POST':
        content = request.form.get("content", "").strip()
        if not content:
            flash('Comment cannot be empty.', 'error')
        else:
            parent_course_code, parent_subject = parent[1], parent[2]
            c.execute("INSERT INTO Reviews (course_code, name, subject, content, comment_for) VALUES (?, ?, ?, ?, ?)",
                                            (parent_course_code, session.get('username'), parent_subject, content, review_id))
            db.commit()
            flash('Comment posted!', 'success')

    c.execute("SELECT id, course_code, name, subject, difficulty, workload_hours, content, comment_for FROM Reviews WHERE id = ?", (review_id,))
    cols = [d[0] for d in c.description]
    row = c.fetchone()
    post = dict(zip(cols, row))

    c.execute("SELECT id, course_code, name, subject, difficulty, workload_hours, content, comment_for FROM Reviews WHERE comment_for = ? ORDER BY id ASC", (review_id,))
    cols = [d[0] for d in c.description]
    comments = [dict(zip(cols, row)) for row in c.fetchall()]

    for comment in comments:
        c.execute("SELECT id, name, content FROM Reviews WHERE comment_for = ? ORDER BY id DESC LIMIT 3", (comment['id'],))
        reply_cols = [d[0] for d in c.description]
        comment['top_replies'] = [dict(zip(reply_cols, row)) for row in c.fetchall()]

    db.close()
    return render_template("forum_detail.html", post=post, comments=comments)


@app.route("/courses")
def disp_courses():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM Courses ORDER BY course_subject, course_name")
    cols = [d[0] for d in c.description]
    courses = [dict(zip(cols, row)) for row in c.fetchall()]
    db.close()
    return render_template("courses.html", courses=courses)

@app.route("/courses/<int:course_id>")
def disp_course(course_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM Courses WHERE course_id = ?", (course_id,))
    cols = [d[0] for d in c.description]
    row = c.fetchone()
    db.close()
    if not row:
        flash("Course not found", "error")
        return redirect(url_for("disp_courses"))
    course = dict(zip(cols, row))
    prereqs = json.loads(course['prereqs']) if course.get('prereqs') else []
    return render_template("course.html", course=course, prereqs=prereqs)


@app.route("/api/courses", methods=["GET"])
def get_courses():
    try:
        courses = db.select_query("SELECT * FROM Courses")
        return jsonify(courses)
    except Exception as e:
        return jsonify({"error": str(e)}), SERVER_ERROR

@app.route("/prereqs")
def disp_prereq_graph():
    return render_template('prereqs.html')

@app.route("/planner")
def disp_planner():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM Courses ORDER BY course_subject, course_code")
    cols = [d[0] for d in c.description]
    courses = [dict(zip(cols, row)) for row in c.fetchall()]
    db.close()
    return render_template("planner.html", courses=courses)

if __name__ == "__main__":
    build_db.populate_database()
    app.debug = False
    app.run()