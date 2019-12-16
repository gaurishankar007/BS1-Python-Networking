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

#
B = (1, 2, 3, 4, 5)
print(sum(B))
print(max(B))
print(min(B))

# exchanging the value of a and b
a = 4
b = 5
(a, b) = (b, a)
print(a)
print(b)
# Creating colon of a tuple
Tuple = (78, False, 99.99, [], "I")
from copy import deepcopy
New_Tuple = deepcopy(Tuple)
New_Tuple[3].append("Gauri")
New_Tuple[3].append(358)
print(New_Tuple)

#
B = ("a")
print(B)  # It will print 'a' only not ("a") because B is string not tuple until you gave a comma at the end in this case
C = ("a",)
print(C)