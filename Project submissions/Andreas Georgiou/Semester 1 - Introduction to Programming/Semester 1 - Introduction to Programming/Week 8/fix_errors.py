import random

random_numbers = []

size = int(raw_input("How many numbers do you need?"))
limit = int(raw_input("Up to what limit?"))

for r in range(1, size +1):
    random_num = random.randrange(1, limit +1)
    random_numbers.insert(len(random_numbers),random_num)
    print "Adding", random_num

random_numbers.sort()

print "\n", "Sorted numbers ->>"

for n in random_numbers:
    print n
