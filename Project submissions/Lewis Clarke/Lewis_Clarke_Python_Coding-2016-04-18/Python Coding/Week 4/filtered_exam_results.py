exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88,
 57, 31, 9, 35, 47, 56, 45, 14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44,
  56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15]

exam_pass = []
for x in exam_results:
    if x >= 50:
        exam_pass.append(x)
print exam_pass
print len(exam_pass)
