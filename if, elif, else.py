# Comparision of numbers
a = input("Enter the value of a  ")
b = input("Enter the value of b ")
c = input("Enter the value of c ")
if a > b and a > c:
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")
# Another method
a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
c = float(input("Enter the third number"))
if a > b and a > c:
    temp = a
elif b > a and b > c:
    temp = b
else:
    temp = c
print("The greatest number is", temp)

# Calculation of grade you have got in the exam
a = int(input("Enter the percentage you have got "))
if a >= 90:
    print("You have got A+")
elif a >= 80:
    print("You have got A")
elif a >= 70:
    print("You have got B+")
elif a >= 60:
    print("You have got B")
else:
    print("you failed the exam.")
# Another way
grade = 82
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
else:
    print('D')

# Finding x and y are equal or greater or lesser.
x = input("Put the value of x ")
y = input("Put the value of y ")
if x == y:
    print("x and y are equal.")
elif x > y:
    print("x is the greatest number.")
else:
    print("y is the greatest number.")

# Finding the given number odd or even
x = int(input("Enter the number "))
if x % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# printing the day when the equivalent number of the day is input
a = int(input("Enter the number "))
while a < 8:
    if a == 1:
        print("Sunday")
        break
    elif a == 2:
        print('Monday')
        break
    elif a == 3:
        print("Tuesday")
        break
    elif a == 4:
        print("Wednesday")
        break
    elif a == 5:
        print("Thursday")
        break
    elif a == 6:
        print("Friday")
        break
    else:
        print("Saturday and its holiday.")
        break
# Another Duplicate Method
a = int(input("Enter the number "))
if a == 1:
    print("Sunday")
elif a == 2:
    print('Monday')
elif a == 3:
    print("Tuesday")
elif a == 4:
    print("Wednesday")
elif a == 5:
    print("Thursday")
elif a == 6:
    print("Friday")
elif a == 7:
    print("Saturday and its holiday.")
else:
    print("Error number.please Put number between 1-7.")

# It will print nothing that means no output
if None:
    print("This is None statement.")

# "if not" statement
a = 10
b = 20
if not a > 10:
    print(f"{a} is less than {b}.")
else:
    print(f"{b} is less than {a}.")