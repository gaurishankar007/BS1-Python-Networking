from tkinter import *  # importing everything from the tkinter module

Expression = ''  # Globally declaring the expression variable


def click_number(number):  # A function to update the Expression in the text entry box
    global Expression   # pointing out the global expression variable
    Expression = Expression + str(number)  # Concatenating the Expression with the strings
    New_Expression1.set(Expression)  # Updating the Expression by set method


def click_equal():  # Try and except statement is used for handling the errors like zero division error etc.
    try:
        global Expression
        result = str(eval(Expression))  # eval function evaluates the expression into code
        # and returns the integer as a result and str function convert the result into string
        New_Expression2.set(result)
        Expression = ""  # initialize(Start the new value) the expression variable by empty string

    except:
        New_Expression2.set("Fuck you Invalid Input Aahaha!")
        Expression = ''  # initialize(Start the new value) the expression variable by empty string


def clear():  # Function to clear the contents of text entry box
    global Expression
    New_Expression1.set('')
    New_Expression2.set("")
    Expression = ""  # initialize(Start the new value) the expression variable by empty string


Cal = Tk()
Cal.title("Smart Calculator")
Cal.geometry('500x450')
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

New_Expression1 = StringVar()  # StringVar() is the variable class we create an instance of this class
# That means the str value of this variable can be changeable

Screen = Entry(Frm0, textvariable=New_Expression1, font=('Chiller', 38, 'bold'), bg='light blue', relief=GROOVE, border=0)
Screen.pack(expand=True, fill=BOTH)

New_Expression1.set("Start Calculating")

New_Expression2 = StringVar()

Result = Entry(Frm0, textvariable=New_Expression2, font=('Chiller', 38, 'bold'), bg='light green', relief=GROOVE, border=0)
Result.pack(expand=True, fill=BOTH)

N7 = Button(Frm2, text="7", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(7))
N7.pack(side=LEFT)
N8 = Button(Frm2, text="8", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(8))
N8.pack(side=LEFT)
N9 = Button(Frm2, text="9", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(9))
N9.pack(side=LEFT)
Add = Button(Frm2, text="+", height=3, width=12, activebackground="blue", activeforeground='white', font=('chiller', 15, 'bold'), command=lambda: click_number('+'))
Add.pack(side=LEFT)
Sub = Button(Frm2, text="-", height=3, width=12, activebackground='blue', activeforeground='white', font=('chiller', 15, 'bold'), command=lambda: click_number("-"))
Sub.pack(side=RIGHT)

N4 = Button(Frm3, text="4", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(4))
N4.pack(side=LEFT)
N5 = Button(Frm3, text="5", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(5))
N5.pack(side=LEFT)
N6 = Button(Frm3, text="6", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(6))
N6.pack(side=LEFT)
Mul = Button(Frm3, text="*", height=3, width=12, activebackground='blue', activeforeground='white', font=('chiller', 15, 'bold'), command=lambda: click_number('*'))
Mul.pack(side=LEFT)
Div = Button(Frm3, text="/", height=3, width=12, activebackground='blue', activeforeground='white', font=('chiller', 15, 'bold'), command=lambda: click_number("/"))
Div.pack(side=RIGHT)

N1 = Button(Frm4, text="1", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(1))
N1.pack(side=LEFT)
N2 = Button(Frm4, text="2", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(2))
N2.pack(side=LEFT)
N3 = Button(Frm4, text="3", height=3, width=12, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(3))
N3.pack(side=LEFT)
Equ = Button(Frm4, text='=', height=3, width=16, activebackground='blue', activeforeground='white', font=('Arial', 15, 'bold'), command=lambda: click_equal())
Equ.pack(side=RIGHT)


Zero = Button(Frm5, text="0", height=3, width=19, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number(0))
Zero.pack(side=LEFT)
Dut = Button(Frm5, text=".", height=3, width=17, activebackground='green', font=('chiller', 15, 'bold'), relief=GROOVE, border=0, command=lambda: click_number('.'))
Dut.pack(side=LEFT)
Clear = Button(Frm5, text="Clear", height=3, width=25, activebackground='red', activeforeground='white', font=('chiller', 15, 'bold'), command=lambda: clear())
Clear.pack(side=RIGHT)

mainloop()