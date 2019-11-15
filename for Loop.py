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
# In this process,it tries to print numbers less than 10 but also sees the if and prints numbers up to 8
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
# Another way
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
# Printing the prime numbers only given in the certain range
for x in range(2, 21):
    a = True
    for y in range(2, x):
        if x % y == 0:
            a = False
            break
    if a == True:
        print(x)