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

# 9.
a = int(input("Enter the year"))
if a % 4 == 0 and a % 100 != 0:
    print("LEAP YEAR")
elif a % 400 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")
