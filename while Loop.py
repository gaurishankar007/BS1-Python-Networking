# When the value of "a" tries to overcome "10" then it will stop printing the value of a
# But in this case the value of "a" never increases up to 10 and "2" is printed continuously
# So
a = 2
while a < 10:
    print(a)
# In this case,break stop printing the value of "a" more than one time
a = 6
while a < 9:
    print(a)
    break
# In this case, it will print the value of "a" up to less than 6
a = 1
while a < 6:
    print(a)
    a = a + 1

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

# Finding the multiplication of a number
x = int(input('Enter the number for multiplication '))
y = 1
while y <= 10:
    print(str(x) + "*" + str(y) + "=" + str(x*y))
    y = y + 1
# Another way
x = 5
y = 1
while y <= 10:
    a = x * y
    y = y + 1
    print(f"{x}*{y}=" + str(a))

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

# Finding the factorial of a number.
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

#
A = 'abcdef'
i = 'a'
while i in A:
    A = A[:-1]  # OR:- A = A[0 : -1]
    print(i, end=" ")