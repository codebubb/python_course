import random

a = random.randrange(20)

list_of_numbers = []
for i in range(a):
    list_of_numbers.append(random.randrange(100))

while True:
    try:
        pick = int(raw_input("Pick a number you want to display:"))
        print list_of_numbers[pick], "is the number you're looking for!"
    except (IndexError, ValueError):
        print "Please only enter numbers under", a
