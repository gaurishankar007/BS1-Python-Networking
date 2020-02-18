a = int(13 / 2)
print(a)  # 6
print(int(13.5 / 2))  # 6

print(float(13.5 / 2))  # 6.75

print(round(6.49))  # 6
print(round(6.5))  # 6
print(round(6.51))  # 7
print(round(6.8))  # 7

print(33 == 33.0)  # True


# String
print("xyzadfgigh".endswith("igh"))  # True
print("abc DEF".capitalize())  # Abc def
#prints
#Gauri
#Anuragh
#Shirshak
print("""Gauri   
Anuragh
Shirshak""")  # This is an example of docstring


# Eval
a = '5'
b = '2'
print(eval(a + b))  # 52
print(eval(a) + eval(b))  # 7
print(eval("1" + "2"))  # 12
print(eval(" 1 + 6"))  # 7
c = eval(input("Add two numbers"))  # it prints the sum of the two strings i.e. '2' + '3' = 5
print(c)


# List
List = [1, 2, 3, 4, 5]
print(List*2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# set
a = {1, 2, 3, 4}
a.update([5, 6, 7, 2])
print(a)