import random
highest = 10
my_number = random.randint(1, highest+1)

print("Try and guess the right number, between 1 and {}: ".format(highest))
while my_number != guess:
    guess = int(input())

    print("You got it wrong, try again!")
    break
if my_number == guess:
    print("Well done! You got it!")
