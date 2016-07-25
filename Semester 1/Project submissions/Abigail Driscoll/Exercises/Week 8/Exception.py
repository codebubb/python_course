import random
try:
    list_of_numbers = []
    for i in range(random.randrange(20)):
        list_of_numbers.append(random.randrange(100))

    pick = int(input("Pick a number you want to display: "))

    print("You picked: ", list_of_numbers[pick])

except IndexError:
    print("That value doesn't exist")
except TypeError:
    print("Please enter a number")
# except IOError:
    #etc etc etc

