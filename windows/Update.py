from tkinter import *
from tkinter import messagebox
import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'students.db')
    return sqlite3.connect(db_path)

def update_student_window():
    update_win = Toplevel()
    update_win.title("Update Student")
    update_win.geometry("450x600")
    update_win.configure(bg="#F4F7FB")

    selected_student_id = [None]  # Use list to pass by reference

    def search_student():
        search_value = entry_search.get().strip()

        if not search_value:
            messagebox.showerror("Error", "Please enter a Student ID or Name!")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Try to search by ID if numeric
            if search_value.isdigit():
                cursor.execute("SELECT * FROM students WHERE id = ?", (int(search_value),))
            else:
                # Search by name (case-insensitive, partial match)
                cursor.execute("SELECT * FROM students WHERE LOWER(name) LIKE LOWER(?)", (f"%{search_value}%",))
            
            student = cursor.fetchone()
            conn.close()

            if not student:
                messagebox.showerror("Error", "Student not found!")
                entry_name.delete(0, END)
                entry_age.delete(0, END)
                entry_dept.delete(0, END)
                entry_gpa.delete(0, END)
                return

            selected_student_id[0] = student[0]
            entry_name.delete(0, END)
            entry_name.insert(0, student[1])
            entry_age.delete(0, END)
            entry_age.insert(0, str(student[2]))
            entry_dept.delete(0, END)
            entry_dept.insert(0, student[3])
            entry_gpa.delete(0, END)
            entry_gpa.insert(0, str(student[4]))

            messagebox.showinfo("Success", "Student found!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_student():
        if selected_student_id[0] is None:
            messagebox.showerror("Error", "Please search for a student first!")
            return

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
                "UPDATE students SET name = ?, age = ?, department = ?, gpa = ? WHERE id = ?",
                (name, int(age), dept, float(gpa), selected_student_id[0])
            )
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", f"Student {name} updated successfully!")
            update_win.destroy()

        except ValueError:
            messagebox.showerror("Error", "Age must be a number and GPA a decimal.")

    Label(
        update_win,
        text="Update Student Details",
        font=("Arial", 18, "bold"),
        bg="#F4F7FB",
        fg="#2C3E50"
    ).pack(pady=20)

    # Search Section
    search_frame = Frame(update_win, bg="#F4F7FB")
    search_frame.pack(padx=30, pady=10, fill="x")

    Label(search_frame, text="Search by ID or Name:", bg="#F4F7FB", fg="#2C3E50", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
    search_container = Frame(search_frame, bg="#F4F7FB")
    search_container.pack(fill="x", pady=5)

    entry_search = Entry(search_container, font=("Arial", 12), bd=1, relief="solid")
    entry_search.pack(side="left", fill="x", expand=True, ipady=3)

    Button(
        search_container,
        text="Search",
        bg="#27AE60",
        fg="white",
        font=("Arial", 10, "bold"),
        command=search_student,
        bd=0,
        cursor="hand2"
    ).pack(side="left", padx=(5, 0), ipadx=15, ipady=5)

    # Input Fields Section
    container = Frame(
        update_win,
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
        update_win,
        text="Update Student",
        bg="#4A90E2",
        fg="white",
        font=("Arial", 12, "bold"),
        command=update_student,
        bd=0,
        cursor="hand2"
    ).pack(pady=20, ipadx=40, ipady=5)


# if __name__ == "__main__":
#     root = Tk()
#     root.withdraw()
#     update_student_window()
#     root.mainloop()
