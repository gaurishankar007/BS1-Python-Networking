# Printing numbers from the set
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(len(a))
print(sum(b))
print(max(b))
print(min(b))
print(a.update([6, 7, 8, 9]))

# Create a 3 sets for fruits, with random items, now, i need to get data how many items among the  sets are repeated
# And how many of them are unique, in total get all the unrepeated items
F1 = {'apple', 'orange', 'Guava'}
F2 = {'Mango', 'Graves', 'orange'}
F3 = {'orange', 'pineapple', 'watermelon'}
if F1.intersection(F2) == F2.intersection(F3):
    print("The repeated item is", F1.intersection(F2))
    print("The number of the repeated items is ", len(F1.intersection(F2)))
x = F1.union(F2)
y = F2.union(F3)
print("All the unique items are", x.union(y))
a = F1.symmetric_difference(F2)
b = F2.symmetric_difference(F3)
print("The unrepeated items are", a.union(b))