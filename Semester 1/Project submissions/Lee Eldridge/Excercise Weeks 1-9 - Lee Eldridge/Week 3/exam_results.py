exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56, 45, 14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18, 100, 30, 8, 15, 15]
 
def p():
    results = raw_input("Would you like to: add an exam result (add), view the exam results (view) or find the average of the current scores (average)? ").lower()
    if results == "average":
        print ""
        print "The average of the current exam results is",sum(exam_results) / len(exam_results)
        print ""
    elif results == "view":
        print exam_results
        print ""
    elif results == "add":
        new_result = raw_input("What is the new result you would like to input? ")
        new_result = int(new_result)
        exam_results.append(new_result)
        print "All added thank you!"
    else:
        print "Please enter either add, view or average."
        print ""
    
    p()
    
p()
