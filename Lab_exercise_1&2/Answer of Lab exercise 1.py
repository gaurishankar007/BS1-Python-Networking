# 1.
x = 0
for i in range(3):
     a = int(input("Enter the number "))
     x = x + a
print(x)

# 2.
a = int(input("Enter the length of  the base "))
b = int(input('Enter the length of the height '))
x = (a * b) / 2
print(x)

# 3.
a = int(input("Enter the total number of students "))
b = int(input("Enter the total number of apples taken "))
x = b // a
y = b % a
print(f"Each students will get {x} apple and the remaining apple in the basket are {y}.")

# 4.
a = int(input("Enter the number of minutes passed since midnight "))
b = a // 60
c = a % 60
for i in range(a):  # Here, for loop repeats the if condition the number of times you have entered.
    if b > 23:
        b = b - 23
    else:
        break  # Here, break stops the if condition when it becomes unsatisfied.
print(str(b) + ':' + str(c))

# 5.
a = int(input("Enter the number of students in class A "))
b = int(input("Enter the number of students in class B "))
c = int(input("Enter the number of students in class C "))
x = a // 2
if a % 2 != 0:
    x = x + 1
y = b // 2
if b % 2 != 0:
    y = y + 1
z = c // 2
if c % 2 != 0:
    z = z + 1
print(x + y + z)

# 6.Finding a person body mass index(BMI)
x = float(input("Enter the weigh of your body in kg "))
y = float(input("Enter the height of your body in meter "))
z = x / (y**2)
print("Your BMI is " + str(z))

# 7.
a = 4  # Distance in miles
b = 25  # Bus Speed in mph
x = b / 60 # Bus speed in mile per minute
c = 10  # Total stops
d = 2  # Time taken in each stops in minute
e = (a / x) + c * d
print(f"The total time taken in the bus journey is {e} minutes.")
# Another
Fh = 7  # Speed of jogging to the first mile in mph
Fs = Fh / 60  # Speed of jogging to the first mile in mile per minute
Sh = 15  # Speed of jogging to the next two miles in mph
Ss = Sh / 60  # Speed of jogging to the next two miles in mile per minute
ee = (2 / Fs) + (2 / Ss)
print(f"Total time taken to reach the university by jogging is {ee} minutes.")
print("Thus,jogging will be quicker than the bus.")

# 8.
r = int(input("Enter the radius of the circle "))
PI = 22 / 7
A = PI * r**2
print("The Area of the circle is " + str(A))

# 9.
a = int(input("Enter the number up to which you want the sum "))
Sum = (a * (a + 1)) / 2
print(Sum)
# Another way using for loop
b = 1
for i in range(2, a + 1):
    b = b + i
print(b)

# 10.
x = int(input("Enter the Seconds "))
a = x / 60
if a > 1:
    print(str(a) + " Minutes")
else:
    print(str(a) + " Minute")
b = x / 3600
if b > 1:
    print(str(b) + " Hours")
else:
    print(str(b) + " Hour")
c = x / 86400
if c > 1:
    print(str(c) + " Days")
else:
    print(str(c) + " Day")




