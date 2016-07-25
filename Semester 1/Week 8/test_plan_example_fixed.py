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
try:
    result = float(number1)/float(number2)
    print number1, "divided by", number2, "=", result
except ZeroDivisionError:
    print number1, "divided by", number2, "=", 0
