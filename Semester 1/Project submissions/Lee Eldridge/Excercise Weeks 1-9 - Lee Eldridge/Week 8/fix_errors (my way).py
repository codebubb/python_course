import random
random_numbers = []
size = int(raw_input("How many numbers do you need?"))
limit = int(raw_input("Up to what limit?"))
for r in range(0, size):
    random_num = random.randrange(limit+1)
    random_numbers.insert(len(random_numbers),random_num)
    print "Adding", random_num

random_numbers.sort()

print "Sorted numbers ->>"

for e in random_numbers:
    print e
