import random
import math

print random.random()

print random.random()

print random.random()

print math.ceil(random.random())

print random.random()


rand_float = random.random()

floor_num = math.floor(rand_float)

print floor_num


print int(random.random() * 10) + 1 #must add 1 otherwise the number will be 0 - 9

print random.randrange(1,26)# return a random number between the cumber in the range



colours = ['green', 'red', 'blue', 'purple', 'orange']
print colours[ random.randrange(len(colours)) ]

print random.choice(colours)
