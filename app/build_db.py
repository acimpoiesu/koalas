'''
Alexandru Cimpoiesu, Shafin Kazi, Mustafa Abdullah, Jalen Chen
koalas
SoftDev pd4
p05
06/01/26
'''
#
# import sqlite3, csv, os, sys
#
# CSV_FILE_PATH = None
# DB_FILE_PATH = 'koalas.db'
#
# def create_database(table_name):
#     db = sqlite3.connect(DB_FILE_PATH)
#     cursor = db.cursor()
#
#         table_query = f'''
#         CREATE TABLE IF NOT EXISTS {table_name} (
#             id INTEGER,
#             user TEXT,
#             pass TEXT,
#             grad_year INTEGER
#         )
#         '''
#         cursor.execute(table_query)
#
#         if not os.path.exists(CSV_FILE_PATH):
#             print(f"could not find {CSV_FILE_PATH}")
#             return
#
#         print(f"currently reading from {CSV_FILE_PATH}")
#
#         with open (CSV_FILE_PATH, mode = "r", encoding="utf-8") as csv_file:
#             csv_file = csv.reader(csv_file)
#             next(csv_file, None)
#             insert_query = f'''
#             INSERT INTO {table_name} (
#             id, user, pass, grad_year
#             ) VALUES (?, ?, ?, ?)
#             '''
#         row_count = 0
#         for row in csv_file:
#             try:
#                 cursor.execute(insert_query, row)
#             except:
#                 print(f"failed on row {row_count}")
#                 sys.exit(1)
#             row_count += 1
#     db.commit()
#     db.close()
#
#     print(f"finished reading")
#
# if __name__ == "__main__":
#     create_database(users)

import sqlite3
from db import general_query, insert_query, select_query


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
    

    
create_tables()
