# This is a just simple example of checking

# This is the first question
a = input("Enter the first number")
b = input("Enter the second number")
c = int(a)+int(b)
print("The required sum is "+str(c))

# This is the second question
l = input("Enter the length")
b = input("Enter the bridth")
c = int(l)*int(b)
print("The required Area is "+str(c))

# This is the third question
a = input("Enter your name")
print("Hello "+a+",have a nice day!")

# This is the fourth question
x = int(input("Enter the value of x"))
y = int(input("Enter the value of y"))
z = x**3+3*x**2*y+3*x*y**2+y**3
print("The required result is "+str(z))

# This is the Home-Work
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
x = (-b+(b**2-4*a*c)**.5)/(2*a)
y = (-b-(b**2-4*a*c)**.5)/(2*a)
print("The required solutions of the given quadratic equation are "+str(x)+","+str(y))

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

# Comparision of numbers(Another method)
a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
c = float(input("Enter the third number"))

if a > b and a > c:
    temp = a
elif b > a and b > c:
    temp = b
else:
    temp = c
print("The greatest number is ", temp)

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

# Printing all odd numbers <100 using while loop.
n = 1
while n < 100:
    print(n)
    n = n + 2
# Another method
a = 99
while a > 0:
    print(a)
    a = a - 2

# Printing all even number <100 using while loop.
n = 2
while n < 100:
    print(n)
    n = n + 2

# Finding the given number odd or even
x = int(input("Enter the number "))
if x % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Finding the multiplication of a number
x = int(input('Enter the number for multiplication '))
y = 1
while y <= 100:
    print(str(x) + "*" + str(y) + "=" + str(x*y))
    y = y + 1
# Another way
x = 5
y = 1
while y <= 10:
    a = x * y
    y = y + 1
    print(f"{x}*{y}=" + str(a))

#
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

#
for a in range(10):
    print(a)
for b in range(2, 8):
    print(b)
for a in range(5):
    print("Hello!")
for i in range(5, 10, 2):
    print(i)
for i in range(5, 11, 2):  # Same as above
    print(i)
for i in range(5, 12, 2):
    print(i)
for i in range(11, 1, -2):  # Printing numbers in decreasing form
    print(i)
for i in range(99, 0, -2):  # Printing all odd numbers less than 100
    print(i)

# In this process,
# When you put the first number b becomes b+a(1st no.)
# Then b becomes b+a(1st no.)+a(2nd no.)
# And at last b=b+a(2nd no.)+a(3rd no.)
# Similarly, it goes on like this for further ranges
b = ''
for x in range(3):
    a = input("Enter the numbers ")
    b = b + a
print(b)
# Same Question but a bit different in answer
a = ""
for x in range(3):
    x = input("Enter the numbers ")
    a = a + x
    print(a)

# printing the numbers in the required interval
# Using while loop(In this process,it tries prints numbers less than 10 but also sees the if and prints numbers up to 8)
n = 0
while n < 10:
    print(n)
    if n == 8:
        break
    n = n + 1
# In this process,10 is replaced by 8 and prints number less than 8
n = 1
while n < 10:
    if n == 8:
        break
    print(n)
    n = n + 1
# Using for loop
# In this process,it tries prints numbers less than 10 but also sees the if and prints numbers up to 8
for a in range(10):
    print(a)
    if a == 8:
        break  # Here,the meaning of the break is to stop printing the value of a when it's value becomes 8
# In this process,10 is replaced by 8 and prints number less than 8
for i in range(10):
    if i == 8:
        break
    print(i)
# This  is just an example of understanding the purpose of break
a = int(input("Enter the number "))
for i in range(2, a):
    if a % i != 0:
        print("This is a prime number.")
        break  # In this,break makes the result stop when the last result is printed after if condition is satisfied.
    else:
        print("This is not a prime number.")

# Finding the factorial of a number.
a = int(input("Enter the number "))
b = 1
for a in range(a + 1):
    if a > 0:
        b = b * a
print(b)
# Another Way
a = int(input("Enter the number "))
for i in range(1,a):
    a = a * i
print(a)
#
a = int(input("Enter the number"))
b = 1
for i in range(1,a + 1,1):
    b = b * i
print(b)
# In this,the answer is different because of indentation of the "print(b)" is different
a = int(input("Enter the number "))
b = 1
for a in range(a + 1):
    if a > 0:
        b = b * a
    print(b)
# Using while loop
x = int(input("Enter the number "))
y = 1
while x > 0:
    y = y * x
    x = x - 1
print(y)
# Another way
a = 5
b = 1
while b < 5:
    a = b * a
    b = b + 1
print(a)

# Finding the given number is prime number or not
x = int(input("Enter the number "))
y = True
for i in range(2, x):
    if x % i == 0:
        y = False
        break
print(y)
# Another way
a = int(input("Enter the number "))
x = "This is a prime number."
for i in range(2, a):
    if a % i == 0:
        x = "This is not a prime number."
        break
print(x)

# Finding the certain range of number is prime or not
for x in range(2, 21):
    a = True
    for y in range(2, x):
        if x % y == 0:
            a = False
            break
    if a == True:
        print(str(x) + " is a prime number.")
    else:
        print(str(x) + " is not a prime number.")
# To print the prime numbers only in the certain range
for x in range(2, 21):
    a = True
    for y in range(2, x):
        if x % y == 0:
            a = False
            break
    if a == True:
        print(x)

# Finding the prime number of a certain range
# and put them in list
Primes = [] # Empty List
a = int(input("Enter the range "))
for i in range(2, a):
    x = True
    for j in range(2, i):
        if i % j == 0:
            x = False
            break
    if x == True:
        Primes.append(i)  # add to list if prime
print(Primes)
#
b = []
c = int(input("Enter the range "))
for x in range(2, c):
    a = True
    for y in range(2, x):
        if x % y == 0:
            a = False
            break
    if a == True:
        b.append(x)
print(b)

#
#
A = [[1, 2, 3, 4, 5], "anup", "bishnu"]
print(A[0])
print(A[0][4])
print(A[1])
print(A[2][4])
for i in A[0]:
    print(i)
for j in A[2]:
    print(j)
print(len(A))
A.append(6)
print(A)
A[2] = 5
print(A)

L1 = [2, 1]
L2 = [4, 5]
L3 = L1 + L2
print(L3)
L1.extend([0, 6])
print(L1)

#
L = []
L1 = ["1", "2", "3", "4", "5"]
L2 = ['a', 'b', 'c', 'd', 'e']
for i in L1[:]:
    for j in L2[:]:
        a = i + j
        if i == '1':
            if j == 'a':
                L.append(a)
        elif i == "2":
            if j == 'b':
                L.append(a)
        elif i == "3":
            if j == 'c':
                L.append(a)
        elif i == "4":
            if j == 'd':
                L.append(a)
        elif i == "5":
            if j == 'e':
                L.append(a)
        else:
            L.append(a)
print(L)












