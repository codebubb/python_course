import random
my_number = int(random.random()*10)+1

turns = 1
while True:
    turns += 1
    if turns % 2 == 0:
        print ('Player 1 its your guess')
        x = int(raw_input('Pick a number between 1 - 10: '))
        if x == my_number:
            print ('Player 1 wins!!')
            break
        else:
            print ('ooooh so close\n')
    if turns % 2 == 1:
        print ('Player 2 its your guess')
        y = int(raw_input('Pick a number between 1 - 10: '))
        if y == my_number:
            print ('Player 2 wins!!')
            break
        else:
            print ('ooooh so close\n')
