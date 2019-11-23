# 1.
List = [1, 2, 3, 4, 5]
a = "5 is not in the list."
for i in List[:]:
    if 5 / i == 1:
        a = "5 is in the list."
        break
print(a)

# 2.
a = int(input("Enter the number you have got in the first subject over 60 marks."))
b = int(input("Enter the number you have got in the first subject over 75 marks."))
c = int(input("Enter the number you have got in the first subject over 40 marks."))
d = int(input("Enter the number you have got in the first subject over 60 marks."))
x = a + b + c + d
y = 235
z = (x / 235) * 100
print(f"You have got {x} marks over {y} and the percentage is {z}.")
if z >= 90:
    print("You have got A+.")
elif z >= 80:
    print("You have got A.")
elif z >= 70:
    print("You have got B+.")
elif z >= 60:
    print("You have got B.")
elif z >= 50:
    print("You have got C+.")
elif z >= 40:
    print("You have got c.")
else:
    print("You have failed the exam.")

# 3.
a = int(input("Enter the number "))
if a % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 4.
a = int(input("Enter the first number."))
b = int(input("Enter the second number."))
c = int(input("Enter the third number."))
if a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b > c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

# 5.
a = int(input("Enter the given number"))
x = True
y = False
if a > 0:
    print(x)
elif a < 0:
    print(y)
else:
    print("Zero")

# 6.
a = input("Enter an integer number...")
print(a[-1])

# 7.
a = input('Enter a positive real number...')


# 8.
x = 0
for i in range(3):
    a = int(input("Enter a three digit number..."))
    x = x + a
print(x)

# 9.
a = int(input("Enter the year"))
if a % 4 == 0 and a % 100 != 0:
    print("LEAP YEAR")
elif a % 400 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")

# 10.
a = int(input("Enter the first integer..."))
b = int(input("Enter the second integer..."))
c = int(input("Enter the third integer..."))
if a == b or a == c or b ==c:
    print(0)
else:
    print(f'Sum = {a + b + c}')

# 11.
a = 10**3
print(f"The result of 10**3 is {a}.")

# 12.
x = 5
x += 3
print(f'The value of x after we run x+=3 is {x}')

# 13.
print(f'The result of APPLE > apple is {"APPLE" > "apple"}.')

# 14.
print(f"The result of float(1) is {float(1)}")

# 15.
a = 2
b = 3
c = 4
d = 3
print(f'a) {a == b}')
print(f"b) {a != d}")
print(f"c) {b == d}")
print(f"d) {a != c}")
print(f"e) {a + c}")
print(f"f) {b / d}")
print(f"g) {b > a}")
print(f"h) {a < d}")
print(f"i) {b-a == c-b}")
print(f"j) {b >= d}")
