import random

def random_num(n):
    return random.sample(range(100), n)

print random_num(5)
