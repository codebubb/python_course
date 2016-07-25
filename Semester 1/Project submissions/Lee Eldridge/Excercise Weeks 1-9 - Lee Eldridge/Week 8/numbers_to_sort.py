import time
print "Opening 'exam_results.txt', please wait..."
time.sleep(3)
print "Sorting results..."
time.sleep(3)
with open('exam_results.txt', 'r') as f:
    read = f.read()
    f.close()
print "Opening and Sorting Completed."
print "Here are the list of exam results:"
time.sleep(0.5)
list = read.split()
list = [int(x) for x in list]
list.sort()

for e in list:
    print e
