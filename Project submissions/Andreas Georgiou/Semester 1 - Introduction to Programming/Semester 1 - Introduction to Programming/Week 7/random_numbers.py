import random

def rand_list(values):
    for num in range(values):
        print random.randrange(1,101)
        
rand_list(input("How many random number would you like to display? "))
