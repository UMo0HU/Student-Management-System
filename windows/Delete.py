from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import colors as c

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'students.db')
    return sqlite3.connect(db_path)

def delete_student_window():
    delete_win = Toplevel()
    delete_win.title("Delete Student")
    delete_win.geometry("450x450")
    delete_win.configure(bg=c.BG)

    # Variable to store the selection (default to ID)
    delete_mode = StringVar(value="id")

    def execute_delete():
        selection = delete_mode.get()
        value = entry_value.get().strip()

        if not value:
            messagebox.showerror("Error", f"Please enter the Student {selection.upper()}.")
            return

        confirm = messagebox.askyesno("Confirm Deletion", f"Delete student where {selection} is '{value}'?")
        if not confirm:
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            if selection == "id":
                cursor.execute("DELETE FROM students WHERE id = ?", (value,))
            else:
                cursor.execute("DELETE FROM students WHERE name = ?", (value,))
            
            if cursor.rowcount > 0:
                conn.commit()
                messagebox.showinfo("Success", "Record deleted successfully!")
                delete_win.destroy()
            else:
                messagebox.showwarning("Not Found", f"No student found with that {selection}.")
            
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

    # UI Design
    Label(delete_win, text="Delete Student", font=("Arial", 18, "bold"), bg=c.BG, fg=c.TEXT).pack(pady=20)

    container = Frame(delete_win, bg=c.CARD, padx=20, pady=20, highlightbackground=c.BORDER, highlightthickness=1)
    container.pack(padx=30, pady=10, fill="both")

    Label(container, text="Delete By:", bg=c.CARD, fg=c.TEXT, font=("Arial", 10, "bold")).pack(anchor="w")

    # Selection Buttons
    radio_frame = Frame(container, bg=c.CARD)
    radio_frame.pack(fill="x", pady=10)

    Radiobutton(radio_frame, text="Student ID", variable=delete_mode, value="id", bg=c.CARD, font=("Arial", 10)).pack(side=LEFT, padx=10)
    Radiobutton(radio_frame, text="Student Name", variable=delete_mode, value="name", bg=c.CARD, font=("Arial", 10)).pack(side=LEFT, padx=10)

    Label(container, text="Enter Value:", bg=c.CARD, fg=c.TEXT, font=("Arial", 10, "bold")).pack(anchor="w", pady=(15, 0))
    
    entry_value = Entry(container, font=("Arial", 12), bd=1, relief="solid")
    entry_value.pack(fill="x", pady=5, ipady=3)

    Button(
        delete_win, 
        text="Confirm Delete", 
        bg=c.DANGER, 
        fg="white", 
        font=("Arial", 12, "bold"),
        command=execute_delete,
        bd=0,
        cursor="hand2"
    ).pack(pady=25, ipadx=40, ipady=5)