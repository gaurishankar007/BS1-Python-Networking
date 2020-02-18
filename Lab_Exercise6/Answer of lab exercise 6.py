# 1.
A = [2, 4, 88, 35, 53, 98, 7, 60]
B = len(A)


def sum(n):
    if n == 0:
        return n
    else:
        return A[n - 1] + sum(n - 1)


print("Sum=" + str(sum(B)))
# Another way
A = [12, 40, 78, 356, 503, 988, 779, 560]
B = len(A)


def sum1(l, n):
    if n == 0:
        return n
    else:
        return l[n - 1] + sum1(l, n - 1)


print(f"The sum of the list is {sum1(A, B)}.")


# 2.


def multiplication(a, b):
    if b == 1:
        return a
    else:
        return a * b


n = int(input("Enter the range up to which you want the multiplication of 3: "))
if n < 1:
    print("Invalid input.")
for i in range(1, n + 1):
    print(f"{3} * {i} = {multiplication(3, i)}")


# 3.


def sum2(a):
    if a == 0 or a == 1:
        return a
    else:
        return a + sum2(a - 1)


n = int(input("Enter the last integer up to which you want the sum "))
print(f"The sum of the first {n} integer is {sum2(n)}.")


# 4.


def palindrome_string(a, b):
    if a == b:
        return "The given string is palindrome."
    else:
        return 'The given string is not palindrome.'


U = input("Enter any string here ")
A = U.split()
B = "".join(A)
C = len(B)
D = C - 1
E = ''
while D >= 0:
    E = E + B[D]
    D = D - 1
print(palindrome_string(B, E))


# 5.


def palindrome_string(a, b):
    if a == b:
        return "The given number is palindrome."
    else:
        return 'The given number is not palindrome.'


U = int(input("Enter any number here "))
A = str(U).split()
B = "".join(A)
C = len(B)
D = C - 1
E = ''
while D >= 0:
    E = E + B[D]
    D = D - 1
print(palindrome_string(B, E))


# Another Way


def pal(a):
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


String = int(input('Write any number here '))
if pal(str(String)):
    print("The given number is palindrome.")
else:
    print("The given number is not palindrome.")