exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56, 45,
                14, 74, 35, 6, 79, 62, 17, 83, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7, 21, 18,
                100, 30, 8, 15, 15]
 
def p():
    results = raw_input("Would you like to: add an exam result (add), view the exam results (view), see how many have passed (pass) or find the average of the current scores (average)? ").lower()
    if results == "average":
        print ""
        print "The average of the current exam results is",float(sum(exam_results)) / float(len(exam_results))
        print ""
    elif results == "view":
        print exam_results
        print ""
    elif results == "add":
        new_result = raw_input("What is the new result you would like to input? ")
        new_result = int(new_result)
        exam_results.append(new_result)
        print "All added, thank you!"
    elif results == "pass":
        count = 0
        for values in exam_results:
            if values > 50:
                count = count + 1
                print values
        print ""
        print "The total amount of students who achieved over 50% and therefore passed is", str(count) + "."
        print ""
            
    else:
        print "Please enter either add, view or average."
        print ""
    
    p()
    
p()
