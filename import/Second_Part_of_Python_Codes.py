import Testing1
a = input("Enter the operation you want to be done ")
p = int(input("Enter the first number "))
q = int(input('Enter the second number '))

x = int(input("Enter the first number "))
y = int(input('Enter the second number '))

r = int(input("Enter the first number "))
s = int(input('Enter the second number '))

v = int(input("Enter the first number "))
w = int(input('Enter the second number '))

if a == "+":
    print(Testing1.add(p, q))
elif a == '-':
    print(Testing1.subtract(x, y))
elif a == '*':
    print(Testing1.multiply(r, s))

elif a == '/':
    print(Testing1.divide(v, w))


