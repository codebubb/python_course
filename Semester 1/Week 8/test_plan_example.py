def get_number(msg="Please enter a number:"):
    while True:
        try:
            number = int(raw_input(msg))
            break
        except TypeError:
            print "That isn't a valid number"
    return number


number1 = get_number()
number2 = get_number("And another one:")

print number1, "divided by", number2, "=", float(number1)/float(number2)
