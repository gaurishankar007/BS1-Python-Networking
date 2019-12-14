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
# Adding two list
L1 = [8, 9]
L2 = [4, 5]
L3 = L1 + L2
print(L3)

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
L = [6, 3, 6, 8, 9, 2, 1,3]
L.remove(3)
print(L1)
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
        if i == '1':
            if j == 'a':
                L.append(a)
        elif i == "2":
            if j == 'b':
                L.append(a)
        elif i == "3":
            if j == 'c':
                L.append(a)
        elif i == "4":
            if j == 'd':
                L.append(a)
        elif i == "5":
            if j == 'e':
                L.append(a)
        else:
            L.append(a)
print(L)

# Sorting and printing the items of the list by ascending and descending
a = [1, 2, 5, 8, 9, 45, 67, 0, 3, 7, 4, 25]
print(sorted(a))
print(sorted(a, reverse=True))

b =['a', 'N', 'g', 'A', 'h', 'mobile', 'vision', 'Mango', 'Car']
print(sorted(b))
print(sorted(b, reverse=True))













