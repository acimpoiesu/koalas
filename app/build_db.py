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

DB_FILE = "koalas.db"

db = sqlite3.connect(DB_FILE)
cursor = db.cursor()

cursor.executescript(
    """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    );
    """
)

db.commit()
db.close()
