# Q.NO.1
def max(a, b, c):
    x = a > b and a > c
    y = b > a and b > c
    z = c > a and c > b
    return x, y, z
p = int(input("Enter the first numbers"))
q = int(input("Enter the second numbers"))
r = int(input("Enter the third numbers"))
S = max(p, q, r)
if S[0] == True:
    print("Max number is " + str(p))
if S[1] == True:
    print("Max number is " + str(q))
else:
    print("Max number is " + str(r))

# Q.NO.2
def fizz_buzz(a):
    x = a % 3 == 0
    y = a % 5 == 0
    z = a % 3 == 0 and a % 5 == 0
    return x, y, z
p = int(input("Enter a number"))
q = fizz_buzz(p)
if q[2] == True:
    print("FizzBuzz")
elif q[0] == True:
    print("Fizz")
elif q[1] == True:
    print("Buzz")
else:
    print(p)


# Q.NO.3
A = []
x = int(input("Enter the limit..."))
for i in range(x):
    j = str(i)
    A.append(j)
    if i % 2 == 0:
        A[i] = A[i] + " EVEN"
    elif i % 2 != 0:
        A[i] = A[i] + " ODD"
    else:
        break
for j in A:
    def showNumbers(a):
        limit = a
        return limit
    b = j
    c = showNumbers(b)
    print(c)

# Q.NO.4
def showNumbers(a):
    x = a
    return x
p = int(input("Enter the limit..."))
q = showNumbers(p)
r = 0
for i in range(1, q + 1):
    if i % 3 == 0 or i % 5 == 0:
        r = r + i
print(r)

# Q.NO.5
def show_stars(rows):
    p = rows
    return p
a = int(input("Enter a number..."))
b = show_stars(a)
x = ''
for i in range(b):
   x = x + "*"
   print(x)

# Q.NO.6
A = input("Write any word ")
b = len(A)
c = b-1
d = ''
while c >= 0:
    d = d + A[c]
    c = c - 1
print(d)

# Q.NO.7
A = input("Write a word...")
x = ""
y = ''
for i in range(len(A)):
    if A[i].isupper() == True:
        x = x + A[i]
print(f'The number of upper case is {len(x)}.')
for j in range(len(A)):
    if A[j].islower() == True:
        y = y + A[j]
print(f'The number of lower case is {len(y)}.')
# Q.NO.8
x = int(input("Enter a number..."))
a = True
for i in range(2, x):
    if x % i == 0:
        a = False
if a == True:
    print("This is a prime number.")
else:
    print("This is not a prime number.")

# Q.NO.9
A = input("Write any word ")
B = A.split()
C = "".join(B)
x = len(C)
y = x-1
z = ''
while y >= 0:
    z = z + C[y]
    y = y - 1
if C == z:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")

# Q.NO.10
P = input("Write any word...")
for i in range(len(P)):
    if i % 2 == 0:
        print(P[i])

# Q.NO.11
def factorial(x):
    cal = x
    return cal
p = int(input("Enter a number..."))
q = 1
for a in range(2, p + 1):
    q = q * a
z = factorial(q)
print(z)

