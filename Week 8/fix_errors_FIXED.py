import random

random_numbers = []

size  = int(raw_input("How many numbers do you need?"))
limit = int(raw_input("Up to what limit?"))

for r in range(size):
    random_num = random.randrange(limit)
    random_numbers.append(random_num)
    print "Adding", random_num

random_numbers.sort()

print "Sorted numbers ->>"

index = 0
while True:
    print random_numbers[index]
    index += 1
    if index > len(random_numbers) -1 :
        break
    
    