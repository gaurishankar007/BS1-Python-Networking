# Creating txt file using python programing language
X = open("A_Text_File.txt", "w+")
X.write("Creating txt file using python programing language")
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