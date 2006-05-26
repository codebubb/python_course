import rand

random_numbers = []

size  = int(raw_input("How many numbers do you need?"))
limit = int(raw_input("Up to what limit?"))

for r in range(1, size)
    random_num = rand.randrange(limit)
    random_numbers.insert(len(random_numbers),random_num)
    print "Adding", random_num

random_number.sort()

print "Sorted numbers ->>"

index = 1
while True:
    print random_numbers[index]
    index += 1
    if index > len(random_numbers):
        break
    
    
