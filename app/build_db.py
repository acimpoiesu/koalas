'''
Alexandru Cimpoiesu, Shafin Kazi, Mustafa Abdullah, Jalen Chen
koalas
SoftDev pd4
p05
06/01/26
'''


import sqlite3
from db import general_query, insert_query, select_query
import re
import json
import csv

CSV_PATH = '../sheet.csv'

def create_tables():
    general_query("DROP TABLE IF EXISTS Users;")
    general_query("DROP TABLE IF EXISTS Courses;")
    general_query("DROP TABLE IF EXISTS Reviews;")
    general_query("DROP TABLE IF EXISTS Schedules;")

    general_query("""
        CREATE TABLE IF NOT EXISTS Users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username     TEXT,
            password     TEXT,
            grad_year    INTEGER
        );
    """)

    general_query("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id          INTEGER PRIMARY KEY,
            course_code        TEXT,
            course_name        TEXT,
            course_subject     TEXT,
            prereqs            TEXT,
            course_description TEXT
        );
    """)

    general_query('''
        CREATE TABLE IF NOT EXISTS Reviews (
            id             INTEGER PRIMARY KEY,
            course_code    TEXT,
            name           TEXT,
            subject        TEXT,
            prereqs        TEXT,
            difficulty     INTEGER,
            workload_hours INTEGER,
            tags           TEXT,
            content        TEXT,
            comment_for    INTEGER
        );
    ''')

    general_query('''
        CREATE TABLE IF NOT EXISTS Schedules (
            id               INTEGER PRIMARY KEY,
            user_id          TEXT,
            course_id        TEXT,
            FOREIGN KEY (user_id) REFERENCES Users(id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );
    ''')

def parse_prereqs(req_string):
    if not req_string:
        return []
    reqs = []
    req_string = req_string.upper()
    grades = []
    if 'FRESHMEN' in req_string:
        grades.append(9)
    if 'SOPHOMORES' in req_string:
        grades.append(10)
    if 'JUNIORS' in req_string:
        grades.append(11)
    if 'SENIORS' in req_string:
        grades.append(12)
    if grades:
        reqs.append({"type": "grade_level", "allowed_grades": grades})
    passed_match = re.findall(r'PASSED\s+([A-Z0-9]+)', req_string)
    if passed_match:
        reqs.append({"type": "passed", "courses": passed_match})
    avg_match = re.search(r'AVG\s*?[>=]\s*?(\d+)', req_string)
    if avg_match:
        reqs.append({"type": "subject_avg", "min_grade": int(avg_match.group(1))})
    course_grade_match = re.search(r'(\d+)\+\s*IN\s*(.*)', req_string)
    if course_grade_match:
        reqs.append({"type": "course_grade", "min_grade": int(course_grade_match.group(1)), "course_name": course_grade_match.group(2).strip()})
    if not reqs:
        reqs.append({"type": "raw", "text": req_string.strip()})
    return reqs


def populate_courses(course_code, course_name, course_subject, prereqs, course_description):
    insert_query('Courses', {
        'course_code': course_code,
        'course_name': course_name,
        'course_subject': course_subject,
        'prereqs': prereqs,
        'course_description': course_description
    })

def populate_database():
    create_tables()
    populate_courses_csv(CSV_PATH)

#     for course in course_catalog:
#         populate_courses(
#             course_code=course['code'],
#             course_name=course['name'],
#             course_subject=course['subj'],
#             prereqs=json.dumps(course['reqs']),
#             course_description=(course['description'])
#
#         )

def populate_courses_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row['COURSE'].strip()
            name = row['TITLE'].strip().title()
            subject = row['DEPARTMENT'].strip()
            reqs = row['COURSE REQ (CATALOG)'].strip()
            description = row['DESCRIPTION'].strip()
            structured_prereqs = parse_prereqs(reqs)
            populate_courses(
                course_code = code,
                course_name = name,
                course_subject = subject,
                prereqs = json.dumps(structured_prereqs),
                course_description = description
            )

if __name__ == "__main__":
    populate_database()
