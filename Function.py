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

# Write a function print a matrix based on user like if user types 3 row and 3 column
# You should print 3*3 matrix with all 1's
a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# Adding lists in an empty list with elements
A = []
for i in range(3):
    A.append([])
    for j in range(3):
        A[i].append(1)
print(A)

# printing average masks
M = [['name', 'maths', 'english', 'physics', 'com', 'nepali'],
     ['john', 88, 86, 76, 66, 76],
     ['sam', 77, 67, 87, 67, 55],
     ['anna', 67, 65, 67, 76, 65],
     ['ben', 87, 78, 67, 77, 57],
     ['jeff', 90, 80, 79, 88, 70]]
# Printing Average Mask In Math
a = 0
for i in range(len(M)):
    if i != 0:
        a = a + M[i][1]
b = a / (len(M)-1)
print(f'The average mask in math of all students is {b}.')
# Printing Total and Average Mask of ben
c = 0
for j in range(len(M[4])):
    if j != 0:
        c = c + M[4][j]
d = c / (len(M[0]) - 1)
print(f'The total mask of ben is {c} and his average mask is {d}.')



