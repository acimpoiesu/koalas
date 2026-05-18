'''
Alexandru Cimpoiesu, Shafin Kazi, Mustafa Abdullah, Jalen Chen
koalas
SoftDev pd4
p05
06/01/26
'''


import sqlite3
from db import general_query, insert_query, select_query
import json
import csv

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
            prereqs            TEXT
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

    
# def populate_users(id, username, password, grad_year):
#     insert_query('Users',
#         "id":          null,
#         "username":    username,
#         "password":    password,
#         "grad_year":   grad_year
#     )
# 
# def populate_courses(course_id, course_code, course_name, course_subject, prereqs):
#     insert_query('Courses',
#         'course_id':    course_id,
#         'course_code':  course_code,
#         'course_name':  course_name,
#         'course_subject':    course_subject,
#         'prereqs':   ", ".join(prereqs) 
#     )
    
# def populate_reviews(id )
    
def populate_courses(course_code, course_name, course_subject, prereqs):
    insert_query('Courses', {
        'course_code': course_code,
        'course_name': course_name,
        'course_subject': course_subject,
        'prereqs': prereqs
    })

def populate_database():
    create_tables()
    populate_courses_csv('../sheet.csv')

    # temp data
    course_catalog = [
        {'code': 'EES81QFC', 'name': 'Fr composition 1', 'subj': 'English', 'reqs': ["Grade 9"]},
        {'code': 'EES83QEL', 'name': 'Foundations of lit 1', 'subj': 'English', 'reqs': ["passed EES81QFC", "taking EES82QFC"]},
        {'code': 'EES85QAM', 'name': 'American lit eng 5', 'subj': 'English', 'reqs': ["Grade 11"]},
        {'code': 'EES85QCN', 'name': 'Creative nonfiction eng5', 'subj': 'English', 'reqs': ["Grade 11"]},
        {'code': 'EES85QMC', 'name': 'Writing to make change eng5', 'subj': 'English', 'reqs': ["Grade 11"]},
        {'code': 'EES85QPW', 'name': 'Poetry eng5', 'subj': 'English', 'reqs': ["Grade 11"]},
        {'code': 'EES85QWW', 'name': 'Writers wksp eng5', 'subj': 'English', 'reqs': ["Grade 11"]},
        {'code': 'EES85X1', 'name': 'Ap eng lang - american literary history', 'subj': 'English', 'reqs': ["Grade 11", "English GPA >= 94"]},
        {'code': 'EES85X3', 'name': 'Ap eng lang - defining american voices', 'subj': 'English', 'reqs': ["Grade 11", "English GPA >= 94"]},
        {'code': 'EES85X7', 'name': 'Ap eng lang - contemporaries classics', 'subj': 'English', 'reqs': ["Grade 11", "English GPA >= 94"]},
        {'code': 'EES85XA', 'name': 'Ap eng lang - amer places & perspectives', 'subj': 'English', 'reqs': ["Grade 11", "English GPA >= 94"]},
        {'code': 'EES87CEE', 'name': 'Existentialism eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QCL', 'name': 'Eng7 climate literature', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QCN', 'name': 'Creative nonfiction eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QMC', 'name': 'Writing to make change eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QPW', 'name': 'Poetry eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QFS', 'name': 'Science fiction eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QWS', 'name': 'Shakespearean lit eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QWR', 'name': 'Writing in the world eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QWV', 'name': 'Womens voices eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87QWW', 'name': 'Writers wksp eng7', 'subj': 'English', 'reqs': ["Grade 12"]},
        {'code': 'EES87X3', 'name': 'Ap eng lit - great books', 'subj': 'English', 'reqs': ["Grade 12", "English GPA >= 92"]},
        {'code': 'EES87X5', 'name': 'Ap eng lit - society & self', 'subj': 'English', 'reqs': ["Grade 12", "English GPA >= 92"]},
        {'code': 'EES87XGP', 'name': 'Ap eng lit global perspectives', 'subj': 'English', 'reqs': ["Grade 12", "English GPA >= 92"]},
        {'code': 'MCS21X', 'name': 'Ap calc ab 1', 'subj': 'Math', 'reqs': ["Math GPA >= 88", "taking/passed MPS22", "NOT passed MCS43X"]},
        {'code': 'MCS43X', 'name': 'Ap calc bc 1', 'subj': 'Math', 'reqs': ["Math GPA >= 94 OR tag MCS43X_APPLY", "taking/passed MPS22"]},
        {'code': 'MSS21X', 'name': 'Ap stats 1', 'subj': 'Math', 'reqs': ["Math GPA >= 88", "taking/passed MPS22", "NOT taking MSS22X"]},
        {'code': 'SBS43X', 'name': 'Ap biology 3', 'subj': 'Science', 'reqs': ["Grade >= 11", "Science GPA >= 91 OR tag SBS43X_APPLY", "NOT passed SBS21X"]},
        {'code': 'SCS21X', 'name': 'Ap chemistry 1', 'subj': 'Science', 'reqs': ["Chemistry Grade >= 92", "NOT taking/passed SCS22X"]},
        {'code': 'SCS43X', 'name': 'Ap chemistry 3', 'subj': 'Science', 'reqs': ["Grade >= 11", "Science GPA >= 91"]},
        {'code': 'SPS21X', 'name': 'Ap physics 1', 'subj': 'Science', 'reqs': ["Physics Grade >= 90 OR tag SPS43X_APPLY"]},
        {'code': 'SPS43X', 'name': 'Ap phys c mech', 'subj': 'Science', 'reqs': ["Physics Grade >= 94", "Math GPA >= 94", "passed MCS21X OR MCS43X OR MCS65C"]},
        {'code': 'SQS21X', 'name': 'Ap psychology 1', 'subj': 'Science', 'reqs': ["Grade >= 11", "Science GPA >= 91", "NOT passed HBS21X"]},
        {'code': 'SQS85QJI', 'name': 'Junior Research', 'subj': 'Science', 'reqs': ["Grade 11", "Math GPA >= 91", "Science GPA >= 91"]},
        {'code': 'SQS87QJI', 'name': 'Regeneron', 'subj': 'Science', 'reqs': ["taking SBS86QJI OR SQS86QJI"]},
        {'code': 'SWS11QOC', 'name': 'Oceanography', 'subj': 'Science', 'reqs': ["Grade >= 11"]},
        {'code': 'MKS21X', 'name': 'Ap comp sci a 1 of 2', 'subj': 'Computer Science', 'reqs': ["CS Grade >= 85 (MKS21/QA) OR (taking MKS21 AND GPA >= 85 AND apply tag)", "NOT passed MKS21XH"]},
        {'code': 'MKS65C', 'name': 'System level programming', 'subj': 'Computer Science', 'reqs': ["taking/passed APCS (MKS21X/22X) OR SoftDev (MKS21QJI/43/44) OR Graphics (MKS66C) OR Cyber (MKS11QCY)"]}
    ]

    for course in course_catalog:
        populate_courses( 
            course_code=course['code'], 
            course_name=course['name'], 
            course_subject=course['subj'], 
            prereqs=json.dumps(course['reqs'])
        )

def populate_courses_csv(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row['COURSE'].strip()
            name = row['TITLE'].strip().title()
            subject = row['DEPARTMENT'].strip()
            reqs = row['COURSE REQ (CATALOG)'].strip()

            prereqs_list = [reqs] if reqs else []

            populate_courses(
                course_code = code,
                course_name = name,
                course_subject = subject,
                prereqs = json.dumps(prereqs_list)
            )

if __name__ == "__main__":
    populate_database()