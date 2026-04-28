from tkinter import *
from tkinter import ttk
import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'students.db')
    return sqlite3.connect(db_path)

def view_students_window():
    view_win = Toplevel()
    view_win.title("View Students")
    view_win.geometry("600x500")
    view_win.configure(bg="#F4F7FB")

    Label(
        view_win, 
        text="All Students", 
        font=("Arial", 18, "bold"), 
        bg="#F4F7FB", 
        fg="#2C3E50" 
    ).pack(pady=20)

    # Container for Treeview and Scrollbar
    container = Frame(view_win, bg="#FFFFFF", highlightbackground="#E1E8F0", highlightthickness=1)
    container.pack(padx=20, pady=10, fill="both", expand=True)

    scroll_y = Scrollbar(container, orient=VERTICAL)
    
    # Treeview styles
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", font=("Arial", 10), rowheight=25)

    columns = ("id", "name", "age", "department", "gpa")
    tree = ttk.Treeview(container, columns=columns, show="headings", yscrollcommand=scroll_y.set)
    scroll_y.config(command=tree.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    tree.heading("id", text="ID")
    tree.heading("name", text="Name")
    tree.heading("age", text="Age")
    tree.heading("department", text="Department")
    tree.heading("gpa", text="GPA")

    tree.column("id", width=50, anchor=CENTER)
    tree.column("name", width=180, anchor=W)
    tree.column("age", width=60, anchor=CENTER)
    tree.column("department", width=160, anchor=W)
    tree.column("gpa", width=60, anchor=CENTER)

    tree.pack(fill="both", expand=True)

    # Fetch Data
    def fetch_data():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", END, values=row)
            conn.close()
        except Exception as e:
            print("Error fetching data:", e)

    fetch_data()

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    view_students_window()
    root.mainloop()
