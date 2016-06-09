##############
# BINGO
# Version 1
# Created by Andreas Georgiou
##############

import random

num_so_far = []

def rand_num():
    global num_so_far
    random_num = random.randrange(0,30)
    print "\n", random_num
    print set(num_so_far)
   
    
    if raw_input("Press 'Enter' to draw another number.") == "":
        num_so_far.append(random_num)
        rand_num()
        
rand_num()
