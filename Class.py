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





