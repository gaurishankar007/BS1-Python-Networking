import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Assigning a string variable for making it global
Name = ""  # for employee name
Email = ""  # for employee email


# Creating The Main Constructor that means the main tkinter Window through which other pages appears as Frames
class EMP(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Employee Management System')
        self.configure(bg="dark orange")
        self.Page = None
        self.switch_page(HomePage)  # Popping up the Homepage at first

    # Creating Frame Switcher that means page switcher
    def switch_page(self, page_name):
        if self.Page is not None:  # Destroying the previous Page before jumping to another if it exits.
            self.Page.destroy()
        self.Page = page_name(self)
        self.Page.pack()  #  Packing the new page


# Creating HomePage of the Employee Management System
class HomePage(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)

        # Creating Labels for heading
        tk.Label(self, text='             ', bg='dark orange', font=('Arial', 20, 'bold')).grid(row=0, column=0)
        tk.Label(self, text='Welcome To NIT College Employee Page', font=('Arial', 20, 'bold'), fg='Black', bg='dark orange').grid(row=0, column=1)
        tk.Label(self, text='             ', bg='dark orange', font=('Arial', 20, 'bold')).grid(row=0, column=2)
        tk.Label(self, text='             ').grid(row=1, column=0)

        # Creating Buttons for "SignIn", "Register" and "Exit"
        self.BS = tk.Button(self, text='SignIn', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(SignInPage))
        self.BS.grid(row=2, column=1)
        tk.Label(self, text='             ').grid(row=3, column=0)

        tk.Label(self, text="If you don't have an account, register please!", font=('Arial', 15, 'bold'), fg="black").grid(row=4, column=1)
        self.BR = tk.Button(self, text='Register', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(RegisterPage))
        self.BR.grid(row=5, column=1)
        tk.Label(self, text='             ').grid(row=6, column=0)

        self.BE = tk.Button(self, text="Exit", height=2, width=10, bg="#2E026C", fg="white", font=("Arial", 10, 'bold'), command=access.destroy)
        self.BE.grid(row=7, column=1)
        tk.Label(self, text='             ').grid(row=8, column=0)


# Creating Signing Page for the employees and the administrator
class SignInPage(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)
        self.accessing = access

        # Creating Labels for Heading
        tk.Label(self, text='                                 ').grid(row=0, column=0)
        tk.Label(self, text='Sign in page', font=('Arial', 20, 'bold'), fg='dark blue').grid(
            row=0, column=1)
        tk.Label(self, text='                                 ').grid(row=1, column=2)

        # Creating Labels along with Entries For Email and Password
        tk.Label(self, text="Email:", font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky=E)
        self.EE = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EE.grid(row=2, column=1, sticky=W)

        tk.Label(self, text='Password:', font=('Arial', 12, 'bold')).grid(row=4, column=0, sticky=E)
        self.EP = tk.Entry(self, textvariable='', show='*', width=60, bg='orange')
        self.EP.grid(row=4, column=1, sticky=W)

        # Creating Buttons for "Login", "Back" and Buttons to go to directly to Registration page for those who haven't registered yet
        self.BL = tk.Button(self, text='Login', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: self.read())
        self.BL.grid(row=5, column=1)
        tk.Label(self, text='                                 ').grid(row=6, column=0)

        self.BB = tk.Button(self, text='Back', height=1, width=10, bg="dark green", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(HomePage))
        self.BB.grid(row=7, column=1)
        tk.Label(self, text='                                 ').grid(row=8, column=0)

        tk.Label(self, text="Don't have an account!", fg='dark red', font=('chiller', 18, 'normal')).grid(row=9, column=2)
        self.BR = tk.Button(self, text="Click Here", height=1, width=10, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), relief=GROOVE, border=0, command=lambda: access.switch_page(RegisterPage))
        self.BR.grid(row=10, column=2)
        tk.Label(self, text='                                 ').grid(row=11, column=0)

    # Creating function to check whether the entered email and password is correct or not and if correct then login in the related page
    def read(self):
        try:  # If email is correct
            global Name
            global Email
            text_file = open(f"{self.EE.get()}.txt", 'r')
            reading1 = text_file.readlines()  # Reading user data
            reading2 = ("".join(reading1)).split()  # Joining the items of reading1 and again splitting them into another list
            reading3 = (" ".join(reading2[:-1])).split()  # Joining the names of reading2 and again splitting them into another list
            Email += f"{self.EE.get()}"
            if reading2[-1] == self.EP.get() and reading2[-1] == "gauri853" :  # If the password is correct for Administrator
                self.destroy()
                self.accessing.switch_page(AdministratorPage)
            elif reading2[-1] == self.EP.get():  # If the password is correct for Employees
                # Adding name of the employee to "Name" for popping it up in the login page
                if len(reading3) == 2:  # If middle name does not exits
                    Name += f"{reading3[0]} {reading3[1]}"
                else:  # If middle name exits
                    Name += f"{reading3[0]} {reading3[1]} {reading3[2]}"
                messagebox.showinfo("Login Successful", f"{Name}, You have logged In successfully.")
                self.destroy()
                self.accessing.switch_page(LogInPage)
            else:  # if the password is not correct popping up message
                messagebox.showerror("Invalid Password!", "Password did not matched.")
        except:  # If email is not correct, popping up error messages
            if self.EE.get() == "" and self.EP.get() == "":
                messagebox.showerror("No Inputs Entered!", "Please enter your email and password.")
            elif self.EE.get() != "" and self.EP.get() != "":
                messagebox.showerror("Invalid Inputs Entered!", "Please enter correct email and password.")
            elif self.EE.get() == "":
                messagebox.showerror("Empty Email!", "Please enter your email.")
            elif self.EE.get() != "":
                messagebox.showerror("Invalid Email!", "Please enter correct email.")
            elif self.EP.get() == "":
                messagebox.showerror("Empty Password", "Please enter your password.")
            elif self.EP.get() != "":
                messagebox.showerror("Invalid Password", "Please enter correct password.")



# Registration page for the employees
class RegisterPage(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)

        # Creating Labels for Heading
        tk.Label(self, text='                                 ').grid(row=0, column=0)
        tk.Label(self, text='Registration page', font=('Arial', 20, 'bold'), fg='dark blue').grid(row=0, column=1)
        tk.Label(self, text='                                 ').grid(row=1, column=2)

        # Creating Labels and Entries for the form
        tk.Label(self, text="First Name:", font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky=E)
        self.EFN = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EFN.grid(row=2, column=1, sticky=W)

        tk.Label(self, text="Middle Name:", font=('Arial', 12, 'bold')).grid(row=3, column=0, sticky=E)
        self.EMN = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EMN.grid(row=3, column=1, sticky=W)

        tk.Label(self, text='Last Name:', font=('Arial', 12, 'bold')).grid(row=4, column=0, sticky=E)
        self.ELN = tk.Entry(self, textvariable='', width=60, bg='orange')
        self.ELN.grid(row=4, column=1, sticky=W)

        tk.Label(self, text='Email:', font=('Arial', 12, 'bold')).grid(row=5, column=0, sticky=E)
        self.EE = tk.Entry(self, textvariable='', width=60, bg='orange')
        self.EE.grid(row=5, column=1, sticky=W)

        tk.Label(self, text='password:', font=('Arial', 12, 'bold')).grid(row=6, column=0, sticky=E)
        self.EP = tk.Entry(self, textvariable='', show='*', width=60, bg='orange')
        self.EP.grid(row=6, column=1, sticky=W)

        tk.Label(self, text='Confirm Password:', font=('Arial', 12, 'bold')).grid(row=7, column=0, sticky=E)
        self.ECP = tk.Entry(self, textvariable='', show="*", width=60, bg='orange')
        self.ECP.grid(row=7, column=1, sticky=W)

        # Creating Buttons for "Reset', "Register" , to go back, to go to directly to SignIn Page if already registered
        self.BR = tk.Button(self, text='Reset', height=1, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(RegisterPage))
        self.BR.grid(row=8, column=1)
        tk.Label(self, text='                                 ').grid(row=9, column=0)

        self.BRG = tk.Button(self, text='Register', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: self.save())
        self.BRG.grid(row=10, column=1)
        tk.Label(self, text='                                 ').grid(row=11, column=0)

        self.BB = tk.Button(self, text='Back', height=1, width=10, bg="dark green", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(HomePage))
        self.BB.grid(row=12, column=1)
        tk.Label(self, text='                                 ').grid(row=13, column=0)

        tk.Label(self, text="Already have an account!", fg="dark green", font=('chiller', 18, 'normal')).grid(row=14, column=2)
        self.BS = tk.Button(self, text="Click Here", height=1, width=10, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), relief=GROOVE, border=0, command=lambda: access.switch_page(SignInPage))
        self.BS.grid(row=15, column=2)
        tk.Label(self, text='                                 ').grid(row=16, column=0)

    # Creating function for saving data
    def save(self):
        import re  # For validity of email while registering
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'  # For validity of email while registering
        try:  # Checking whether any entries are empty or not and other things
            if self.EFN.get() == ""  and self.ELN.get() == "" and self.EE.get() == "" and self.EP.get() == "" and self.ECP.get() == "":
                messagebox.showerror("No Inputs Entered!", "Please fill up your registration form first.")
            elif self.EFN.get() == "" or self.ELN.get() == "" or self.EE.get() == "" or self.EP.get() == "" or self.ECP.get() == "":
                messagebox.showerror("Some Inputs Are Left Empty!", "Please completely fill up your registration form first.")
            elif not (re.search(regex, self.EE.get())):  # Checking email is valid or not
                messagebox.showerror("Invalid Email", "Please put a valid email.")
            elif len(self.EP.get()) < 6:  # checking the length of the password
                messagebox.showinfo("Insufficient Password length", "Please make sure that your password have at least six characters.")
            elif self.EP.get() == self.ECP.get():  # Checking the password and confirm password is correct or or not
                try:  # If correct, checking the account if already exits or not
                    data_file = open(f"{self.EE.get()}.txt", 'r')
                    messagebox.showerror("Email Exits", "This email is already used. Please check whether same employee might being registered again.")
                except:  # If not exits then saving the data
                    text_file = open(f"{self.EE.get()}.txt", 'w+')
                    if self.EMN.get() == "":  # If middle name does not exists
                        text_file.write(f"{self.EFN.get()} {self.ELN.get()}\n" f'{self.ECP.get()}\n')
                        messagebox.showinfo("Registration Successful",f"{self.EFN.get()} {self.ELN.get()},you are successfully registered in NIT College as an employee. Now logIn.")
                    else:  # if middle name exists
                        text_file.write(f"{self.EFN.get()} {self.EMN.get()} {self.ELN.get()}\n" f'{self.ECP.get()}')
                        messagebox.showinfo("Registration Successful", f"{self.EFN.get()} {self.EMN.get()} {self.ELN.get()}, you have been successfully registered in NIT College as an employee, Now logIn.")
            else: # If the confirm password is not equal to password, generating error condition for exception
               print(5 / 0)
        except:  # Showing error message for invalid password
            messagebox.showerror("Invalid Confirm Password!","Password did not matched.")



# Creating Login Page for the employees
class LogInPage(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)
        global Name  # Making Name global to access the name of the employee
        global Email  # Making Name global to access the name of the employee

        # Creating Labels for Heading and for name of the employee
        tk.Label(self, text='                                 ').grid(row=0, column=0)
        tk.Label(self, text=f"{Name}", font=('Arial', 20, 'bold'), fg='dark blue').grid(row=0, column=5)
        tk.Label(self, text="(Employee)", font=('Arial', 20, 'bold')).grid(row=1, column=5)
        tk.Label(self, text='                                 ').grid(row=0, column=6)

        # Creating Labels for the employee's details if the employee have been registered in the admin department
        self.D_txt = open("Employees.txt", "r")
        self.read_data = self.D_txt.readlines()  # Reading employees
        self.arrange = ("".join(self.read_data)).split()  # Separating the employees and adding them into another list
        self.no_of_E = len(self.arrange)
        for i in range(self.no_of_E):
            a = (self.arrange[i].replace("_"," ")).split()  # Selecting each employee and removing "_" from their data with " "
            if Name == f"{a[1]} {a[2]} {a[3]}".replace(" ?", "") and Email == f"{a[7]}":
                # ID
                tk.Label(self, text="  ID  ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=1, sticky=W)
                tk.Label(self, text=f"{a[0]}", font=('Arial', 12, 'bold')).grid(row=3, column=1)

                # Name
                tk.Label(self, text="              Name              ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=2, sticky=W)
                tk.Label(self, text=f"{Name}", font=('Arial', 12, 'bold')).grid(row=3, column=2)

                # Age
                tk.Label(self, text="   Age   ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=3, sticky=W)
                tk.Label(self, text=f"{a[4]}", font=('Arial', 12, 'bold')).grid(row=3, column=3)

                # Address
                tk.Label(self, text="      Address     ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=4, sticky=W)
                tk.Label(self, text=f"{a[5]}", font=('Arial', 12, 'bold')).grid(row=3, column=4)

                # Contact No.
                tk.Label(self, text="Contact No.", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=5)
                tk.Label(self, text=f"{a[6]}", font=('Arial', 12, 'bold')).grid(row=3, column=5)

                # Email
                tk.Label(self, text="              Email              ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=6, sticky=W)
                tk.Label(self, text=f"{a[7]}", font=('Arial', 12, 'bold')).grid(row=3, column=6)

                # Gender
                tk.Label(self, text="     Gender     ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=7, sticky=W)
                tk.Label(self, text=f"{a[8]}", font=('Arial', 12, 'bold')).grid(row=3, column=7)

                # Department
                tk.Label(self, text="          Department          ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=2, column=8, sticky=W)
                tk.Label(self, text=f"{a[9]}", font=('Arial', 12, 'bold')).grid(row=3, column=8)


        # Creating Buttons to logout and to exit
        tk.Label(self, text='                                 ').grid(row=4, column=0)
        self.BS = tk.Button(self, text='LogOut', height=1, width=25, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(SignInPage))
        self.BS.grid(row=5, column=5)
        tk.Label(self, text='                                 ').grid(row=6, column=0)
        self.BH = tk.Button(self, text='Exit', height=1, width=10, bg="#2E026C", fg="white", font=("Arial", 10, 'bold'), command=access.destroy)
        self.BH.grid(row=7, column=5)
        tk.Label(self, text='                                 ').grid(row=8, column=0)
        Name = ""  # Assigning the empty string for others to login otherwise their name will be displayed like this "previous name + their actual name"
        Email = ""


# Creating Login Page for Administrator
class AdministratorPage(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)

        # Creating Labels for Heading and for name of the Administrator
        tk.Label(self, text='             ', bg="dark orange", font=('Arial', 20, 'bold')).grid(row=0, column=0)
        tk.Label(self, text='NIT College Employee And Department Management Page', font=('Arial', 20, 'bold'), fg='black', bg="dark orange").grid(row=0, column=1)
        tk.Label(self, text='             ', bg="dark orange", font=('Arial', 20, 'bold')).grid(row=0, column=2)
        tk.Label(self, text="Gauri Shankar Sharma", font=('Arial', 20, 'bold'), fg='dark blue').grid(row=1, column=1)
        tk.Label(self, text="(Administrator)", font=('Arial', 20, 'bold'), fg='black').grid(row=2, column=1)
        tk.Label(self, text='             ', font=('Arial', 20, 'bold')).grid(row=3, column=2)

        # Creating Buttons to view Employee and Department Details, to Logout and to Exit
        self.BE = tk.Button(self, text='View Employees Details', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(EmployeeDetails))
        self.BE.grid(row=4, column=1)
        tk.Label(self, text='             ').grid(row=5, column=0)

        self.BD = tk.Button(self, text='View Departments Details', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(DepartmentDetails))
        self.BD.grid(row=6, column=1)
        tk.Label(self, text='             ').grid(row=7, column=0)

        self.BB = tk.Button(self, text="LogOut", height=1, width=10, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'),command=lambda: access.switch_page(SignInPage))
        self.BB.grid(row=8, column=1)
        tk.Label(self, text='             ').grid(row=9, column=0)

        self.BE = tk.Button(self, text="Exit", height=1, width=10, bg="#2E026C", fg="white", font=("Arial", 10, 'bold'), command=access.destroy)
        self.BE.grid(row=10, column=1)
        tk.Label(self, text='             ').grid(row=11, column=0)



# Creating Employee Detail page
class EmployeeDetails(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)

        # Creating Labels for Heading and ID, Name, Age, Address, Contact No., Gender, Department of the employees
        tk.Label(self, text='                     ').grid(row=0, column=0)
        tk.Label(self, text="Employees", font=('Arial', 20, 'bold'), fg='dark blue').grid(row=0, column=5)
        tk.Label(self, text='                     ').grid(row=0, column=9)

        # Reading data
        self.D_txt = open("Employees.txt", "r")
        self.read_data = self.D_txt.readlines()  # Reading employees
        self.arrange = ("".join(self.read_data)).split()  # Separating the employees and adding them into another list
        self.no_of_E = len(self.arrange)
        for i in range(self.no_of_E):
            a = (self.arrange[i].replace("_", " ")).split()  # Selecting each employee and removing "_" from their data with " "

            # ID
            tk.Label(self, text="  ID  ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=1, sticky=W)
            tk.Label(self, text=f"{a[0]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=1)

            # Name
            tk.Label(self, text="              Name              ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=2, sticky=W)
            self.name = f"{a[1]} {a[2]} {a[3]}".replace(" ?", "")
            tk.Label(self, text=f"{self.name}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=2)

            # Age
            tk.Label(self, text="   Age   ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=3, sticky=W)
            tk.Label(self, text=f"{a[4]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=3)

            # Address
            tk.Label(self, text="      Address     ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=4, sticky=W)
            tk.Label(self, text=f"{a[5]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=4)

            # Contact No.
            tk.Label(self, text="Contact No.", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=5)
            tk.Label(self, text=f"{a[6]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=5)

            # Email
            tk.Label(self, text="              Email              ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=6, sticky=W)
            tk.Label(self, text=f"{a[7]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=6)

            # Gender
            tk.Label(self, text="     Gender     ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=7, sticky=W)
            tk.Label(self, text=f"{a[8]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=7)

            # Department
            tk.Label(self, text="        Department        ", font=('Arial', 15, 'bold'), fg='dark blue').grid(row=1, column=8, sticky=W)
            tk.Label(self, text=f"{a[9]}", font=('Arial', 12, 'bold')).grid(row=(2 + i), column=8)

        # Creating Button to add a new employee and to view department details directly from here without going back
        tk.Label(self, text='                     ').grid(row=(self.no_of_E + 2), column=9)
        self.BE = tk.Button(self, text="Add Employee", height=1, width=25, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(RegistrationForm))
        self.BE.grid(row=(self.no_of_E + 3), column=5)
        tk.Label(self, text='             ').grid(row=(self.no_of_E + 4), column=0)

        self.BD = tk.Button(self, text="View Departments", height=1, width=25, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(DepartmentDetails))
        self.BD.grid(row=(self.no_of_E + 5), column=5)
        tk.Label(self, text='             ').grid(row=(self.no_of_E + 6), column=0)

        # Creating Buttons to go back
        self.BB = tk.Button(self, text="Back", height=1, width=10, bg="dark green", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(AdministratorPage))
        self.BB.grid(row=(self.no_of_E + 7), column=5)
        tk.Label(self, text='             ').grid(row=(self.no_of_E + 8), column=0)


# Creating Department Detail page
class DepartmentDetails(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)

        # Creating Labels for Heading
        tk.Label(self, text='                                 ').grid(row=0, column=0)
        tk.Label(self, text="Departments", font=('Arial', 20, 'bold'), fg='dark blue').grid(row=0, column=1)
        tk.Label(self, text='                                 ').grid(row=0, column=2)

        # Creating Labels for the available departments
        self.D_txt = open("Departments.txt", "r")
        self.read_data = self.D_txt.read()  # Reading departments
        self.arrange = ("".join(self.read_data)).split()
        self.no_of_D = len(self.arrange)
        for j in range(self.no_of_D):
                tk.Label(self, text=f"      {1 + j}. {self.arrange[j]}", font=("Arial", 12, "bold")).grid(row=(1 + j), column=1, sticky=W)  # adding the read departments to Labels

        # Creating Button to add a new department and to view employee details directly from here without going back
        tk.Label(self, text='             ').grid(row=(self.no_of_D + 1), column=2)
        self.BD = tk.Button(self, text="Add Department", height=1, width=25, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(DepartmentForm))
        self.BD.grid(row=(self.no_of_D + 2), column=1)
        tk.Label(self, text='             ').grid(row=(self.no_of_D + 3), column=0)

        self.BE = tk.Button(self, text="View Employees", height=1, width=25, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(EmployeeDetails))
        self.BE.grid(row=(self.no_of_D + 4), column=1)
        tk.Label(self, text='             ').grid(row=(self.no_of_D + 5), column=0)

        # Creating buttons to go back
        self.BB = tk.Button(self, text="Back", height=1, width=10, bg="dark green", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(AdministratorPage))
        self.BB.grid(row=(self.no_of_D + 6), column=1)
        tk.Label(self, text='             ').grid(row=(self.no_of_D + 7), column=0)



# creating Registration form for the Employees
class RegistrationForm(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)

        # Creating Labels for Heading
        tk.Label(self, text='                                 ').grid(row=0, column=0)
        tk.Label(self, text='Employee Registration Form', font=('Arial', 20, 'bold'), fg='dark blue').grid(row=0, column=1)
        tk.Label(self, text='                                 ').grid(row=1, column=2)

        # Creating label for notice
        tk.Label(self, text="Warning: Don't give space in the form below, instead use ',' if needed.", fg='dark red', font=("Arial", 9, "normal")).grid(row=2, column=1, sticky=W)

        # Creating Labels, Entries and Drop down Menus for the form
        tk.Label(self, text="ID:", font=('Arial', 12, 'bold')).grid(row=3, column=0, sticky=E)
        self.EID = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EID.grid(row=3, column=1, sticky=W)

        tk.Label(self, text="First Name:", font=('Arial', 12, 'bold')).grid(row=4, column=0, sticky=E)
        self.EFN = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EFN.grid(row=4, column=1, sticky=W)

        tk.Label(self, text="Middle Name:", font=('Arial', 12, 'bold')).grid(row=5, column=0, sticky=E)
        self.EMN = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EMN.grid(row=5, column=1, sticky=W)

        tk.Label(self, text="Last Name:", font=('Arial', 12, 'bold')).grid(row=6, column=0, sticky=E)
        self.ELN = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.ELN.grid(row=6, column=1, sticky=W)

        tk.Label(self, text='Age:', font=('Arial', 12, 'bold')).grid(row=7, column=0, sticky=E)
        self.EAG = tk.Entry(self, textvariable='', width=60, bg='orange')
        self.EAG.grid(row=7, column=1, sticky=W)

        tk.Label(self, text="Address:", font=('Arial', 12, 'bold')).grid(row=8, column=0, sticky=E)
        self.EAD = tk.Entry(self, textvariable="", width=60, bg='orange')
        self.EAD.grid(row=8, column=1, sticky=W)

        tk.Label(self, text='Contact No.:', font=('Arial', 12, 'bold')).grid(row=9, column=0, sticky=E)
        self.ECN = tk.Entry(self, textvariable='', width=60, bg='orange')
        self.ECN.grid(row=9, column=1, sticky=W)

        tk.Label(self, text='Email:', font=('Arial', 12, 'bold')).grid(row=10, column=0, sticky=E)
        self.EE = tk.Entry(self, textvariable='', width=60, bg='orange')
        self.EE.grid(row=10, column=1, sticky=W)

        # Drop Down Menus For Gender
        tk.Label(self, text='Gender:', font=('Arial', 12, 'bold')).grid(row=11, column=0, sticky=E)
        self.var2 = tk.StringVar()
        self.var2.set("Select your Gender")
        self.DMG = tk.OptionMenu(self, self.var2, "Male", "Female")
        self.DMG.config(font=('Arial', 10, 'bold'), width=20, bg='dark orange', activebackground="blue")
        self.DMG.grid(row=11, column=1, sticky=W)

        # Drop down menu for Department
        tk.Label(self, text='Department:', font=('Arial', 12, 'bold')).grid(row=12, column=0, sticky=E)
        # opening and Reading available departments from saved file
        self.D_txt = open("Departments.txt", "r")
        self.checking1 = self.D_txt.readlines()
        self.checking2 = ("".join(self.checking1)).split()  # Joining the items of checking1 and again splitting them into another list
        self.var3 = tk.StringVar()
        self.var3.set("Select the department you had worked before")
        self.DMD = tk.OptionMenu(self, self.var3, *self.checking2)
        self.DMD.config(font=('Arial', 10, 'bold'), width=45, bg='dark orange', activebackground="blue")
        self.DMD.grid(row=12, column=1, sticky=W)

        # Creating Buttons for "Reset", "Submit' and "Back"
        self.BR = tk.Button(self, text='Reset', height=1, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(RegistrationForm))
        self.BR.grid(row=13, column=1)
        tk.Label(self, text='                                 ').grid(row=14, column=0)

        self.BS = tk.Button(self, text='Submit', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: self.save())
        self.BS.grid(row=15, column=1)
        tk.Label(self, text='                                 ').grid(row=16, column=0)

        self.BE = tk.Button(self, text='Back', height=1, width=10, bg="dark green", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(EmployeeDetails))
        self.BE.grid(row=17, column=1)
        tk.Label(self, text='                                 ').grid(row=18, column=0)

    # Creating function for adding the employee
    def save(self):
        import re  # For validity of email while registering
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'  # For validity of email while registering
        try:  # Checking whether any entries are empty or not and other things
            a = "Select your Gender"
            b = "Select the department you had worked before"
            if self.EID.get() == "" and self.EFN.get() == '' and self.ELN.get() == "" and self.EAG.get() == '' and self.EAD.get() == "" and self.ECN.get() == '' and self.EE.get() == '' and self.var2.get() == a and self.var3.get() == b:
                messagebox.showerror("Form unfulfilled", "Please fill up the form first!")
            elif self.EID.get() == "" or self.EFN.get() == '' or self.ELN.get() == "" or self.EAG.get() == '' or self.EAD.get() == "" or self.ECN.get() == '' or self.EE.get() == '':
                messagebox.showerror("Form unfulfilled", "You have not filled up the form completely!")
            elif not (re.search(regex, self.EE.get())):  # Checking email is valid or not
                messagebox.showerror("Invalid Email", "Please put a valid email.")
            elif self.var2.get() == a and self.var3.get() == b:
                messagebox.showerror("Form unfulfilled", "You have not selected your gender and department.")
            elif self.var2.get() == a:
                messagebox.showerror("Form unfulfilled", "You have not selected your gender.")
            elif self.var3.get() == b:
                messagebox.showerror("Form unfulfilled", "You have not selected the department you have worked before.")
            elif self.EID.get() != "" or self.EAG.get() != '' or self.ECN.get() != '':
                try:
                    b = int(a) / 1
                except:
                    messagebox.showerror("TypeError", "You are allowed to use numbers only in ID or age or contact No.")

            else:  # Checking whether the employee is already registered or not
                data_txt = open("Employees.txt", "r")  # Reading data
                read_data =data_txt.readlines()  # Reading departments
                arrange = ("".join(read_data)).split()  # Separating the employees and adding them into another list
                number_e = len(arrange)
                lis = [1]  # Making a list which will help to create exception condition
                for i in range(number_e):
                    a = (arrange[i].replace("_"," ")).split()  # Selecting each employee and removing "_" from their data wih " "
                    if self.ECN.get() == f"{a[6]}" or self.EE.get() == f"{a[7]}":
                        messagebox.showerror("Contact number or the email found","The contact number or the email address you have used is already taken or the employee might be already registered, Please check the employee first and then register.")
                        lis.append(2)  # appending a item in the list so that exception condition will not be mate
                if len(lis) == 1:  # If condition for creating exception condition
                   print(5 / 0)
        except:  # If employee is not registered before
            file_txt = open("Employees.txt", "a+")
            if self.EMN.get() == "":  # If the employee has not middle name
                file_txt.write(f"{self.EID.get()}_{self.EFN.get()}_?_{self.ELN.get()}_{self.EAG.get()}_{self.EAD.get()}_{self.ECN.get()}_{self.EE.get()}_{self.var2.get()}_{self.var3.get()}\n")
                messagebox.showinfo("Employee registration Successful",f"{self.EFN.get()} {self.ELN.get()} is successfully registered as an employee.")
            else:  # If the employee has middle name
                file_txt.write(f"{self.EID.get()}_{self.EFN.get()}_{self.EMN.get()}_{self.ELN.get()}_{self.EAG.get()}_{self.EAD.get()}_{self.ECN.get()}_{self.EE.get()}_{self.var2.get()}_{self.var3.get()}\n")
                messagebox.showinfo("Employee registration Successful", f"{self.EFN.get()} {self.EMN.get()} {self.ELN.get()} is successfully registered as an employee.")


# Creating DepartmentForm for the departments
class DepartmentForm(tk.Frame):
    def __init__(self, access):
        tk.Frame.__init__(self)
        self.accessing = access

        # Creating Labels for Heading
        tk.Label(self, text='                                 ').grid(row=0, column=0)
        tk.Label(self, text='Department Form', font=('Arial', 20, 'bold'), fg='dark blue').grid(row=0, column=1)
        tk.Label(self, text='                                 ').grid(row=1, column=2)

        # Creating Labels and Entries for the form
        tk.Label(self, text="Department Code:", font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky=E)
        self.EDC = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EDC.grid(row=2, column=1)

        tk.Label(self, text="Department Name:", font=('Arial', 12, 'bold')).grid(row=3, column=0)
        self.EDN = tk.Entry(self, textvariable='', width=60, bg="orange")
        self.EDN.grid(row=3, column=1)

        # Creating Buttons for "Reset', "Submit" and "back'
        self.LB = tk.Button(self, text='Reset', height=1, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: access.switch_page(DepartmentForm))
        self.LB.grid(row=4, column=1)
        tk.Label(self, text='                                 ').grid(row=5, column=0)

        self.LB = tk.Button(self, text='Submit', height=2, width=45, bg="#0607DF", fg="white", font=("Arial", 10, 'bold'), command=lambda: self.add())
        self.LB.grid(row=6, column=1)
        tk.Label(self, text='                                 ').grid(row=7, column=0)

        self.LB = tk.Button(self, text='Back', height=1, width=10, bg="dark green", fg="white",font=("Arial", 10, 'bold'), command=lambda: access.switch_page(DepartmentDetails))
        self.LB.grid(row=8, column=1)
        tk.Label(self, text='                                 ').grid(row=9, column=0)

    # Creating function for adding the department
    def add(self):
        try:  # Checking whether any entries are empty or not and other things
            if self.EDN.get() == "" and self.EDC.get() == '':
                messagebox.showerror("Form unfulfilled", "Please fill up the form first!")
            elif self.EDN.get() == "" or self.EDC.get() == '':
                messagebox.showerror("Form unfulfilled", "You have not filled up the form completely!")
            else:  # Checking whether the department exits or not
                file_txt = open("Departments.txt", "r")
                department_list = file_txt.readlines()
                departments = ("".join(department_list)).split()  # Making list of the departments
                lis = [1]  # Making a list which will help to create exception condition
                for i in departments:
                    if i == f"{self.EDN.get()}({self.EDC.get()})":
                        messagebox.showerror("Department Found", "Departments already exits!")
                        lis.append(2)  # appending a item in the list so that exception condition will not be mate
                if len(lis) == 1:  # If condition for creating exception condition
                   print(5 / 0)
        except:  # If department does not exits before adding it
            file_txt = open("Departments.txt", "a+")
            file_txt.write(f"{self.EDN.get()}({self.EDC.get()})\n")
            messagebox.showinfo("Department Submitted", f"{self.EDN.get()}({self.EDC.get()}) is successfully added.")


Calling = EMP()
Calling.mainloop()