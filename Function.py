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

# Printing the numbers from the list one by one
A = [[1, 2, 3, 4], [5, 6, 7, 8, 9]]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j])
# Another Way
B = [[2, 3, 4], [6, 7, 8]]
for row in B:
    for element in row:
        print(element)

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
x = input("Enter a leter")
y = buha(x)
if y.isupper():
    print("upper")
else:
    print("lower")