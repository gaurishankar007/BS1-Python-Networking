from tkinter import *
Boss = Tk()
Boss.title('Give your name and contact number one by one, hahahahahaha!')
Boss.geometry("")
Boss.configure(bg="dark green")

Name = Label(Boss, text='Full Name').pack()
Number = Label(Boss, text='Contact Number').pack()
Display = Label(Boss, text='', fg='dark red', font=("Chiller", 20, "bold"))  # You can not add ".pack()" here because the text of this label is going to change
Display.pack(expand=True, fill=BOTH)

Room = Frame(Boss)
Room.pack()
Name_Entry = Entry(Room)
Name_Entry.pack()
Number_Entry = Entry(Room)
Number_Entry.pack()


def display():
    Display.configure(text=f' Welcome! {Name_Entry.get()}. Your Contact Number is {Number_Entry.get()}.Hands up, you are under arrest.')


def write():
    Text_File = open('Information.txt', '+w')
    Text_File.write(f' Your name is {Name_Entry.get()} and Contact Number is {Number_Entry.get()}.')



def read():
    Text_File = open('Information.txt', 'r')
    Display.configure(text=Text_File.readline())  # readline() works here same as the read()


btn = Button(Boss, text='Submit', command=display).pack(expand=True, fill=BOTH)
wbtn = Button(Boss, text='Write', command=write).pack(expand=False, fill=BOTH)
rbtn = Button(Boss, text='Read', command=read).pack()
mainloop()
