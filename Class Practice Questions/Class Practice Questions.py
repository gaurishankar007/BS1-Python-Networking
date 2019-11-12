# 1.
a = input("Enter the first number")
b = input("Enter the second number")
c = int(a)+int(b)
print("The required sum is "+str(c))

# 2.
l = input("Enter the length")
b = input("Enter the bridth")
c = int(l)*int(b)
print("The required Area is "+str(c))

# 3.
a = input("Enter your name")
print("Hello "+a+",have a nice day!")

# 4.
x = int(input("Enter the value of x"))
y = int(input("Enter the value of y"))
z = x**3+3*x**2*y+3*x*y**2+y**3
print("The required result is "+str(z))

# 5.
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
x = (-b+(b**2-4*a*c)**.5)/(2*a)
y = (-b-(b**2-4*a*c)**.5)/(2*a)
print("The required solutions of the given quadratic equation are "+str(x)+","+str(y))