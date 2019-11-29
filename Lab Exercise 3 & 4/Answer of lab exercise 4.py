# 1.
A = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        A.append(i)
print(A)

# 2.
F = int(input("Enter the temperature in fahrenheit"))
C = (5 / 9) * (F - 32)
print(f"{c} degree celsius.")

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
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))
Number_of_n= 10
# check if the number of terms is valid
if Number_of_n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(Number_of_n):
        print(fibo(i))

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
