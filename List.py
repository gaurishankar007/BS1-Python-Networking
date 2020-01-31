A = [[1, 2, 3, 4, 5], "anup", "bishnu"]
# printing the particular items from the list
print(A[0])
print(A[0][4])
print(A[1])
print(A[2][4])
for i in A[0]:
    print(i)
for j in A[2]:
    print(j)

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

# Printing the items from the list randomly
import random
print(random.choice(A))
print(random.choice(A))
# Finding how many items are in the list
print(len(A))
# Adding items in the list one by one
A.append(6)
print(A)
for i in range(7, 16):
    A.append(i)
# Replacing the item of the list with another one
A[2] = 5
print(A)
# Adding multiple items in the list
L = [2, 1]
L.extend([0, 6])
print(L)
# Concatenating two list
L1 = [8, 9]
L2 = [4, 5]
L3 = L1 + L2
print(L3)

# Making empty list
N = []
print(N)
O = list()
print(O)
# Some other inbuilt function in list
A = [1, 2, 3, 4, 5]
print(sum(A))  # Gives the sum of all the integer in the list
print(max(A))  # Prints the maximum value of the list
print(min(A))  # Prints the minimum value of the list

# Checking whether a element is in the List or not
L = ["apple", "orange", "Mango", "banana"]
if "orange" in L:
    print("orange is in the list")
else:
    print("orange is not in the list")
if "banana" in L:
    print("banana is in the list")
else:
    print("banana is not in the list")
if "graves" in L:
    print("graves is in the list")
else:
    print("graves is not in the list")

# Adding the number given in the list
L = [22, 33, 44, 55]
A = 0
for i in L:
    A += i
print(A)
# In this process "len" just count the position number of items in the List
B = 0
for j in range(len(L)):
    B += L[j]
print(B)

# In this process "len" just count the position number of items in the List.
# For example there are 4 items in "L" Show len gives 0,1,2,3 as result
L = [22, 33, 44, 55]
for j in range(len(L)):
    print(j)

# Removing items from the list
# using del
L1 = [1, 2, 3, 4, 5, 6, 7]
del(L1[3])
print(L1)
L2 = ["a", "b", 'c', 'd', "a"]
del(L2[1:4])
print(L2)
# Using pop
L1 = [1, 2, 3, 4, 5, 6, 7]
for i in range(-3, 0):
    L1.pop(i)
print(L1)
#
LL = [6, 3, 6, 8, 9, 2, 1,3]
LL.remove(3)
print(LL)
# Removing all the elements of the list
Lis = [1, 3.6, 8, "Hah", True]
Lis.clear()
print(Lis)

# Removing odd numbers from the list
L1 = [1, 2, 3,4, 5, 6, 7, 8, 9]
for i in L1:
    if i % 2 != 0:
        L1.remove(i)
print(L1)

# Class Work
L1 = [1, "red", 2, 3]
L2 = ["apple", "orange", "Mango"]
L3 = ["php", 'python', "java"]
# Concatenate
print(L1+L2)
# Adding L1 in L2
L2.extend(L1)
print(L2)
# Adding a programing language in L3
L3.append("c")
print(L3)
# Removing unwanted data from L1
L1.remove("red")
print(L1)
# printing all the items of the list
L4 = ["apple", "orange", "Mango", "banana"]
for fruit in L2:  # You can write anything instead of "fruit"
    print(fruit)

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
L = []
L1 = ["1", "2", "3", "4", "5"]
L2 = ['a', 'b', 'c', 'd', 'e']
for i in L1[:]:
    for j in L2:
        a = i + j
        if i == '1' and j == 'a':
            L.append(a)
        elif i == "2" and j == 'b':
            L.append(a)
        elif i == "3" and j == 'c':
            L.append(a)
        elif i == "4" and j == 'd':
            L.append(a)
        elif i == "5" and j == 'e':
            L.append(a)
print(L)

# Sorting and printing the items of the list by ascending and descending
a = [1, 2, 5, 8, 9, 45, 67, 0, 3, 7, 4, 25]
print(sorted(a))
print(sorted(a, reverse=True))

b =['a', 'N', 'g', 'A', 'h', 'mobile', 'vision', 'Mango', 'Car']
print(sorted(b))
print(sorted(b, reverse=True))


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












