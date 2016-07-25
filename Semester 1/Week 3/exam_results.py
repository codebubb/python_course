'''
exam_results.py
---------------
Calculate the average of a set of exam results.
'''

# Our list of exam results
exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56, 45, 14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15]


# Numbers to perform the average calculation
number_of_results = len(exam_results)
total_score = 0

for n in exam_results:
    total_score += n # Keep track of the running total

print "The average of the exam results is:", total_score / number_of_results

# or...
# print "The average of the exam results is:", sum(exam_results) / number_of_results
