# NOTE:The every set of codes written below runs one after another that means other occurs after the first one finishes.
# 1)Button:
import tkinter
BG = tkinter.Tk()
BG.title("Buhahaha Aahahaha")
btn = tkinter.Button(BG, text='Suckers, hah!', height=10, width=20, background="yellow", foreground="Blue", command=BG.destroy)
btn.pack()
BG.mainloop()

import tkinter as tk
A = tk.Tk()
A.title("Counting Seconds")  # The font size also effects the height and width of the button
button = tk.Button(A, text='Stop', height=15, width=25, activebackground="orange", activeforeground="red", font=("Arial", 10, 'bold'), command=A.destroy)  # the 'command=r.destroy' makes the visual disappeared
button.pack()
A.mainloop()




# 2)Canvas:
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

from tkinter import *
Disaster = Tk()
w = Canvas(Disaster, height=400, width=700)
w.pack()
a = 200
b = 500
x = int(a / 2)
w.create_line(20, x, b, x)
w.create_rectangle(5, 10, 50, 75, fill='red')
w.create_oval(100, 20, 25, 55)
mainloop()




# 3)CheckButton:
from tkinter import *
Master = Tk()
var1 = IntVar()
Checkbutton(Master, text='Male', variable=var1, activebackground="yellow", activeforeground='red', font=("Arial", 10, 'bold')).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(Master, text='Other', variable=var2, command=Master.destroy).grid(row=2)
var3 = IntVar()
Checkbutton(Master, text="Female", variable=var3, background="pink", foreground="blue", font=("Arial Black", 12, "normal"), command=Master.destroy).grid(row=1, sticky=W)
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




# 4,5)Entry and Label:
from tkinter import *
Master = Tk()
Label(Master, text='First Name =').grid(row=0, sticky=W)
Label(Master, text='Middle Name =').grid(row=1)
Label(Master, text='Last Name =').grid(row=2, sticky=W)
E1 = Entry(Master, foreground="green", font=("cooper black", 10, 'normal'))
E2 = Entry(Master, background='orange', font=("cooper black", 10, 'normal'))
E3 = Entry(Master, bg='yellow', fg='blue', font=("cooper black", 10, 'normal'))


def change_text():
    print("First Name= %s \n Middle Name= %s \n Last Name= %s" % (E1.get(), E2.get(), E3.get()))
    replace = str(f"{E1.get()} {E2.get()} {E3.get()} ")
    New_Label['text'] = replace


BTN = Button(Master, text='Display', height=2, width=10, font=("Arial", 10, 'bold'), command=change_text)
New_Label = Label(Master, fg="red", text='This is a sample text.', font=('chiller', 15, 'bold'))
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
BTN.grid(row=3, column=1)
New_Label.grid(row=4, column=1)
mainloop()



# Printing the sum of two numbers taken from the users
from tkinter import *
Sum = Tk()
Leb1 = Label(Sum, text="First Number=")
Leb2 = Label(Sum, text="Second Number=")
E1 = Entry(Sum)
E2 = Entry(Sum)

def Sums():
    replace = str(f"{int(E1.get()) + int(E2.get())}")
    leb['text'] = replace


But = Button(Sum, text='Sum', fg="Blue", font=('cooper black', 15, 'normal'), command=Sums)
leb = Label(Sum, text='')
Leb1.grid(row=0, column=0)
Leb2.grid(row=1, column=0)
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
But.grid(row=2, column=1)
leb.grid(row=3, column=1)
mainloop()



# Printing Random numbers between 1 to 6
from tkinter import *
Ran = Tk()



def Rand():
    from random import randint
    replace = str(f"{randint(1,6)}")
    leb['text'] = replace


But = Button(Ran, text='Print Random', fg="green", font=('cooper black', 15, 'normal'), command=Rand)
leb = Label(Ran, text='')
But.grid(row=0)
leb.grid(row=1)
mainloop()




# Message_box
#
from tkinter import *
from tkinter import messagebox
Top = Tk()


def hello_call_back():
    messagebox.showinfo("Hello Python", "Hello World")


def show_text():
    label = Label(Top, fg='green', text='This is a sample text.')
    label.pack()


B = Button(Top, text='Hello', font=("Cooper Black", 15, "bold"), command=hello_call_back)
B1 = Button(Top, text='Destroy Button', width=25, command=Top.destroy)
B2 = Button(Top, text="Write in label.", command=show_text)
B.pack()
B1.pack()
B2.pack()
mainloop()




#
from tkinter import *
from tkinter import messagebox
Hah = Tk()


def msb():
    messagebox.showinfo("Yes!", "Surprise MotherFather!")


But = Button(Hah, text="Hey, Press here", font=("chiller", 20, "bold"), command=msb)
But.pack()
But.mainloop()




#
from tkinter import *
what = Tk()


def db1():
    exchange = "Clicked 1"
    Lab['text'] = exchange
    b4['text'] = exchange


def db2():
    exchange = "Clicked 2"
    Lab['text'] = exchange
    b4['text'] = exchange


def db3():
    exchange = "Clicked 3"
    Lab['text'] = exchange
    b4['text'] = exchange


b1 = Button(what, text="1", font=('Arial', 20, 'bold'), command=db1)
b2 = Button(what, text="2", font=('Arial', 20, 'bold'), command=db2)
b3 = Button(what, text="3", font=('Arial', 20, 'bold'), command=db3)
Lab = Label(what, text='click any of the number', font=("chiller", 18, 'bold'))
b4 = Button(what, text="Empty", fg='red', font=("cooper black", 15, "normal"))
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
Lab.grid(row=0, column=1)
b4.grid(row=2, column=1)
mainloop()


# 6)Frame:
from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=TOP)  # Also bottom_frame.pack(side=TOP)
red_button = Button(frame, text="Red", fg='red')
red_button.pack(side=LEFT)
green_button = Button(frame, text='Green', fg='green')
green_button.pack(side=LEFT)
blue_button = Button(frame, text='Blue', fg='blue')
blue_button.pack(side=LEFT)
black_button = Button(bottom_frame, text='Black', fg="black")
black_button.pack(side=BOTTOM)  # Also black_button.pack(side=TOP,RIGHT,LEFT)
root.mainloop()  # Same as mainloop()



from tkinter import *
Frm = Tk()
First_frame = Frame(Frm)
First_frame.pack()
Second_frame = Frame(Frm)
Second_frame.pack(side=BOTTOM)
Blue_button = Button(First_frame, height=15, width=20, text='Blue', fg='blue')
Blue_button.pack(side=LEFT)
Green_button = Button(First_frame, text="Green", fg='green', height=10, width=15)
Green_button.pack(side=LEFT)
Yellow_button = Button(First_frame, text="Yellow", fg='yellow', height=10, width=15)
Yellow_button.pack(side=LEFT)
Red_button = Button(First_frame, text='Red', fg='red', height=15, width=20)
Red_button.pack(side=RIGHT)
Orange_button = Button(First_frame, text='Orange', fg='orange', height=10, width=15)
Orange_button.pack(side=RIGHT)
Pink_button = Button(First_frame, text="Pink", fg='pink', height=10, width=15)
Pink_button.pack(side=RIGHT)
Black_button = Button(Second_frame, text='Black', height=15, width=20)
Black_button.pack()
mainloop()



# Creating Calculator design
from tkinter import *
Cal = Tk()
Frm0 = Frame()
Frm0.pack()
Frm1 = Frame(Cal)
Frm1.pack()
Frm2 = Frame(Cal)
Frm2.pack()
Frm3 = Frame(Cal)
Frm3.pack()
Frm4 = Frame(Cal)
Frm4.pack()
Frm5 = Frame(Cal)
Frm5.pack(side=TOP)

Screen = Label(Frm0, text='', font=('Chiller', 15, 'bold'))
Screen.pack()

Result = Label(Frm1, text='', font=('chiller', 25, 'bold'))
Result.pack()

N7 = Button(Frm2, text="7", height=5, width=5, bg='red', font=('cooper black', 15, 'bold'))
N7.pack(side=LEFT)
N8 = Button(Frm2, text="8", height=5, width=5, bg='blue', font=('cooper black', 15, 'bold'))
N8.pack(side=LEFT)
N9 = Button(Frm2, text="9", height=5, width=5, bg='green', font=('cooper black', 15, 'bold'))
N9.pack(side=LEFT)
Add = Button(Frm2, text="+", height=5, width=5, font=('cooper black', 15, 'bold'))
Add.pack(side=LEFT)
Sub = Button(Frm2, text="-", height=5, width=5, font=('cooper black', 15, 'bold'))
Sub.pack(side=RIGHT)

N4 = Button(Frm3, text="4", height=5, width=5, bg='orange', font=('cooper black', 15, 'bold'))
N4.pack(side=LEFT)
N5 = Button(Frm3, text="5", height=5, width=5, bg='pink', font=('cooper black', 15, 'bold'))
N5.pack(side=LEFT)
N6 = Button(Frm3, text="6", height=5, width=5, bg='brown', font=('cooper black', 15, 'bold'))
N6.pack(side=LEFT)
Mul = Button(Frm3, text="*", height=5, width=5, font=('cooper black', 15, 'bold'))
Mul.pack(side=LEFT)
Div = Button(Frm3, text="/", height=5, width=5, font=('cooper black', 15, 'bold'))
Div.pack(side=RIGHT)

N1 = Button(Frm4, text="1", height=5, width=5, bg='yellow', font=('cooper black', 15, 'bold'))
N1.pack(side=LEFT)
N2 = Button(Frm4, text="2", height=5, width=5, bg='red', font=('cooper black', 15, 'bold'))
N2.pack(side=LEFT)
N3 = Button(Frm4, text="3", height=5, width=5, bg='blue', font=('cooper black', 15, 'bold'))
N3.pack(side=LEFT)
Equ = Button(Frm4, text='=', height=5, width=13, font=('Arial', 14, 'bold'))
Equ.pack(side=RIGHT)

Zero = Button(Frm5, text="0", height=5, bg='green',width=20, font=('cooper black', 15, 'bold'))
Zero.pack(side=LEFT)
Dut = Button(Frm5, text=".", height=5, width=7, font=('cooper black', 15, 'bold'))
Dut.pack(side=RIGHT)

mainloop()
