# NOTE:The every set of codes written below runs one after another that means other occurs after the first one finishes.
# Button:
import tkinter
BG = tkinter.Tk()
BG.title("Buhahaha Aahahaha")
button = tkinter.Button(BG, text='Suckers, hah!', height=10, width=20, background="yellow", foreground="Blue", command=BG.destroy)
button.pack()
BG.mainloop()

import tkinter as tk
A = tk.Tk()
A.title("Counting Seconds")  # The font size also effects the height and width of the button
button = tk.Button(A, text='Stop', height=15, width=25, activebackground="orange", activeforeground="red", font=("Arial", 10, 'bold'), command=A.destroy)  # the 'command=r.destroy' makes the visual disappeared
button.pack()
A.mainloop()


# Canvas:
from tkinter import *
M = Tk()
w = Canvas(M, height=60, width=40)
w.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()

from tkinter import *
S = Tk()
w = Canvas(S, height=600, width=400)
w.pack()
canvas_height = 550
canvas_width = 350
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()


# CheckButton
from tkinter import *
Master = Tk()
var1 = IntVar()
Checkbutton(Master, text='Male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(Master, text='Other', variable=var2, command=Master.destroy).grid(row=2)
var3 = IntVar()
Checkbutton(Master, text="Female", variable=var3, command=Master.destroy).grid(row=1, sticky=W)
mainloop()

from tkinter import *
Student = Tk()
S1 = IntVar()
Checkbutton(Student, text="Windows", variable=S1).grid(row=0, sticky=W)
S2 = IntVar()
Checkbutton(Student, text="Mac", variable=S2, command=Student.destroy).grid(row=0, column=1, sticky=W)
S3 = IntVar()
Checkbutton(Student, text="Linux", variable=S3, command=Student.destroy).grid(row=0, column=2)
S4 = IntVar()
Checkbutton(Student, text="Ios", variable=S4, command=Student.destroy).grid(row=1, column=1, sticky=W)
S5 = IntVar()
Checkbutton(Student, text="Android", variable=S5).grid(row=1, column=0)
mainloop()