'''
hangman.py
'''
import random

words = ['stenographer', 'military', 'python', 'fishcake', 'toothpaste', 'gooseberry']

# Choose a random word
game_word = random.choice(words).lower()

# The 'masked' word
hidden_word = list("_" * len(game_word))

# Keep track of letters incorrectly guessed
incorrect_letters = []

# Hangman image
the_hangman =[
'''







---------
''',
'''

      |
      |
      |
      |
      |
      |
---------
'''
,'''
  ____
     \|
      |
      |
      |
      |
      |
---------
'''
,'''
  ____
 |   \|
 |    |
 O    |
      |
      |
      |
---------
'''
,'''
  ____
 |   \|
 |    |
 O    |
/|\   |
      |
      |
---------
'''
,'''
  ____
 |   \|
 |    |
 O    |
/|\   |
 |    |
/ \   |
---------
'''
               ]

# Amount of wrong letters we can get
guess_limit = len(the_hangman)

# Start game
print "-"*20
print "Hangman"
print "-"*20,"\n"

while True:
    # Only display incorrect letters (and hangman) if there are some
    if len(incorrect_letters): 
        print the_hangman[len(incorrect_letters) -1]
        print "Incorrect letters:", ",".join(incorrect_letters)
    print " ".join(hidden_word), "\n" # The masked word
    guess = raw_input("Guess a letter or solve:").lower()
    if not len(guess): # The user didn't enter anything
        print "You did not enter anything."
    elif len(guess) == 1: # Single letter entered
        if guess in game_word: # Check if the letter is in the word
            for i in range(len(game_word)): # Loop through each letter in word 
                if game_word[i] == guess: # checking if it is equal to the guessed letter
                    hidden_word[i] = guess # if it is, update the 'masked' word
        else:
            if guess not in incorrect_letters: # Otherwise the guess isn't in the answer
                incorrect_letters.append(guess)
    if guess == game_word or "".join(hidden_word) == game_word: # Check if the user solved the hangman
        print "Congrats, the word was",game_word
        break
    if len(incorrect_letters) > guess_limit -1: # Reached the end
        print the_hangman[len(incorrect_letters) -1 ]
        print "Too many guesses!\nTry again."
        break
