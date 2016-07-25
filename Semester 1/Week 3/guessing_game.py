'''
guessing_game.py
----------------
See if the user can guess a number generated randomly by the computer
'''
import random
my_number = int(random.random() * 10) + 1

print "I'm thinking of a number between 1 and 10."
while int(raw_input("What number am I thinking of?")) != my_number:
    print "Nope, not that! Try again..."
print "Well done, yes I was thinking of ", my_number

    
