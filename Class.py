# Operating with bank calculation
class Customer():
    def __init__(self, name, balance):
        self.Nam = name
        self.Rupaiya = balance

    def withdraw(self, amount):
        self.Rupaiya -= amount
        return self.Rupaiya

    def deposit(self, amount):
        self.Rupaiya += amount
        return self.Rupaiya


C1 = Customer("Gauri_Shankar", 25000)  # Creating objects and calling methods
print(C1.withdraw(13755))
print(C1.deposit(15500))
C2 = Customer("SpiderMan", 6958852367)
print(C2.withdraw(0.0001))
print(C2.deposit(999999999999999))

print(C1.Nam)  # prints the name
print(C1.Rupaiya)  # Prints the final amount
C1.Rupaiya = 9000  # Setting new balance
print(C1.Rupaiya)  # printing new balance

# Create a class student and find the total and average masks, highest mask and the topper name
class Student():
    def __init__(self, name):
        self.N = name
        self.a = int(input("Enter the marks you have scored in English."))
        self.b = int(input("Enter the marks you have scored in Nepali."))
        self.c = int(input("Enter the marks you have scored in Physics."))

    def exposing_marks(self):
        total = self.a + self.b + self.c
        average = total / 3
        print(f"Your Total Marks is {total} and Average Marks is {average}.")

    def highest_marks(self):
        if self.a > self.b and self.a > self.c:
            temp = self.a, "in English"
        elif self.b > self.a and self.b > self.a:
            temp = self.b, "in Nepali'"
        else:
            temp = self.c, "in Physics"
        print(f"Highest Marks: {temp}.")


St1 = Student("Ram")
St1.exposing_marks()
St1.highest_marks()
# Another Way
class Student():
    def __init__(self, name, roll_no):
        self.N = name
        self.R = roll_no
        self.Subject = ['English', 'Nepali', 'Maths']
        self.User_Marks = []

    def identity(self):
        print(f"Name: {self.N} \n" f"Roll No.: {self.R}")

    def get_marks(self):
        for i in range(len(self.Subject)):
            m = int(input("Enter the marks you have scored in each subject "))
            self.User_Marks.append(m)

    def display_marks(self):
        total = sum(self.User_Marks)  # "sum" adds the numbers of the list
        average = total / len(self.Subject)
        print(f"Total Marks: {total} \n" f"Average Marks: {average}")

    def highest_marks(self):
        if self.User_Marks[0] > self.User_Marks[1] and self.User_Marks[0] > self.User_Marks[2]:
            temp = self.User_Marks[0], "in English."
        elif self.User_Marks[1] > self.User_Marks[0] and self.User_Marks[1] > self.User_Marks[0]:
            temp = self.User_Marks[1], "in Nepali."
        else:
            temp = self.User_Marks[2], "in Physics"
        print(f"The highest marks is {temp}")


S1 = Student("Gauri Shankar Sharma", 34)  # This is creation of object called x
S1.identity()
S1.get_marks()
S1.display_marks()
S1.highest_marks()

# Create  a class called 'First'
# create two method, one for returning the class name like "this is first class",
# another method to set the name from user 'cname' and should return the name
# "this is the first class renamed to ____"
# // naw call second class, and also return the date from second class
# Create a class called 'Second'
# Create a function to return current date, in the format of "sombar, mangshir 2076"
# for this use a variable and set the time by yourself,


class First():
    def __init__(self, name):
        self.N = name

    def return_name(self):
        return "This is the first class."

    def return_custom_name(self):
        return "This is the first class renamed to " + self.N + "."

    def get_date_from_other_class(self):
        a = Second()
        b = a.get_date()
        return "Date returned from first class using second object is :" + b


class Second():
    def __init__(self):
        self.val = ""

    def get_date(self):
        return "Today's date is sombar, 23 mangshir, 2076."


A = First("John")
print(A.return_name())
print(A.return_custom_name())
print(A.get_date_from_other_class())

# INHERITANCE AND SUBCLASS:
class Course():
    def __init__(self, name, course_name, course_code):
        self.CN = course_name
        self.CC = course_code
        self.N = name
        self.a = int(input("Enter the marks you have scored in English."))
        self.b = int(input("Enter the marks you have scored in Nepali."))
        self.c = int(input("Enter the marks you have scored in Physics."))

    def get_info(self):
        print(f"Name: {self.N} \n" f"Faculty: {self.CN} \n" f"Code: {self.CC}")


class Student(Course):

    def exposing_marks(self):
        total = self.a + self.b + self.c
        average = total / 3
        print(f"Average Marks: {average}")


St1 = Student("GauriShankarSharma", "Science", "38")
St1.get_info()
St1.exposing_marks()

# Working on more than two class
class Person():
    def __init__(self, name, address, phone, age):
        self.N = name
        self.AD = address
        self.P = phone
        self.AG = age

    def introduction(self):
        return f" \n Hi!, my name is {self.N}. \n" f'Address: {self.AD}\n' f"Phone No.: {self.P} \n" f"Age: {self.AG}"


class Teacher(Person):
    def __init__(self, name, address, phone, age, subject):
        Person.__init__(self, name, address, phone, age)
        self.S = subject

    def introduction1(self):
        return f'Subject: {self.S}'


class Student(Person):
    def __init__(self, name, address, phone, age, class_section, roll_no, group):
        Person.__init__(self, name, address, phone, age)
        self.C = class_section
        self.R = roll_no
        self.G = group

    def introduction2(self):
        return f"Class-Section: {self.C} \n" f"Roll-No.: {self.R} \n" f"Group: {self.G}"


P1 = Person('John', 'New york', 4635464463, 26)
print(P1.introduction())

T1 = Teacher('Munerilal', 'Saptari', 36458966, 34, 'Math')
print(T1.introduction())
print(T1.introduction1())

S1 = Student('Gauri Shankar Sharma', 'Morang', 635465, 18, '27-A', 34, 'None')
print(S1.introduction())
print(S1.introduction2())

# Create a class Animal, with function, and a variable with animal name,
#         can breath,
#         can run,
#         can speak,
# Create child class human,
#      with one extra function, can think
# Create child class to animal called dog
#       with one extra function, is loyal
# Now, using OOP, print, human can think, similarly human can breath, run and speak and aslo for dog,
# print dog is loyal, and can breath run and speak, using concept of inheritance.


class Animal():
    def __init__(self, name):
        self.N = name

    def can_breath(self):
        return f'\n{self.N} can breath.'

    def can_run(self):
        return f"{self.N} can run."

    def can_speak(self):
        return f"{self.N} can speak."


class Human(Animal):

    def can_think(self):
        return f"{self.N} can think."


class Dog(Animal):

    def is_loyal(self):
        return f"{self.N} is loyal."


A1 = Animal("leopard")
print(A1.can_breath())
print(A1.can_run())
print(A1.can_speak())

H1 = Human("Brad")
print(H1.can_breath())
print(H1.can_run())
print(H1.can_speak())
print((H1.can_think()))

D1 = Dog("Tom")
print(D1.can_breath())
print(D1.can_run())
print(D1.can_speak())
print(D1.is_loyal())

# Polymorphism
class Person():
    def __init__(self, name, address, phone):
        self.N = name
        self.A = address
        self.P = phone

    def introduction(self):
        return f"Hi, my name is {self.N}. \n" f'Address: {self.A}\n' f'Phone: {self.P}'


class Teacher(Person):
    def __init__(self, name, address, phone, subject):
        Person.__init__(self, name, address, phone)
        self.S = subject

    def introduction(self):
        return f'\nHi, my name is {self.N} and I am a teacher.\n' f'Address: {self.A}\n' f'Phone: {self.P}\n' f'Subject: {self.S}'


T1 = Teacher("Ram", 'Kathmandu', 9834697156, 'Math')
print(T1.introduction())

# Create a class called Calculation and create a function add
# implement polymorphism in function where two or three parameter can be passed


class Calculation:

    def add(self, a, b, c=0):  # implementing polymorphism in the function
        sum = a + b + c
        return sum


A = Calculation()
print(A.add(1, 2, 3))


#
class Country():
    def __init__(self, capital_city, language):
        self.C = capital_city
        self.L = language

    def capital_city(self):
        return f"My country's capital city is {self.C}."

    def language(self):
        return f"My country's language is {self.L}"


class Nepal(Country):
    def __init__(self, capital_city, language, status):
        Country. __init__(self, capital_city, language)
        self.S = status

    def intro(self):
        return f"Nepal's capital city is {self.C}."

    def language(self):
        return f"Nepal's national language is Nepali."

    def status(self):
        return f"Nepal is an {self.S} country."


class America(Country):
    def __init__(self, capital_city, language, status):
        Country.__init__(self, capital_city, language)
        self.S = status

    def intro(self):
        return f"\nAmerica's capital city is {self.C}."

    def language(self):
        return f"America's national language is Nepali."

    def status(self):
        return f"America is an {self.S} country."


N1 = Nepal("Kathmandu", "Nepali", "underdeveloped")
print(N1.intro())
print(N1.language())
print(N1.status())

A1 = America("New york", "English", "developed")
print(A1.intro())
print(A1.language())
print(A1.status())












