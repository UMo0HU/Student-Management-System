import sqlite3

def connect():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        gpa REAL
    )
    """)
    conn.commit()
    conn.close()