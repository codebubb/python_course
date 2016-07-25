print "Choose any two number you would like to multiply!"
print "-------------------------------------------------"

def multiply_two_nums():
    number_1 = raw_input("Enter the first number: ")
    if number_1.isdigit() == False:
        print "Enter numbers only."
        multiply_two_nums()
    number_2 = raw_input("Enter the second number: ")
    if number_2.isdigit() == False:
        print "Enter numbers only."
        multiply_two_nums()

    number_1 = int(number_1)
    number_2 = int(number_2)
    total = number_1 * number_2
    
    print "-------------------------------------------------"
    print "The total of your chosen numbers multiplied is " + str(total)
    print "-------------------------------------------------"

    multiply_two_nums()

multiply_two_nums()
