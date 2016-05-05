'''
insertion_sort.py
-----------------
Simple implementation of insertion sort
'''
import random
import time

unsorted_numbers = [random.randrange(100) for n in range(10)] # Get 10 random numbers

print unsorted_numbers

for i in range(len(unsorted_numbers)):
    j = i
    while j > 0 and unsorted_numbers[j-1] > unsorted_numbers[j]:
        print "Swapping", unsorted_numbers[j], "with", unsorted_numbers[j-1]
        unsorted_numbers[j], unsorted_numbers[j-1] = unsorted_numbers[j-1], unsorted_numbers[j]
        j -=1
    time.sleep(2)
    print unsorted_numbers

print "Finished."

