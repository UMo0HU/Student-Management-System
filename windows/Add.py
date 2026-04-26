from tkinter import *
from tkinter import messagebox
import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'students.db')
    return sqlite3.connect(db_path)

def add_student_window():
    add_win = Toplevel()
    add_win.title("Add New Student")
    add_win.geometry("450x500")
    add_win.configure(bg="#F4F7FB") 

    def save_student():
        name = entry_name.get()
        age = entry_age.get()
        dept = entry_dept.get()
        gpa = entry_gpa.get()

        if not (name and age and dept and gpa):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, age, department, gpa) VALUES (?, ?, ?, ?)",
                (name, int(age), dept, float(gpa))
            )
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            add_win.destroy() 
            
        except ValueError:
            messagebox.showerror("Error", "Age must be a number and GPA a decimal.")

   
    Label(
        add_win, 
        text="Add Student Details", 
        font=("Arial", 18, "bold"), 
        bg="#F4F7FB", 
        fg="#2C3E50" 
    ).pack(pady=20)

    container = Frame(
        add_win, 
        bg="#FFFFFF", 
        padx=20, 
        pady=20, 
        highlightbackground="#E1E8F0", 
        highlightthickness=1
    )
    container.pack(padx=30, pady=10, fill="both", expand=True)

    def create_input(label_text):
        Label(container, text=label_text, bg="#FFFFFF", fg="#2C3E50", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
        entry = Entry(container, font=("Arial", 12), bd=1, relief="solid")
        entry.pack(fill="x", pady=5, ipady=3)
        return entry

    entry_name = create_input("Full Name:")
    entry_age = create_input("Age:")
    entry_dept = create_input("Department:")
    entry_gpa = create_input("GPA:")

    Button(
        add_win, 
        text="Save Student", 
        bg="#4A90E2", 
        fg="white", 
        font=("Arial", 12, "bold"),
        command=save_student,
        bd=0,
        cursor="hand2"
    ).pack(pady=20, ipadx=40, ipady=5)


if __name__ == "__main__":
    root = Tk()
    root.withdraw() 
    add_student_window()
    root.mainloop()