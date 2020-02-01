from tkinter import *


class Gui:
    def __init__(self, root):
        self.Root = root
        self.label = Label(root, text='Press the buttons.')
        self.label.pack()
        Button(self.Root, text='1', command=lambda: self.pressed(1)).pack(side=LEFT)
        Button(root, text='2', command=lambda: self.pressed(2)).pack()
        Button(root, text='3', command=lambda: self.pressed(3)).pack(side=RIGHT)

    def pressed(self, number):
        self.label.config(text=f'You have pressed Button {str(number)}.' )
        # same as above [self.label['text'] = 'You have pressed Button ' + str(number)]


root = Tk()
root.title("Hello! World")
root.configure(bg="dark blue")
gui = Gui(root)
root.mainloop()


#
import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None  # Instead of using "None", You can also use stings and numbers and "True", "False"
# You can also use "self.frame" instead because "_" just make the variable private
        self.switch_frame(Login)  # To call switch_frame function 'self.' needed as  you are in constructor

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Login(tk.Frame):
    def __init__(self, main_master):
        tk.Frame.__init__(self)
        tk.Label(self, text='This is the Login Page.').pack()
        tk.Button(self, text="Open Employee Page", command=lambda: main_master.switch_frame(Employee)).pack()
        tk.Button(self, text='Open Department Page', command=lambda: main_master.switch_frame(Department)).pack()
        tk.Button(self, text='Open College Page', command=lambda: main_master.switch_frame(College)).pack()


class Employee(tk.Frame):
    def __init__(self, master1):
        tk.Frame.__init__(self)
        tk.Label(self, text="This is Employee Page.").pack()
        tk.Button(self, text="Return to Login Page", command=lambda: master1.switch_frame(Login)).pack()


class Department(tk.Frame):
    def __init__(self, master2):
        tk.Frame.__init__(self)
        tk.Label(self, text="This is Department Page.").pack()
        tk.Button(self, text="Return to Login Page", command=lambda: master2.switch_frame(Login)).pack()


class College(tk.Frame):
    def __init__(self, master3):
        tk.Frame.__init__(self)
        tk.Label(self, text="This is College Page.").pack()
        tk.Button(self, text="Return to Login Page", command=lambda: master3.switch_frame(Login)).pack()


Calling = MainApp()
# Calling.switch_frame(Login) You can also call this function at last instead of calling in constructor
Calling.mainloop()




#
import tkinter as tk


class Controller(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.window = "Empty"

    def window_changer(self, window_name):
        if self.window is not "Empty":
            self.window.destroy()
        self.window = window_name(self)
        self.window.pack()


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        tk.Label(self, text="--Welcome to a new world where you can be anything you want--", font=("cooper black", 15, 'bold')).pack()
        tk.Button(self, text="I want to be Spider Man", bg="dark red", font=("Arial", 15, 'normal'), command=lambda: master.window_changer(IronMan)).pack()
        tk.Button(self, text="I want to be Super Man", bg='dark blue', font=("Arial", 15, 'normal'), command=lambda: master.window_changer(SuperMan)).pack()
        tk.Button(self, text="I want to be Pad Man", bg='dark green',font=("Arial", 15, 'normal'), command=lambda: master.window_changer(PadMan)).pack()
        tk.Button(self, text="I want to be surprised", font=("Arial", 15, 'normal'), command=lambda: master.window_changer(Surprise)).pack()


class IronMan(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        tk.Label(self, text="You are now Spider Man.Go, save the world.", font=("cooper black", 15, 'bold')).pack()
        tk.Button(self, text="I want to be another super hero.", font=("Arial", 15, 'normal'), command=lambda: master.window_changer(HomePage)).pack()


class SuperMan(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        tk.Label(self, text="You are now Super Man.Go, save the world.", font=("cooper black", 15, 'bold')).pack()
        tk.Button(self, text="I want to be another super hero.", font=("Arial", 15, 'normal'), command=lambda: master.window_changer(HomePage)).pack()


class PadMan(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        tk.Label(self, text="You are now Pad Man.Go, do something for the woman movement.", font=("cooper black", 15, 'bold')).pack()
        tk.Button(self, text="I want to be another super hero.", font=("Arial", 15, 'normal'), command=lambda: master.window_changer(HomePage)).pack()


class Surprise(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        tk.Label(self, text="Surprise ASSHOLE! You can not be any of the above super hero except for the Pad Man, Aahahaha.", font=("cooper black", 15, 'bold')).pack()
        tk.Button(self, text="Ok, i get it", font=("Arial", 15, 'normal'), command=lambda: master.window_changer(HomePage)).pack()


Call = Controller()
Call.window_changer(HomePage)
Call.mainloop()

