print "Welcome to the Python Calculator!"
print "This is where you can multiply any two numbers of your choice."


def p():
    first_number = raw_input("Please enter your first number.")
    second_number = raw_input("Please enter your second number.")

    int_first_number = int(first_number)
    int_second_number = int(second_number)

    a = int_first_number * int_second_number

    print "Ah, so the multiplication of %s and %s equals %s." % (int_first_number, int_second_number, a)
    print "Now choose your next numbers."

    p()

p()
