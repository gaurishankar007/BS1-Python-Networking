# Adding numbers
def func(a, b, c):
    adding = a + b + c
    return adding
p = int(input("Enter the 1st No."))
q = int(input("Enter the 2nd No."))
r = int(input("Enter the 3rd No."))
i = func(p, q, r)  # Calling the function
print(i)
# OR
j = func(2, 4, 8)  # Calling the function
print(j)
# Another The Way(Not Recommended to do)
def lol():
    sum = a + b
    return sum
a = 3
b = 7
print(lol())

# Write as function to pass a no and return weather it is odd or even
def noob(a, b):
    sum = a + b
    return sum
p = 0
q = int(input("Enter the number"))
R = noob(p, q)
if R % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# Another way
def no(a):
    r = a % 2
    return r
s = int(input("Enter the number"))
T = no(s)
if T == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Write a function to pass a letter and check weather the string is upper or lower case
def buha(a):
      aaha = a
      return aaha
x = input("Enter a letter")
y = buha(x)
if y.isupper():
    print("upper")
else:
    print("lower")

# Write a function that gives sum of all the odd number up to the number you have given
def dog(a):
    sum = a
    return sum
x = int(input("Enter the number up to which you want the sum of the odd numbers..."))
y = 0
for i in range(x + 1):
    if i % 2 != 0:
        y = y + i
z = dog(y)
print(y)



# FUNCTION RECURSION:
# Finding Factorial of a number using
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)
P = int(input("Enter the number of which you want to calculate the factorial..."))
if P < 0:
    print("Murkha Manushya! don't you know that the factorial of negative number doesn't exist, Aahahahha.")
elif P == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {P} is {factorial(P)}.")

# Python program to display the Fibonacci sequence(It goes from 0 to 50)
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
Number_of_n= 10
# check if the number of terms is valid
if Number_of_n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(Number_of_n):
        print(fibo(i))

# Printing the given index of number from the Fibonacci Series
# In this case the starting point of the fibonacci series is '1' but not '0'
# Because we haven't given input to start from '0'
# The Fibonacci Series are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,.........
# The Fibonacci numbers Fn are defined by F1 = 1; F2 = 1 and
# Fn = Fn−1 + Fn−2 for n > 2:
# So the next element in the sequence is the sum of the previous two.
# Hence F3 = F2 + F1 = 1 + 1 = 2 and the sequence starts
def fibo1(a):
    if a <= 1:
        return a
    else:
        return fibo1(a - 1) + fibo1(a - 2)
n = int(input("Enter the index of the number in fibonacci series..."))
if n < 0:
    print("Please don't enter negative integers.")
else:
    print(fibo1(n))

# printing Fibonacci Series as per as the user range like up to 10 number of Fibonacci Series
def fibo2(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibo2(x - 1) + fibo2(x - 2)
a = int(input("Enter '0' or '1' from where you want to start the fibonacci series...."))
b = int(input("Enter the number of fibonacci series you want...."))
if b < 0:
    print("Don't enter a negative integer.")
else:
    if a == 1:
        print("Your required fibonacci series is:")
        for i in range(a, b + 1):
            print(i, ':', fibo2(i))
    else:
        print("Your required fibonacci series is:")
        for i in range(a, b):
            print(i + 1, ':', fibo2(i))


# The Lucas numbers Ln are defined by L0 = 2; L1 = 1 and
# L
# n = Ln−1 + Ln−2 for n > 1:
# So the next element in the sequence is the sum of the previous two.
# Hence L2 = L1 + L0 = 2 + 1 = 3 and the sequence starts:

def lucas(n):
    if n < 0:
        raise ValueError("n should be +ve")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# when you give input like print(lucas(-5)) this then the following code will appear
# Traceback (most recent call last):
#   File "C:/Users/Gouri/Learning Python/Testing2.py", line 16, in <module>
#     print(lucas(-5))
#   File "C:/Users/Gouri/Learning Python/Testing2.py", line 7, in lucas
#     raise ValueError("n should be +ve")
# ValueError: n should be +ve


p = int(input("Enter the range of the lucas number up to which you want the lucas number series: "))
x = []
for i in range(0, p):
    x.append(lucas(i))
print(f"The required lucas number series are: {x}")


# The Golden Ratio is a number that appears throughout the natural
# world. A sequence of approximations to it is given by Gn where
# G1 = 1; and Gn = 1 + (1/Gn−1) for n > 1:
# Hence G2 = 1 + (1/G1) = 1 + 1 = 2 and G3 = 1 + (1/G2) = 1 + 1/2 = 3/2.


def golden_ratio(n):
    if n < 1:
        return "Please enter value greater than 0."
    elif n == 1:
        return 1
    else:
        return 1 + (1 / golden_ratio(n - 1))


p = int(input("Enter the indexing number: "))
print(golden_ratio(p))


# The Triangle Numbers are those generated by counting the number of
# * needed to create triangles as in the image below. Note that each
# row requires one more dot than the previous.
#                                     *
#                         *          * *
#               *        * *        * * *
#       *      * *      * * *      * * * *
# *    * *    * * *    * * * *    * * * * *
# 1     3       6         10         15
# The Triangle Numbers are those generated by counting the number of
# dots needed to create triangles as in the image below. Note that each
# row requires one more dot than the previous.


def triangle_number(n):
    if n < 1:
        return "Enter a number greater than zero."
    elif n == 1:
        return 1
    else:
        # Every triangle number is the sum of the previous triangle number and the position number of the triangle
        return n + triangle_number(n - 1)


p = int(input("Enter the tringle position number: "))
print(triangle_number(p))





