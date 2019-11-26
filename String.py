# get an input from user an capitalize all of them,
# Similarly iterate them and print individually,
A = input("Enter a word..")
print(len(A))  # print the number of letter in the word(it will also count the space between the two words)
print(A[3])
print(A.upper())
print(A.lower())
for i in A:
    print(i)

# Other basic operations on strings
a = "Gauri Shankar Sharma'"
b = a.replace("G", "g")
print(b)
print(a.count('a'))  # prints the number of 'a'
print(a.count('r'))  # prints the number of 'r'
c = list(a)
print(c)  # stores the every letter of the string in a list even the space between the word like:'i', ' ', 's', 'h'
print(c.count("S"))
d = "".join(c)  # joining all the elements of the list and making it string again
print(d)
e = "*".join(c)  # joining all the element of the list with '*' and making it string again


# Join different words together like:"Today is Monday"=>'TodayisMonday'
# Replace Today with Yesterday
# join the words in this way:Today#is#Monday
# Now split this word in to Today is Monday again
B = "Today is Monday"
x = B.split()  # Splitting the every word of the sentence and putting them in a list
print(x)
y = "".join(x)  # printing "TodayisMonday"
print(y)
C = B.replace("Today", "Yesterday")
print(C.replace("is", "was"))  # Printing "Today was Monday"
D = "#".join(x)
print(D)  # printing "Today#is#Monday"
E = D.replace("#", " ")
print(E)
F = B.split(" ")   # Splitting the every word of the sentence and putting them in a list
print(F)
