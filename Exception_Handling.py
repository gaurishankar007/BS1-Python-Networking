#
try:
    length = int(input("Enter the length of the square: "))  # once the value of the length is invalid then
    area = length ** 2  # it will go to except and prints but will not ask to enter the length again
    print(area)
except:
    print("Invalid value for radius.")


# In this case, when the input is invalid then 'while loop' will again ask to enter valid value until value is correct
# Its because when we put right value then while condition terminates(ends) because the value of "success" becomes True
# But when we put wrong value the while condition does not terminate because the value of "success" remains False
success = False
while success == False:
    try:
        radius = int(input("Enter the radius: "))
        area = 3.14 * radius ** 2
        print(area)
        success = True
    except:
        print("Invalid value for radius.")

#
a = True
while a == True:
    try:
        a = int(input("Enter a number"))
        print(a / a)
        a = False
    except:
        print("Invalid Inpuat.")


# Create a function divide with two parameter a, b
# now it should return the divided value like a/b,
# now if the input from user ie. b is 0, our program should produce a nice exception errror,


def divide(a, b):
    x = a / b
    return x


S = True
while S == True:
    try:
        p = int(input("Enter the dividend "))
        q = int(input('Enter the divider '))
        print(divide(p, q))
        S = False
    except:
        print("Invalid input.")


# Use exception handling to report out of bound error also for multiple error
# print(5) // this gives error now to use try catch to handle these errors
try:
    b = 5 / 0
    a = [1, 2, 3]
    print(a[5])

except(IndexError, ZeroDivisionError):
    print("Invalid input")