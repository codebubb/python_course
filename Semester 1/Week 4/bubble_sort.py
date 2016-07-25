'''
bubble_sort.py
--------------
Unomptimised bubble sort algorithm

'''
import time

results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56, 45, 14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15]

print results

time.sleep(2)

while True:
    swapsHappened = 0 # Keep track of if a swapped has occured on this 'pass'
    for i in range(len(results)-1): 
        if results[i] > results[i+1]:
            #print ">>>",results[i], "swapped with", results[i+1]
            results[i], results[i+1] = results[i+1], results[i] # Swapping values over
            swapsHappened += 1
    print results
   # time.sleep(2)
    if not swapsHappened: # Stop when no more swaps have occurred
        break
    
print "Finished."
