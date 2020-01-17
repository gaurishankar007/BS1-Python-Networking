from tkinter import *


class Gui:
    def __init__(self, root):
        self.root = Root
        self.label = Label(Root, text='Press the buttons.')
        self.label.pack()
        Button(self.root, text='1', command=lambda: self.pressed(1)).pack(side=LEFT)
        Button(Root, text='2', command=lambda: self.pressed(2)).pack()
        Button(Root, text='3', command=lambda: self.pressed(3)).pack(side=RIGHT)

    def pressed(self, number):
        self.label.config(text='You have pressed Button ' + str(number))
        # same as above [self.label['text'] = 'You have pressed Button ' + str(number)]


Root = Tk()
Root.title("Hello! World")
Root.configure(bg="dark blue")
gui = Gui(Root)
Root.mainloop()


#
import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='This is the Login Page.').pack()
        tk.Button(self, text="Open Employee Page", command=lambda: master.switch_frame(Employee)).pack()
        tk.Button(self, text='Open Department Page', command=lambda: master.switch_frame(Department)).pack()
        tk.Button(self, text='Open College Page', command=lambda: master.switch_frame(College)).pack()


class Employee(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Employee Page.").pack()
        tk.Button(self, text="Return to Login Page", command=lambda: master.switch_frame(Login)).pack()


class Department(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Department Page.").pack()
        tk.Button(self, text="Return to Login Page", command=lambda: master.switch_frame(Login)).pack()


class College(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is College Page.").pack()
        tk.Button(self, text="Return to Login Page", command=lambda: master.switch_frame(Login)).pack()


Calling = MainApp()
Calling.mainloop()

