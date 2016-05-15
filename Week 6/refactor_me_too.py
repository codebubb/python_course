# and me!

list_of_numbers = []

while True:
    number = raw_input("Please enter a number (leave blank to end):")
    if not number:
        break
    if not number.isdigit():
        print number, "isn't a number!"
    else:
        number = int(number)
        list_of_numbers.append(number)
        middle_pos = len(list_of_numbers) / 2
        print "Middle element is", list_of_numbers[middle_pos]

list_of_numbers.sort()
middle_pos = len(list_of_numbers) / 2
print "Middle element is", list_of_numbers[middle_pos]
