print ""
print "Exam Results Average Score:"

exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56, 45, 14,74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15]
total = 0

for i in exam_results:
    total = total + i

print "- - - - - - -"
print "|           |"
print "|   ", total / len(exam_results), "    |"
print "|           |"
print "- - - - - - -"
print "----------------------------------------------------------------------"

view_results = raw_input("Would you like to view the exam results? 'YES' or 'NO': " )
view_results = view_results.upper()
if view_results == "YES":
    print ""
    print "Exam results:"
    print " 21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9"
    print " 35, 47, 56, 45, 14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47"
    print " 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15"
    print ""
    print "There is", len(exam_results), "exam results in the list."
    print "----------------------------------------------------------------------"
else:
    print "----------------------------------------------------------------------"
