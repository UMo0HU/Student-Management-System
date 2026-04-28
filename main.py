from tkinter import *
import colors as c
from windows.Add import add_student_window
from windows.View import view_students_window
from windows.Delete import delete_student_window
import database

database.create_table()

root = Tk()
root.title("Student Management System")
root.geometry("500x400")

root.configure(bg=c.BG)

title = Label(
    root,
    text="Student Management System",
    font=("Arial", 20, "bold"),
    bg=c.BG,
    fg=c.TEXT
)
title.place(x=70, y=30)

card = Frame(root, bg=c.CARD, width=420, height=275, highlightbackground=c.BORDER, highlightthickness=1)
card.place(x=40, y=100)

btn1 = Button(card, text="Add Student", bg=c.PRIMARY, fg="white", font=("Arial", 12), width=15, bd=0, command=add_student_window)
btn1.place(x=30, y=30)

btn2 = Button(card, text="View Students", bg=c.PRIMARY, fg="white", font=("Arial", 12), width=15, bd=0, command=view_students_window)
btn2.place(x=220, y=30)

btn3 = Button(card, text="Update Student", bg=c.PRIMARY, fg="white", font=("Arial", 12), width=15, bd=0)
btn3.place(x=30, y=110)

btn4 = Button(
    card, 
    text="Delete Student", 
    bg=c.DANGER, 
    fg="white", 
    font=("Arial", 12), 
    width=15, 
    bd=0, 
    command=delete_student_window 
)
btn4.place(x=220, y=110)

btn5 = Button(card, text="Search Student", bg=c.PRIMARY, fg="white", font=("Arial", 12), width=15, bd=0)
btn5.place(x=30, y=190)

btn6 = Button(card, text="Statistics", bg=c.PRIMARY, fg="white", font=("Arial", 12), width=15, bd=0)
btn6.place(x=220, y=190)

root.mainloop()