
exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56, 45, 14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15]
new_results = []
for n in exam_results:
    if n >= 50:
        new_results.append(n)
        
print new_results


filter(exam_results) 


'''
# or
def passes(n): return n >= 50

print filter(passes, exam_results)

# or

print filter(lambda n: n >=50, exam_results)
'''
