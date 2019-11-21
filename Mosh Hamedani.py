Name = input("what is your name? ")
Favorite_Colour = input("What is your favorite colour? ")
print(Name + " likes " + Favorite_Colour + " .")

Weight_in_pound = input("what is your weight? ")
Weight_in_kilograms = int(Weight_in_pound)/2.2046
print("You  are " + str(Weight_in_kilograms) + " kilograms.")

a = """
Hi,John 
How are you today?
You looks desperate.
What happened man?"""
print(a)
#
Name = "Gauri Shankar Sharma"
print(Name[0])
print(Name[6])
print(Name[-1])
print(Name[-8])
print(Name[0:4])
print(Name[0:5])
print(Name[0:9])
print(Name[:])
print(Name[1:9])
print(Name[3:5])
print(Name[8:])
print(Name[6:-1])
print(Name[2:-4])

#
a = 'Gauri'
b = "Shankar"
c = 'Sharma'
print(f"{a} [{b}] {c} is a bachelor student in Softwarica College.")
# The another way
z = a + " [" + b + "] " + c + "is a bachelor student in Sofwarica College."
print(z)