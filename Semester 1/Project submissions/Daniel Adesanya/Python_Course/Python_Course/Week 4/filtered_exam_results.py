def p():
        exam_results = [21, 11, 4, 96, 48, 5, 13, 64, 28, 33, 43, 20, 70, 24, 88, 57, 31, 9, 35, 47, 56,
                        45, 14, 74, 3, 6, 79, 62, 17, 8, 5, 8, 44, 56, 60, 47, 17, 23, 96, 66, 17, 43, 7,
                        21, 18, 100, 30, 8, 15, 15]
        exam = raw_input("Would you like to see those who have passed or failed the exam? ").lower()
        if exam == "passed":
                for e in exam_results:
                        if e > 50:
                                print e
        elif exam == "failed":
                for e in exam_results:
                        if e < 50:
                                print e
                p()
p()
