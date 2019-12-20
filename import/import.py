import math
print(math.cos(0))
print(math.sin(30))
print(math.tan(45))

print(math.factorial(6))
print(math.gcd(195, 130))

import datetime
print(datetime.datetime.now())  # prints the whole date and time
print(datetime.datetime.now().year)  # prints the year
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

import random  # importing the whole library
print(random.randint(1, 10))  # Generates number from 1 to 10 prints a number randomly

from random import randint  # importing only a certain function from the library
print(randint(1, 10))