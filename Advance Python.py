# Slicing List
L = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]
print(L[2:])  # print [333, 4444, 55555, 666666, 7777777, 88888888, 999999999]
print(L[:5])  # print [1, 22, 333, 4444, 55555]
print(L[1:5])  # print [22, 333, 4444, 55555]
print(L[1:5:2])  # print [22, 4444] jumping steps
print(L[:])  # print [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]
print(L[::])  # print [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]
print(L[::-1])  # print reverse [999999999, 88888888, 7777777, 666666, 55555, 4444, 333, 22, 1]

# Slicing Tuple
T = (22, 33, 12, 32, 43, 77)
print(T[0])  # prints 22
print(T[1:5])  # prints (33, 12, 32, 43)
print(T[1:])  # prints (33, 12, 32, 43, 77)
print(T[:3])  # prints (22, 33, 12)
print(T[1:5:2])  # prints (33, 32) jumping steps from front side
print(T[::-2])  # prints (77, 32, 33) jumping steps from back side

# Slicing String
S = "Python is cool"
print(S[0])  # prints ""p""
print(S[1:5])  # prints ""ytho""
print(S[1:])  # prints ""ython is cool""
print(S[:3])  # prints ""Pyt""
print(S[1:5:2])  # prints ""yh""
print(S[:: -1])  # prints ""looc si nohtyP""


# LIST COMPREHENSION:
# L = []
# for i in range(1, 6)
#     L.append(i)
# print(L)

L = [i for i in range(1, 6)]
print(L)

# L = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     L.append(num)
# print(L)

L1 = [int(input("Enter a number: ")) for i in range(5)]
print(L1)

# L2 = [1, 2, 3, 4]
# L3 = []
# for num in L2:
#     L3.append(num**2)

L2 = [1, 2, 3, 4]
L3 = [num**2 for num in L2]
print(L3)

# L4 = [5, 6, 7, 8, 9]
# L5 = []
# for i in L4:
#     if i % 2 == 0:
#         L5.append(i)

L4 = [5, 6, 7, 8, 9]
L5 = [i for i in L4 if i % 2 == 0]
print(L5)

# from random import randint
# L6 = []
# for i in range(5):
#     L.append(randint(1, 10))

from random import randint
L6 = [randint(1, 10) for i in range(5)]
print(L6)


# STRING FORMATTING:
Name = "John"
Age = 22
print("Hello %s, you are %s years old." % (Name, Age))  # Hello John, you are 22 years old.
Weight = 77
print("Name: %s, Age: %s, Weight: %s" % (Name, Age, Weight))  # Name: John, Age: 22, Weight: 77

N = "John the don"
A = 30
W = 72
print("name: %s, age: %d, weight: %d" % (N, A, W))  # name: John the don, age: 30, weight: 72
print("name: %s, age: %d, weight: %04d" % (N, A, W))  # name: John the don, age: 30, weight: 0072

pi = 3.141592653589793
print("pi is %.2f" % pi)  # pi is 3.14
print("pi is %.4f" % pi)  # pi is 3.1416
