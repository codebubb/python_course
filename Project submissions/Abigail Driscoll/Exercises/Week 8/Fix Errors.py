import random

random_numbers = []
size = int(input("How many numbers do you need? "))
size += 1
limit = int(input("Up to what limit? "))
for r in range(1, size):
    random_num = random.randrange(limit)
    random_numbers.insert(len(random_numbers), random_num)
    print("Adding", random_num)
random_numbers.sort()
print("Sorted numbers ->>")
index = 1
while True:
    print(random_numbers)
    index += 1
    if index > len(random_numbers):
        break
