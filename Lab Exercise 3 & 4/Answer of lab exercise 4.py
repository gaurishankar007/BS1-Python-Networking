# ITERATION AND COLLECTION:
# 1.
A = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        A.append(i)
print(A)

# 2.
F = int(input("Enter the temperature in fahrenheit"))
C = (5 / 9) * (F - 32)
print(f"{C} degree celsius.")

# 3.
X = 6
for i in range(1, 10):
    Y = int(input("Guess a number between 1 and 9..."))
    if Y == 6:
        print("Well Guessed!")
        break
# 4.
P = int(input("Enter the maximum number of '*' you want at the middle "))
Q = ''
for i in range(1, P + 1):
    Q = Q + "*"
    print(Q)
L = list(Q)
for j in range(P - 1, 0, -1):
    del(L[j])
    S = "".join(L)
    print(S)

# 5.
A = input("Write any word ")
b = len(A)
c = b-1
d = ''
while c >= 0:
    d = d + A[c]
    c = c - 1
print(d)

# 6.
x = int(input("Enter the starting number..."))
y = int(input("Enter the ending number..."))
A = []
B = []
for i in range(x, y + 1):
    if i % 2 == 0:
        A.append(i)
for j in range(x, y + 1):
    if j % 2 != 0:
        B.append(j)
print(f"The number of EVEN Numbers is {len(A)} and ODD Numbers is {len(B)}")

# 7.
A = []
for i in range(0, 7):
    A.append(i)
A.remove(3)
A.remove(6)
for j in A:
    print(j)

# 8.
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
x = 10
for i in range(x):
    print(fibonacci(i))

# 9.
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)
P = int(input("Enter the number of which you want to calculate the factorial..."))
if P < 0:
    print("Murkha Manushya! don't you know that the factorial of negative number doesn't exist, Aahahahha.")
elif P == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {P} is {factorial(P)}.")

# 10.
String = input("Enter a string containing both digits and letters...")
L1 = []
L2 = []
for i in String:
    L1.append(i)
    if i.isupper() == True or i.islower() == True:
        L2.append(i)
        L1.remove(i)
print(f"The number of letters is {len(L2)}.")
print(f"The number of digits is {len(L1)}.")



# LIST:
# 1, 2.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
y = 1
for i in A:
    x = x + i
    y = y * i
print(f'The sum of the all the items in the list is {x}.')
print(f'The multiplies of all the items in the list is {y}.')

# 3, 4.
B = [4, 6, 9, 15, 89, 10, 5, 46, 12]
for i in range(len(B)):
    if B[0] > B[1] and B[0] > B[i]:
        temp = B[0]
    elif B[1] > B[2]and B[1] > B[i]:
        temp = B[1]
    elif B[2] > B[3] and B[2] > B[i]:
        temp = B[2]
    elif B[3] > B[4] and B[3] > B[i]:
        temp = B[3]
    elif B[4] > B[5] and B[4] > B[i]:
        temp = B[4]
    elif B[5] > B[6] and B[5] > B[i]:
        temp = B[5]
    elif B[6] > B[7] and B[6] > B[i]:
        temp = B[6]
    elif B[7] > B[8] and B[7] > B[i]:
        temp = B[7]
    else:
        temp = B[8]
print(f"The largest number in the list is {temp}.")
for j in range(len(B)):
    if B[0] < B[1] and B[0] < B[j]:
        temp = B[0]
    elif B[1] < B[2]and B[1] < B[j]:
        temp = B[1]
    elif B[2] < B[3] and B[2] < B[j]:
        temp = B[2]
    elif B[3] < B[4] and B[3] < B[j]:
        temp = B[3]
    elif B[4] < B[5] and B[4] < B[j]:
        temp = B[4]
    elif B[5] < B[6] and B[5] < B[j]:
        temp = B[5]
    elif B[6] < B[7] and B[6] < B[j]:
        temp = B[6]
    elif B[7] < B[8] and B[7] < B[j]:
        temp = B[7]
    else:
        temp = B[8]
print(f"The smallest number in the list is {temp}.")

# 5.
C = ['madam', 'yeah', 'buhaha', 'dad', '9089', 'python']
D = []
for i in range(len(C)):
    if C[i][0] == C[i][-1]:
        D.append(C[i])
print(len(D))

# 6.
E = []
F = [1, 2, 3, 4, 5]
if len(E) == 0:
    print("List E is empty.")
else:
    print("List E is not empty.")
if len(F) == 0:
    print("List F is empty.")
else:
    print("List F is not empty.")

# 7.
G = [1, 2, 'Ram', 'Mango', 7, 0, 'Top']
F = G.copy()
print(F)

# 8.
H = [1, 4, 98, 374, "Sir", 653, 0, "House"]
del(H[0])
del(H[3:5])
print(H)

# 9.
Lis = [1, 5, False, 5.9, "help", True, "Hahahaha"]
import random
print("random.choice() to select random item from list - ", random.choice(Lis))
print("random.choice() to select random item from list - ", random.choice(Lis))



# TUPLE:
# 1.
p = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(p)

# 2.
q = ("Star", True, False, 1, 8.9)
print(p)

# 3.
a = (0, -1, -2, -3, -4, -5, -6, -7, -8, -9)
print(a[-6])

# 4.
b = ('orange', 4, 26, 'oh!', 685, 'ram', 0, 9)
for i in b:
    print(i)

# 5.
# Tuple once created, it is immutable.
# So, items can not be directly added in to a tuple.
# But if there is any item that is list in the tuple, then you can add items in that list weather it is empty or not
Tuple = (78, False, 99.99, [5], "I")
from copy import deepcopy
Tuple1 = deepcopy(Tuple)
Tuple1[3].append(358)
print(Tuple1)

# 6.
X = (1, 2, 'Gauri', 3, 4, 5, "BlaBla")
Y = []
for i in X:
    Y.append(str(i))
Z = " ".join(Y)
print(Z)

# 7.
x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(x[3])
print(x[-4])

# 8.
Tuple = (78, False, 99.99, [], "I")
from copy import deepcopy
New_Tuple = deepcopy(Tuple)
New_Tuple[3].append("Gauri")
New_Tuple[3].append(358)
print(New_Tuple)



# SET:
# 1, 2.
x = {1, 22, 333, 4444, 55555}
print(x)
for i in x:
    print(i, end=' ')  # The "end=' '" will iterate the value of 'i' in a line with space
# 3, 4.
a ={"a", 2, "b", 9, 10, "x"}
b = {"s"}
c = a.union(b)
print(c)
print(c.difference(b))

# 5.
y = {'Gauri', 5, "Shankar", 0, 10.5, "Bro"}
if "Gauri" in y:
    z = {"Gauri"}
    print(y.difference(z))
if 10 in y:
    z = {10}
    print(y.difference(z))

# 6.
a = {1, 2, 3, 4, 5, 'A', 'B'}
b = {2, 3, 5, 7, 11, 'B', 'C'}
print(a.intersection(b))


# DICTIONARY:
# 1.
D = {}

# 2.
D1 = {"Name": ["Bikesh", "Harichandra", "Gauri", "Prabesh"], "Roll No.": [47, 8, 34, 23]}
D1["Age"] = [56, 58, 18, 256]
print(D1)

# 3.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
for i in (dic2, dic3):
    dic1.update(i)
print(dic1)

# 4.
D4 = {'Name': "GauriShankarSharma", 'BankBalance': 10000000000}
if "Name" in D4:
    for i in D4.keys():
        if i == "Name":
            print(i)
if "BankBalance" in D4:
    for j in D4.keys():
        if j != "Name":
            print(j)
if "Apple" in D4:
    for i in D4.keys():
        if i == "Gauri":
            print(i)

# 5.
D5 = {"Student Name": ["Ram", "Memo", "Dita"], "Marks": [39, 46, 45]}
for i, j in D5.items():
    print(i + ":", j, end=', ')

# 6.
D6 = {}
x = int(input("Enter the number from 1 to ..."))
for i in range(1, x + 1):
    a = i**2
    D6.update({i: a})
print(D6)

# 7.
D7 = {}
for i in range(1, 16):
    a = i**2
    D7.update({i: a})
print(D7)

# 8.
d1 = {"Fruits": 'Watermelon', "Roll No.": 21}
d2 = {"Batch": "27A", "Subject": "Introduction to computing"}
D8 = d1.copy()
D8.update(d2)
print(D8)

# 9.
D9 = {"Student Name": ["Ram", "Memo", "Dita"], "Marks": [39, 46, 45]}
for i, j in D9.items():
    print(i + ":", j, end=', ')

# 10.
a = 0
b = 0
D10 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for i in D10.keys():
    a = a + i
for j in D10.values():
    b = b + j
print(a + b)