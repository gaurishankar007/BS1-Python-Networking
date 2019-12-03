# you can not write and read at the same time in the same txt file
# In all case the '+' sign means to create a new file if it does not exist
# Creating txt file using python programing language
X = open("A_Text_File.txt", "w+")
X.write("Creating txt file using python programing language \n" "Hahahahha")  # "\n" makes one line space
X.close()

# Create a file name file.txt inside the python project folder you are working on,
# Now open that file using 'r' mode,
# And use read and store in a variable
# Now print that variable
P = open("TextFile.txt", "r")
print(P.read())
P.close()
# Printing in list
Q = open("TextFile.txt", "r")
R = Q.readlines()
print(R)
Q.close()
# printing line by line with specific space
for i in R:
    print(i)
Q.close()

# Writing in the text file
A = open("TextFile1.txt", "w")
A.write("printing Numbers From 0 T0 4 in a line.")
A.write("\n")  # Keeping space between the above written sentence and below numbers
for j in range(5):
    A.write(str(j))
A.write("\n")  # Again keeping space
# writing in the text line by line
A.write("Printing Numbers From 0 To 4 line by line.")
A.write("\n")
for k in range(5):
    A.write(str(k))
    A.write("\n")
A.close()

# Append in python file handling
Q = open("TextFile2.txt", "+a")
Q.write("Practising append \n" "Does this worked?\n" "Yeah! Man,this worked.")


# Use function to get the file in format given below
# Then calculate the total marks, average marks, highest marks in each subjects and the topper name
# 'Name', 'English', 'Chemistry, 'Physics', 'Nepali', 'Drawing'
# 'Ram', '89', '67', '67', '67', '77'
# 'Shyam', '90', '85', '65', '73', '69'
# 'Sita', '96', '75', '59', '86', '77'
# 'Gita', '88', '87', '72', '63', '91'
X = open("Student_Marks.txt", "r")
Y = X.readlines()

a = []
for i in Y:
    a.append(i)  # ["'Name', 'English', 'Chemistry, 'Physics', 'Nepali', 'Drawing' \n", "'Ram', '89', '67', '67', '67', '77' \n", "'Shyam', '90', '85', '65', '73', '69'\n", "'Sita', '96', '75', '59', '86', '77'\n", "'Gita', '88', '87', '72', '63', '91'"]

b = a[0].split()  # ["'Name',", "'English',", "'Chemistry,", "'Physics',", "'Nepali',", "'Drawing'"]
b1 = (''.join(b).replace(',', ' ')).replace("'", "")  # Name English Chemistry Physics Nepali Drawing
b2 = b1.split()  # ['Name', 'English', 'Chemistry', 'Physics', 'Nepali', 'Drawing']

c = a[1].split()  # ["'Ram',", "'89',", "'67',", "'67',", "'67',", "'77'"]
c1 = (''.join(c).replace(',', ' ')).replace("'", "")  # Ram 89 67 67 67 77
c2 = c1.split()  # ['Ram', '89', '67', '67', '67', '77']

d = a[2].split()
d1 = (''.join(d).replace(',', ' ')).replace("'", "")
d2 = d1.split()  # ['Shyam', '90', '85', '65', '73', '69']

e = a[3].split()
e1 = (''.join(e).replace(',', ' ')).replace("'", "")
e2 = e1.split()  # ['Sita', '96', '75', '59', '86', '77']

f = a[4].split()
f1 = (''.join(f).replace(',', ' ')).replace("'", "")
f2 = f1.split()  # ['Gita', '88', '87', '72', '63', '91']
# Printing the total marks and the average marks of each students
cc = 0
dd = 0
ee = 0
ff = 0
for i in c2:
    if i != "Ram":
     cc = cc + int(i)
print(f"The total marks of Ram is {cc} and average marks is {cc / 5}.")
for j in d2:
    if j != "Shyam":
        dd += int(j)
print(f"The total marks of Shyam is {dd} and average marks is {dd / 5}.")
for k in e2:
    if k != "Sita":
     ee += int(k)
print(f"The total marks of Sita is {ee} and average marks is {ee / 5}.")
for l in f2:
    if l != "Gita":
        ff += int(l)
print(f"The total marks of Gita is {ff} and average marks is {ff / 5}.")
# printing the highest marks in each subjects
if int(c2[1]) > int(d2[1]) and int(c2[1]) > int(e2[1]) and int(c2[1]) > int(f2[1]):
    temp = int(c2[1])
elif int(d2[1]) > int(c2[1]) and int(d2[1]) > int(e2[1]) and int(d2[1]) > int(f2[1]):
    temp = int(c2[1])
elif int(e2[1]) > int(c2[1]) and int(e2[1]) > int(d2[1]) and int(e2[1]) > int(f2[1]):
    temp = int(e2[1])
else:
    temp = int(f2[1])
print(f"The highest marks in English is {temp}.")
if int(c2[2]) > int(d2[2]) and int(c2[2]) > int(e2[2]) and int(c2[2]) > int(f2[2]):
    temp = int(c2[2])
elif int(d2[2]) > int(c2[2]) and int(d2[2]) > int(e2[2]) and int(d2[2]) > int(f2[2]):
    temp = int(c2[2])
elif int(e2[2]) > int(c2[2]) and int(e2[2]) > int(d2[2]) and int(e2[2]) > int(f2[2]):
    temp = int(e2[2])
else:
    temp = int(f2[2])
print(f"The highest marks in Chemistry is {temp}.")
if int(c2[3]) > int(d2[3]) and int(c2[3]) > int(e2[3]) and int(c2[3]) > int(f2[3]):
    temp = int(c2[3])
elif int(d2[3]) > int(c2[3]) and int(d2[3]) > int(e2[3]) and int(d2[3]) > int(f2[3]):
    temp = int(c2[3])
elif int(e2[3]) > int(c2[3]) and int(e2[3]) > int(d2[3]) and int(e2[3]) > int(f2[3]):
    temp = int(e2[3])
else:
    temp = int(f2[3])
print(f"The highest marks in Physics is {temp}.")
if int(c2[4]) > int(d2[4]) and int(c2[4]) > int(e2[4]) and int(c2[4]) > int(f2[4]):
    temp = int(c2[4])
elif int(d2[4]) > int(c2[4]) and int(d2[4]) > int(e2[4]) and int(d2[4]) > int(f2[4]):
    temp = int(c2[4])
elif int(e2[4]) > int(c2[4]) and int(e2[4]) > int(d2[4]) and int(e2[4]) > int(f2[4]):
    temp = int(e2[4])
else:
    temp = int(f2[4])
print(f"The highest marks in Nepali is {temp}.")
if int(c2[5]) > int(d2[5]) and int(c2[5]) > int(e2[5]) and int(c2[5]) > int(f2[5]):
    temp = int(c2[5])
elif int(d2[5]) > int(c2[5]) and int(d2[5]) > int(e2[5]) and int(d2[5]) > int(f2[5]):
    temp = int(c2[5])
elif int(e2[5]) > int(c2[5]) and int(e2[5]) > int(d2[5]) and int(e2[5]) > int(f2[5]):
    temp = int(e2[5])
else:
    temp = int(f2[5])
print(f"The highest marks in Drawing is {temp}.")
# Printing the topper name
if cc > dd and cc > ee and cc > ff:
    temp = "Ram"
elif dd > cc and dd > ee and dd > ff:
    temp = "Shyam"
elif ee > cc and ee > dd and ee > ff:
    temp = "Sita"
else:
    temp = "Gita"
print(f"And the topper name is {temp}.")

