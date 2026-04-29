from tkinter import *
import colors as c
from windows.Add import add_student_window
from windows.View import view_students_window
from windows.Delete import delete_student_window
from windows.Update import update_student_window
from windows.Search import search_students_window
from windows.Statistics import stats_window
import database

database.create_table()

root = Tk()
root.title("Student Management System")
root.geometry("500x400")

root.configure(bg=c.BG)


def open_window(window_func):
    root.withdraw()

    before = root.winfo_children()

    window_func()

    after = root.winfo_children()
    new_windows = [w for w in after if w not in before]

    if new_windows:
        win = new_windows[-1]

        win.protocol("WM_DELETE_WINDOW", win.destroy)
        win.bind("<Destroy>", lambda e: root.deiconify() if str(e.widget) == str(win) else None)

        btn = Button(
            win,
            text="Back",
            bg=c.PRIMARY,
            fg="white",
            font=("Arial", 16, "bold"),
            command=win.destroy,
            bd=0,
            cursor="hand2"
        )
        btn.place(x=4, y=15)
        btn.lift()


title = Label(
    root,
    text="Student Management System",
    font=("Arial", 20, "bold"),
    bg=c.BG,
    fg=c.TEXT
)
title.place(x=70, y=30)

card = Frame(root, bg=c.CARD, width=420, height=275,
             highlightbackground=c.BORDER, highlightthickness=1)
card.place(x=40, y=100)

btn1 = Button(card, text="Add Student", bg=c.PRIMARY, fg="white",
              font=("Arial", 12), width=15, bd=0,
              command=lambda: open_window(add_student_window))
btn1.place(x=30, y=30)

btn2 = Button(card, text="View Students", bg=c.PRIMARY, fg="white",
              font=("Arial", 12), width=15, bd=0,
              command=lambda: open_window(view_students_window))
btn2.place(x=220, y=30)

btn3 = Button(card, text="Update Student", bg=c.PRIMARY, fg="white",
              font=("Arial", 12), width=15, bd=0,
              command=lambda: open_window(update_student_window))
btn3.place(x=30, y=110)

btn4 = Button(card, text="Delete Student", bg=c.DANGER, fg="white",
              font=("Arial", 12), width=15, bd=0,
              command=lambda: open_window(delete_student_window))
btn4.place(x=220, y=110)

btn5 = Button(card, text="Search Student", bg=c.PRIMARY, fg="white",
              font=("Arial", 12), width=15, bd=0,
              command=lambda: open_window(search_students_window))
btn5.place(x=30, y=190)

btn6 = Button(card, text="Statistics", bg=c.PRIMARY, fg="white",
              font=("Arial", 12), width=15, bd=0,
              command=lambda: open_window(stats_window))
btn6.place(x=220, y=190)

root.mainloop()