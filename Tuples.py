A = ("python", 2, 1, 23, 43, 4)  # Here 'A' is Tuple
print(A)
print(len(A))
print(A[0])
print(A[-1])
# A[1] = 4  # gives error, can’t modify tuples
# A.append(12)  # error, can’t modify tuples
for i in A:
    print(i)
for j in range(len(A)):
    print(A[j])
# exchanging the value of a and b
a = 4
b = 5
(a, b) = (b, a)
print(a)
print(b)