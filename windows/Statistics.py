from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import colors as c


def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'students.db')
    return sqlite3.connect(db_path)


def get_statistics():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM students")
        total_students = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(gpa) FROM students")
        avg_gpa = cursor.fetchone()[0]

        cursor.execute("SELECT MAX(gpa) FROM students")
        max_gpa = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT department) FROM students")
        total_departments = cursor.fetchone()[0]

        conn.close()

        return total_students, avg_gpa, max_gpa, total_departments

    except:
        messagebox.showerror("Error", "Failed to load statistics")
        return 0, 0, 0, 0


def stats_window():
    stats_win = Toplevel()
    stats_win.title("Statistics")
    stats_win.geometry("450x450")
    stats_win.configure(bg=c.BG)

    total, avg, max_gpa, depts = get_statistics()

    if avg is None:
        avg = 0

    Label(
        stats_win,
        text="Students Statistics",
        font=("Arial", 18, "bold"),
        bg=c.BG,
        fg=c.TEXT
    ).pack(pady=20)

    container = Frame(
        stats_win,
        bg=c.CARD,
        padx=20,
        pady=20,
        highlightbackground=c.BORDER,
        highlightthickness=1
    )
    container.pack(padx=30, pady=10, fill="both", expand=True)

    Label(container, text=f"Total Students: {total}", bg=c.CARD, fg=c.TEXT, font=("Arial", 12, "bold")).pack(pady=10, anchor="w")

    Label(container, text=f"Average GPA: {round(avg, 2)}", bg=c.CARD, fg=c.TEXT, font=("Arial", 12, "bold")).pack(pady=10, anchor="w")

    Label(container, text=f"Highest GPA: {max_gpa}", bg=c.CARD, fg=c.TEXT, font=("Arial", 12, "bold")).pack(pady=10, anchor="w")

    Label(container, text=f"Departments Count: {depts}", bg=c.CARD, fg=c.TEXT, font=("Arial", 12, "bold")).pack(pady=10, anchor="w")