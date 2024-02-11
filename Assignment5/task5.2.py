import random

myList = []

for i in range(10):
    myList.append(random.randint(1, 100))

print(min(myList), max(myList))

