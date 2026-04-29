from tkinter import *
from tkinter import ttk
import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'students.db')
    return sqlite3.connect(db_path)

def search_students_window():
    root = Toplevel()
    root.title("Students Search")
    root.geometry("")
    root.configure(padx=15, pady=15)

    top_frame = Frame(root)
    top_frame.pack(fill="x", pady=(45, 10))

    Label(top_frame, text="Search by:").pack(side=LEFT, padx=5)

    field_var = StringVar(value="name")

    for field in ["name", "id", "age", "department", "gpa"]:
        Radiobutton(
            top_frame,
            text=field.capitalize(),
            variable=field_var,
            value=field
        ).pack(side=LEFT, padx=3)

    Label(top_frame, text="Keyword:").pack(side=LEFT, padx=10)
    keyword_var = StringVar()
    keyword_entry = Entry(top_frame, textvariable=keyword_var, width=25)
    keyword_entry.pack(side=LEFT, padx=5)

    search_btn = Button(top_frame, text="Search")
    search_btn.pack(side=LEFT, padx=5)

    table_frame = Frame(root)
    table_frame.pack(fill="both", expand=True)

    columns = ("ID", "Name", "Age", "Department", "GPA")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    scrollbar = Scrollbar(table_frame, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    status_var = StringVar()
    Label(root, textvariable=status_var).pack(anchor="w", pady=5)

    def load_data():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, department, gpa FROM students")
        rows = cursor.fetchall()
        conn.close()

        for row in tree.get_children():
            tree.delete(row)
        for r in rows:
            tree.insert("", END, values=r)
        status_var.set(f"{len(rows)} record(s)")

    def search():
        keyword = keyword_var.get().strip()
        field = field_var.get()
        conn = get_db_connection()
        cursor = conn.cursor()

        if keyword == "":
            cursor.execute("SELECT id, name, age, department, gpa FROM students")
        else:
            numeric_fields = ["id", "age", "gpa"]
            if field in numeric_fields:
                try:
                    float(keyword)
                except:
                    status_var.set("Enter valid number")
                    return
                cursor.execute(
                    f"SELECT id, name, age, department, gpa FROM students WHERE {field}=?",
                    (keyword,)
                )
            else:
                cursor.execute(
                    f"SELECT id, name, age, department, gpa FROM students WHERE {field} LIKE ?",
                    (f"%{keyword}%",)
                )

        rows = cursor.fetchall()
        conn.close()

        for row in tree.get_children():
            tree.delete(row)
        for r in rows:
            tree.insert("", END, values=r)
        status_var.set(f"{len(rows)} result(s)")

    search_btn.config(command=search)
    keyword_entry.bind("<Return>", lambda e: search())

    load_data()

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    search_students_window()
    root.mainloop()